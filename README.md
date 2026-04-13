# F&O Accumulation Analyzer

Offline Python CLI tools that ingest NSE F&O derivative analytics CSV/XLSX sheets and emit hybrid **Markdown + JSON** analysis files containing symmetric multi-signal accumulation/distribution scores, Triple Convergence detection, phase classification, and — for the 7-day edition — rolling window trajectory and regime analysis for every F&O stock in the input.

The output files are designed to be pasted directly back into an LLM for re-analysis without the LLM needing to re-do any arithmetic. The Markdown half carries human-readable context; the embedded JSON block carries the full structured payload for programmatic consumption.

---

## 1. Project Layout

```
fno_accumulation_analyzer/
│
├── fno_analyzer.py              # v2.0.1 — 2-date analyzer with dual input modes
│                                #           [1] combined CSV  [2] folder of 2 single-day CSVs
├── fno_analyzer_7day.py         # v2.1 — 7-day multi-window analyzer (directory input)
│
├── pyproject.toml               # Explicit [build-system] (Rule #22)
├── requirements.in              # Top-level deps source for pip-compile
├── requirements.txt             # Hash-pinned lockfile (generated, Rule #20)
├── README.md                    # This file
│
└── logs/                        # Auto-created on first run
    ├── fno_analyzer_YYYY-MM-DD.log
    └── fno_analyzer_7day_YYYY-MM-DD.log
```

Input data files and output analysis files live **outside** this project folder, in whatever directory holds your daily F&O exports.

---

## 2. Which Tool to Use

| Scenario | Use |
|---|---|
| One combined CSV with 2 dates per symbol (has `Date` column) | `fno_analyzer.py` — mode [1] |
| Two single-day CSVs in a folder (no `Date` column) | `fno_analyzer.py` — mode [2] (folder combine) |
| Multiple single-day CSVs, want trajectory/regime analysis | `fno_analyzer_7day.py` |
| Latest positioning signal only | `fno_analyzer.py` (either mode) or `fno_analyzer_7day.py` — all produce identical latest-window scores |
| Need to detect sustained patterns vs one-day events | `fno_analyzer_7day.py` — only this has persistence metrics |

The two scripts are independent. v2.1 is not a replacement for v2.0.1; they serve different analytical scopes.

---

## 3. Setup (One-Time)

### 3.1 Virtual environment (Rule #12)

```bash
python -m venv .venv
source .venv/bin/activate          # Linux/macOS
# .venv\Scripts\activate           # Windows PowerShell
```

### 3.2 Generate hash-pinned lockfile (Rule #20)

```bash
pip install --only-binary :all: pip-tools
pip-compile --generate-hashes --output-file=requirements.txt requirements.in
```

### 3.3 Install (Rule #19 — wheels only)

```bash
pip install --only-binary :all: --require-hashes -r requirements.txt
```

Development-only (not reproducible):

```bash
pip install --only-binary :all: pandas openpyxl
```

---

## 4. Usage

### 4.1 v2.0.1 — Two-Date Analyzer (Two Input Modes)

```bash
python fno_analyzer.py
```

The script asks you to choose one of two input modes at startup:

```
======================================================================
  F&O Accumulation Analyzer v2.0.1
======================================================================
Input mode:
  [1] Single combined CSV/XLSX (2 dates per symbol in one file)
  [2] Folder with 2 single-day CSVs (auto-combine then analyze)
Enter choice [1/2]:
```

#### Mode [1] — Single Combined File

Use this when you already have **one CSV/XLSX with both dates** in it (rows include a `Date` column, 2 rows per symbol).

```
Enter choice [1/2]: 1
Enter path to Derivative Analytics CSV/XLSX: /path/to/Derivative_Analytics_9_10.csv

✓ Analyzed 213 symbols | Skipped: 0
✓ Output written: /path/to/fno_analysis_Derivative_Analytics_9_10_20260413_143210.md
```

#### Mode [2] — Folder Combine

Use this when you have **two single-day CSV files** (one row per symbol, no `Date` column — date comes from the filename). The script auto-discovers files matching `Derivative_Analytics_DD-Mon-YYYY.*` in the directory, picks the **2 most recent** by date, merges them in-memory, and scores the pair.

```
Enter choice [1/2]: 2
Enter directory containing 2 daily Derivative_Analytics_*.csv files: /path/to/FNO_Data

Found 2 dated file(s):
  • Derivative_Analytics_09-Apr-2026.csv → 2026-04-09
  • Derivative_Analytics_10-Apr-2026.csv → 2026-04-10

✓ Analyzed 213 symbols | Skipped: 0
✓ Output written: /path/to/FNO_Data/fno_analysis_combined_2026-04-09_to_2026-04-10_20260413_143210.md
```

**Folder-mode behavior rules:**

| Scenario | Behavior |
|---|---|
| More than 2 dated files in folder | Picks the **2 most recent** by filename date; older files ignored |
| Exactly 2 dated files | Uses both |
| Only 1 dated file | **Errors out** — `"Found 1 dated file(s)... need at least 2 for 2-date analysis"` |
| No matching files | **Errors out** — same message with 0 count |
| Files that don't match pattern | Silently ignored (logged in audit log) |

**Folder-mode does NOT write a merged CSV to disk.** The combine happens in-memory only; your input directory stays clean. The output `.md` is written alongside the input files, with both source files' SHA-256 hashes plus a combined hash in the `meta` block for audit.

### 4.2 v2.1 — Seven-Day Multi-Window Analyzer

```bash
python fno_analyzer_7day.py
```

Prompts once for a **directory**. Auto-discovers files matching `Derivative_Analytics_DD-Mon-YYYY.*`, sorts by date, picks 7 most recent:

```
========================================================================
  F&O 7-Day Accumulation Analyzer v2.1
========================================================================
Enter directory containing Derivative_Analytics_*.csv/xlsx files: /path/to/FNO_Data

Found 7 file(s):
  • Derivative_Analytics_04-Apr-2026.csv → 2026-04-04
  • Derivative_Analytics_05-Apr-2026.csv → 2026-04-05
  • Derivative_Analytics_08-Apr-2026.csv → 2026-04-08
  • Derivative_Analytics_09-Apr-2026.csv → 2026-04-09
  • Derivative_Analytics_10-Apr-2026.csv → 2026-04-10
  • Derivative_Analytics_11-Apr-2026.csv → 2026-04-11
  • Derivative_Analytics_12-Apr-2026.csv → 2026-04-12

✓ Analyzed 213 symbols across 7 days | Skipped: 0
✓ Output written: /path/to/FNO_Data/fno_7day_analysis_2026-04-04_to_2026-04-12_20260413_143210.md
```

Both scripts write output **alongside the input** with auto-suffix (`_v2`, `_v3`, …) if a file with the same timestamp exists. **Scripts never overwrite prior analyses.**

---

## 5. Input Schema

Both scripts use **name-based column access**; extra columns (`Lot Size`, `Close`, etc.) are silently ignored. Required columns (exact header names):

| Column | Type | Description | v2.0 | v2.1 |
|---|---|---|:---:|:---:|
| `Date` | `DD-MMM-YY` | Trading date (e.g., `09-Apr-26`) | ✅ | ❌ (from filename) |
| `Symbol` | string | NSE F&O symbol | ✅ | ✅ |
| `Chg %` | float | **Pre-computed** price change % | ✅ | ✅ |
| `Cumulative Future OI` | int | Total futures open interest | ✅ | ✅ |
| `OI Chg %` | float | Day-level futures OI change % | ✅ | ✅ |
| `Volume (Times)` | float | Volume ratio vs average | ✅ | ✅ |
| `Delivery (Times)` | float | Delivery ratio vs average | ✅ | ✅ |
| `Cumulative Call OI` | int | Total call OI | ✅ | ✅ |
| `Cumulative Put OI` | int | Total put OI | ✅ | ✅ |
| `Put Call Ratio (PCR)` | float | PCR on that date | ✅ | ✅ |
| `PCR Change 1D` | float | **Pre-computed** PCR delta | ✅ | ✅ |

### 5.1 v2.0 Row Expectations

Exactly **2 rows per symbol**, one per date. Symbols with 0, 1, or 3+ rows are logged as warnings and excluded. Blank rows and rows missing critical fields (`Symbol`, `Date`, `Chg %`, `PCR`, `Cumulative Future OI`) dropped silently.

### 5.2 v2.1 Filename Pattern

Input files must match: `Derivative_Analytics_<day>-<mon>-<year>.<csv|xlsx>`

The regex tolerates spaces, dashes, or underscores between tokens. Case-insensitive. Valid examples:

- `Derivative_Analytics_01-Apr-2026.csv`
- `derivative analytics 10 apr 26.xlsx`
- `Derivative-Analytics_12-Apr-2026.csv`

Files not matching the pattern are silently ignored (logged in audit log). Each day's file contains **one row per symbol** — no `Date` column needed, date comes from filename.

### 5.3 v2.1 Tolerant Mode

If fewer than 7 matching files are found:
- **≥ 3 files**: Runs with prominent warning in Markdown header and `meta.data_completeness_warning` JSON field
- **< 3 files**: Refuses to run

Symbols missing from some days are included if they appear in ≥ 2 days total.

### 5.4 v2.1 Expiry Detection

If the window contains an NSE monthly F&O expiry (last Thursday of any month within range), a prominent warning is surfaced in both Markdown and JSON. Futures OI interpretation across expiry should be treated with caution due to natural position rollover.

---

## 6. Scoring Methodology (v2.0 Engine — Frozen, Symmetric)

Both scripts use the same underlying engine. Each 2-day window produces a **signed score**: positive = accumulation, negative = distribution, magnitude = conviction.

### 6.1 Signal 1a — PCR Level (on d2)

| PCR_d2 | Score | Meaning |
|---|---:|---|
| ≥ 1.00 | **+3** | Put writers dominant (strongest bullish) |
| 0.85 – 0.99 | **+2** | Approaching bullish zone |
| 0.75 – 0.84 | **+1** | Neutral-to-bullish |
| 0.55 – 0.74 | **0** | Neutral |
| 0.40 – 0.54 | **−2** | Call writers dominant (bearish ceiling) |
| < 0.40 | **−3** | Heavy call writing (strongest bearish) |

### 6.2 Signal 1b — PCR Trajectory

| PCR Chg 1D | Score |
|---|---:|
| > +0.08 | **+2** (surging) |
| +0.03 to +0.08 | **+1** (rising) |
| −0.03 to +0.03 | **0** |
| −0.08 to −0.03 | **−1** (easing) |
| < −0.08 | **−2** (collapsing) |

### 6.3 Signal 2 — Futures OI × Price (Four Quadrants)

`fut_oi_chg_pct = (oi_d2 − oi_d1) / oi_d1 × 100`

| OI Direction | Price Direction | Score | Classification |
|---|---|---:|---|
| > +2% | > +0.5% | **+3** | ★ NEW LONGS (Bullish) |
| > 0 | > 0 | **+2** | Mild long build |
| > +2% | < −0.5% | **−3** | ⚠ NEW SHORTS (Bearish) |
| > 0 | < 0 | **−2** | Mild short build |
| < −2% | > +0.5% | **+1** | ↑ Short Covering (Weak Bull, lagging) |
| < −2% | < −0.5% | **−2** | ↓ Long Liquidation (Bearish, lagging) |
| otherwise | otherwise | **0** | → Consolidation |

### 6.4 Signal 3 — Delivery (Gated by Price Direction)

| Avg Delivery | Price ↑ | Price Flat (±0.3%) | Price ↓ |
|---|---:|---:|---:|
| ≥ 1.0x | **+3** Accumulation | **+1** Ambiguous | **−3** Distribution |
| 0.70 – 0.99x | **+2** | **+0.5** | **−2** |
| 0.50 – 0.69x | **+1** | **0** | **−1** |
| < 0.50x | **0** | **0** | **0** |

**Acceleration / peak bonus:**
- Delivery change > +0.3 + price ↑ → **+1** / + price ↓ → **−1**
- Peak delivery ≥ 1.5x + price ↑ → **+1** / + price ↓ → **−1**

### 6.5 Signal 4 — Volume (with Safety Rail)

Volume amplifies direction established by Signal 2. If Signal 2 = Consolidation, Signal 4 contributes **0** regardless of magnitude.

| Avg Volume | Score |
|---|---:|
| ≥ 1.5x | **±1** (sign follows Signal 2) |
| 1.0 – 1.49x | **±0.5** |
| < 1.0x | **0** |

### 6.6 Signal 5 — Options OI Growth & Lean

- Put OI growth > Call OI growth AND Put growth > +5% → bullish lean (**+1**)
- Call OI growth > Put OI growth AND Call growth > +5% → bearish lean (**−1**)

Lean adds **±0.5**. Total options OI growth additional bonus:

| Total Options OI Growth | Score |
|---|---:|
| > +15% | **±1** (sign follows lean) |
| +5% to +15% | **±0.5** (sign follows lean) |

### 6.7 Signal 6 — Single-Day OI Surge on d2 (Gated by Price)

| OI Chg % on d2 | Price Direction | Score |
|---|---|---:|
| > +5% | ↑ | **+1** |
| > +5% | ↓ | **−1** |
| +2% to +5% | ↑ | **+0.5** |
| +2% to +5% | ↓ | **−0.5** |

### 6.8 Tier Thresholds (Signed)

| Score Range | Tier |
|---|---|
| ≥ +9 | **TIER 1 — STRONG ACCUMULATION** |
| +7 to +8.9 | **TIER 2 — ACCUMULATION** |
| +5 to +6.9 | **TIER 3 — BUILDING LONG** |
| +3 to +4.9 | **WATCH (mild bullish)** |
| −2.9 to +2.9 | **NO SIGNAL** |
| −3 to −4.9 | **WATCH (mild bearish)** |
| −5 to −6.9 | **TIER 3 — BUILDING SHORT** |
| −7 to −8.9 | **TIER 2 — DISTRIBUTION** |
| ≤ −9 | **TIER 1 — STRONG DISTRIBUTION** |

### 6.9 Triple Convergence (OI-Gated)

TC fires **only** when OI expansion accompanies the other two signals. Without new positions being created, Price↑ + PCR↑ is just sentiment noise.

- **★★★ TC (LONG)**: Price↑ + OI↑ + PCR↑
- **★★★ TC (SHORT)**: Price↓ + OI↑ + PCR↓

All other combinations downgrade to `★★ DOUBLE`, `★ SINGLE`, or `○ NONE` with a direction label.

### 6.10 Phase Classification (Ghost-Phase Protected)

Every symbol falls into exactly one of 7 phases. Explicit if/elif chain with `no_signal` as guaranteed terminal `else`.

| Phase | Condition |
|---|---|
| `phase_2_long` | Interpretation contains "NEW LONGS" AND avg delivery ≥ 1.0x |
| `phase_1_long` | Avg delivery ≥ 0.70x AND fut_oi_chg > 0 AND price ↑ |
| `pre_phase_1_long` | PCR Chg > +0.05 AND fut_oi_chg ≤ 0 AND price ≥ 0 |
| `phase_2_short` | Interpretation contains "NEW SHORTS" AND avg delivery ≥ 1.0x |
| `phase_1_short` | Avg delivery ≥ 0.70x AND fut_oi_chg > 0 AND price ↓ |
| `pre_phase_1_short` | PCR Chg < −0.05 AND fut_oi_chg ≤ 0 AND price ≤ 0 |
| `no_signal` | None of the above |

Each phase carries a one-line description in both Markdown and the `phase_descriptions` JSON block.

---

## 7. v2.1 Additional Metrics (7-Day Trajectory)

v2.1 applies the v2.0 engine to **all adjacent 2-day windows** within the input range (6 windows for 7 days), then computes trajectory metrics:

| Metric | Definition | Purpose |
|---|---|---|
| `window_scores` | Array of signed scores, one per rolling window | Raw per-window breakdown |
| `bullish_windows` | Count of windows scoring ≥ +3 | How many days had accumulation signal |
| `bearish_windows` | Count of windows scoring ≤ −3 | How many days had distribution signal |
| `neutral_windows` | Count of remaining windows | Indecision count |
| `persistence_score` | Recency-weighted mean of window scores | Latest windows weighted heaviest |
| `pcr_slope_7d` | Linear regression slope of PCR across days | PCR trend direction |
| `pcr_first`, `pcr_last` | PCR values at window endpoints | Net PCR change |
| `days_delivery_institutional` | Count of days with delivery ≥ 1.0x | Sustained vs one-day event |
| `days_delivery_above_normal` | Count of days with delivery ≥ 0.70x | Broader accumulation persistence |
| `cumulative_oi_chg_pct_window` | Net futures OI change across full window | Multi-day OI trend |
| `cumulative_price_chg_pct_window` | Compounded price change across window | Net directional move |
| `regime` | Classification (see below) | One-word persistence summary |

### Regime Classification

| Regime | Condition |
|---|---|
| **SUSTAINED BULLISH** | ≥60% of windows scored ≥ +3 |
| **SUSTAINED BEARISH** | ≥60% of windows scored ≤ −3 |
| **MIXED BULLISH-LEANING** | More bullish windows than bearish |
| **MIXED BEARISH-LEANING** | More bearish windows than bullish |
| **CHOPPY / INDECISIVE** | Equal bullish and bearish windows |

The **latest window** (day 6 → day 7) provides the actionable "what's happening now" signal — identical semantics to v2.0. Trajectory metrics reveal whether that latest signal is a one-session event or a sustained pattern.

---

## 8. Output File Structure

### 8.1 Filenames

- **v2.0.1 mode [1]** (combined file): `fno_analysis_<input_stem>_<YYYYMMDD_HHMMSS>.md`
- **v2.0.1 mode [2]** (folder combine): `fno_analysis_combined_<date1>_to_<date2>_<YYYYMMDD_HHMMSS>.md`
- **v2.1**: `fno_7day_analysis_<start_date>_to_<end_date>_<YYYYMMDD_HHMMSS>.md`

All outputs are written **alongside the input(s)** — never into the project folder. Auto-suffix (`_v2`, `_v3`, …) is applied if two runs collide at the same second.

### 8.2 Markdown Sections

**v2.0:**
1. Header — input file, SHA-256, timestamp, dates, symbol counts, model version
2. Tier thresholds reference
3. Top 15 Bullish Leaders (table)
4. Top 15 Bearish Leaders (table)
5. Phase Map (all 7 phases with inline descriptions)
6. Warnings (if any)
7. **Fenced JSON block** — full payload

**v2.1:** Same as v2.0 plus:
- Data completeness warning (if < 7 days)
- Expiry warning (if NSE monthly expiry in window)
- Per-file SHA-256 + combined hash
- Scoring strategy explanation
- Regime classification reference
- **Top 10 Sustained-Bullish Persistence**
- **Top 10 Sustained-Bearish Persistence**
- Trajectory columns in all tables (regime, window counts, persistence, PCR slope, cumulative OI)

### 8.3 JSON Schema (v2.1)

```json
{
  "meta": {
    "input_directory": "...",
    "days_used": 7,
    "input_files": [{"file": "...", "date": "...", "sha256": "..."}, ...],
    "combined_sha256": "...",
    "generated_at": "2026-04-13T14:32:10",
    "symbols_analyzed": 213,
    "data_completeness_warning": null,
    "expiry_warning": null,
    "expiry_dates_detected": [],
    "model_version": "2.1",
    "scoring_strategy": "C — rolling 2-day windows (v2 engine) + 7-day trajectory",
    "known_limitations": [...]
  },
  "phase_descriptions": { "phase_2_long": "...", ... },
  "rankings": [
    {
      "rank": 1,
      "symbol": "NAM-INDIA",
      "days_available": 7,
      "latest_score": 16.0,
      "latest_tier": "TIER 1 — STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "★ NEW LONGS (Bullish)",
      "latest_triple_convergence": {...},
      "latest_date_d1": "2026-04-11",
      "latest_date_d2": "2026-04-12",
      "trajectory": {
        "window_scores": [...],
        "bullish_windows": 6, "bearish_windows": 0, "neutral_windows": 0,
        "persistence_score": 13.5,
        "pcr_slope_7d": 0.08, "pcr_first": 0.52, "pcr_last": 1.42,
        "days_delivery_institutional": 5,
        "cumulative_oi_chg_pct_window": 18.2,
        "cumulative_price_chg_pct_window": 7.1,
        "regime": "SUSTAINED BULLISH"
      },
      "all_windows": [ /* full per-window scoring breakdown with all signals */ ],
      "daily_timeline": [ /* per-day raw snapshots */ ]
    }
  ],
  "phase_map": { "phase_2_long": [...], ... },
  "warnings": [...]
}
```

v2.0 JSON is a subset — no `trajectory`, `all_windows`, or `daily_timeline` (single window only).

JSON contains every computed value plus raw daily snapshots, so a downstream reader can re-challenge any conclusion or apply alternate scoring weights without re-reading source CSVs.

---

## 9. Logging & Audit Trail (Rule #1)

Every run writes structured JSON lines to `logs/fno_analyzer_<YYYY-MM-DD>.log` or `logs/fno_analyzer_7day_<YYYY-MM-DD>.log`:

```json
{"ts":"2026-04-13 14:32:10,123","level":"INFO","msg":{"event":"run_start","directory":"...","model_version":"2.1"}}
{"ts":"2026-04-13 14:32:10,456","level":"INFO","msg":{"event":"files_discovered","total_matches":7,"selected":7,"selected_dates":["2026-04-04", ...]}}
{"ts":"2026-04-13 14:32:10,512","level":"INFO","msg":{"event":"day_loaded","file":"...","date":"2026-04-04","symbols":213}}
{"ts":"2026-04-13 14:32:11,234","level":"INFO","msg":{"event":"run_complete","output":"...","symbols":213}}
```

Each output file includes SHA-256 hash(es) of input file(s) in its meta block — tamper-evident linkage between input and analysis.

This is **not** a full append-only hash-chained audit table (Rule #24) — that level of rigor is appropriate for production compliance systems, not for a local analysis tool.

---

## 10. Security Notes

These tools do not and will not:

- Make any network calls (fully offline — Rules #26, #28, #30 moot)
- Read secrets from environment variables at build or install time (Rule #21)
- Hardcode credentials, keys, or endpoints (Rule #10)
- Execute arbitrary code from input CSVs (name-based column access, `safe_float` only parses numerics, no `eval`)

The only file-system access: read input files, write output Markdown alongside them, append to `logs/`.

---

## 11. Operational Rules Honoured

| Rule | Where |
|---|---|
| #1 Structured logging & audit logs | `setup_logger()`, JSON file handler, SHA-256 per input in meta |
| #2 Secure data ingestion | `safe_float`, `safe_str` helpers; blank-row tolerance; missing-column detection |
| #6 Confirm before implementing | Architecture + matrix discussions precede all code changes |
| #7 Test run after each code file | v2.0 validated on 213 symbols; v2.1 validated on 3-day test with manual spot-checks |
| #8 Confirm code final before docs | This README written only after v2.1 sign-off |
| #12 Virtual environment mandatory | Documented in Section 3 |
| #16 Robust error handling (IFERROR) | `safe_*` helpers + critical-field guards; fail-fast on missing columns |
| #18 Enterprise file structure | `logs/` dir, sectioned scripts, pyproject + requirements.in |
| #19 `--only-binary :all:` for pip | Documented in setup |
| #20 Hash-pinned dependencies | `requirements.txt` via `pip-compile --generate-hashes` |
| #21 No secrets in build/install | No secrets anywhere |
| #22 Explicit `[build-system]` | Present; both scripts as entry points |
| #23 Prefer packaged wheels | pandas + openpyxl both publish wheels |
| #31 Design for constraints | 2-day window = minimum viable for change-detection |
| #33 Design for failure | Graceful handling of missing days, symbols, blank rows, malformed dates |
| #35 Treat complexity as cost | Two focused scripts instead of one bloated multi-mode tool |
| #36 Code for the next human | Clear names, labeled sections, inline comments on weights |

---

## 12. Known Limitations

1. **PCR < 0.40 during parabolic crash** may be oversold bounce setup, not true bearish. Model calls it "strongest bearish"; treat with caution during capitulation phases.

2. **Short Covering and Long Liquidation are lagging indicators.** Price + OI moving in opposite directions typically marks the end of a move. Signal 2 labels these as "(lagging)" in the interpretation field.

3. **No market context (Nifty trend, sector breadth).** A stock scoring +12 in a crashing market differs meaningfully from +12 in a rising market. Model treats stocks in isolation. **Planned for v3.**

4. **No multi-day smoothing within a window.** 2-day windows are sensitive to single-day noise (fat-finger trades, expiry mechanics). v2.1 trajectory metrics partially compensate by surfacing persistence across windows.

5. **NSE monthly expiry within a window** (v2.1) distorts futures OI interpretation due to natural position rollover. Script detects and warns but does not mathematically correct.

6. **Exactly 2 rows per symbol required** (v2.0). Custom date ranges outside the script's expectations need pre-processing.

7. **Scoring weights are frozen.** Adjusting requires editing `score_window()` directly. Consistency across analyses matters more than per-run tuning.

8. **Only DD-Mon-YYYY filename pattern** (v2.1). Numeric-month patterns like `01-04-2026` not recognized.

---

## 13. Version

**v2.0.1 (fno_analyzer.py) + v2.1.0 (fno_analyzer_7day.py)** — 2026-04-13.

### Changelog

**v1.0.0** (2026-04-12) — Initial 2-date analyzer with long-biased scoring. Tested on 213-symbol NSE F&O dataset.

**v2.0.0** (2026-04-13) — Symmetric signed scoring. Key fixes:
- Delivery gated by price direction (fixes v1 distribution-as-accumulation bug)
- Triple Convergence requires OI expansion (fixes short-covering false TC)
- Volume safety rail (zero during Consolidation)
- 6-phase map (3 long + 3 short) with ghost-phase protection
- `directional_sign()` helper to prevent sign-flip bugs
- Backward compatible with v1 for purely bullish setups (NAM-INDIA 16.0 → 16.0)

**v2.0.1** (2026-04-13) — Added folder-combine input mode to `fno_analyzer.py`:
- Interactive prompt at startup to choose [1] combined file or [2] folder combine
- Mode [2] auto-discovers 2 single-day CSVs by filename pattern, picks 2 most recent, combines in-memory (no intermediate file written)
- Mode-aware Markdown header and JSON meta (`input_mode`, per-file SHA-256, combined hash)
- Scoring engine unchanged; both modes produce identical per-symbol scores for the same pair of dates

**v2.1.0** (2026-04-13) — Separate 7-day multi-window analyzer alongside v2.0.1:
- Directory auto-discovery of dated daily files
- Scoring strategy C: rolling 2-day windows through input range
- 7-day trajectory metrics (persistence, regime, PCR slope, delivery-days, cumulative OI)
- Tolerant mode (minimum 3 days) with visible completeness warning
- NSE monthly expiry detection and warning
- `fno_analyzer.py` and `fno_analyzer_7day.py` ship side-by-side as independent tools

### Validated Against

- **v2.0.1 mode [1]**: 213-symbol NSE F&O dataset (09-Apr-26 / 10-Apr-26). All symbols scored; zero warnings; math validated manually for NAM-INDIA (+16.0, Tier 1 Strong Accumulation) and COALINDIA (−15.5, Tier 1 Strong Distribution).
- **v2.0.1 mode [2]**: Same 213-symbol dataset split into 2 single-day CSVs in a test directory (including a 3-file folder to verify latest-2 selection, and a 1-file folder to verify error behavior). NAM-INDIA latest-window score identical to mode [1]: 16.0. Per-file + combined SHA-256 hashes correctly captured in meta.
- **v2.1**: 3-day tolerant-mode test (01-Apr, 09-Apr, 10-Apr). All 213 symbols produced rolling window scores; trajectory metrics computed; NAM-INDIA latest window matches v2.0.1 (16.0) confirming cross-script backward compatibility; expiry detection correctly identified no expiry in window.
