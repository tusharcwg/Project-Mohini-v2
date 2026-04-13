#!/usr/bin/env python3
"""
F&O Accumulation Analyzer — 7-Day Multi-Window (v2.1)
======================================================
Ingests up to 7 daily derivative analytics CSV/XLSX files from a directory,
auto-discovers them by filename pattern, runs the v2 symmetric scoring model
across 6 rolling 2-day windows, and emits a hybrid Markdown+JSON artifact
with latest score, 7-day trajectory, persistence, and phase map.

Usage:  python fno_analyzer_7day.py
        (prompts once for directory; picks latest 7 files by filename date)

Input file pattern (case-insensitive):
    Derivative_Analytics_DD-Mon-YYYY.{csv,xlsx}

Tolerant mode: minimum 3 days required; fewer = fall back to pairwise analysis
with data completeness warning in output.

v2.1 adds (on top of v2.0):
  - Directory auto-discovery & 7 latest files selection
  - 6 rolling 2-day windows scored independently
  - Score persistence (count of bullish/bearish windows)
  - 7-day PCR slope, delivery persistence (days with ≥1.0x)
  - Cumulative 7-day futures OI change
  - NSE monthly expiry (last Thursday) detection & warning
"""
from __future__ import annotations

import calendar
import hashlib
import json
import logging
import math
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, date
from pathlib import Path
from typing import Any

MODEL_VERSION = "2.1"
FLAT_PRICE_THRESHOLD = 0.3
MIN_DAYS = 3
MAX_DAYS = 7
FILENAME_PATTERN = re.compile(
    r"derivative[_\s-]*analytics[_\s-]*(\d{1,2})[_\s-]*([a-z]{3})[_\s-]*(\d{2,4})",
    re.IGNORECASE,
)

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1 — LOGGING (Rule #1)
# ─────────────────────────────────────────────────────────────────────────────

def setup_logger(script_dir: Path) -> logging.Logger:
    logs_dir = script_dir / "logs"
    logs_dir.mkdir(exist_ok=True)
    log_path = logs_dir / f"fno_analyzer_7day_{datetime.now().strftime('%Y-%m-%d')}.log"
    logger = logging.getLogger("fno_analyzer_7day")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fh = logging.FileHandler(log_path, encoding="utf-8")
        fh.setFormatter(logging.Formatter(
            '{"ts":"%(asctime)s","level":"%(levelname)s","msg":%(message)s}'
        ))
        logger.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
        logger.addHandler(ch)
    return logger


def log_event(logger: logging.Logger, level: str, event: str, **kv: Any) -> None:
    getattr(logger, level)(json.dumps({"event": event, **kv}, default=str))


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2 — SAFE HELPERS (Rule #16)
# ─────────────────────────────────────────────────────────────────────────────

def safe_float(val: Any) -> float | None:
    try:
        if val is None: return None
        if isinstance(val, float) and math.isnan(val): return None
        s = str(val).strip()
        if s == "" or s.lower() in ("nan", "none", "null", "-"): return None
        return float(s.replace(",", "").replace("%", "").replace("+", ""))
    except (ValueError, TypeError):
        return None


def safe_str(val: Any) -> str | None:
    if val is None: return None
    if isinstance(val, float) and math.isnan(val): return None
    s = str(val).strip()
    return s if s else None


def directional_sign(value: float, flat_threshold: float = 0.0) -> int:
    if value > flat_threshold: return 1
    if value < -flat_threshold: return -1
    return 0


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3 — DIRECTORY AUTO-DISCOVERY
# ─────────────────────────────────────────────────────────────────────────────

MONTH_MAP = {m.lower(): i for i, m in enumerate(calendar.month_abbr) if m}


def parse_filename_date(filename: str) -> date | None:
    m = FILENAME_PATTERN.search(filename)
    if not m: return None
    day_s, mon_s, year_s = m.groups()
    mon = MONTH_MAP.get(mon_s.lower())
    if not mon: return None
    try:
        day = int(day_s)
        year = int(year_s)
        if year < 100: year += 2000
        return date(year, mon, day)
    except ValueError:
        return None


def discover_files(directory: Path, logger: logging.Logger) -> list[tuple[Path, date]]:
    """Scan directory for Derivative_Analytics_*.{csv,xlsx}, return up to 7 most recent."""
    candidates: list[tuple[Path, date]] = []
    for f in directory.iterdir():
        if not f.is_file(): continue
        if f.suffix.lower() not in (".csv", ".xlsx", ".xls"): continue
        d = parse_filename_date(f.name)
        if d is None: continue
        candidates.append((f, d))
    candidates.sort(key=lambda x: x[1], reverse=True)
    picked = candidates[:MAX_DAYS]
    picked.sort(key=lambda x: x[1])  # chronological order for processing
    log_event(logger, "info", "files_discovered",
              total_matches=len(candidates), selected=len(picked),
              selected_dates=[str(d) for _, d in picked])
    return picked


def detect_nse_monthly_expiry(dates: list[date]) -> list[date]:
    """NSE monthly F&O expiry = last Thursday of the month. Return any found in window."""
    expiries = []
    months_seen = {(d.year, d.month) for d in dates}
    for y, m in months_seen:
        last_day = calendar.monthrange(y, m)[1]
        for dd in range(last_day, 0, -1):
            candidate = date(y, m, dd)
            if candidate.weekday() == 3:  # Thursday
                if dates[0] <= candidate <= dates[-1]:
                    expiries.append(candidate)
                break
    return sorted(expiries)


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4 — INPUT LOADER
# ─────────────────────────────────────────────────────────────────────────────

REQUIRED_COLS = [
    "Symbol", "Chg %", "Cumulative Future OI", "OI Chg %", "Volume (Times)",
    "Delivery (Times)", "Cumulative Call OI", "Cumulative Put OI",
    "Put Call Ratio (PCR)", "PCR Change 1D",
]


def load_single_day(path: Path, file_date: date, logger: logging.Logger) -> tuple[dict, list]:
    """Load a single-day CSV/XLSX. Date comes from filename. Returns {symbol: row_dict}, skipped."""
    try:
        import pandas as pd
    except ImportError:
        print("ERROR: pandas required. Install: pip install --only-binary :all: pandas openpyxl")
        sys.exit(1)

    ext = path.suffix.lower()
    if ext == ".csv":
        df = pd.read_csv(path, encoding="utf-8-sig")
    elif ext in (".xlsx", ".xls"):
        df = pd.read_excel(path)
    else:
        raise ValueError(f"Unsupported extension: {ext}")

    df.columns = [str(c).strip().lstrip("\ufeff") for c in df.columns]
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"{path.name} missing columns: {missing}")

    rows, skipped = {}, []
    for idx, r in df.iterrows():
        sym = safe_str(r.get("Symbol"))
        chg = safe_float(r.get("Chg %"))
        pcr = safe_float(r.get("Put Call Ratio (PCR)"))
        fut = safe_float(r.get("Cumulative Future OI"))
        if not sym or chg is None or pcr is None or fut is None:
            skipped.append({"file": path.name, "row": int(idx) + 2, "reason": "missing critical field"})
            continue
        rows[sym] = {
            "date": file_date.isoformat(),
            "date_obj": file_date,
            "symbol": sym, "chg_pct": chg, "fut_oi": fut,
            "oi_chg": safe_float(r.get("OI Chg %")) or 0.0,
            "volume": safe_float(r.get("Volume (Times)")) or 0.0,
            "delivery": safe_float(r.get("Delivery (Times)")) or 0.0,
            "call_oi": safe_float(r.get("Cumulative Call OI")) or 0.0,
            "put_oi": safe_float(r.get("Cumulative Put OI")) or 0.0,
            "pcr": pcr,
            "pcr_chg": safe_float(r.get("PCR Change 1D")) or 0.0,
        }
    return rows, skipped


def load_all_days(files: list[tuple[Path, date]], logger: logging.Logger) -> tuple[dict, list]:
    """Build {symbol: [day1_row, day2_row, ...]} across all 7 days."""
    per_day = []
    all_skipped = []
    for path, d in files:
        rows, skipped = load_single_day(path, d, logger)
        per_day.append((d, rows))
        all_skipped.extend(skipped)
        log_event(logger, "info", "day_loaded", file=path.name, date=str(d), symbols=len(rows))

    all_symbols = set()
    for _, rows in per_day:
        all_symbols.update(rows.keys())

    combined: dict[str, list[dict]] = {}
    for sym in all_symbols:
        timeline = [rows[sym] for _, rows in per_day if sym in rows]
        if len(timeline) >= 2:
            combined[sym] = timeline
        else:
            all_skipped.append({"symbol": sym, "reason": f"only {len(timeline)} day(s) of data; need ≥2"})
    return combined, all_skipped


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5 — v2 SCORING MODEL (unchanged, applied to each 2-day window)
# ─────────────────────────────────────────────────────────────────────────────

def score_window(d1: dict, d2: dict) -> dict:
    """Score a single 2-day window. Returns dict with score, signals, interpretation, TC, phase."""
    score, signals = 0.0, []
    price_chg = d2["chg_pct"]
    price_sign = directional_sign(price_chg, FLAT_PRICE_THRESHOLD)
    pcr_d1, pcr_d2 = d1["pcr"], d2["pcr"]

    # Signal 1a — PCR Level
    if pcr_d2 >= 1.0:       score += 3; signals.append(f"PCR {pcr_d2:.2f} ABOVE 1.0 — put writers dominant")
    elif pcr_d2 >= 0.85:    score += 2; signals.append(f"PCR {pcr_d2:.2f} approaching bullish zone")
    elif pcr_d2 >= 0.75:    score += 1; signals.append(f"PCR {pcr_d2:.2f} neutral-to-bullish")
    elif pcr_d2 >= 0.55:    signals.append(f"PCR {pcr_d2:.2f} neutral")
    elif pcr_d2 >= 0.40:    score -= 2; signals.append(f"PCR {pcr_d2:.2f} call writers dominant")
    else:                   score -= 3; signals.append(f"PCR {pcr_d2:.2f} heavy call writing")

    # Signal 1b — PCR Trajectory
    pcr_change = d2["pcr_chg"]
    if pcr_change > 0.08:    score += 2; signals.append(f"PCR surging +{pcr_change:.2f}")
    elif pcr_change > 0.03:  score += 1; signals.append(f"PCR rising +{pcr_change:.2f}")
    elif pcr_change < -0.08: score -= 2; signals.append(f"PCR collapsing {pcr_change:+.2f}")
    elif pcr_change < -0.03: score -= 1; signals.append(f"PCR easing {pcr_change:+.2f}")

    # Signal 2 — Futures OI × Price
    fut_oi_chg = ((d2["fut_oi"] - d1["fut_oi"]) / d1["fut_oi"] * 100.0) if d1["fut_oi"] else 0.0
    oi_sign = directional_sign(fut_oi_chg, 0.0)
    s2_active = True
    if fut_oi_chg > 2 and price_chg > 0.5:
        score += 3; interp = "★ NEW LONGS (Bullish)"
        signals.append(f"★ NEW LONGS: FutOI {fut_oi_chg:+.1f}% + Price {price_chg:+.1f}%")
    elif fut_oi_chg > 0 and price_chg > 0:
        score += 2; interp = "Mild long build"
    elif fut_oi_chg > 2 and price_chg < -0.5:
        score -= 3; interp = "⚠ NEW SHORTS (Bearish)"
        signals.append(f"⚠ NEW SHORTS: FutOI {fut_oi_chg:+.1f}% + Price {price_chg:+.1f}%")
    elif fut_oi_chg > 0 and price_chg < 0:
        score -= 2; interp = "Mild short build"
    elif fut_oi_chg < -2 and price_chg > 0.5:
        score += 1; interp = "↑ SHORT COVERING (lagging)"
    elif fut_oi_chg < -2 and price_chg < -0.5:
        score -= 2; interp = "↓ LONG LIQUIDATION (lagging)"
    else:
        interp = "→ CONSOLIDATION"; s2_active = False

    # Signal 3 — Delivery gated by price
    avg_del = (d1["delivery"] + d2["delivery"]) / 2.0
    peak_del = max(d1["delivery"], d2["delivery"])
    del_chg = d2["delivery"] - d1["delivery"]

    if avg_del >= 1.0:
        if price_sign > 0:   score += 3; signals.append(f"Del {avg_del:.2f}x + Price↑ INSTITUTIONAL ACCUMULATION")
        elif price_sign < 0: score -= 3; signals.append(f"Del {avg_del:.2f}x + Price↓ INSTITUTIONAL DISTRIBUTION")
        else:                score += 1
    elif avg_del >= 0.70:
        if price_sign > 0:   score += 2
        elif price_sign < 0: score -= 2
        else:                score += 0.5
    elif avg_del >= 0.50:
        if price_sign > 0:   score += 1
        elif price_sign < 0: score -= 1

    if del_chg > 0.3:
        if price_sign > 0:   score += 1
        elif price_sign < 0: score -= 1
    if peak_del >= 1.5:
        if price_sign > 0:   score += 1
        elif price_sign < 0: score -= 1

    # Signal 4 — Volume (safety rail)
    avg_vol = (d1["volume"] + d2["volume"]) / 2.0
    if s2_active:
        vol_dir = 1 if "LONGS" in interp or "long build" in interp or "COVERING" in interp else \
                  -1 if "SHORTS" in interp or "short build" in interp or "LIQUIDATION" in interp else 0
        if avg_vol >= 1.5:   score += 1 * vol_dir
        elif avg_vol >= 1.0: score += 0.5 * vol_dir

    # Signal 5 — Options OI lean + growth
    call_g = ((d2["call_oi"] - d1["call_oi"]) / d1["call_oi"] * 100.0) if d1["call_oi"] else 0.0
    put_g  = ((d2["put_oi"]  - d1["put_oi"])  / d1["put_oi"]  * 100.0) if d1["put_oi"]  else 0.0
    tot1, tot2 = d1["call_oi"] + d1["put_oi"], d2["call_oi"] + d2["put_oi"]
    opt_g = ((tot2 - tot1) / tot1 * 100.0) if tot1 else 0.0
    lean = 0
    if put_g > call_g and put_g > 5:    lean = +1
    elif call_g > put_g and call_g > 5: lean = -1
    if lean != 0:
        score += 0.5 * lean
        if opt_g > 15:   score += 1 * lean
        elif opt_g > 5:  score += 0.5 * lean

    # Signal 6 — Single-day OI surge on d2
    if d2["oi_chg"] > 5 and price_sign > 0:    score += 1
    elif d2["oi_chg"] > 5 and price_sign < 0:  score -= 1
    elif d2["oi_chg"] > 2 and price_sign > 0:  score += 0.5
    elif d2["oi_chg"] > 2 and price_sign < 0:  score -= 0.5

    # Triple Convergence (OI-gated)
    pcr_sign = directional_sign(pcr_change, 0.0)
    if oi_sign > 0 and price_sign > 0 and pcr_sign > 0:
        tc = {"status": "★★★ TC (LONG)", "direction": "long", "count": 3}
    elif oi_sign > 0 and price_sign < 0 and pcr_sign < 0:
        tc = {"status": "★★★ TC (SHORT)", "direction": "short", "count": 3}
    else:
        lu = sum([price_sign > 0, oi_sign > 0, pcr_sign > 0])
        sd = sum([price_sign < 0, oi_sign > 0, pcr_sign < 0])
        if lu >= sd:
            tc = {"status": f"★★ DOUBLE (long)" if lu == 2 else (f"★ SINGLE" if lu == 1 else "○ NONE"),
                  "direction": "long" if lu >= 2 else "none", "count": lu}
        else:
            tc = {"status": f"★★ DOUBLE (short)" if sd == 2 else "○ NONE",
                  "direction": "short" if sd >= 2 else "none", "count": sd}

    phase = classify_phase(interp, avg_del, fut_oi_chg, price_sign, pcr_change)

    return {
        "score": round(score, 2), "signals": signals, "interpretation": interp,
        "triple_convergence": tc, "phase": phase,
        "price_chg_pct": price_chg, "price_sign": price_sign,
        "pcr_d1": pcr_d1, "pcr_d2": pcr_d2, "pcr_chg": pcr_change,
        "fut_oi_chg_pct": round(fut_oi_chg, 2), "oi_sign": oi_sign,
        "avg_del": round(avg_del, 3), "peak_del": peak_del, "del_chg": round(del_chg, 3),
        "avg_vol": round(avg_vol, 3),
        "call_oi_growth_pct": round(call_g, 2), "put_oi_growth_pct": round(put_g, 2),
        "opt_oi_growth_pct": round(opt_g, 2),
        "date_d1": d1["date"], "date_d2": d2["date"],
    }


def classify_phase(interp: str, avg_del: float, fut_oi_chg: float,
                   price_sign: int, pcr_chg: float) -> str:
    if "NEW LONGS" in interp and avg_del >= 1.0:                       return "phase_2_long"
    if avg_del >= 0.70 and fut_oi_chg > 0 and price_sign > 0:          return "phase_1_long"
    if pcr_chg > 0.05 and fut_oi_chg <= 0 and price_sign >= 0:         return "pre_phase_1_long"
    if "NEW SHORTS" in interp and avg_del >= 1.0:                      return "phase_2_short"
    if avg_del >= 0.70 and fut_oi_chg > 0 and price_sign < 0:          return "phase_1_short"
    if pcr_chg < -0.05 and fut_oi_chg <= 0 and price_sign <= 0:        return "pre_phase_1_short"
    return "no_signal"


PHASE_DESCRIPTIONS = {
    "phase_2_long": "Futures leverage — new longs + institutional delivery ≥1.0x",
    "phase_1_long": "Cash accumulation — delivery ≥0.70x, OI building, price rising",
    "pre_phase_1_long": "Derivatives leading cash — PCR rising without OI build",
    "phase_2_short": "Short leverage — new shorts + institutional delivery ≥1.0x",
    "phase_1_short": "Distribution — delivery ≥0.70x, OI building, price falling",
    "pre_phase_1_short": "Derivatives leading cash (bearish) — PCR collapsing without OI build",
    "no_signal": "No clear positioning phase",
}


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 6 — 7-DAY TRAJECTORY METRICS
# ─────────────────────────────────────────────────────────────────────────────

def linear_slope(values: list[float]) -> float:
    """Simple least-squares slope of values vs index 0..n-1."""
    n = len(values)
    if n < 2: return 0.0
    mean_x = (n - 1) / 2.0
    mean_y = sum(values) / n
    num = sum((i - mean_x) * (v - mean_y) for i, v in enumerate(values))
    den = sum((i - mean_x) ** 2 for i in range(n))
    return num / den if den else 0.0


def compute_trajectory(timeline: list[dict], windows: list[dict]) -> dict:
    """Compute 7-day trajectory metrics from per-day timeline and rolling window scores."""
    window_scores = [w["score"] for w in windows]
    bullish_windows = sum(1 for s in window_scores if s >= 3)
    bearish_windows = sum(1 for s in window_scores if s <= -3)
    neutral_windows = len(window_scores) - bullish_windows - bearish_windows

    pcr_series = [t["pcr"] for t in timeline]
    del_series = [t["delivery"] for t in timeline]
    pcr_slope = linear_slope(pcr_series)
    days_del_inst = sum(1 for d in del_series if d >= 1.0)
    days_del_above_normal = sum(1 for d in del_series if d >= 0.70)

    # Cumulative 7-day futures OI change
    fut_oi_first, fut_oi_last = timeline[0]["fut_oi"], timeline[-1]["fut_oi"]
    cum_oi_chg = ((fut_oi_last - fut_oi_first) / fut_oi_first * 100.0) if fut_oi_first else 0.0

    # Cumulative price change across the full window
    # Using product of (1 + chg%/100) across days 1..n (day 0 is baseline)
    cum_price_factor = 1.0
    for t in timeline[1:]:
        cum_price_factor *= (1 + t["chg_pct"] / 100.0)
    cum_price_chg = (cum_price_factor - 1) * 100.0

    # Persistence score: mean of window scores weighted toward recency (linear weights)
    n = len(window_scores)
    if n:
        weights = [i + 1 for i in range(n)]  # 1, 2, ..., n
        weighted_sum = sum(w * s for w, s in zip(weights, window_scores))
        persistence_score = weighted_sum / sum(weights)
    else:
        persistence_score = 0.0

    # Regime classification
    if bullish_windows >= max(3, int(0.6 * len(window_scores))):
        regime = "SUSTAINED BULLISH"
    elif bearish_windows >= max(3, int(0.6 * len(window_scores))):
        regime = "SUSTAINED BEARISH"
    elif bullish_windows > bearish_windows:
        regime = "MIXED BULLISH-LEANING"
    elif bearish_windows > bullish_windows:
        regime = "MIXED BEARISH-LEANING"
    else:
        regime = "CHOPPY / INDECISIVE"

    return {
        "window_scores": window_scores,
        "bullish_windows": bullish_windows,
        "bearish_windows": bearish_windows,
        "neutral_windows": neutral_windows,
        "total_windows": len(window_scores),
        "pcr_slope_7d": round(pcr_slope, 4),
        "pcr_first": round(pcr_series[0], 2) if pcr_series else None,
        "pcr_last": round(pcr_series[-1], 2) if pcr_series else None,
        "days_delivery_institutional": days_del_inst,
        "days_delivery_above_normal": days_del_above_normal,
        "total_days": len(timeline),
        "cumulative_oi_chg_pct_window": round(cum_oi_chg, 2),
        "cumulative_price_chg_pct_window": round(cum_price_chg, 2),
        "persistence_score": round(persistence_score, 2),
        "regime": regime,
    }


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 7 — PER-SYMBOL ROLL-UP
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class SymbolResult:
    symbol: str
    rank: int
    days_available: int
    latest_score: float
    latest_tier: str
    latest_sign: str
    latest_phase: str
    latest_interpretation: str
    latest_triple_convergence: dict
    latest_date_d1: str
    latest_date_d2: str
    trajectory: dict
    all_windows: list[dict] = field(default_factory=list)
    daily_timeline: list[dict] = field(default_factory=list)


def tier_from_score(s: float) -> tuple[str, str]:
    if s >= 9:   return "TIER 1 — STRONG ACCUMULATION", "bullish"
    if s >= 7:   return "TIER 2 — ACCUMULATION", "bullish"
    if s >= 5:   return "TIER 3 — BUILDING LONG", "bullish"
    if s >= 3:   return "WATCH (mild bullish)", "bullish"
    if s > -3:   return "NO SIGNAL", "neutral"
    if s > -5:   return "WATCH (mild bearish)", "bearish"
    if s > -7:   return "TIER 3 — BUILDING SHORT", "bearish"
    if s > -9:   return "TIER 2 — DISTRIBUTION", "bearish"
    return "TIER 1 — STRONG DISTRIBUTION", "bearish"


def build_symbol_result(sym: str, timeline: list[dict]) -> SymbolResult:
    windows = [score_window(timeline[i], timeline[i + 1]) for i in range(len(timeline) - 1)]
    latest = windows[-1]
    tier, sign = tier_from_score(latest["score"])
    trajectory = compute_trajectory(timeline, windows)

    # Reduced daily timeline for JSON (no dupes of big fields)
    daily = [{
        "date": t["date"], "price_chg_pct": t["chg_pct"], "pcr": t["pcr"],
        "pcr_chg_1d": t["pcr_chg"], "fut_oi": int(t["fut_oi"]), "oi_chg_pct": t["oi_chg"],
        "delivery": t["delivery"], "volume": t["volume"],
        "call_oi": int(t["call_oi"]), "put_oi": int(t["put_oi"]),
    } for t in timeline]

    return SymbolResult(
        symbol=sym, rank=0, days_available=len(timeline),
        latest_score=latest["score"], latest_tier=tier, latest_sign=sign,
        latest_phase=latest["phase"], latest_interpretation=latest["interpretation"],
        latest_triple_convergence=latest["triple_convergence"],
        latest_date_d1=latest["date_d1"], latest_date_d2=latest["date_d2"],
        trajectory=trajectory, all_windows=windows, daily_timeline=daily,
    )


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 8 — OUTPUT EMITTER
# ─────────────────────────────────────────────────────────────────────────────

def resolve_output_path(out_dir: Path, start: date, end: date) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = out_dir / f"fno_7day_analysis_{start}_to_{end}_{ts}.md"
    if not base.exists(): return base
    n = 2
    while True:
        c = out_dir / f"fno_7day_analysis_{start}_to_{end}_{ts}_v{n}.md"
        if not c.exists(): return c
        n += 1


def emit_output(results: list[SymbolResult], meta: dict, warnings: list, out_path: Path) -> None:
    # Sort by absolute latest score so top bullish + top bearish both surface
    results.sort(key=lambda r: abs(r.latest_score), reverse=True)
    for i, r in enumerate(results, 1):
        r.rank = i

    phase_map: dict[str, list[str]] = {k: [] for k in PHASE_DESCRIPTIONS}
    for r in results:
        phase_map.setdefault(r.latest_phase, []).append(r.symbol)

    bullish_sorted = sorted([r for r in results if r.latest_score > 0], key=lambda r: r.latest_score, reverse=True)
    bearish_sorted = sorted([r for r in results if r.latest_score < 0], key=lambda r: r.latest_score)

    # Persistence leaders — sustained regime across multiple windows
    persistent_bulls = sorted([r for r in results if r.trajectory["regime"] in ("SUSTAINED BULLISH", "MIXED BULLISH-LEANING")],
                              key=lambda r: (r.trajectory["bullish_windows"], r.trajectory["persistence_score"]), reverse=True)
    persistent_bears = sorted([r for r in results if r.trajectory["regime"] in ("SUSTAINED BEARISH", "MIXED BEARISH-LEANING")],
                              key=lambda r: (r.trajectory["bearish_windows"], -r.trajectory["persistence_score"]), reverse=True)

    payload = {
        "meta": {**meta, "model_version": MODEL_VERSION,
                 "scoring_strategy": "C — rolling 2-day windows (v2 engine) + 7-day trajectory",
                 "known_limitations": [
                     "PCR <0.40 during parabolic crash may be oversold bounce",
                     "Short Covering and Long Liquidation are lagging signals",
                     "NSE monthly expiry within window distorts OI interpretation",
                     "No market context (Nifty trend) — planned for v3",
                 ]},
        "phase_descriptions": PHASE_DESCRIPTIONS,
        "rankings": [asdict(r) for r in results],
        "phase_map": phase_map,
        "warnings": warnings,
    }

    md = [f"# F&O 7-Day Accumulation Analysis (v{MODEL_VERSION})", ""]
    if meta.get("data_completeness_warning"):
        md += [f"> ⚠ **{meta['data_completeness_warning']}**", ""]
    if meta.get("expiry_warning"):
        md += [f"> ⚠ **{meta['expiry_warning']}**", ""]

    md += [
        f"- **Input directory:** `{meta['input_directory']}`",
        f"- **Files analyzed ({meta['days_used']}):**",
    ]
    for f_info in meta["input_files"]:
        md.append(f"  - `{f_info['file']}` (date {f_info['date']}, SHA-256 `{f_info['sha256'][:16]}…`)")
    md += [
        f"- **Combined hash:** `{meta['combined_sha256']}`",
        f"- **Generated:** {meta['generated_at']}",
        f"- **Symbols with ≥2 days:** {meta['symbols_analyzed']} | **Skipped:** {len(warnings)}",
        f"- **Rolling windows per symbol:** up to {meta['days_used'] - 1}", "",
        "## Scoring Strategy (C — Rolling Multi-Window)",
        "",
        "Each symbol is scored across all adjacent 2-day windows within the input range "
        "using the v2.0 symmetric engine. The **latest window** (last 2 days) gives the "
        "actionable \"what's happening now\" signal, identical in semantics to v2.0. "
        "The **7-day trajectory** metrics (persistence, regime, PCR slope, delivery-days, "
        "cumulative OI) describe whether the latest signal is a one-session event or part "
        "of a sustained pattern.",
        "",
        "## Regime Classification",
        "",
        "| Regime | Condition |",
        "|---|---|",
        "| SUSTAINED BULLISH | ≥60% of windows scored ≥+3 (min 3 windows) |",
        "| SUSTAINED BEARISH | ≥60% of windows scored ≤−3 (min 3 windows) |",
        "| MIXED BULLISH-LEANING | More bullish windows than bearish |",
        "| MIXED BEARISH-LEANING | More bearish windows than bullish |",
        "| CHOPPY / INDECISIVE | Equal bullish/bearish windows |",
        "",
        "## Top 15 Bullish (by Latest Score)",
        "",
        "| Rank | Symbol | Latest | Tier | Regime | Bull/Bear/Neut | Persist | PCR 7d | Cum OI% | Phase |",
        "|---:|:---|---:|:---|:---|:---:|---:|:---:|---:|:---|",
    ]
    for r in bullish_sorted[:15]:
        t = r.trajectory
        md.append(f"| {r.rank} | {r.symbol} | {r.latest_score:+.1f} | {r.latest_tier} | "
                  f"{t['regime']} | {t['bullish_windows']}/{t['bearish_windows']}/{t['neutral_windows']} | "
                  f"{t['persistence_score']:+.2f} | {t['pcr_first']:.2f}→{t['pcr_last']:.2f} | "
                  f"{t['cumulative_oi_chg_pct_window']:+.1f}% | {r.latest_phase} |")

    md += ["", "## Top 15 Bearish (by Latest Score)", "",
           "| Rank | Symbol | Latest | Tier | Regime | Bull/Bear/Neut | Persist | PCR 7d | Cum OI% | Phase |",
           "|---:|:---|---:|:---|:---|:---:|---:|:---:|---:|:---|"]
    for r in bearish_sorted[:15]:
        t = r.trajectory
        md.append(f"| {r.rank} | {r.symbol} | {r.latest_score:+.1f} | {r.latest_tier} | "
                  f"{t['regime']} | {t['bullish_windows']}/{t['bearish_windows']}/{t['neutral_windows']} | "
                  f"{t['persistence_score']:+.2f} | {t['pcr_first']:.2f}→{t['pcr_last']:.2f} | "
                  f"{t['cumulative_oi_chg_pct_window']:+.1f}% | {r.latest_phase} |")

    md += ["", "## Top 10 Sustained-Bullish Persistence", "",
           "| Symbol | Latest | Regime | Bull Windows | Persist Score | Days Del≥1.0x |",
           "|:---|---:|:---|:---:|---:|:---:|"]
    for r in persistent_bulls[:10]:
        t = r.trajectory
        md.append(f"| {r.symbol} | {r.latest_score:+.1f} | {t['regime']} | "
                  f"{t['bullish_windows']}/{t['total_windows']} | {t['persistence_score']:+.2f} | "
                  f"{t['days_delivery_institutional']}/{t['total_days']} |")

    md += ["", "## Top 10 Sustained-Bearish Persistence", "",
           "| Symbol | Latest | Regime | Bear Windows | Persist Score | Days Del≥1.0x |",
           "|:---|---:|:---|:---:|---:|:---:|"]
    for r in persistent_bears[:10]:
        t = r.trajectory
        md.append(f"| {r.symbol} | {r.latest_score:+.1f} | {t['regime']} | "
                  f"{t['bearish_windows']}/{t['total_windows']} | {t['persistence_score']:+.2f} | "
                  f"{t['days_delivery_institutional']}/{t['total_days']} |")

    md += ["", "## Phase Map (based on latest window)", ""]
    for phase, desc in PHASE_DESCRIPTIONS.items():
        syms = phase_map.get(phase, [])
        md += [f"### `{phase}` ({len(syms)})", f"_{desc}_", "", f"{', '.join(syms) if syms else '(none)'}", ""]

    if warnings:
        md += ["## Warnings", ""]
        for w in warnings[:50]:
            md.append(f"- `{w.get('symbol', w.get('file','?'))}`: {w.get('reason','?')}")
        if len(warnings) > 50:
            md.append(f"- … and {len(warnings) - 50} more (see JSON)")
        md.append("")

    md += ["## Structured Data (re-analysis payload)", "", "```json",
           json.dumps(payload, indent=2, default=str), "```", ""]
    out_path.write_text("\n".join(md), encoding="utf-8")


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 9 — MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main() -> int:
    script_dir = Path(__file__).resolve().parent
    logger = setup_logger(script_dir)
    print("=" * 72)
    print(f"  F&O 7-Day Accumulation Analyzer v{MODEL_VERSION}")
    print("=" * 72)
    raw = input("Enter directory containing Derivative_Analytics_*.csv/xlsx files: ").strip().strip('"').strip("'")
    if not raw:
        print("ERROR: No directory provided."); return 1
    directory = Path(os.path.expanduser(raw)).resolve()
    if not directory.exists() or not directory.is_dir():
        print(f"ERROR: Not a directory: {directory}"); return 1

    try:
        log_event(logger, "info", "run_start", directory=str(directory), model_version=MODEL_VERSION)
        files = discover_files(directory, logger)
        if len(files) < MIN_DAYS:
            print(f"ERROR: Found only {len(files)} file(s); need ≥{MIN_DAYS}.")
            return 1
        print(f"\nFound {len(files)} file(s):")
        for p, d in files:
            print(f"  • {p.name} → {d}")
        print()

        combined, skipped = load_all_days(files, logger)
        dates_in_range = [d for _, d in files]
        expiries = detect_nse_monthly_expiry(dates_in_range)
        results = [build_symbol_result(sym, tl) for sym, tl in combined.items()]

        completeness_msg = None
        if len(files) < MAX_DAYS:
            completeness_msg = f"Incomplete data — only {len(files)} days available, not {MAX_DAYS}."
        expiry_msg = None
        if expiries:
            expiry_msg = (f"NSE monthly expiry within window ({', '.join(str(e) for e in expiries)}). "
                          "Futures OI interpretation may be distorted by position rollover; treat Signal 2 with caution.")

        input_files_meta = []
        combined_hasher = hashlib.sha256()
        for p, d in files:
            h = sha256_file(p)
            combined_hasher.update(h.encode())
            input_files_meta.append({"file": p.name, "date": str(d), "sha256": h})

        meta = {
            "input_directory": str(directory),
            "days_used": len(files),
            "input_files": input_files_meta,
            "combined_sha256": combined_hasher.hexdigest(),
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "symbols_analyzed": len(results),
            "data_completeness_warning": completeness_msg,
            "expiry_warning": expiry_msg,
            "expiry_dates_detected": [str(e) for e in expiries],
        }

        out_path = resolve_output_path(directory, dates_in_range[0], dates_in_range[-1])
        emit_output(results, meta, skipped, out_path)
        log_event(logger, "info", "run_complete", output=str(out_path), symbols=len(results))
        print(f"\n✓ Analyzed {len(results)} symbols across {len(files)} days | Skipped: {len(skipped)}")
        if completeness_msg: print(f"⚠ {completeness_msg}")
        if expiry_msg:       print(f"⚠ {expiry_msg}")
        print(f"✓ Output written: {out_path}")
        return 0
    except Exception as e:
        log_event(logger, "error", "run_failed", error=str(e), error_type=type(e).__name__)
        print(f"ERROR: {e}"); return 2


if __name__ == "__main__":
    sys.exit(main())
