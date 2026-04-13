#!/usr/bin/env python3
"""
F&O Accumulation Analyzer v2.0.1
================================
Ingests a derivative analytics CSV/XLSX (2 dates per symbol), computes a
SYMMETRIC multi-signal scoring model (signed score from strong distribution
to strong accumulation), and emits a hybrid Markdown+JSON artifact for
downstream analysis.

Two input modes (interactive choice at startup):
  [1] Combined file — single CSV/XLSX with 2 dates per symbol
  [2] Folder combine — directory with 2 single-day CSVs, auto-discovered
      by filename pattern Derivative_Analytics_DD-Mon-YYYY.{csv,xlsx},
      combined in-memory (not written to disk) and scored

v2.0.1 changes from v2.0:
  - Added folder-combine input mode (auto-discover 2 latest dated files)
  - Mode-aware Markdown header and JSON meta
  - Scoring engine unchanged; folder mode feeds same downstream path

v2.0 changes from v1.0:
  - Signed score: bearish setups scored symmetrically (was long-biased)
  - Delivery gated by price direction (fixes v1 distribution-as-accumulation bug)
  - Triple Convergence requires OI expansion (fixes short-covering false TC)
  - Volume safety rail: zero contribution when Signal 2 = Consolidation
  - Phase map: 6 phases (3 long + 3 short) with ghost-phase protection
  - directional_sign() helper prevents sign-flip bugs across signals

All per-symbol signal breakdowns preserved in JSON for re-analysis.
"""
from __future__ import annotations

import hashlib
import json
import logging
import math
import os
import sys
from dataclasses import dataclass, field, asdict
from datetime import date, datetime
from pathlib import Path
from typing import Any

MODEL_VERSION = "2.0.1"
FLAT_PRICE_THRESHOLD = 0.3  # % — price moves within ±0.3% counted as flat

# Filename date pattern for folder-combine mode. Tolerant of spaces/dashes/underscores
# between tokens. Matches: Derivative_Analytics_01-Apr-2026.csv, etc.
import calendar as _calendar
import re as _re
FILENAME_DATE_PATTERN = _re.compile(
    r"derivative[_\s-]*analytics[_\s-]*(\d{1,2})[_\s-]*([a-z]{3})[_\s-]*(\d{2,4})",
    _re.IGNORECASE,
)
_MONTH_ABBR = {m.lower(): i for i, m in enumerate(_calendar.month_abbr) if m}

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1 — LOGGING SETUP (Rule #1: structured logging)
# ─────────────────────────────────────────────────────────────────────────────

def setup_logger(script_dir: Path) -> logging.Logger:
    logs_dir = script_dir / "logs"
    logs_dir.mkdir(exist_ok=True)
    log_path = logs_dir / f"fno_analyzer_{datetime.now().strftime('%Y-%m-%d')}.log"
    logger = logging.getLogger("fno_analyzer")
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
# SECTION 2 — SAFE VALUE EXTRACTION (Rule #16: IFERROR equivalent)
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
    """Return +1 / 0 / -1. Values within ±flat_threshold treated as flat."""
    if value > flat_threshold: return 1
    if value < -flat_threshold: return -1
    return 0


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3 — INPUT LOADER (CSV + XLSX, blank-row tolerant)
# ─────────────────────────────────────────────────────────────────────────────

EXPECTED_COLS = {
    "date": "Date",
    "symbol": "Symbol",
    "chg_pct": "Chg %",
    "fut_oi": "Cumulative Future OI",
    "oi_chg": "OI Chg %",
    "volume": "Volume (Times)",
    "delivery": "Delivery (Times)",
    "call_oi": "Cumulative Call OI",
    "put_oi": "Cumulative Put OI",
    "pcr": "Put Call Ratio (PCR)",
    "pcr_chg": "PCR Change 1D",
}


# Required columns for folder-mode (single-day files — no Date column, date comes from filename)
FOLDER_REQUIRED_COLS = [
    "Symbol", "Chg %", "Cumulative Future OI", "OI Chg %", "Volume (Times)",
    "Delivery (Times)", "Cumulative Call OI", "Cumulative Put OI",
    "Put Call Ratio (PCR)", "PCR Change 1D",
]


def parse_filename_date(filename: str) -> "date | None":
    """Extract trading date from filename; returns None if unparseable."""
    from datetime import date
    m = FILENAME_DATE_PATTERN.search(filename)
    if not m:
        return None
    day_s, mon_s, year_s = m.groups()
    mon = _MONTH_ABBR.get(mon_s.lower())
    if not mon:
        return None
    try:
        day = int(day_s)
        year = int(year_s)
        if year < 100:
            year += 2000
        return date(year, mon, day)
    except ValueError:
        return None


def discover_dated_files(directory: Path, logger: logging.Logger) -> list[tuple[Path, "date"]]:
    """Scan directory for Derivative_Analytics_*.{csv,xlsx}, return sorted by date (oldest first)."""
    candidates = []
    for f in directory.iterdir():
        if not f.is_file():
            continue
        if f.suffix.lower() not in (".csv", ".xlsx", ".xls"):
            continue
        d = parse_filename_date(f.name)
        if d is None:
            continue
        candidates.append((f, d))
    candidates.sort(key=lambda x: x[1], reverse=True)  # newest first
    # Pick 2 most recent
    picked = candidates[:2]
    picked.sort(key=lambda x: x[1])  # chronological for processing
    log_event(logger, "info", "folder_files_discovered",
              total_matches=len(candidates), selected_count=len(picked),
              selected_files=[{"file": p.name, "date": str(d)} for p, d in picked])
    return picked


def load_from_folder(directory: Path, logger: logging.Logger) -> tuple[list[dict], list[dict], list[tuple[Path, "date"]]]:
    """Load 2 single-day CSV/XLSX files from a directory, inject Date from filename,
    return rows in the same shape as load_input() for uniform downstream processing."""
    try:
        import pandas as pd
    except ImportError:
        print("ERROR: pandas required. Install with: pip install --only-binary :all: pandas openpyxl")
        sys.exit(1)

    files = discover_dated_files(directory, logger)
    if len(files) < 2:
        raise ValueError(
            f"Found {len(files)} dated file(s) matching 'Derivative_Analytics_DD-Mon-YYYY.*' in "
            f"{directory}; need at least 2 for 2-date analysis."
        )

    rows, skipped = [], []
    for path, file_date in files:
        ext = path.suffix.lower()
        if ext == ".csv":
            df = pd.read_csv(path, encoding="utf-8-sig")
        elif ext in (".xlsx", ".xls"):
            df = pd.read_excel(path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
        df.columns = [str(c).strip().lstrip("\ufeff") for c in df.columns]
        missing = [c for c in FOLDER_REQUIRED_COLS if c not in df.columns]
        if missing:
            raise ValueError(f"{path.name} missing required columns: {missing}")

        # Inject Date (from filename) and parse every row
        date_str = file_date.strftime("%d-%b-%y")
        for idx, r in df.iterrows():
            sym = safe_str(r.get("Symbol"))
            chg = safe_float(r.get("Chg %"))
            pcr = safe_float(r.get("Put Call Ratio (PCR)"))
            fut = safe_float(r.get("Cumulative Future OI"))
            if not sym or chg is None or pcr is None or fut is None:
                skipped.append({"file": path.name, "row": int(idx) + 2, "reason": "missing critical field"})
                continue
            rows.append({
                "date": date_str, "symbol": sym,
                "chg_pct": chg, "fut_oi": fut,
                "oi_chg": safe_float(r.get("OI Chg %")) or 0.0,
                "volume": safe_float(r.get("Volume (Times)")) or 0.0,
                "delivery": safe_float(r.get("Delivery (Times)")) or 0.0,
                "call_oi": safe_float(r.get("Cumulative Call OI")) or 0.0,
                "put_oi": safe_float(r.get("Cumulative Put OI")) or 0.0,
                "pcr": pcr,
                "pcr_chg": safe_float(r.get("PCR Change 1D")) or 0.0,
            })
        log_event(logger, "info", "folder_day_loaded",
                  file=path.name, date=date_str, rows_added=len([r for r in rows if r["date"] == date_str]))
    return rows, skipped, files


def load_input(path: Path, logger: logging.Logger) -> tuple[list[dict], list[dict]]:
    try:
        import pandas as pd
    except ImportError:
        print("ERROR: pandas required. Install with: pip install --only-binary :all: pandas openpyxl")
        sys.exit(1)

    ext = path.suffix.lower()
    if ext == ".csv":
        df = pd.read_csv(path, encoding="utf-8-sig")
    elif ext in (".xlsx", ".xls"):
        df = pd.read_excel(path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    df.columns = [str(c).strip().lstrip("\ufeff") for c in df.columns]
    missing = [v for v in EXPECTED_COLS.values() if v not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    rows, skipped = [], []
    for idx, r in df.iterrows():
        sym = safe_str(r.get("Symbol"))
        dt = safe_str(r.get("Date"))
        chg = safe_float(r.get("Chg %"))
        pcr = safe_float(r.get("Put Call Ratio (PCR)"))
        fut = safe_float(r.get("Cumulative Future OI"))
        if not sym or not dt or chg is None or pcr is None or fut is None:
            skipped.append({"row": int(idx) + 2, "reason": "missing critical field"})
            continue
        rows.append({
            "date": dt, "symbol": sym,
            "chg_pct": chg, "fut_oi": fut,
            "oi_chg": safe_float(r.get("OI Chg %")) or 0.0,
            "volume": safe_float(r.get("Volume (Times)")) or 0.0,
            "delivery": safe_float(r.get("Delivery (Times)")) or 0.0,
            "call_oi": safe_float(r.get("Cumulative Call OI")) or 0.0,
            "put_oi": safe_float(r.get("Cumulative Put OI")) or 0.0,
            "pcr": pcr,
            "pcr_chg": safe_float(r.get("PCR Change 1D")) or 0.0,
        })
    log_event(logger, "info", "input_loaded", rows_valid=len(rows), rows_skipped=len(skipped))
    return rows, skipped


def pair_by_symbol(rows: list[dict], logger: logging.Logger) -> tuple[dict, list]:
    by_sym: dict[str, list[dict]] = {}
    for r in rows:
        by_sym.setdefault(r["symbol"], []).append(r)

    def parse_dt(s: str) -> datetime:
        for fmt in ("%d-%b-%y", "%d-%b-%Y", "%Y-%m-%d", "%d/%m/%Y"):
            try: return datetime.strptime(s, fmt)
            except ValueError: continue
        return datetime.min

    pairs, warnings = {}, []
    for sym, recs in by_sym.items():
        if len(recs) != 2:
            warnings.append({"symbol": sym, "reason": f"expected 2 rows, got {len(recs)}"})
            continue
        recs.sort(key=lambda x: parse_dt(x["date"]))
        pairs[sym] = {"d1": recs[0], "d2": recs[1]}
    log_event(logger, "info", "pairing_complete", paired=len(pairs), warned=len(warnings))
    return pairs, warnings


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4 — SCORING MODEL v2.0 (symmetric, signed score)
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class SymbolResult:
    symbol: str
    score: float
    score_sign: str  # "bullish" | "bearish" | "neutral"
    tier: str
    rank: int
    date_d1: str
    date_d2: str
    price_chg_pct: float
    price_sign: int  # +1/0/-1
    pcr_d1: float
    pcr_d2: float
    pcr_chg: float
    fut_oi_chg_pct: float
    oi_sign: int  # +1/0/-1
    avg_del: float
    peak_del: float
    del_chg: float
    avg_vol: float
    call_oi_growth_pct: float
    put_oi_growth_pct: float
    opt_oi_growth_pct: float
    interpretation: str
    triple_convergence: dict
    phase: str
    signals: list[str] = field(default_factory=list)


def score_symbol(sym: str, pair: dict) -> SymbolResult:
    d1, d2 = pair["d1"], pair["d2"]
    score, signals = 0.0, []

    price_chg = d2["chg_pct"]
    price_sign = directional_sign(price_chg, FLAT_PRICE_THRESHOLD)

    # ── Signal 1a — PCR Level (symmetric) ──
    pcr_d1, pcr_d2 = d1["pcr"], d2["pcr"]
    if pcr_d2 >= 1.0:
        score += 3; signals.append(f"PCR {pcr_d2:.2f} ABOVE 1.0 — put writers dominant (strongest bullish)")
    elif pcr_d2 >= 0.85:
        score += 2; signals.append(f"PCR {pcr_d2:.2f} — approaching bullish zone")
    elif pcr_d2 >= 0.75:
        score += 1; signals.append(f"PCR {pcr_d2:.2f} — neutral-to-bullish")
    elif pcr_d2 >= 0.55:
        signals.append(f"PCR {pcr_d2:.2f} — neutral")
    elif pcr_d2 >= 0.40:
        score -= 2; signals.append(f"PCR {pcr_d2:.2f} — call writers dominant (bearish ceiling)")
    else:
        score -= 3; signals.append(f"PCR {pcr_d2:.2f} BELOW 0.40 — heavy call writing (strongest bearish)")

    # ── Signal 1b — PCR Trajectory (symmetric) ──
    pcr_change = d2["pcr_chg"]
    if pcr_change > 0.08:
        score += 2; signals.append(f"PCR surging +{pcr_change:.2f} (1D)")
    elif pcr_change > 0.03:
        score += 1; signals.append(f"PCR rising +{pcr_change:.2f} (1D)")
    elif pcr_change < -0.08:
        score -= 2; signals.append(f"PCR collapsing {pcr_change:+.2f} (1D)")
    elif pcr_change < -0.03:
        score -= 1; signals.append(f"PCR easing {pcr_change:+.2f} (1D)")

    # ── Signal 2 — Futures OI × Price (four quadrants, symmetric) ──
    fut_oi_chg = ((d2["fut_oi"] - d1["fut_oi"]) / d1["fut_oi"] * 100.0) if d1["fut_oi"] else 0.0
    oi_sign = directional_sign(fut_oi_chg, 0.0)

    s2_active = True  # whether Signal 2 produced a non-zero interpretation (drives volume rail)
    if fut_oi_chg > 2 and price_chg > 0.5:
        score += 3; interp = "★ NEW LONGS (Bullish)"
        signals.append(f"★ NEW LONGS: FutOI {fut_oi_chg:+.1f}% + Price {price_chg:+.1f}%")
    elif fut_oi_chg > 0 and price_chg > 0:
        score += 2; interp = "Mild long build"
        signals.append(f"Mild long build: FutOI {fut_oi_chg:+.1f}% + Price {price_chg:+.1f}%")
    elif fut_oi_chg > 2 and price_chg < -0.5:
        score -= 3; interp = "⚠ NEW SHORTS (Bearish)"
        signals.append(f"⚠ NEW SHORTS: FutOI {fut_oi_chg:+.1f}% + Price {price_chg:+.1f}%")
    elif fut_oi_chg > 0 and price_chg < 0:
        score -= 2; interp = "Mild short build"
        signals.append(f"Mild short build: FutOI {fut_oi_chg:+.1f}% + Price {price_chg:+.1f}%")
    elif fut_oi_chg < -2 and price_chg > 0.5:
        score += 1; interp = "↑ SHORT COVERING (Weak Bull, lagging)"
        signals.append(f"Short covering: FutOI {fut_oi_chg:+.1f}% + Price {price_chg:+.1f}%")
    elif fut_oi_chg < -2 and price_chg < -0.5:
        score -= 2; interp = "↓ LONG LIQUIDATION (Bearish, lagging)"
        signals.append(f"Long liquidation: FutOI {fut_oi_chg:+.1f}% + Price {price_chg:+.1f}%")
    else:
        interp = "→ CONSOLIDATION"
        s2_active = False
        signals.append(f"Consolidation: FutOI {fut_oi_chg:+.1f}%, Price {price_chg:+.1f}%")

    # ── Signal 3 — Delivery gated by price direction ──
    avg_del = (d1["delivery"] + d2["delivery"]) / 2.0
    peak_del = max(d1["delivery"], d2["delivery"])
    del_chg = d2["delivery"] - d1["delivery"]

    def _delivery_score(level: float, p_sign: int) -> tuple[float, str]:
        if level >= 1.0:
            if p_sign > 0:  return +3, f"Delivery AVG {level:.2f}x + Price↑ — institutional ACCUMULATION"
            if p_sign < 0:  return -3, f"Delivery AVG {level:.2f}x + Price↓ — institutional DISTRIBUTION"
            return +1, f"Delivery AVG {level:.2f}x + Price flat — ambiguous (mild long)"
        if level >= 0.70:
            if p_sign > 0:  return +2, f"Delivery AVG {level:.2f}x + Price↑ — above-normal accumulation"
            if p_sign < 0:  return -2, f"Delivery AVG {level:.2f}x + Price↓ — above-normal distribution"
            return +0.5, f"Delivery AVG {level:.2f}x + Price flat — ambiguous"
        if level >= 0.50:
            if p_sign > 0:  return +1, f"Delivery AVG {level:.2f}x + Price↑ — moderate accumulation"
            if p_sign < 0:  return -1, f"Delivery AVG {level:.2f}x + Price↓ — moderate distribution"
            return 0, f"Delivery AVG {level:.2f}x — moderate, neutral direction"
        return 0, f"Delivery AVG {level:.2f}x — speculative / low conviction"

    ds, dmsg = _delivery_score(avg_del, price_sign)
    score += ds; signals.append(dmsg)

    # Signal 3b — acceleration / peak (gated by price)
    if del_chg > 0.3:
        if price_sign > 0:  score += 1; signals.append(f"Delivery accelerating {d1['delivery']:.2f}→{d2['delivery']:.2f}x + Price↑")
        elif price_sign < 0: score -= 1; signals.append(f"Delivery accelerating {d1['delivery']:.2f}→{d2['delivery']:.2f}x + Price↓ (selling surge)")
    if peak_del >= 1.5:
        if price_sign > 0:  score += 1; signals.append(f"Delivery peak {peak_del:.2f}x + Price↑ — heavy accumulation day")
        elif price_sign < 0: score -= 1; signals.append(f"Delivery peak {peak_del:.2f}x + Price↓ — heavy distribution day")

    # ── Signal 4 — Volume (safety rail: zero if Signal 2 inactive) ──
    avg_vol = (d1["volume"] + d2["volume"]) / 2.0
    if not s2_active:
        signals.append(f"Volume {avg_vol:.2f}x suppressed — Consolidation state (safety rail)")
    else:
        s2_dir = 1 if score > 0 else (-1 if score < 0 else 0)
        # Volume amplifies in the direction that Signal 2 established
        vol_dir = 1 if "LONGS" in interp or "long build" in interp or "COVERING" in interp else \
                  -1 if "SHORTS" in interp or "short build" in interp or "LIQUIDATION" in interp else 0
        if avg_vol >= 1.5:
            score += 1 * vol_dir
            signals.append(f"High volume {avg_vol:.2f}x amplifying {'bullish' if vol_dir>0 else 'bearish'} conviction")
        elif avg_vol >= 1.0:
            score += 0.5 * vol_dir
            signals.append(f"Normal volume {avg_vol:.2f}x amplifying {'bullish' if vol_dir>0 else 'bearish'} conviction")

    # ── Signal 5 — Options OI growth + lean ──
    call_g = ((d2["call_oi"] - d1["call_oi"]) / d1["call_oi"] * 100.0) if d1["call_oi"] else 0.0
    put_g  = ((d2["put_oi"]  - d1["put_oi"])  / d1["put_oi"]  * 100.0) if d1["put_oi"]  else 0.0
    tot1, tot2 = d1["call_oi"] + d1["put_oi"], d2["call_oi"] + d2["put_oi"]
    opt_g = ((tot2 - tot1) / tot1 * 100.0) if tot1 else 0.0

    # Lean determines sign
    lean = 0
    if put_g > call_g and put_g > 5:
        lean = +1
        signals.append(f"Put OI faster (+{put_g:.0f}%) than Call (+{call_g:.0f}%) — bullish lean")
    elif call_g > put_g and call_g > 5:
        lean = -1
        signals.append(f"Call OI faster (+{call_g:.0f}%) than Put (+{put_g:.0f}%) — bearish lean")

    if lean != 0:
        score += 0.5 * lean
        if opt_g > 15:
            score += 1 * lean
            signals.append(f"Options OI surged {opt_g:+.0f}% — heavy {'bullish' if lean>0 else 'bearish'} positioning")
        elif opt_g > 5:
            score += 0.5 * lean
            signals.append(f"Options OI up {opt_g:+.0f}% — {'bullish' if lean>0 else 'bearish'} positioning")

    # ── Signal 6 — Single-day OI surge on d2 (capped ±1, gated by price) ──
    s6_contrib = 0.0
    if d2["oi_chg"] > 5 and price_sign > 0:
        s6_contrib = +1; signals.append(f"{d2['date']} OI surge +{d2['oi_chg']:.1f}% + Price↑ — aggressive long entry")
    elif d2["oi_chg"] > 5 and price_sign < 0:
        s6_contrib = -1; signals.append(f"{d2['date']} OI surge +{d2['oi_chg']:.1f}% + Price↓ — aggressive short entry")
    elif d2["oi_chg"] > 2 and price_sign > 0:
        s6_contrib = +0.5; signals.append(f"{d2['date']} OI build +{d2['oi_chg']:.1f}% + Price↑")
    elif d2["oi_chg"] > 2 and price_sign < 0:
        s6_contrib = -0.5; signals.append(f"{d2['date']} OI build +{d2['oi_chg']:.1f}% + Price↓")
    score += s6_contrib

    # ── Triple Convergence — OI-gated (v2 fix) ──
    pcr_sign = directional_sign(pcr_change, 0.0)
    tc = {
        "price_up": price_sign > 0, "oi_up": oi_sign > 0, "pcr_up": pcr_sign > 0,
        "price_down": price_sign < 0, "oi_down": oi_sign < 0, "pcr_down": pcr_sign < 0,
    }
    if oi_sign > 0 and price_sign > 0 and pcr_sign > 0:
        tc["direction"] = "long"; tc["status"] = "★★★ TRIPLE CONVERGENCE (LONG)"; tc["count"] = 3
    elif oi_sign > 0 and price_sign < 0 and pcr_sign < 0:
        tc["direction"] = "short"; tc["status"] = "★★★ TRIPLE CONVERGENCE (SHORT)"; tc["count"] = 3
    else:
        # Count bullish or bearish alignment without TC status
        long_count = sum([tc["price_up"], tc["oi_up"], tc["pcr_up"]])
        short_count = sum([tc["price_down"], tc["oi_down"], tc["pcr_down"]])
        if long_count >= short_count:
            tc["direction"] = "long" if long_count >= 2 else "none"
            tc["count"] = long_count
            tc["status"] = f"★★ DOUBLE (long)" if long_count == 2 else (f"★ SINGLE" if long_count == 1 else "○ NONE")
        else:
            tc["direction"] = "short" if short_count >= 2 else "none"
            tc["count"] = short_count
            tc["status"] = f"★★ DOUBLE (short)" if short_count == 2 else (f"★ SINGLE" if short_count == 1 else "○ NONE")

    # ── Tier — symmetric signed thresholds ──
    s = score
    if s >= 9:       tier, sign = "TIER 1 — STRONG ACCUMULATION", "bullish"
    elif s >= 7:     tier, sign = "TIER 2 — ACCUMULATION", "bullish"
    elif s >= 5:     tier, sign = "TIER 3 — BUILDING LONG", "bullish"
    elif s >= 3:     tier, sign = "WATCH (mild bullish)", "bullish"
    elif s > -3:     tier, sign = "NO SIGNAL", "neutral"
    elif s > -5:     tier, sign = "WATCH (mild bearish)", "bearish"
    elif s > -7:     tier, sign = "TIER 3 — BUILDING SHORT", "bearish"
    elif s > -9:     tier, sign = "TIER 2 — DISTRIBUTION", "bearish"
    else:            tier, sign = "TIER 1 — STRONG DISTRIBUTION", "bearish"

    # ── Phase classification — explicit if/elif/.../else (ghost-phase protection) ──
    phase = _classify_phase(interp, avg_del, fut_oi_chg, price_sign, pcr_change)

    return SymbolResult(
        symbol=sym, score=round(s, 2), score_sign=sign, tier=tier, rank=0,
        date_d1=d1["date"], date_d2=d2["date"],
        price_chg_pct=price_chg, price_sign=price_sign,
        pcr_d1=pcr_d1, pcr_d2=pcr_d2, pcr_chg=pcr_change,
        fut_oi_chg_pct=round(fut_oi_chg, 2), oi_sign=oi_sign,
        avg_del=round(avg_del, 3), peak_del=peak_del, del_chg=round(del_chg, 3),
        avg_vol=round(avg_vol, 3),
        call_oi_growth_pct=round(call_g, 2), put_oi_growth_pct=round(put_g, 2),
        opt_oi_growth_pct=round(opt_g, 2),
        interpretation=interp, triple_convergence=tc, phase=phase, signals=signals,
    )


def _classify_phase(interp: str, avg_del: float, fut_oi_chg: float,
                    price_sign: int, pcr_chg: float) -> str:
    """Explicit if/elif chain. no_signal is the guaranteed terminal branch."""
    # Bullish phases (most specific first)
    if "NEW LONGS" in interp and avg_del >= 1.0:
        return "phase_2_long"
    if avg_del >= 0.70 and fut_oi_chg > 0 and price_sign > 0:
        return "phase_1_long"
    if pcr_chg > 0.05 and fut_oi_chg <= 0 and price_sign >= 0:
        return "pre_phase_1_long"
    # Bearish phases (mirror)
    if "NEW SHORTS" in interp and avg_del >= 1.0:
        return "phase_2_short"
    if avg_del >= 0.70 and fut_oi_chg > 0 and price_sign < 0:
        return "phase_1_short"
    if pcr_chg < -0.05 and fut_oi_chg <= 0 and price_sign <= 0:
        return "pre_phase_1_short"
    # Ghost-phase protection: terminal else
    return "no_signal"


PHASE_DESCRIPTIONS = {
    "phase_2_long": "Futures leverage stage — new longs being built with institutional-grade delivery (≥1.0x). Cash accumulation done; institutions now using futures for leveraged upside.",
    "phase_1_long": "Cash accumulation stage — delivery above normal (≥0.70x), futures OI building, price rising. Core positions still being filled.",
    "pre_phase_1_long": "Derivatives leading cash — PCR rising (+0.05+) without futures OI build yet. Put writers creating a floor before cash market confirms.",
    "phase_2_short": "Short leverage stage — new shorts being built with institutional-grade delivery (≥1.0x). Distribution confirmed; futures being used for leveraged downside.",
    "phase_1_short": "Distribution stage — delivery above normal (≥0.70x), futures OI building, price falling. Institutions offloading into liquidity.",
    "pre_phase_1_short": "Derivatives leading cash (bearish) — PCR collapsing (-0.05+) without futures OI build yet. Put writers abandoning floor before cash market sells off.",
    "no_signal": "No clear positioning phase — signals inconclusive or consolidating.",
}


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5 — OUTPUT EMITTER (Hybrid Markdown + JSON)
# ─────────────────────────────────────────────────────────────────────────────

def resolve_output_path(input_path: Path) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = input_path.parent / f"fno_analysis_{input_path.stem}_{ts}.md"
    if not base.exists(): return base
    n = 2
    while True:
        c = input_path.parent / f"fno_analysis_{input_path.stem}_{ts}_v{n}.md"
        if not c.exists(): return c
        n += 1


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def emit_output(results: list[SymbolResult], meta: dict, warnings: list, out_path: Path) -> None:
    # Sort by absolute score so top bullish AND top bearish both surface
    results.sort(key=lambda r: abs(r.score), reverse=True)
    for i, r in enumerate(results, 1):
        r.rank = i

    phase_map: dict[str, list[str]] = {k: [] for k in PHASE_DESCRIPTIONS}
    for r in results:
        phase_map.setdefault(r.phase, []).append(r.symbol)

    # Separate leaderboards by sign
    bullish_sorted = sorted([r for r in results if r.score > 0], key=lambda r: r.score, reverse=True)
    bearish_sorted = sorted([r for r in results if r.score < 0], key=lambda r: r.score)

    payload = {
        "meta": {**meta, "model_version": MODEL_VERSION,
                 "model_changes_from_v1": [
                     "Signed symmetric scoring (was long-biased)",
                     "Delivery gated by price direction (fixes distribution-as-accumulation)",
                     "Triple Convergence requires OI expansion (fixes short-cover false TC)",
                     "Volume safety rail (zero when Signal 2 = Consolidation)",
                     "6 phase map (3 long + 3 short) with ghost-phase protection",
                 ],
                 "known_limitations": [
                     "PCR <0.40 during parabolic crash may be oversold bounce, not true bearish",
                     "Short Covering and Long Liquidation are lagging, not leading",
                     "No market context (Nifty trend) integration — planned for v3",
                     "No multi-day smoothing — requires input schema expansion (v3)",
                 ]},
        "phase_descriptions": PHASE_DESCRIPTIONS,
        "rankings": [asdict(r) for r in results],
        "triple_convergence": [{"symbol": r.symbol, **r.triple_convergence} for r in results],
        "phase_map": phase_map,
        "warnings": warnings,
    }

    md = [
        "# F&O Accumulation Analysis (v2.0)", "",
    ]
    if meta.get("input_mode") == "folder_combine":
        md.append(f"- **Input mode:** Folder combine (auto-discovered 2 daily files)")
        md.append(f"- **Input directory:** `{meta['input_directory']}`")
        md.append(f"- **Files combined:**")
        for f_info in meta["input_files"]:
            md.append(f"  - `{f_info['file']}` (date {f_info['date']}, SHA-256 `{f_info['sha256'][:16]}…`)")
        md.append(f"- **Combined SHA-256:** `{meta['combined_sha256']}`")
    else:
        md.append(f"- **Input mode:** Single combined file")
        md.append(f"- **Input:** `{meta['input_file']}`")
        md.append(f"- **SHA-256:** `{meta['input_sha256']}`")
    md += [
        f"- **Generated:** {meta['generated_at']}",
        f"- **Dates analyzed:** {meta['dates']}",
        f"- **Symbols analyzed:** {meta['symbols_analyzed']} | **Skipped:** {len(warnings)}",
        f"- **Model version:** {MODEL_VERSION}", "",
        "## Methodology (v2.0 — symmetric)", "",
        "Signed multi-signal scoring: positive scores = accumulation; negative scores = distribution. "
        "Signals: PCR level & trajectory, Futures OI × Price (four quadrants), Delivery gated by price direction, "
        "Volume (amplifier, suppressed during Consolidation), Options OI growth & lean, single-day OI surge. "
        "Triple Convergence requires OI expansion — Price↑+PCR↑ without OI↑ is Short Covering, not TC.", "",
        "## Tier Thresholds (Signed)", "",
        "| Score Range | Tier |", "|---|---|",
        "| ≥ +9 | TIER 1 — STRONG ACCUMULATION |",
        "| +7 to +8.9 | TIER 2 — ACCUMULATION |",
        "| +5 to +6.9 | TIER 3 — BUILDING LONG |",
        "| +3 to +4.9 | WATCH (mild bullish) |",
        "| −2.9 to +2.9 | NO SIGNAL |",
        "| −3 to −4.9 | WATCH (mild bearish) |",
        "| −5 to −6.9 | TIER 3 — BUILDING SHORT |",
        "| −7 to −8.9 | TIER 2 — DISTRIBUTION |",
        "| ≤ −9 | TIER 1 — STRONG DISTRIBUTION |", "",
        "## Top 15 Bullish Leaders", "",
        "| Rank | Symbol | Score | Tier | Price% | PCR | PCRΔ | AvgDel | FutOI% | Phase | Interpretation |",
        "|---:|:---|---:|:---|---:|:---:|---:|---:|---:|:---|:---|",
    ]
    for r in bullish_sorted[:15]:
        md.append(f"| {r.rank} | {r.symbol} | {r.score:+.1f} | {r.tier} | {r.price_chg_pct:+.2f}% | "
                  f"{r.pcr_d1:.2f}→{r.pcr_d2:.2f} | {r.pcr_chg:+.2f} | {r.avg_del:.2f}x | "
                  f"{r.fut_oi_chg_pct:+.1f}% | {r.phase} | {r.interpretation} |")
    md += ["", "## Top 15 Bearish Leaders", "",
           "| Rank | Symbol | Score | Tier | Price% | PCR | PCRΔ | AvgDel | FutOI% | Phase | Interpretation |",
           "|---:|:---|---:|:---|---:|:---:|---:|---:|---:|:---|:---|"]
    for r in bearish_sorted[:15]:
        md.append(f"| {r.rank} | {r.symbol} | {r.score:+.1f} | {r.tier} | {r.price_chg_pct:+.2f}% | "
                  f"{r.pcr_d1:.2f}→{r.pcr_d2:.2f} | {r.pcr_chg:+.2f} | {r.avg_del:.2f}x | "
                  f"{r.fut_oi_chg_pct:+.1f}% | {r.phase} | {r.interpretation} |")

    md += ["", "## Phase Map", ""]
    for phase, desc in PHASE_DESCRIPTIONS.items():
        syms = phase_map.get(phase, [])
        md.append(f"### `{phase}` ({len(syms)})")
        md.append(f"_{desc}_")
        md.append("")
        md.append(f"{', '.join(syms) if syms else '(none)'}")
        md.append("")

    if warnings:
        md += ["## Warnings (Skipped Symbols)", ""]
        for w in warnings:
            md.append(f"- `{w.get('symbol','?')}`: {w.get('reason','?')}")
        md.append("")

    md += ["## Structured Data (re-analysis payload)", "", "```json",
           json.dumps(payload, indent=2, default=str), "```", ""]
    out_path.write_text("\n".join(md), encoding="utf-8")


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 6 — MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main() -> int:
    script_dir = Path(__file__).resolve().parent
    logger = setup_logger(script_dir)
    print("=" * 70)
    print(f"  F&O Accumulation Analyzer v{MODEL_VERSION}")
    print("=" * 70)
    print("Input mode:")
    print("  [1] Single combined CSV/XLSX (2 dates per symbol in one file)")
    print("  [2] Folder with 2 single-day CSVs (auto-combine then analyze)")
    mode = input("Enter choice [1/2]: ").strip()
    if mode not in ("1", "2"):
        print("ERROR: Invalid choice. Enter 1 or 2.")
        return 1

    try:
        if mode == "1":
            raw = input("Enter path to Derivative Analytics CSV/XLSX: ").strip().strip('"').strip("'")
            if not raw:
                print("ERROR: No path provided."); return 1
            input_path = Path(os.path.expanduser(raw)).resolve()
            if not input_path.exists() or not input_path.is_file():
                print(f"ERROR: File not found: {input_path}"); return 1

            log_event(logger, "info", "run_start",
                      mode="combined_file", input=str(input_path), model_version=MODEL_VERSION)
            rows, skipped_rows = load_input(input_path, logger)
            output_dir = input_path.parent
            output_stem = input_path.stem
            input_meta = {
                "input_file": input_path.name,
                "input_sha256": sha256_file(input_path),
                "input_mode": "combined_file",
            }
            discovered_files = None

        else:  # mode == "2"
            raw = input("Enter directory containing 2 daily Derivative_Analytics_*.csv files: ").strip().strip('"').strip("'")
            if not raw:
                print("ERROR: No path provided."); return 1
            directory = Path(os.path.expanduser(raw)).resolve()
            if not directory.exists() or not directory.is_dir():
                print(f"ERROR: Not a directory: {directory}"); return 1

            log_event(logger, "info", "run_start",
                      mode="folder_combine", directory=str(directory), model_version=MODEL_VERSION)
            rows, skipped_rows, discovered_files = load_from_folder(directory, logger)
            print(f"\nFound 2 dated file(s):")
            for p, d in discovered_files:
                print(f"  • {p.name} → {d}")
            print()
            output_dir = directory
            output_stem = f"combined_{discovered_files[0][1]}_to_{discovered_files[1][1]}"
            # Combined hash of both input files for audit trail
            combined_h = hashlib.sha256()
            file_hashes = []
            for p, d in discovered_files:
                h = sha256_file(p)
                combined_h.update(h.encode())
                file_hashes.append({"file": p.name, "date": str(d), "sha256": h})
            input_meta = {
                "input_mode": "folder_combine",
                "input_directory": str(directory),
                "input_files": file_hashes,
                "combined_sha256": combined_h.hexdigest(),
            }

        # Shared downstream path — identical for both modes
        pairs, pair_warnings = pair_by_symbol(rows, logger)
        results = [score_symbol(sym, pair) for sym, pair in pairs.items()]
        dates_set = sorted({r["date"] for r in rows})

        meta = {
            **input_meta,
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "dates": dates_set,
            "symbols_analyzed": len(results),
            "rows_skipped_blank": len(skipped_rows),
        }
        warnings = skipped_rows + pair_warnings

        # Output path resolution — auto-suffix, never overwrite
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        candidate = output_dir / f"fno_analysis_{output_stem}_{ts}.md"
        if candidate.exists():
            n = 2
            while True:
                candidate = output_dir / f"fno_analysis_{output_stem}_{ts}_v{n}.md"
                if not candidate.exists():
                    break
                n += 1
        out_path = candidate

        emit_output(results, meta, warnings, out_path)
        log_event(logger, "info", "run_complete", output=str(out_path), symbols=len(results))
        print(f"\n✓ Analyzed {len(results)} symbols | Skipped: {len(warnings)}")
        print(f"✓ Output written: {out_path}")
        return 0
    except Exception as e:
        log_event(logger, "error", "run_failed", error=str(e), error_type=type(e).__name__)
        print(f"ERROR: {e}"); return 2


if __name__ == "__main__":
    sys.exit(main())
