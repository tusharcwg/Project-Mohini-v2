# F&O 7-Day Accumulation Analysis (v2.1)

> ⚠ **Incomplete data — only 3 days available, not 7.**

- **Input directory:** `/tmp/test_7day`
- **Files analyzed (3):**
  - `Derivative_Analytics_01-Apr-2026.csv` (date 2026-04-01, SHA-256 `cb3362da62aca229…`)
  - `Derivative_Analytics_09-Apr-2026.csv` (date 2026-04-09, SHA-256 `50adb1bb1481d7e6…`)
  - `Derivative_Analytics_10-Apr-2026.csv` (date 2026-04-10, SHA-256 `8561d2dacd1c9718…`)
- **Combined hash:** `602bc244854eb2f3847e3be1550674446d4d934e2b8bbafee612940ca02f1bef`
- **Generated:** 2026-04-13T04:31:49
- **Symbols with ≥2 days:** 213 | **Skipped:** 1
- **Rolling windows per symbol:** up to 2

## Scoring Strategy (C — Rolling Multi-Window)

Each symbol is scored across all adjacent 2-day windows within the input range using the v2.0 symmetric engine. The **latest window** (last 2 days) gives the actionable "what's happening now" signal, identical in semantics to v2.0. The **7-day trajectory** metrics (persistence, regime, PCR slope, delivery-days, cumulative OI) describe whether the latest signal is a one-session event or part of a sustained pattern.

## Regime Classification

| Regime | Condition |
|---|---|
| SUSTAINED BULLISH | ≥60% of windows scored ≥+3 (min 3 windows) |
| SUSTAINED BEARISH | ≥60% of windows scored ≤−3 (min 3 windows) |
| MIXED BULLISH-LEANING | More bullish windows than bearish |
| MIXED BEARISH-LEANING | More bearish windows than bullish |
| CHOPPY / INDECISIVE | Equal bullish/bearish windows |

## Top 15 Bullish (by Latest Score)

| Rank | Symbol | Latest | Tier | Regime | Bull/Bear/Neut | Persist | PCR 7d | Cum OI% | Phase |
|---:|:---|---:|:---|:---|:---:|---:|:---:|---:|:---|
| 1 | POWERINDIA | +16.0 | TIER 1 — STRONG ACCUMULATION | MIXED BULLISH-LEANING | 2/0/0 | +15.67 | 0.78→1.05 | +30.6% | phase_2_long |
| 2 | NAM-INDIA | +16.0 | TIER 1 — STRONG ACCUMULATION | MIXED BULLISH-LEANING | 2/0/0 | +13.17 | 0.73→1.42 | +430.6% | phase_2_long |
| 4 | ABB | +15.0 | TIER 1 — STRONG ACCUMULATION | MIXED BULLISH-LEANING | 2/0/0 | +14.83 | 1.05→1.16 | +13.6% | phase_2_long |
| 5 | SONACOMS | +14.5 | TIER 1 — STRONG ACCUMULATION | CHOPPY / INDECISIVE | 1/1/0 | +8.17 | 0.65→0.78 | +8.4% | phase_2_long |
| 6 | CUMMINSIND | +13.5 | TIER 1 — STRONG ACCUMULATION | MIXED BULLISH-LEANING | 2/0/0 | +11.00 | 0.73→0.79 | +11.2% | phase_2_long |
| 9 | BAJAJ-AUTO | +13.0 | TIER 1 — STRONG ACCUMULATION | MIXED BULLISH-LEANING | 2/0/0 | +11.33 | 0.73→1.14 | -5.9% | pre_phase_1_long |
| 10 | ADANIENSOL | +13.0 | TIER 1 — STRONG ACCUMULATION | MIXED BULLISH-LEANING | 1/0/1 | +9.50 | 0.72→0.68 | +9.4% | phase_2_long |
| 11 | POLYCAB | +13.0 | TIER 1 — STRONG ACCUMULATION | MIXED BULLISH-LEANING | 2/0/0 | +10.00 | 0.72→1.15 | +1.3% | phase_2_long |
| 12 | GODREJPROP | +12.5 | TIER 1 — STRONG ACCUMULATION | MIXED BULLISH-LEANING | 1/0/1 | +7.50 | 0.87→0.90 | +4.6% | phase_1_long |
| 13 | UNIONBANK | +12.5 | TIER 1 — STRONG ACCUMULATION | MIXED BULLISH-LEANING | 1/0/1 | +8.00 | 0.77→0.91 | +0.9% | phase_2_long |
| 14 | WAAREEENER | +12.0 | TIER 1 — STRONG ACCUMULATION | MIXED BULLISH-LEANING | 2/0/0 | +10.17 | 0.54→0.65 | +30.7% | phase_2_long |
| 15 | 360ONE | +12.0 | TIER 1 — STRONG ACCUMULATION | MIXED BULLISH-LEANING | 2/0/0 | +12.67 | 0.45→0.99 | +94.0% | phase_1_long |
| 16 | ABCAPITAL | +11.5 | TIER 1 — STRONG ACCUMULATION | CHOPPY / INDECISIVE | 1/1/0 | +6.17 | 0.93→1.04 | -2.0% | phase_1_long |
| 17 | PIDILITIND | +11.0 | TIER 1 — STRONG ACCUMULATION | CHOPPY / INDECISIVE | 1/1/0 | +5.50 | 1.00→0.86 | +7.6% | phase_2_long |
| 19 | HEROMOTOCO | +10.0 | TIER 1 — STRONG ACCUMULATION | MIXED BULLISH-LEANING | 1/0/1 | +6.00 | 0.89→0.96 | +10.1% | phase_1_long |

## Top 15 Bearish (by Latest Score)

| Rank | Symbol | Latest | Tier | Regime | Bull/Bear/Neut | Persist | PCR 7d | Cum OI% | Phase |
|---:|:---|---:|:---|:---|:---:|---:|:---:|---:|:---|
| 3 | COALINDIA | -15.5 | TIER 1 — STRONG DISTRIBUTION | CHOPPY / INDECISIVE | 1/1/0 | -8.50 | 0.78→0.54 | +23.4% | phase_2_short |
| 7 | TCS | -13.5 | TIER 1 — STRONG DISTRIBUTION | MIXED BEARISH-LEANING | 0/1/1 | -8.67 | 1.01→0.56 | +9.9% | phase_2_short |
| 8 | SUNPHARMA | -13.0 | TIER 1 — STRONG DISTRIBUTION | CHOPPY / INDECISIVE | 1/1/0 | -7.33 | 1.24→0.69 | +13.8% | phase_2_short |
| 18 | NAUKRI | -11.0 | TIER 1 — STRONG DISTRIBUTION | MIXED BEARISH-LEANING | 0/2/0 | -10.33 | 0.48→0.44 | +6.2% | phase_1_short |
| 21 | INFY | -10.0 | TIER 1 — STRONG DISTRIBUTION | MIXED BEARISH-LEANING | 0/2/0 | -9.17 | 1.05→0.73 | +8.4% | phase_2_short |
| 26 | COFORGE | -9.5 | TIER 1 — STRONG DISTRIBUTION | MIXED BEARISH-LEANING | 0/1/1 | -6.83 | 0.58→0.59 | -3.6% | phase_2_short |
| 48 | MAXHEALTH | -7.0 | TIER 2 — DISTRIBUTION | CHOPPY / INDECISIVE | 1/1/0 | -2.83 | 0.77→0.53 | +14.9% | no_signal |
| 76 | ONGC | -6.0 | TIER 3 — BUILDING SHORT | MIXED BEARISH-LEANING | 0/1/1 | -3.50 | 0.81→0.47 | +2.9% | no_signal |
| 137 | DELHIVERY | -3.5 | WATCH (mild bearish) | CHOPPY / INDECISIVE | 1/1/0 | +0.67 | 0.44→0.50 | +7.8% | pre_phase_1_short |
| 140 | PPLPHARMA | -3.5 | WATCH (mild bearish) | MIXED BEARISH-LEANING | 0/2/0 | -5.00 | 0.81→0.50 | +0.0% | no_signal |
| 150 | GLENMARK | -3.0 | WATCH (mild bearish) | MIXED BEARISH-LEANING | 0/1/1 | -1.17 | 0.38→0.52 | -8.2% | pre_phase_1_short |
| 161 | MANKIND | -3.0 | WATCH (mild bearish) | CHOPPY / INDECISIVE | 1/1/0 | -0.50 | 0.67→0.50 | +3.0% | no_signal |
| 162 | NHPC | -3.0 | WATCH (mild bearish) | CHOPPY / INDECISIVE | 1/1/0 | +0.33 | 0.63→0.58 | +14.3% | no_signal |
| 165 | LTM | -2.5 | NO SIGNAL | MIXED BULLISH-LEANING | 1/0/1 | -0.17 | 0.99→0.91 | +13.3% | no_signal |
| 166 | SWIGGY | -2.5 | NO SIGNAL | MIXED BEARISH-LEANING | 0/1/1 | -4.17 | 0.73→0.56 | +0.7% | no_signal |

## Top 10 Sustained-Bullish Persistence

| Symbol | Latest | Regime | Bull Windows | Persist Score | Days Del≥1.0x |
|:---|---:|:---|:---:|---:|:---:|
| POWERINDIA | +16.0 | MIXED BULLISH-LEANING | 2/2 | +15.67 | 2/3 |
| ABB | +15.0 | MIXED BULLISH-LEANING | 2/2 | +14.83 | 3/3 |
| NAM-INDIA | +16.0 | MIXED BULLISH-LEANING | 2/2 | +13.17 | 2/3 |
| 360ONE | +12.0 | MIXED BULLISH-LEANING | 2/2 | +12.67 | 1/3 |
| BAJAJ-AUTO | +13.0 | MIXED BULLISH-LEANING | 2/2 | +11.33 | 2/3 |
| CUMMINSIND | +13.5 | MIXED BULLISH-LEANING | 2/2 | +11.00 | 2/3 |
| WAAREEENER | +12.0 | MIXED BULLISH-LEANING | 2/2 | +10.17 | 2/3 |
| POLYCAB | +13.0 | MIXED BULLISH-LEANING | 2/2 | +10.00 | 2/3 |
| DIVISLAB | +8.0 | MIXED BULLISH-LEANING | 2/2 | +9.33 | 1/3 |
| COCHINSHIP | +10.0 | MIXED BULLISH-LEANING | 2/2 | +9.17 | 3/3 |

## Top 10 Sustained-Bearish Persistence

| Symbol | Latest | Regime | Bear Windows | Persist Score | Days Del≥1.0x |
|:---|---:|:---|:---:|---:|:---:|
| NAUKRI | -11.0 | MIXED BEARISH-LEANING | 2/2 | -10.33 | 2/3 |
| INFY | -10.0 | MIXED BEARISH-LEANING | 2/2 | -9.17 | 2/3 |
| PPLPHARMA | -3.5 | MIXED BEARISH-LEANING | 2/2 | -5.00 | 1/3 |
| TCS | -13.5 | MIXED BEARISH-LEANING | 1/2 | -8.67 | 1/3 |
| COFORGE | -9.5 | MIXED BEARISH-LEANING | 1/2 | -6.83 | 1/3 |
| SWIGGY | -2.5 | MIXED BEARISH-LEANING | 1/2 | -4.17 | 1/3 |
| ONGC | -6.0 | MIXED BEARISH-LEANING | 1/2 | -3.50 | 1/3 |
| HYUNDAI | +1.5 | MIXED BEARISH-LEANING | 1/2 | -2.83 | 1/3 |
| JSWENERGY | -1.5 | MIXED BEARISH-LEANING | 1/2 | -2.67 | 1/3 |
| BIOCON | +0.0 | MIXED BEARISH-LEANING | 1/2 | -2.33 | 0/3 |

## Phase Map (based on latest window)

### `phase_2_long` (22)
_Futures leverage — new longs + institutional delivery ≥1.0x_

POWERINDIA, NAM-INDIA, ABB, SONACOMS, CUMMINSIND, ADANIENSOL, POLYCAB, UNIONBANK, WAAREEENER, PIDILITIND, COCHINSHIP, MOTILALOFS, VEDL, VOLTAS, SIEMENS, SUZLON, WIPRO, RVNL, ASTRAL, OBEROIRLTY, SUPREMEIND, GODFRYPHLP

### `phase_1_long` (43)
_Cash accumulation — delivery ≥0.70x, OI building, price rising_

GODREJPROP, 360ONE, ABCAPITAL, HEROMOTOCO, ASIANPAINT, CAMS, KOTAKBANK, VBL, LICI, DIVISLAB, LAURUSLABS, AMBER, UNITDSPR, RECLTD, TATAPOWER, JINDALSTEL, KALYANKJIL, ADANIENT, NATIONALUM, POLICYBZR, IREDA, UPL, JSWSTEEL, LTF, KAYNES, ETERNAL, HINDUNILVR, MCX, PHOENIXLTD, SOLARINDS, NESTLEIND, MANAPPURAM, HINDALCO, IRFC, NMDC, ICICIPRULI, DIXON, BAJAJHLDNG, PFC, KFINTECH, HUDCO, MAZDOCK, VMM

### `pre_phase_1_long` (19)
_Derivatives leading cash — PCR rising without OI build_

BAJAJ-AUTO, MOTHERSON, MARICO, FEDERALBNK, BHEL, ASHOKLEY, MFSL, TMPV, LUPIN, ICICIBANK, PREMIERENE, TORNTPHARM, TITAN, HDFCLIFE, SBIN, LT, GRASIM, IEX, AUROPHARMA

### `phase_2_short` (5)
_Short leverage — new shorts + institutional delivery ≥1.0x_

COALINDIA, TCS, SUNPHARMA, INFY, COFORGE

### `phase_1_short` (2)
_Distribution — delivery ≥0.70x, OI building, price falling_

NAUKRI, MPHASIS

### `pre_phase_1_short` (2)
_Derivatives leading cash (bearish) — PCR collapsing without OI build_

DELHIVERY, GLENMARK

### `no_signal` (120)
_No clear positioning phase_

BOSCHLTD, AMBUJACEM, SAMMAANCAP, LODHA, INDIANB, MAXHEALTH, TVSMOTOR, EICHERMOT, TRENT, HINDPETRO, ULTRACEMCO, OFSS, BHARATFORG, PNBHOUSING, HAL, JIOFIN, BLUESTARCO, GMRAIRPORT, ONGC, GAIL, YESBANK, BSE, CGPOWER, CHOLAFIN, PAYTM, M&M, BAJFINANCE, HDFCAMC, ADANIPORTS, CROMPTON, CIPLA, ADANIGREEN, BPCL, INDHOTEL, DRREDDY, INOXWIND, DLF, CANBK, CDSL, ANGELONE, PNB, COLPAL, BAJAJFINSV, AXISBANK, ZYDUSLIFE, HINDZINC, IDFCFIRSTB, BANKBARODA, DALBHARAT, AUBANK, IDEA, TATACONSUM, JUBLFOOD, NBCC, EXIDEIND, MUTHOOTFIN, PPLPHARMA, ADANIPOWER, INDIGO, PAGEIND, BHARTIARTL, SHRIRAMFIN, TATASTEEL, APOLLOHOSP, IOC, NYKAA, RBLBANK, MARUTI, DABUR, FORCEMOT, BRITANNIA, MANKIND, NHPC, SRF, PIIND, LTM, SWIGGY, TATAELXSI, NUVAMA, HAVELLS, BANKINDIA, BDL, INDUSTOWER, CONCOR, INDUSINDBK, PERSISTENT, NTPC, HDFCBANK, LICHSGFIN, BEL, SBILIFE, JSWENERGY, PRESTIGE, KEI, TORNTPOWER, APLAPOLLO, FORTIS, KPITTECH, OIL, HYUNDAI, SHREECEM, POWERGRID, TECHM, SAIL, PATANJALI, ITC, ALKEM, HCLTECH, ICICIGI, PGEL, BANDHANBNK, PETRONET, RELIANCE, UNOMINDA, GODREJCP, SBICARD, TIINDIA, DMART, BIOCON, TATATECH

## Warnings

- `Derivative_Analytics_01-Apr-2026.csv`: missing critical field

## Structured Data (re-analysis payload)

```json
{
  "meta": {
    "input_directory": "/tmp/test_7day",
    "days_used": 3,
    "input_files": [
      {
        "file": "Derivative_Analytics_01-Apr-2026.csv",
        "date": "2026-04-01",
        "sha256": "cb3362da62aca2294ff0024b09c6a5cf42e2b6b2db98946c797c77a42566a0f7"
      },
      {
        "file": "Derivative_Analytics_09-Apr-2026.csv",
        "date": "2026-04-09",
        "sha256": "50adb1bb1481d7e67dd5a594b73a79d6606e5906c0353b41085a30013f75152c"
      },
      {
        "file": "Derivative_Analytics_10-Apr-2026.csv",
        "date": "2026-04-10",
        "sha256": "8561d2dacd1c9718c7aa59042a058e4126ac416f6525d8517ff014cb35eb74c7"
      }
    ],
    "combined_sha256": "602bc244854eb2f3847e3be1550674446d4d934e2b8bbafee612940ca02f1bef",
    "generated_at": "2026-04-13T04:31:49",
    "symbols_analyzed": 213,
    "data_completeness_warning": "Incomplete data \u2014 only 3 days available, not 7.",
    "expiry_warning": null,
    "expiry_dates_detected": [],
    "model_version": "2.1",
    "scoring_strategy": "C \u2014 rolling 2-day windows (v2 engine) + 7-day trajectory",
    "known_limitations": [
      "PCR <0.40 during parabolic crash may be oversold bounce",
      "Short Covering and Long Liquidation are lagging signals",
      "NSE monthly expiry within window distorts OI interpretation",
      "No market context (Nifty trend) \u2014 planned for v3"
    ]
  },
  "phase_descriptions": {
    "phase_2_long": "Futures leverage \u2014 new longs + institutional delivery \u22651.0x",
    "phase_1_long": "Cash accumulation \u2014 delivery \u22650.70x, OI building, price rising",
    "pre_phase_1_long": "Derivatives leading cash \u2014 PCR rising without OI build",
    "phase_2_short": "Short leverage \u2014 new shorts + institutional delivery \u22651.0x",
    "phase_1_short": "Distribution \u2014 delivery \u22650.70x, OI building, price falling",
    "pre_phase_1_short": "Derivatives leading cash (bearish) \u2014 PCR collapsing without OI build",
    "no_signal": "No clear positioning phase"
  },
  "rankings": [
    {
      "symbol": "POWERINDIA",
      "rank": 1,
      "days_available": 3,
      "latest_score": 16.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          15.0,
          16.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.135,
        "pcr_first": 0.78,
        "pcr_last": 1.05,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 30.64,
        "cumulative_price_chg_pct_window": 9.68,
        "persistence_score": 15.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 15.0,
          "signals": [
            "PCR 0.96 approaching bullish zone",
            "PCR surging +0.11",
            "\u2605 NEW LONGS: FutOI +25.2% + Price +5.4%",
            "Del 1.15x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 5.4,
          "price_sign": 1,
          "pcr_d1": 0.78,
          "pcr_d2": 0.96,
          "pcr_chg": 0.11,
          "fut_oi_chg_pct": 25.16,
          "oi_sign": 1,
          "avg_del": 1.15,
          "peak_del": 1.52,
          "del_chg": 0.74,
          "avg_vol": 1.495,
          "call_oi_growth_pct": 101.39,
          "put_oi_growth_pct": 149.35,
          "opt_oi_growth_pct": 122.36,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 16.0,
          "signals": [
            "PCR 1.05 ABOVE 1.0 \u2014 put writers dominant",
            "PCR surging +0.09",
            "\u2605 NEW LONGS: FutOI +4.4% + Price +4.1%",
            "Del 2.17x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 4.06,
          "price_sign": 1,
          "pcr_d1": 0.96,
          "pcr_d2": 1.05,
          "pcr_chg": 0.09,
          "fut_oi_chg_pct": 4.38,
          "oi_sign": 1,
          "avg_del": 2.175,
          "peak_del": 2.83,
          "del_chg": 1.31,
          "avg_vol": 2.075,
          "call_oi_growth_pct": 26.71,
          "put_oi_growth_pct": 38.54,
          "opt_oi_growth_pct": 32.51,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.42,
          "pcr": 0.78,
          "pcr_chg_1d": 0.11,
          "fut_oi": 289200,
          "oi_chg_pct": 1.47,
          "delivery": 0.78,
          "volume": 0.88,
          "call_oi": 79300,
          "put_oi": 61600
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 5.4,
          "pcr": 0.96,
          "pcr_chg_1d": 0.11,
          "fut_oi": 361950,
          "oi_chg_pct": 13.68,
          "delivery": 1.52,
          "volume": 2.11,
          "call_oi": 159700,
          "put_oi": 153600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 4.06,
          "pcr": 1.05,
          "pcr_chg_1d": 0.09,
          "fut_oi": 377800,
          "oi_chg_pct": 4.38,
          "delivery": 2.83,
          "volume": 2.04,
          "call_oi": 202350,
          "put_oi": 212800
        }
      ]
    },
    {
      "symbol": "NAM-INDIA",
      "rank": 2,
      "days_available": 3,
      "latest_score": 16.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          7.5,
          16.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.345,
        "pcr_first": 0.73,
        "pcr_last": 1.42,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 430.56,
        "cumulative_price_chg_pct_window": 5.76,
        "persistence_score": 13.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 7.5,
          "signals": [
            "PCR 0.52 call writers dominant",
            "PCR surging +0.21",
            "\u2605 NEW LONGS: FutOI +354.9% + Price +0.6%",
            "Del 1.32x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 0.6,
          "price_sign": 1,
          "pcr_d1": 0.73,
          "pcr_d2": 0.52,
          "pcr_chg": 0.21,
          "fut_oi_chg_pct": 354.86,
          "oi_sign": 1,
          "avg_del": 1.32,
          "peak_del": 1.82,
          "del_chg": -1.0,
          "avg_vol": 1.525,
          "call_oi_growth_pct": 3718.18,
          "put_oi_growth_pct": 2637.5,
          "opt_oi_growth_pct": 3263.16,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 16.0,
          "signals": [
            "PCR 1.42 ABOVE 1.0 \u2014 put writers dominant",
            "PCR surging +0.90",
            "\u2605 NEW LONGS: FutOI +16.6% + Price +5.1%",
            "Del 1.20x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 5.13,
          "price_sign": 1,
          "pcr_d1": 0.52,
          "pcr_d2": 1.42,
          "pcr_chg": 0.9,
          "fut_oi_chg_pct": 16.64,
          "oi_sign": 1,
          "avg_del": 1.2,
          "peak_del": 1.58,
          "del_chg": 0.76,
          "avg_vol": 1.2,
          "call_oi_growth_pct": 43.81,
          "put_oi_growth_pct": 291.32,
          "opt_oi_growth_pct": 128.64,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 7.92,
          "pcr": 0.73,
          "pcr_chg_1d": 0.0,
          "fut_oi": 398750,
          "oi_chg_pct": 0.0,
          "delivery": 1.82,
          "volume": 2.12,
          "call_oi": 6875,
          "put_oi": 5000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.6,
          "pcr": 0.52,
          "pcr_chg_1d": 0.21,
          "fut_oi": 1813750,
          "oi_chg_pct": 19.67,
          "delivery": 0.82,
          "volume": 0.93,
          "call_oi": 262500,
          "put_oi": 136875
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 5.13,
          "pcr": 1.42,
          "pcr_chg_1d": 0.9,
          "fut_oi": 2115625,
          "oi_chg_pct": 16.64,
          "delivery": 1.58,
          "volume": 1.47,
          "call_oi": 377500,
          "put_oi": 535625
        }
      ]
    },
    {
      "symbol": "COALINDIA",
      "rank": 3,
      "days_available": 3,
      "latest_score": -15.5,
      "latest_tier": "TIER 1 \u2014 STRONG DISTRIBUTION",
      "latest_sign": "bearish",
      "latest_phase": "phase_2_short",
      "latest_interpretation": "\u26a0 NEW SHORTS (Bearish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (SHORT)",
        "direction": "short",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          5.5,
          -15.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.12,
        "pcr_first": 0.78,
        "pcr_last": 0.54,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 23.42,
        "cumulative_price_chg_pct_window": -3.37,
        "persistence_score": -8.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": 5.5,
          "signals": [
            "PCR 0.64 neutral",
            "PCR surging +0.09",
            "\u2605 NEW LONGS: FutOI +14.6% + Price +1.1%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.08,
          "price_sign": 1,
          "pcr_d1": 0.78,
          "pcr_d2": 0.64,
          "pcr_chg": 0.09,
          "fut_oi_chg_pct": 14.63,
          "oi_sign": 1,
          "avg_del": 0.78,
          "peak_del": 0.97,
          "del_chg": -0.38,
          "avg_vol": 0.855,
          "call_oi_growth_pct": 63.88,
          "put_oi_growth_pct": 35.02,
          "opt_oi_growth_pct": 51.27,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -15.5,
          "signals": [
            "PCR 0.54 call writers dominant",
            "PCR collapsing -0.10",
            "\u26a0 NEW SHORTS: FutOI +7.7% + Price -4.4%",
            "Del 1.34x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -4.4,
          "price_sign": -1,
          "pcr_d1": 0.64,
          "pcr_d2": 0.54,
          "pcr_chg": -0.1,
          "fut_oi_chg_pct": 7.67,
          "oi_sign": 1,
          "avg_del": 1.34,
          "peak_del": 2.09,
          "del_chg": 1.5,
          "avg_vol": 1.58,
          "call_oi_growth_pct": 37.69,
          "put_oi_growth_pct": 17.0,
          "opt_oi_growth_pct": 29.61,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.23,
          "pcr": 0.78,
          "pcr_chg_1d": -0.02,
          "fut_oi": 52404300,
          "oi_chg_pct": 2.08,
          "delivery": 0.97,
          "volume": 0.99,
          "call_oi": 17010000,
          "put_oi": 13207050
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.08,
          "pcr": 0.64,
          "pcr_chg_1d": 0.09,
          "fut_oi": 60069600,
          "oi_chg_pct": -1.65,
          "delivery": 0.59,
          "volume": 0.72,
          "call_oi": 27876150,
          "put_oi": 17832150
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -4.4,
          "pcr": 0.54,
          "pcr_chg_1d": -0.1,
          "fut_oi": 64677150,
          "oi_chg_pct": 7.67,
          "delivery": 2.09,
          "volume": 2.44,
          "call_oi": 38381850,
          "put_oi": 20862900
        }
      ]
    },
    {
      "symbol": "ABB",
      "rank": 4,
      "days_available": 3,
      "latest_score": 15.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          14.5,
          15.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.055,
        "pcr_first": 1.05,
        "pcr_last": 1.16,
        "days_delivery_institutional": 3,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 13.61,
        "cumulative_price_chg_pct_window": 4.49,
        "persistence_score": 14.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 14.5,
          "signals": [
            "PCR 1.05 ABOVE 1.0 \u2014 put writers dominant",
            "PCR rising +0.08",
            "\u2605 NEW LONGS: FutOI +8.4% + Price +0.8%",
            "Del 1.63x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 0.75,
          "price_sign": 1,
          "pcr_d1": 1.05,
          "pcr_d2": 1.05,
          "pcr_chg": 0.08,
          "fut_oi_chg_pct": 8.43,
          "oi_sign": 1,
          "avg_del": 1.63,
          "peak_del": 1.9,
          "del_chg": 0.54,
          "avg_vol": 1.385,
          "call_oi_growth_pct": 86.48,
          "put_oi_growth_pct": 86.79,
          "opt_oi_growth_pct": 86.64,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 15.0,
          "signals": [
            "PCR 1.16 ABOVE 1.0 \u2014 put writers dominant",
            "PCR surging +0.11",
            "\u2605 NEW LONGS: FutOI +4.8% + Price +3.7%",
            "Del 2.04x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 3.71,
          "price_sign": 1,
          "pcr_d1": 1.05,
          "pcr_d2": 1.16,
          "pcr_chg": 0.11,
          "fut_oi_chg_pct": 4.78,
          "oi_sign": 1,
          "avg_del": 2.045,
          "peak_del": 2.19,
          "del_chg": 0.29,
          "avg_vol": 1.835,
          "call_oi_growth_pct": 9.54,
          "put_oi_growth_pct": 20.61,
          "opt_oi_growth_pct": 15.21,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.04,
          "pcr": 1.05,
          "pcr_chg_1d": 0.02,
          "fut_oi": 2005625,
          "oi_chg_pct": 1.24,
          "delivery": 1.36,
          "volume": 1.09,
          "call_oi": 356875,
          "put_oi": 373750
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.75,
          "pcr": 1.05,
          "pcr_chg_1d": 0.08,
          "fut_oi": 2174625,
          "oi_chg_pct": 2.23,
          "delivery": 1.9,
          "volume": 1.68,
          "call_oi": 665500,
          "put_oi": 698125
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.71,
          "pcr": 1.16,
          "pcr_chg_1d": 0.11,
          "fut_oi": 2278500,
          "oi_chg_pct": 4.78,
          "delivery": 2.19,
          "volume": 1.99,
          "call_oi": 729000,
          "put_oi": 842000
        }
      ]
    },
    {
      "symbol": "SONACOMS",
      "rank": 5,
      "days_available": 3,
      "latest_score": 14.5,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.5,
          14.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.065,
        "pcr_first": 0.65,
        "pcr_last": 0.78,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 8.36,
        "cumulative_price_chg_pct_window": 3.85,
        "persistence_score": 8.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -4.5,
          "signals": [
            "PCR 0.69 neutral",
            "PCR easing -0.07"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -2.0,
          "price_sign": -1,
          "pcr_d1": 0.65,
          "pcr_d2": 0.69,
          "pcr_chg": -0.07,
          "fut_oi_chg_pct": 0.25,
          "oi_sign": 1,
          "avg_del": 0.81,
          "peak_del": 1.25,
          "del_chg": 0.88,
          "avg_vol": 0.765,
          "call_oi_growth_pct": 196.76,
          "put_oi_growth_pct": 215.18,
          "opt_oi_growth_pct": 204.04,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 14.5,
          "signals": [
            "PCR 0.78 neutral-to-bullish",
            "PCR surging +0.09",
            "\u2605 NEW LONGS: FutOI +8.1% + Price +6.0%",
            "Del 1.44x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 5.97,
          "price_sign": 1,
          "pcr_d1": 0.69,
          "pcr_d2": 0.78,
          "pcr_chg": 0.09,
          "fut_oi_chg_pct": 8.1,
          "oi_sign": 1,
          "avg_del": 1.445,
          "peak_del": 1.64,
          "del_chg": 0.39,
          "avg_vol": 1.86,
          "call_oi_growth_pct": 14.35,
          "put_oi_growth_pct": 28.59,
          "opt_oi_growth_pct": 20.18,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.27,
          "pcr": 0.65,
          "pcr_chg_1d": -0.05,
          "fut_oi": 12437425,
          "oi_chg_pct": 0.32,
          "delivery": 0.37,
          "volume": 0.48,
          "call_oi": 1173550,
          "put_oi": 766850
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.0,
          "pcr": 0.69,
          "pcr_chg_1d": -0.07,
          "fut_oi": 12468050,
          "oi_chg_pct": -1.23,
          "delivery": 1.25,
          "volume": 1.05,
          "call_oi": 3482675,
          "put_oi": 2416925
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 5.97,
          "pcr": 0.78,
          "pcr_chg_1d": 0.09,
          "fut_oi": 13477450,
          "oi_chg_pct": 8.1,
          "delivery": 1.64,
          "volume": 2.67,
          "call_oi": 3982475,
          "put_oi": 3107825
        }
      ]
    },
    {
      "symbol": "CUMMINSIND",
      "rank": 6,
      "days_available": 3,
      "latest_score": 13.5,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          6.0,
          13.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.03,
        "pcr_first": 0.73,
        "pcr_last": 0.79,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 11.19,
        "cumulative_price_chg_pct_window": 7.14,
        "persistence_score": 11.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 6.0,
          "signals": [
            "PCR 0.65 neutral",
            "\u2605 NEW LONGS: FutOI +5.0% + Price +2.3%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 2.32,
          "price_sign": 1,
          "pcr_d1": 0.73,
          "pcr_d2": 0.65,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": 4.99,
          "oi_sign": 1,
          "avg_del": 0.93,
          "peak_del": 1.57,
          "del_chg": 1.28,
          "avg_vol": 0.91,
          "call_oi_growth_pct": 90.31,
          "put_oi_growth_pct": 70.02,
          "opt_oi_growth_pct": 81.78,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 13.5,
          "signals": [
            "PCR 0.79 neutral-to-bullish",
            "PCR surging +0.14",
            "\u2605 NEW LONGS: FutOI +5.9% + Price +4.7%",
            "Del 1.50x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 4.71,
          "price_sign": 1,
          "pcr_d1": 0.65,
          "pcr_d2": 0.79,
          "pcr_chg": 0.14,
          "fut_oi_chg_pct": 5.91,
          "oi_sign": 1,
          "avg_del": 1.5,
          "peak_del": 1.57,
          "del_chg": -0.14,
          "avg_vol": 1.54,
          "call_oi_growth_pct": 15.4,
          "put_oi_growth_pct": 41.39,
          "opt_oi_growth_pct": 25.62,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.42,
          "pcr": 0.73,
          "pcr_chg_1d": -0.06,
          "fut_oi": 3389000,
          "oi_chg_pct": -0.26,
          "delivery": 0.29,
          "volume": 0.38,
          "call_oi": 477000,
          "put_oi": 346200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 2.32,
          "pcr": 0.65,
          "pcr_chg_1d": 0.02,
          "fut_oi": 3558000,
          "oi_chg_pct": 2.22,
          "delivery": 1.57,
          "volume": 1.44,
          "call_oi": 907800,
          "put_oi": 588600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 4.71,
          "pcr": 0.79,
          "pcr_chg_1d": 0.14,
          "fut_oi": 3768200,
          "oi_chg_pct": 5.91,
          "delivery": 1.43,
          "volume": 1.64,
          "call_oi": 1047600,
          "put_oi": 832200
        }
      ]
    },
    {
      "symbol": "TCS",
      "rank": 7,
      "days_available": 3,
      "latest_score": -13.5,
      "latest_tier": "TIER 1 \u2014 STRONG DISTRIBUTION",
      "latest_sign": "bearish",
      "latest_phase": "phase_2_short",
      "latest_interpretation": "\u26a0 NEW SHORTS (Bearish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (SHORT)",
        "direction": "short",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.0,
          -13.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.225,
        "pcr_first": 1.01,
        "pcr_last": 0.56,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 9.94,
        "cumulative_price_chg_pct_window": -1.37,
        "persistence_score": -8.67,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": 1.0,
          "signals": [
            "PCR 0.72 neutral",
            "PCR collapsing -0.22"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.16,
          "price_sign": 1,
          "pcr_d1": 1.01,
          "pcr_d2": 0.72,
          "pcr_chg": -0.22,
          "fut_oi_chg_pct": 0.63,
          "oi_sign": 1,
          "avg_del": 0.86,
          "peak_del": 0.97,
          "del_chg": 0.22,
          "avg_vol": 1.075,
          "call_oi_growth_pct": 130.63,
          "put_oi_growth_pct": 65.08,
          "opt_oi_growth_pct": 97.65,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -13.5,
          "signals": [
            "PCR 0.56 neutral",
            "PCR collapsing -0.16",
            "\u26a0 NEW SHORTS: FutOI +9.3% + Price -2.5%",
            "Del 1.54x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -2.5,
          "price_sign": -1,
          "pcr_d1": 0.72,
          "pcr_d2": 0.56,
          "pcr_chg": -0.16,
          "fut_oi_chg_pct": 9.25,
          "oi_sign": 1,
          "avg_del": 1.535,
          "peak_del": 2.1,
          "del_chg": 1.13,
          "avg_vol": 1.805,
          "call_oi_growth_pct": 29.73,
          "put_oi_growth_pct": 0.07,
          "opt_oi_growth_pct": 17.27,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.09,
          "pcr": 1.01,
          "pcr_chg_1d": -0.01,
          "fut_oi": 31669925,
          "oi_chg_pct": -7.41,
          "delivery": 0.75,
          "volume": 0.83,
          "call_oi": 7099575,
          "put_oi": 7187075
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.16,
          "pcr": 0.72,
          "pcr_chg_1d": -0.22,
          "fut_oi": 31869250,
          "oi_chg_pct": -1.65,
          "delivery": 0.97,
          "volume": 1.32,
          "call_oi": 16373700,
          "put_oi": 11864475
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -2.5,
          "pcr": 0.56,
          "pcr_chg_1d": -0.16,
          "fut_oi": 34818175,
          "oi_chg_pct": 9.25,
          "delivery": 2.1,
          "volume": 2.29,
          "call_oi": 21241325,
          "put_oi": 11873225
        }
      ]
    },
    {
      "symbol": "SUNPHARMA",
      "rank": 8,
      "days_available": 3,
      "latest_score": -13.0,
      "latest_tier": "TIER 1 \u2014 STRONG DISTRIBUTION",
      "latest_sign": "bearish",
      "latest_phase": "phase_2_short",
      "latest_interpretation": "\u26a0 NEW SHORTS (Bearish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (SHORT)",
        "direction": "short",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.0,
          -13.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.275,
        "pcr_first": 1.24,
        "pcr_last": 0.69,
        "days_delivery_institutional": 3,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 13.76,
        "cumulative_price_chg_pct_window": -3.48,
        "persistence_score": -7.33,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": 4.0,
          "signals": [
            "PCR 0.89 approaching bullish zone"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.15,
          "price_sign": 0,
          "pcr_d1": 1.24,
          "pcr_d2": 0.89,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 10.1,
          "oi_sign": 1,
          "avg_del": 1.105,
          "peak_del": 1.19,
          "del_chg": -0.17,
          "avg_vol": 1.04,
          "call_oi_growth_pct": 76.24,
          "put_oi_growth_pct": 27.23,
          "opt_oi_growth_pct": 49.14,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -13.0,
          "signals": [
            "PCR 0.69 neutral",
            "PCR collapsing -0.20",
            "\u26a0 NEW SHORTS: FutOI +3.3% + Price -3.6%",
            "Del 1.42x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -3.62,
          "price_sign": -1,
          "pcr_d1": 0.89,
          "pcr_d2": 0.69,
          "pcr_chg": -0.2,
          "fut_oi_chg_pct": 3.32,
          "oi_sign": 1,
          "avg_del": 1.415,
          "peak_del": 1.81,
          "del_chg": 0.79,
          "avg_vol": 1.575,
          "call_oi_growth_pct": 75.22,
          "put_oi_growth_pct": 35.61,
          "opt_oi_growth_pct": 56.53,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -1.63,
          "pcr": 1.24,
          "pcr_chg_1d": 0.04,
          "fut_oi": 17297700,
          "oi_chg_pct": 1.26,
          "delivery": 1.19,
          "volume": 1.17,
          "call_oi": 2627450,
          "put_oi": 3250100
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.15,
          "pcr": 0.89,
          "pcr_chg_1d": 0.01,
          "fut_oi": 19044900,
          "oi_chg_pct": 1.81,
          "delivery": 1.02,
          "volume": 0.91,
          "call_oi": 4630500,
          "put_oi": 4135250
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -3.62,
          "pcr": 0.69,
          "pcr_chg_1d": -0.2,
          "fut_oi": 19677000,
          "oi_chg_pct": 3.32,
          "delivery": 1.81,
          "volume": 2.24,
          "call_oi": 8113700,
          "put_oi": 5607700
        }
      ]
    },
    {
      "symbol": "BAJAJ-AUTO",
      "rank": 9,
      "days_available": 3,
      "latest_score": 13.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          8.0,
          13.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.205,
        "pcr_first": 0.73,
        "pcr_last": 1.14,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -5.87,
        "cumulative_price_chg_pct_window": 4.78,
        "persistence_score": 11.33,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 8.0,
          "signals": [
            "PCR 0.88 approaching bullish zone",
            "Del 1.08x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.61,
          "price_sign": 1,
          "pcr_d1": 0.73,
          "pcr_d2": 0.88,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -3.64,
          "oi_sign": -1,
          "avg_del": 1.08,
          "peak_del": 1.31,
          "del_chg": -0.46,
          "avg_vol": 1.28,
          "call_oi_growth_pct": 50.55,
          "put_oi_growth_pct": 81.39,
          "opt_oi_growth_pct": 63.58,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 13.0,
          "signals": [
            "PCR 1.14 ABOVE 1.0 \u2014 put writers dominant",
            "PCR surging +0.26",
            "Del 1.55x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 3.12,
          "price_sign": 1,
          "pcr_d1": 0.88,
          "pcr_d2": 1.14,
          "pcr_chg": 0.26,
          "fut_oi_chg_pct": -2.31,
          "oi_sign": -1,
          "avg_del": 1.555,
          "peak_del": 2.26,
          "del_chg": 1.41,
          "avg_vol": 1.68,
          "call_oi_growth_pct": 0.63,
          "put_oi_growth_pct": 29.52,
          "opt_oi_growth_pct": 14.17,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.3,
          "pcr": 0.73,
          "pcr_chg_1d": -0.02,
          "fut_oi": 3449025,
          "oi_chg_pct": -0.97,
          "delivery": 1.31,
          "volume": 1.09,
          "call_oi": 555075,
          "put_oi": 406275
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.61,
          "pcr": 0.88,
          "pcr_chg_1d": 0.0,
          "fut_oi": 3323325,
          "oi_chg_pct": 1.14,
          "delivery": 0.85,
          "volume": 1.47,
          "call_oi": 835650,
          "put_oi": 736950
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.12,
          "pcr": 1.14,
          "pcr_chg_1d": 0.26,
          "fut_oi": 3246450,
          "oi_chg_pct": -2.31,
          "delivery": 2.26,
          "volume": 1.89,
          "call_oi": 840900,
          "put_oi": 954525
        }
      ]
    },
    {
      "symbol": "ADANIENSOL",
      "rank": 10,
      "days_available": 3,
      "latest_score": 13.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          2.5,
          13.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.02,
        "pcr_first": 0.72,
        "pcr_last": 0.68,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 9.43,
        "cumulative_price_chg_pct_window": 7.89,
        "persistence_score": 9.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 2.5,
          "signals": [
            "PCR 0.53 call writers dominant",
            "PCR rising +0.05",
            "\u2605 NEW LONGS: FutOI +5.6% + Price +0.5%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": 0.51,
          "price_sign": 1,
          "pcr_d1": 0.72,
          "pcr_d2": 0.53,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": 5.58,
          "oi_sign": 1,
          "avg_del": 0.6,
          "peak_del": 0.95,
          "del_chg": 0.7,
          "avg_vol": 0.695,
          "call_oi_growth_pct": 230.73,
          "put_oi_growth_pct": 144.82,
          "opt_oi_growth_pct": 194.69,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 13.0,
          "signals": [
            "PCR 0.68 neutral",
            "PCR surging +0.15",
            "\u2605 NEW LONGS: FutOI +3.6% + Price +7.3%",
            "Del 2.63x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 7.34,
          "price_sign": 1,
          "pcr_d1": 0.53,
          "pcr_d2": 0.68,
          "pcr_chg": 0.15,
          "fut_oi_chg_pct": 3.65,
          "oi_sign": 1,
          "avg_del": 2.63,
          "peak_del": 4.31,
          "del_chg": 3.36,
          "avg_vol": 2.14,
          "call_oi_growth_pct": 21.09,
          "put_oi_growth_pct": 53.67,
          "opt_oi_growth_pct": 32.44,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.32,
          "pcr": 0.72,
          "pcr_chg_1d": -0.15,
          "fut_oi": 18860850,
          "oi_chg_pct": -3.03,
          "delivery": 0.25,
          "volume": 0.43,
          "call_oi": 856575,
          "put_oi": 618975
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.51,
          "pcr": 0.53,
          "pcr_chg_1d": 0.05,
          "fut_oi": 19913175,
          "oi_chg_pct": -0.93,
          "delivery": 0.95,
          "volume": 0.96,
          "call_oi": 2832975,
          "put_oi": 1515375
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 7.34,
          "pcr": 0.68,
          "pcr_chg_1d": 0.15,
          "fut_oi": 20639475,
          "oi_chg_pct": 3.65,
          "delivery": 4.31,
          "volume": 3.32,
          "call_oi": 3430350,
          "put_oi": 2328750
        }
      ]
    },
    {
      "symbol": "POLYCAB",
      "rank": 11,
      "days_available": 3,
      "latest_score": 13.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.0,
          13.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.215,
        "pcr_first": 0.72,
        "pcr_last": 1.15,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 1.26,
        "cumulative_price_chg_pct_window": 1.68,
        "persistence_score": 10.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 4.0,
          "signals": [
            "PCR 0.97 approaching bullish zone"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.09,
          "price_sign": 0,
          "pcr_d1": 0.72,
          "pcr_d2": 0.97,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": -1.76,
          "oi_sign": -1,
          "avg_del": 0.8,
          "peak_del": 1.09,
          "del_chg": 0.58,
          "avg_vol": 0.81,
          "call_oi_growth_pct": 56.25,
          "put_oi_growth_pct": 108.59,
          "opt_oi_growth_pct": 78.21,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 13.0,
          "signals": [
            "PCR 1.15 ABOVE 1.0 \u2014 put writers dominant",
            "PCR surging +0.18",
            "\u2605 NEW LONGS: FutOI +3.1% + Price +1.6%",
            "Del 1.18x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.59,
          "price_sign": 1,
          "pcr_d1": 0.97,
          "pcr_d2": 1.15,
          "pcr_chg": 0.18,
          "fut_oi_chg_pct": 3.07,
          "oi_sign": 1,
          "avg_del": 1.18,
          "peak_del": 1.27,
          "del_chg": 0.18,
          "avg_vol": 1.03,
          "call_oi_growth_pct": 1.94,
          "put_oi_growth_pct": 21.72,
          "opt_oi_growth_pct": 11.65,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.19,
          "pcr": 0.72,
          "pcr_chg_1d": 0.0,
          "fut_oi": 2062625,
          "oi_chg_pct": 7.75,
          "delivery": 0.51,
          "volume": 0.67,
          "call_oi": 527375,
          "put_oi": 381375
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.09,
          "pcr": 0.97,
          "pcr_chg_1d": -0.02,
          "fut_oi": 2026375,
          "oi_chg_pct": -0.89,
          "delivery": 1.09,
          "volume": 0.95,
          "call_oi": 824000,
          "put_oi": 795500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.59,
          "pcr": 1.15,
          "pcr_chg_1d": 0.18,
          "fut_oi": 2088625,
          "oi_chg_pct": 3.07,
          "delivery": 1.27,
          "volume": 1.11,
          "call_oi": 840000,
          "put_oi": 968250
        }
      ]
    },
    {
      "symbol": "GODREJPROP",
      "rank": 12,
      "days_available": 3,
      "latest_score": 12.5,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.5,
          12.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.015,
        "pcr_first": 0.87,
        "pcr_last": 0.9,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 4.57,
        "cumulative_price_chg_pct_window": 0.85,
        "persistence_score": 7.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -2.5,
          "signals": [
            "PCR 0.80 neutral-to-bullish",
            "PCR rising +0.04"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.39,
          "price_sign": -1,
          "pcr_d1": 0.87,
          "pcr_d2": 0.8,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": 2.15,
          "oi_sign": 1,
          "avg_del": 0.665,
          "peak_del": 0.71,
          "del_chg": -0.09,
          "avg_vol": 0.705,
          "call_oi_growth_pct": 42.14,
          "put_oi_growth_pct": 30.25,
          "opt_oi_growth_pct": 36.6,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 12.5,
          "signals": [
            "PCR 0.90 approaching bullish zone",
            "PCR surging +0.10",
            "\u2605 NEW LONGS: FutOI +2.4% + Price +1.2%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.24,
          "price_sign": 1,
          "pcr_d1": 0.8,
          "pcr_d2": 0.9,
          "pcr_chg": 0.1,
          "fut_oi_chg_pct": 2.37,
          "oi_sign": 1,
          "avg_del": 0.975,
          "peak_del": 1.33,
          "del_chg": 0.71,
          "avg_vol": 1.15,
          "call_oi_growth_pct": 22.46,
          "put_oi_growth_pct": 37.75,
          "opt_oi_growth_pct": 29.26,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.5,
          "pcr": 0.87,
          "pcr_chg_1d": -0.01,
          "fut_oi": 7828425,
          "oi_chg_pct": -0.52,
          "delivery": 0.71,
          "volume": 0.83,
          "call_oi": 1512775,
          "put_oi": 1321650
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.39,
          "pcr": 0.8,
          "pcr_chg_1d": 0.04,
          "fut_oi": 7997000,
          "oi_chg_pct": 0.52,
          "delivery": 0.62,
          "volume": 0.58,
          "call_oi": 2150225,
          "put_oi": 1721500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.24,
          "pcr": 0.9,
          "pcr_chg_1d": 0.1,
          "fut_oi": 8186475,
          "oi_chg_pct": 2.37,
          "delivery": 1.33,
          "volume": 1.72,
          "call_oi": 2633125,
          "put_oi": 2371325
        }
      ]
    },
    {
      "symbol": "UNIONBANK",
      "rank": 13,
      "days_available": 3,
      "latest_score": 12.5,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -1.0,
          12.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.07,
        "pcr_first": 0.77,
        "pcr_last": 0.91,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.87,
        "cumulative_price_chg_pct_window": 1.82,
        "persistence_score": 8.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -1.0,
          "signals": [
            "PCR 0.82 neutral-to-bullish",
            "PCR easing -0.05"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.52,
          "price_sign": -1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.82,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": -1.16,
          "oi_sign": -1,
          "avg_del": 0.595,
          "peak_del": 0.88,
          "del_chg": 0.57,
          "avg_vol": 0.665,
          "call_oi_growth_pct": 56.41,
          "put_oi_growth_pct": 66.8,
          "opt_oi_growth_pct": 60.94,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 12.5,
          "signals": [
            "PCR 0.91 approaching bullish zone",
            "PCR surging +0.09",
            "\u2605 NEW LONGS: FutOI +2.1% + Price +2.4%",
            "Del 1.08x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 2.35,
          "price_sign": 1,
          "pcr_d1": 0.82,
          "pcr_d2": 0.91,
          "pcr_chg": 0.09,
          "fut_oi_chg_pct": 2.06,
          "oi_sign": 1,
          "avg_del": 1.085,
          "peak_del": 1.29,
          "del_chg": 0.41,
          "avg_vol": 0.815,
          "call_oi_growth_pct": 1.14,
          "put_oi_growth_pct": 12.14,
          "opt_oi_growth_pct": 6.11,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.53,
          "pcr": 0.77,
          "pcr_chg_1d": -0.02,
          "fut_oi": 99735075,
          "oi_chg_pct": -4.23,
          "delivery": 0.31,
          "volume": 0.49,
          "call_oi": 16629150,
          "put_oi": 12823650
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.52,
          "pcr": 0.82,
          "pcr_chg_1d": -0.05,
          "fut_oi": 98580150,
          "oi_chg_pct": 4.87,
          "delivery": 0.88,
          "volume": 0.84,
          "call_oi": 26010150,
          "put_oi": 21390450
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.35,
          "pcr": 0.91,
          "pcr_chg_1d": 0.09,
          "fut_oi": 100606800,
          "oi_chg_pct": 2.06,
          "delivery": 1.29,
          "volume": 0.79,
          "call_oi": 26306625,
          "put_oi": 23987925
        }
      ]
    },
    {
      "symbol": "WAAREEENER",
      "rank": 14,
      "days_available": 3,
      "latest_score": 12.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          6.5,
          12.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.055,
        "pcr_first": 0.54,
        "pcr_last": 0.65,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 30.66,
        "cumulative_price_chg_pct_window": 5.0,
        "persistence_score": 10.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 6.5,
          "signals": [
            "PCR 0.51 call writers dominant",
            "\u2605 NEW LONGS: FutOI +22.2% + Price +3.4%",
            "Del 1.77x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 3.43,
          "price_sign": 1,
          "pcr_d1": 0.54,
          "pcr_d2": 0.51,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": 22.17,
          "oi_sign": 1,
          "avg_del": 1.77,
          "peak_del": 2.61,
          "del_chg": 1.68,
          "avg_vol": 1.595,
          "call_oi_growth_pct": 86.37,
          "put_oi_growth_pct": 76.72,
          "opt_oi_growth_pct": 82.99,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 12.0,
          "signals": [
            "PCR 0.65 neutral",
            "PCR surging +0.14",
            "\u2605 NEW LONGS: FutOI +7.0% + Price +1.5%",
            "Del 1.85x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.52,
          "price_sign": 1,
          "pcr_d1": 0.51,
          "pcr_d2": 0.65,
          "pcr_chg": 0.14,
          "fut_oi_chg_pct": 6.95,
          "oi_sign": 1,
          "avg_del": 1.85,
          "peak_del": 2.61,
          "del_chg": -1.52,
          "avg_vol": 1.775,
          "call_oi_growth_pct": -0.3,
          "put_oi_growth_pct": 26.78,
          "opt_oi_growth_pct": 8.86,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.66,
          "pcr": 0.54,
          "pcr_chg_1d": -0.08,
          "fut_oi": 3235750,
          "oi_chg_pct": -1.17,
          "delivery": 0.93,
          "volume": 1.29,
          "call_oi": 902825,
          "put_oi": 487025
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 3.43,
          "pcr": 0.51,
          "pcr_chg_1d": -0.03,
          "fut_oi": 3953075,
          "oi_chg_pct": 13.08,
          "delivery": 2.61,
          "volume": 1.9,
          "call_oi": 1682625,
          "put_oi": 860650
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.52,
          "pcr": 0.65,
          "pcr_chg_1d": 0.14,
          "fut_oi": 4227825,
          "oi_chg_pct": 6.95,
          "delivery": 1.09,
          "volume": 1.65,
          "call_oi": 1677550,
          "put_oi": 1091125
        }
      ]
    },
    {
      "symbol": "360ONE",
      "rank": 15,
      "days_available": 3,
      "latest_score": 12.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          14.0,
          12.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.27,
        "pcr_first": 0.45,
        "pcr_last": 0.99,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 94.0,
        "cumulative_price_chg_pct_window": 4.22,
        "persistence_score": 12.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 14.0,
          "signals": [
            "PCR 0.78 neutral-to-bullish",
            "PCR surging +0.21",
            "\u2605 NEW LONGS: FutOI +93.2% + Price +2.7%",
            "Del 1.21x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 2.72,
          "price_sign": 1,
          "pcr_d1": 0.45,
          "pcr_d2": 0.78,
          "pcr_chg": 0.21,
          "fut_oi_chg_pct": 93.25,
          "oi_sign": 1,
          "avg_del": 1.21,
          "peak_del": 1.94,
          "del_chg": 1.46,
          "avg_vol": 1.28,
          "call_oi_growth_pct": 710.43,
          "put_oi_growth_pct": 1281.25,
          "opt_oi_growth_pct": 888.93,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 12.0,
          "signals": [
            "PCR 0.99 approaching bullish zone",
            "PCR surging +0.21",
            "Del 1.22x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.46,
          "price_sign": 1,
          "pcr_d1": 0.78,
          "pcr_d2": 0.99,
          "pcr_chg": 0.21,
          "fut_oi_chg_pct": 0.39,
          "oi_sign": 1,
          "avg_del": 1.22,
          "peak_del": 1.94,
          "del_chg": -1.44,
          "avg_vol": 1.275,
          "call_oi_growth_pct": 3.33,
          "put_oi_growth_pct": 31.9,
          "opt_oi_growth_pct": 15.81,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.36,
          "pcr": 0.45,
          "pcr_chg_1d": -0.02,
          "fut_oi": 2599000,
          "oi_chg_pct": 0.58,
          "delivery": 0.48,
          "volume": 0.57,
          "call_oi": 105500,
          "put_oi": 48000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 2.72,
          "pcr": 0.78,
          "pcr_chg_1d": 0.21,
          "fut_oi": 5022500,
          "oi_chg_pct": 9.63,
          "delivery": 1.94,
          "volume": 1.99,
          "call_oi": 855000,
          "put_oi": 663000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.46,
          "pcr": 0.99,
          "pcr_chg_1d": 0.21,
          "fut_oi": 5042000,
          "oi_chg_pct": 0.39,
          "delivery": 0.5,
          "volume": 0.56,
          "call_oi": 883500,
          "put_oi": 874500
        }
      ]
    },
    {
      "symbol": "ABCAPITAL",
      "rank": 16,
      "days_available": 3,
      "latest_score": 11.5,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.5,
          11.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.055,
        "pcr_first": 0.93,
        "pcr_last": 1.04,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -2.05,
        "cumulative_price_chg_pct_window": 1.03,
        "persistence_score": 6.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -4.5,
          "signals": [
            "PCR 0.97 approaching bullish zone",
            "Del 1.29x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -1.14,
          "price_sign": -1,
          "pcr_d1": 0.93,
          "pcr_d2": 0.97,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -2.23,
          "oi_sign": -1,
          "avg_del": 1.295,
          "peak_del": 1.94,
          "del_chg": 1.29,
          "avg_vol": 1.17,
          "call_oi_growth_pct": 22.26,
          "put_oi_growth_pct": 27.25,
          "opt_oi_growth_pct": 24.67,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 11.5,
          "signals": [
            "PCR 1.04 ABOVE 1.0 \u2014 put writers dominant",
            "PCR rising +0.07",
            "Del 1.48x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 2.2,
          "price_sign": 1,
          "pcr_d1": 0.97,
          "pcr_d2": 1.04,
          "pcr_chg": 0.07,
          "fut_oi_chg_pct": 0.18,
          "oi_sign": 1,
          "avg_del": 1.485,
          "peak_del": 1.94,
          "del_chg": -0.91,
          "avg_vol": 1.255,
          "call_oi_growth_pct": 1.77,
          "put_oi_growth_pct": 9.33,
          "opt_oi_growth_pct": 5.49,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.64,
          "pcr": 0.93,
          "pcr_chg_1d": 0.04,
          "fut_oi": 44971700,
          "oi_chg_pct": -2.03,
          "delivery": 0.65,
          "volume": 0.78,
          "call_oi": 6727000,
          "put_oi": 6268200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.14,
          "pcr": 0.97,
          "pcr_chg_1d": -0.01,
          "fut_oi": 43970400,
          "oi_chg_pct": 3.43,
          "delivery": 1.94,
          "volume": 1.56,
          "call_oi": 8224300,
          "put_oi": 7976300
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.2,
          "pcr": 1.04,
          "pcr_chg_1d": 0.07,
          "fut_oi": 44051000,
          "oi_chg_pct": 0.18,
          "delivery": 1.03,
          "volume": 0.95,
          "call_oi": 8370000,
          "put_oi": 8720300
        }
      ]
    },
    {
      "symbol": "PIDILITIND",
      "rank": 17,
      "days_available": 3,
      "latest_score": 11.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -5.5,
          11.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.07,
        "pcr_first": 1.0,
        "pcr_last": 0.86,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 7.58,
        "cumulative_price_chg_pct_window": 0.16,
        "persistence_score": 5.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -5.5,
          "signals": [
            "PCR 0.84 neutral-to-bullish",
            "\u26a0 NEW SHORTS: FutOI +4.8% + Price -0.6%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.56,
          "price_sign": -1,
          "pcr_d1": 1.0,
          "pcr_d2": 0.84,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 4.84,
          "oi_sign": 1,
          "avg_del": 0.935,
          "peak_del": 0.94,
          "del_chg": -0.01,
          "avg_vol": 0.915,
          "call_oi_growth_pct": 124.42,
          "put_oi_growth_pct": 88.52,
          "opt_oi_growth_pct": 106.49,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 11.0,
          "signals": [
            "PCR 0.86 approaching bullish zone",
            "\u2605 NEW LONGS: FutOI +2.6% + Price +0.7%",
            "Del 1.34x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 0.72,
          "price_sign": 1,
          "pcr_d1": 0.84,
          "pcr_d2": 0.86,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": 2.62,
          "oi_sign": 1,
          "avg_del": 1.34,
          "peak_del": 1.75,
          "del_chg": 0.82,
          "avg_vol": 1.185,
          "call_oi_growth_pct": -0.57,
          "put_oi_growth_pct": 2.05,
          "opt_oi_growth_pct": 0.62,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.71,
          "pcr": 1.0,
          "pcr_chg_1d": -0.2,
          "fut_oi": 7475500,
          "oi_chg_pct": 0.35,
          "delivery": 0.94,
          "volume": 0.96,
          "call_oi": 428000,
          "put_oi": 427000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.56,
          "pcr": 0.84,
          "pcr_chg_1d": -0.02,
          "fut_oi": 7837000,
          "oi_chg_pct": 0.04,
          "delivery": 0.93,
          "volume": 0.87,
          "call_oi": 960500,
          "put_oi": 805000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.72,
          "pcr": 0.86,
          "pcr_chg_1d": 0.02,
          "fut_oi": 8042000,
          "oi_chg_pct": 2.62,
          "delivery": 1.75,
          "volume": 1.5,
          "call_oi": 955000,
          "put_oi": 821500
        }
      ]
    },
    {
      "symbol": "NAUKRI",
      "rank": 18,
      "days_available": 3,
      "latest_score": -11.0,
      "latest_tier": "TIER 1 \u2014 STRONG DISTRIBUTION",
      "latest_sign": "bearish",
      "latest_phase": "phase_1_short",
      "latest_interpretation": "Mild short build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (SHORT)",
        "direction": "short",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -9.0,
          -11.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 2,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.02,
        "pcr_first": 0.48,
        "pcr_last": 0.44,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 6.16,
        "cumulative_price_chg_pct_window": -4.05,
        "persistence_score": -10.33,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -9.0,
          "signals": [
            "PCR 0.50 call writers dominant",
            "PCR rising +0.04",
            "\u26a0 NEW SHORTS: FutOI +4.1% + Price -2.9%",
            "Del 1.09x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_short",
          "price_chg_pct": -2.93,
          "price_sign": -1,
          "pcr_d1": 0.48,
          "pcr_d2": 0.5,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": 4.14,
          "oi_sign": 1,
          "avg_del": 1.09,
          "peak_del": 1.65,
          "del_chg": 1.12,
          "avg_vol": 1.415,
          "call_oi_growth_pct": 36.63,
          "put_oi_growth_pct": 43.98,
          "opt_oi_growth_pct": 39.01,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -11.0,
          "signals": [
            "PCR 0.44 call writers dominant",
            "PCR easing -0.06",
            "Del 1.70x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.15,
          "price_sign": -1,
          "pcr_d1": 0.5,
          "pcr_d2": 0.44,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": 1.94,
          "oi_sign": 1,
          "avg_del": 1.7,
          "peak_del": 1.75,
          "del_chg": 0.1,
          "avg_vol": 2.035,
          "call_oi_growth_pct": 18.47,
          "put_oi_growth_pct": 4.63,
          "opt_oi_growth_pct": 13.84,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.81,
          "pcr": 0.48,
          "pcr_chg_1d": 0.05,
          "fut_oi": 9671250,
          "oi_chg_pct": -1.18,
          "delivery": 0.53,
          "volume": 0.59,
          "call_oi": 1603125,
          "put_oi": 765750
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.93,
          "pcr": 0.5,
          "pcr_chg_1d": 0.04,
          "fut_oi": 10071375,
          "oi_chg_pct": 5.63,
          "delivery": 1.65,
          "volume": 2.24,
          "call_oi": 2190375,
          "put_oi": 1102500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -1.15,
          "pcr": 0.44,
          "pcr_chg_1d": -0.06,
          "fut_oi": 10266750,
          "oi_chg_pct": 1.94,
          "delivery": 1.75,
          "volume": 1.83,
          "call_oi": 2595000,
          "put_oi": 1153500
        }
      ]
    },
    {
      "symbol": "HEROMOTOCO",
      "rank": 19,
      "days_available": 3,
      "latest_score": 10.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.0,
          10.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.035,
        "pcr_first": 0.89,
        "pcr_last": 0.96,
        "days_delivery_institutional": 3,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 10.08,
        "cumulative_price_chg_pct_window": 3.38,
        "persistence_score": 6.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -2.0,
          "signals": [
            "PCR 0.84 neutral-to-bullish"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.07,
          "price_sign": 0,
          "pcr_d1": 0.89,
          "pcr_d2": 0.84,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": 9.8,
          "oi_sign": 1,
          "avg_del": 1.27,
          "peak_del": 1.28,
          "del_chg": -0.02,
          "avg_vol": 1.2,
          "call_oi_growth_pct": 97.69,
          "put_oi_growth_pct": 85.04,
          "opt_oi_growth_pct": 91.72,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 10.0,
          "signals": [
            "PCR 0.96 approaching bullish zone",
            "PCR surging +0.12",
            "Del 1.36x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 3.45,
          "price_sign": 1,
          "pcr_d1": 0.84,
          "pcr_d2": 0.96,
          "pcr_chg": 0.12,
          "fut_oi_chg_pct": 0.25,
          "oi_sign": 1,
          "avg_del": 1.36,
          "peak_del": 1.46,
          "del_chg": 0.2,
          "avg_vol": 1.36,
          "call_oi_growth_pct": -2.73,
          "put_oi_growth_pct": 11.52,
          "opt_oi_growth_pct": 3.76,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.17,
          "pcr": 0.89,
          "pcr_chg_1d": 0.06,
          "fut_oi": 3551850,
          "oi_chg_pct": 3.75,
          "delivery": 1.28,
          "volume": 1.07,
          "call_oi": 635400,
          "put_oi": 568650
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.07,
          "pcr": 0.84,
          "pcr_chg_1d": -0.03,
          "fut_oi": 3899850,
          "oi_chg_pct": 3.09,
          "delivery": 1.26,
          "volume": 1.33,
          "call_oi": 1256100,
          "put_oi": 1052250
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.45,
          "pcr": 0.96,
          "pcr_chg_1d": 0.12,
          "fut_oi": 3909750,
          "oi_chg_pct": 0.25,
          "delivery": 1.46,
          "volume": 1.39,
          "call_oi": 1221750,
          "put_oi": 1173450
        }
      ]
    },
    {
      "symbol": "ASIANPAINT",
      "rank": 20,
      "days_available": 3,
      "latest_score": 10.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.5,
          10.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.17,
        "pcr_first": 1.44,
        "pcr_last": 1.1,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 7.22,
        "cumulative_price_chg_pct_window": 3.43,
        "persistence_score": 5.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -4.5,
          "signals": [
            "PCR 1.08 ABOVE 1.0 \u2014 put writers dominant",
            "\u26a0 NEW SHORTS: FutOI +6.9% + Price -0.6%",
            "Del 1.07x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_short",
          "price_chg_pct": -0.56,
          "price_sign": -1,
          "pcr_d1": 1.44,
          "pcr_d2": 1.08,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 6.94,
          "oi_sign": 1,
          "avg_del": 1.07,
          "peak_del": 1.18,
          "del_chg": 0.22,
          "avg_vol": 0.975,
          "call_oi_growth_pct": 76.92,
          "put_oi_growth_pct": 32.6,
          "opt_oi_growth_pct": 50.76,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 10.0,
          "signals": [
            "PCR 1.10 ABOVE 1.0 \u2014 put writers dominant",
            "Del 1.14x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 4.01,
          "price_sign": 1,
          "pcr_d1": 1.08,
          "pcr_d2": 1.1,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": 0.26,
          "oi_sign": 1,
          "avg_del": 1.14,
          "peak_del": 1.18,
          "del_chg": -0.08,
          "avg_vol": 1.215,
          "call_oi_growth_pct": 16.09,
          "put_oi_growth_pct": 18.09,
          "opt_oi_growth_pct": 17.13,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.8,
          "pcr": 1.44,
          "pcr_chg_1d": 0.02,
          "fut_oi": 13973750,
          "oi_chg_pct": -0.18,
          "delivery": 0.96,
          "volume": 0.94,
          "call_oi": 1918000,
          "put_oi": 2762000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.56,
          "pcr": 1.08,
          "pcr_chg_1d": 0.01,
          "fut_oi": 14943250,
          "oi_chg_pct": -0.51,
          "delivery": 1.18,
          "volume": 1.01,
          "call_oi": 3393250,
          "put_oi": 3662500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 4.01,
          "pcr": 1.1,
          "pcr_chg_1d": 0.02,
          "fut_oi": 14982750,
          "oi_chg_pct": 0.26,
          "delivery": 1.1,
          "volume": 1.42,
          "call_oi": 3939250,
          "put_oi": 4325000
        }
      ]
    },
    {
      "symbol": "INFY",
      "rank": 21,
      "days_available": 3,
      "latest_score": -10.0,
      "latest_tier": "TIER 1 \u2014 STRONG DISTRIBUTION",
      "latest_sign": "bearish",
      "latest_phase": "phase_2_short",
      "latest_interpretation": "\u26a0 NEW SHORTS (Bearish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (SHORT)",
        "direction": "short",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -7.5,
          -10.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 2,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.16,
        "pcr_first": 1.05,
        "pcr_last": 0.73,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 8.39,
        "cumulative_price_chg_pct_window": -3.99,
        "persistence_score": -9.17,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -7.5,
          "signals": [
            "PCR 0.76 neutral-to-bullish",
            "PCR easing -0.04",
            "\u26a0 NEW SHORTS: FutOI +3.1% + Price -1.1%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.08,
          "price_sign": -1,
          "pcr_d1": 1.05,
          "pcr_d2": 0.76,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 3.12,
          "oi_sign": 1,
          "avg_del": 0.8,
          "peak_del": 1.11,
          "del_chg": 0.62,
          "avg_vol": 0.915,
          "call_oi_growth_pct": 73.52,
          "put_oi_growth_pct": 26.05,
          "opt_oi_growth_pct": 49.18,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -10.0,
          "signals": [
            "PCR 0.73 neutral",
            "\u26a0 NEW SHORTS: FutOI +5.1% + Price -2.9%",
            "Del 1.29x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -2.94,
          "price_sign": -1,
          "pcr_d1": 0.76,
          "pcr_d2": 0.73,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": 5.11,
          "oi_sign": 1,
          "avg_del": 1.29,
          "peak_del": 1.47,
          "del_chg": 0.36,
          "avg_vol": 1.29,
          "call_oi_growth_pct": 17.8,
          "put_oi_growth_pct": 12.91,
          "opt_oi_growth_pct": 15.68,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.01,
          "pcr": 1.05,
          "pcr_chg_1d": 0.03,
          "fut_oi": 74538000,
          "oi_chg_pct": -5.09,
          "delivery": 0.49,
          "volume": 0.64,
          "call_oi": 12075600,
          "put_oi": 12704800
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.08,
          "pcr": 0.76,
          "pcr_chg_1d": -0.04,
          "fut_oi": 76865200,
          "oi_chg_pct": -0.47,
          "delivery": 1.11,
          "volume": 1.19,
          "call_oi": 20953600,
          "put_oi": 16014400
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -2.94,
          "pcr": 0.73,
          "pcr_chg_1d": -0.03,
          "fut_oi": 80794800,
          "oi_chg_pct": 5.11,
          "delivery": 1.47,
          "volume": 1.39,
          "call_oi": 24682400,
          "put_oi": 18082400
        }
      ]
    },
    {
      "symbol": "COCHINSHIP",
      "rank": 22,
      "days_available": 3,
      "latest_score": 10.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          7.5,
          10.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.005,
        "pcr_first": 0.64,
        "pcr_last": 0.65,
        "days_delivery_institutional": 3,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 211.63,
        "cumulative_price_chg_pct_window": 6.15,
        "persistence_score": 9.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 7.5,
          "signals": [
            "PCR 0.61 neutral",
            "\u2605 NEW LONGS: FutOI +164.4% + Price +3.2%",
            "Del 1.44x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 3.2,
          "price_sign": 1,
          "pcr_d1": 0.64,
          "pcr_d2": 0.61,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": 164.45,
          "oi_sign": 1,
          "avg_del": 1.435,
          "peak_del": 1.66,
          "del_chg": -0.45,
          "avg_vol": 3.47,
          "call_oi_growth_pct": 109.3,
          "put_oi_growth_pct": 100.0,
          "opt_oi_growth_pct": 105.69,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 10.0,
          "signals": [
            "PCR 0.65 neutral",
            "PCR rising +0.04",
            "\u2605 NEW LONGS: FutOI +17.8% + Price +2.9%",
            "Del 1.23x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 2.86,
          "price_sign": 1,
          "pcr_d1": 0.61,
          "pcr_d2": 0.65,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": 17.84,
          "oi_sign": 1,
          "avg_del": 1.225,
          "peak_del": 1.24,
          "del_chg": 0.03,
          "avg_vol": 1.325,
          "call_oi_growth_pct": 32.18,
          "put_oi_growth_pct": 41.37,
          "opt_oi_growth_pct": 35.65,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 12.2,
          "pcr": 0.64,
          "pcr_chg_1d": 0.0,
          "fut_oi": 426400,
          "oi_chg_pct": 0.0,
          "delivery": 1.66,
          "volume": 5.75,
          "call_oi": 335600,
          "put_oi": 213200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 3.2,
          "pcr": 0.61,
          "pcr_chg_1d": -0.03,
          "fut_oi": 1127600,
          "oi_chg_pct": 20.94,
          "delivery": 1.21,
          "volume": 1.19,
          "call_oi": 702400,
          "put_oi": 426400
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.86,
          "pcr": 0.65,
          "pcr_chg_1d": 0.04,
          "fut_oi": 1328800,
          "oi_chg_pct": 17.84,
          "delivery": 1.24,
          "volume": 1.46,
          "call_oi": 928400,
          "put_oi": 602800
        }
      ]
    },
    {
      "symbol": "MOTHERSON",
      "rank": 23,
      "days_available": 3,
      "latest_score": 9.5,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -7.0,
          9.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.05,
        "pcr_first": 0.89,
        "pcr_last": 0.99,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 9.95,
        "cumulative_price_chg_pct_window": 3.43,
        "persistence_score": 4.0,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -7.0,
          "signals": [
            "PCR 0.80 neutral-to-bullish",
            "\u26a0 NEW SHORTS: FutOI +13.1% + Price -1.0%",
            "Del 1.15x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -1.02,
          "price_sign": -1,
          "pcr_d1": 0.89,
          "pcr_d2": 0.8,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 13.14,
          "oi_sign": 1,
          "avg_del": 1.145,
          "peak_del": 1.25,
          "del_chg": -0.21,
          "avg_vol": 1.025,
          "call_oi_growth_pct": 67.34,
          "put_oi_growth_pct": 49.85,
          "opt_oi_growth_pct": 59.1,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 9.5,
          "signals": [
            "PCR 0.99 approaching bullish zone",
            "PCR surging +0.19",
            "Del 1.00x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 4.5,
          "price_sign": 1,
          "pcr_d1": 0.8,
          "pcr_d2": 0.99,
          "pcr_chg": 0.19,
          "fut_oi_chg_pct": -2.82,
          "oi_sign": -1,
          "avg_del": 1.005,
          "peak_del": 1.04,
          "del_chg": -0.07,
          "avg_vol": 0.935,
          "call_oi_growth_pct": 5.24,
          "put_oi_growth_pct": 30.37,
          "opt_oi_growth_pct": 16.39,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.42,
          "pcr": 0.89,
          "pcr_chg_1d": 0.03,
          "fut_oi": 128947050,
          "oi_chg_pct": 1.56,
          "delivery": 1.25,
          "volume": 1.08,
          "call_oi": 17871900,
          "put_oi": 15903900
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.02,
          "pcr": 0.8,
          "pcr_chg_1d": -0.02,
          "fut_oi": 145896450,
          "oi_chg_pct": 0.94,
          "delivery": 1.04,
          "volume": 0.97,
          "call_oi": 29907450,
          "put_oi": 23831250
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 4.5,
          "pcr": 0.99,
          "pcr_chg_1d": 0.19,
          "fut_oi": 141782100,
          "oi_chg_pct": -2.82,
          "delivery": 0.97,
          "volume": 0.9,
          "call_oi": 31475700,
          "put_oi": 31069800
        }
      ]
    },
    {
      "symbol": "CAMS",
      "rank": 24,
      "days_available": 3,
      "latest_score": 9.5,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.5,
          9.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.0,
        "pcr_first": 0.85,
        "pcr_last": 0.85,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 29.88,
        "cumulative_price_chg_pct_window": 1.56,
        "persistence_score": 4.83,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -4.5,
          "signals": [
            "PCR 0.79 neutral-to-bullish",
            "PCR surging +0.10",
            "\u26a0 NEW SHORTS: FutOI +26.4% + Price -0.8%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.82,
          "price_sign": -1,
          "pcr_d1": 0.85,
          "pcr_d2": 0.79,
          "pcr_chg": 0.1,
          "fut_oi_chg_pct": 26.41,
          "oi_sign": 1,
          "avg_del": 0.955,
          "peak_del": 1.1,
          "del_chg": 0.29,
          "avg_vol": 1.08,
          "call_oi_growth_pct": 85.22,
          "put_oi_growth_pct": 71.27,
          "opt_oi_growth_pct": 78.81,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 9.5,
          "signals": [
            "PCR 0.85 approaching bullish zone",
            "PCR rising +0.06",
            "\u2605 NEW LONGS: FutOI +2.7% + Price +2.4%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 2.4,
          "price_sign": 1,
          "pcr_d1": 0.79,
          "pcr_d2": 0.85,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": 2.74,
          "oi_sign": 1,
          "avg_del": 0.845,
          "peak_del": 1.1,
          "del_chg": -0.51,
          "avg_vol": 0.905,
          "call_oi_growth_pct": 3.48,
          "put_oi_growth_pct": 11.68,
          "opt_oi_growth_pct": 7.09,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.72,
          "pcr": 0.85,
          "pcr_chg_1d": -0.17,
          "fut_oi": 5340750,
          "oi_chg_pct": 6.0,
          "delivery": 0.81,
          "volume": 0.99,
          "call_oi": 1141500,
          "put_oi": 971250
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.82,
          "pcr": 0.79,
          "pcr_chg_1d": 0.1,
          "fut_oi": 6751500,
          "oi_chg_pct": 4.14,
          "delivery": 1.1,
          "volume": 1.17,
          "call_oi": 2114250,
          "put_oi": 1663500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.4,
          "pcr": 0.85,
          "pcr_chg_1d": 0.06,
          "fut_oi": 6936750,
          "oi_chg_pct": 2.74,
          "delivery": 0.59,
          "volume": 0.64,
          "call_oi": 2187750,
          "put_oi": 1857750
        }
      ]
    },
    {
      "symbol": "MOTILALOFS",
      "rank": 25,
      "days_available": 3,
      "latest_score": 9.5,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          6.0,
          9.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.3,
        "pcr_first": 1.5,
        "pcr_last": 0.9,
        "days_delivery_institutional": 3,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 170.6,
        "cumulative_price_chg_pct_window": 2.8,
        "persistence_score": 8.33,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 6.0,
          "signals": [
            "PCR 0.87 approaching bullish zone",
            "PCR easing -0.07",
            "Del 1.08x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.5,
          "price_sign": 1,
          "pcr_d1": 1.5,
          "pcr_d2": 0.87,
          "pcr_chg": -0.07,
          "fut_oi_chg_pct": 114.86,
          "oi_sign": 1,
          "avg_del": 1.08,
          "peak_del": 1.13,
          "del_chg": 0.1,
          "avg_vol": 1.42,
          "call_oi_growth_pct": 183.45,
          "put_oi_growth_pct": 63.1,
          "opt_oi_growth_pct": 111.17,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 9.5,
          "signals": [
            "PCR 0.90 approaching bullish zone",
            "\u2605 NEW LONGS: FutOI +25.9% + Price +2.3%",
            "Del 1.19x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 2.29,
          "price_sign": 1,
          "pcr_d1": 0.87,
          "pcr_d2": 0.9,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 25.94,
          "oi_sign": 1,
          "avg_del": 1.19,
          "peak_del": 1.25,
          "del_chg": 0.12,
          "avg_vol": 1.045,
          "call_oi_growth_pct": -2.05,
          "put_oi_growth_pct": 2.1,
          "opt_oi_growth_pct": -0.13,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 7.47,
          "pcr": 1.5,
          "pcr_chg_1d": 0.0,
          "fut_oi": 479725,
          "oi_chg_pct": 0.0,
          "delivery": 1.03,
          "volume": 1.73,
          "call_oi": 346425,
          "put_oi": 520800
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.5,
          "pcr": 0.87,
          "pcr_chg_1d": -0.07,
          "fut_oi": 1030750,
          "oi_chg_pct": 18.33,
          "delivery": 1.13,
          "volume": 1.11,
          "call_oi": 981925,
          "put_oi": 849400
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.29,
          "pcr": 0.9,
          "pcr_chg_1d": 0.03,
          "fut_oi": 1298125,
          "oi_chg_pct": 25.94,
          "delivery": 1.25,
          "volume": 0.98,
          "call_oi": 961775,
          "put_oi": 867225
        }
      ]
    },
    {
      "symbol": "COFORGE",
      "rank": 26,
      "days_available": 3,
      "latest_score": -9.5,
      "latest_tier": "TIER 1 \u2014 STRONG DISTRIBUTION",
      "latest_sign": "bearish",
      "latest_phase": "phase_2_short",
      "latest_interpretation": "\u26a0 NEW SHORTS (Bearish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (SHORT)",
        "direction": "short",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -1.5,
          -9.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.005,
        "pcr_first": 0.58,
        "pcr_last": 0.59,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -3.56,
        "cumulative_price_chg_pct_window": -3.63,
        "persistence_score": -6.83,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -1.5,
          "signals": [
            "PCR 0.65 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.43,
          "price_sign": -1,
          "pcr_d1": 0.58,
          "pcr_d2": 0.65,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -9.68,
          "oi_sign": -1,
          "avg_del": 0.945,
          "peak_del": 1.42,
          "del_chg": 0.95,
          "avg_vol": 0.895,
          "call_oi_growth_pct": 54.42,
          "put_oi_growth_pct": 74.28,
          "opt_oi_growth_pct": 61.68,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -9.5,
          "signals": [
            "PCR 0.59 neutral",
            "PCR easing -0.06",
            "\u26a0 NEW SHORTS: FutOI +6.8% + Price -3.2%",
            "Del 1.12x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -3.21,
          "price_sign": -1,
          "pcr_d1": 0.65,
          "pcr_d2": 0.59,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": 6.78,
          "oi_sign": 1,
          "avg_del": 1.125,
          "peak_del": 1.42,
          "del_chg": -0.59,
          "avg_vol": 1.065,
          "call_oi_growth_pct": 18.26,
          "put_oi_growth_pct": 6.99,
          "opt_oi_growth_pct": 13.82,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.52,
          "pcr": 0.58,
          "pcr_chg_1d": 0.01,
          "fut_oi": 19708500,
          "oi_chg_pct": -0.36,
          "delivery": 0.47,
          "volume": 0.63,
          "call_oi": 4183125,
          "put_oi": 2413125
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.43,
          "pcr": 0.65,
          "pcr_chg_1d": 0.03,
          "fut_oi": 17800125,
          "oi_chg_pct": -0.38,
          "delivery": 1.42,
          "volume": 1.16,
          "call_oi": 6459375,
          "put_oi": 4205625
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -3.21,
          "pcr": 0.59,
          "pcr_chg_1d": -0.06,
          "fut_oi": 19007250,
          "oi_chg_pct": 6.78,
          "delivery": 0.83,
          "volume": 0.97,
          "call_oi": 7639125,
          "put_oi": 4499625
        }
      ]
    },
    {
      "symbol": "KOTAKBANK",
      "rank": 27,
      "days_available": 3,
      "latest_score": 9.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -1.5,
          9.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.015,
        "pcr_first": 1.09,
        "pcr_last": 1.12,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.3,
        "cumulative_price_chg_pct_window": -1.48,
        "persistence_score": 5.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -1.5,
          "signals": [
            "PCR 1.05 ABOVE 1.0 \u2014 put writers dominant",
            "PCR collapsing -0.12"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -2.17,
          "price_sign": -1,
          "pcr_d1": 1.09,
          "pcr_d2": 1.05,
          "pcr_chg": -0.12,
          "fut_oi_chg_pct": -0.01,
          "oi_sign": -1,
          "avg_del": 0.61,
          "peak_del": 0.73,
          "del_chg": -0.24,
          "avg_vol": 0.63,
          "call_oi_growth_pct": 20.77,
          "put_oi_growth_pct": 16.77,
          "opt_oi_growth_pct": 18.69,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 9.0,
          "signals": [
            "PCR 1.12 ABOVE 1.0 \u2014 put writers dominant",
            "PCR rising +0.07"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.71,
          "price_sign": 1,
          "pcr_d1": 1.05,
          "pcr_d2": 1.12,
          "pcr_chg": 0.07,
          "fut_oi_chg_pct": 0.31,
          "oi_sign": 1,
          "avg_del": 0.82,
          "peak_del": 1.15,
          "del_chg": 0.66,
          "avg_vol": 0.825,
          "call_oi_growth_pct": -1.51,
          "put_oi_growth_pct": 4.76,
          "opt_oi_growth_pct": 1.71,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.75,
          "pcr": 1.09,
          "pcr_chg_1d": -0.01,
          "fut_oi": 216250000,
          "oi_chg_pct": 2.07,
          "delivery": 0.73,
          "volume": 0.72,
          "call_oi": 19564000,
          "put_oi": 21310000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.17,
          "pcr": 1.05,
          "pcr_chg_1d": -0.12,
          "fut_oi": 216218000,
          "oi_chg_pct": 0.06,
          "delivery": 0.49,
          "volume": 0.54,
          "call_oi": 23628000,
          "put_oi": 24884000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.71,
          "pcr": 1.12,
          "pcr_chg_1d": 0.07,
          "fut_oi": 216888000,
          "oi_chg_pct": 0.31,
          "delivery": 1.15,
          "volume": 1.11,
          "call_oi": 23272000,
          "put_oi": 26068000
        }
      ]
    },
    {
      "symbol": "MARICO",
      "rank": 28,
      "days_available": 3,
      "latest_score": 9.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          6.5,
          9.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.115,
        "pcr_first": 0.93,
        "pcr_last": 1.16,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -2.48,
        "cumulative_price_chg_pct_window": 2.12,
        "persistence_score": 8.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 6.5,
          "signals": [
            "PCR 1.06 ABOVE 1.0 \u2014 put writers dominant",
            "PCR rising +0.05"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.01,
          "price_sign": 0,
          "pcr_d1": 0.93,
          "pcr_d2": 1.06,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": -1.57,
          "oi_sign": -1,
          "avg_del": 1.02,
          "peak_del": 1.27,
          "del_chg": -0.5,
          "avg_vol": 0.99,
          "call_oi_growth_pct": 108.94,
          "put_oi_growth_pct": 137.24,
          "opt_oi_growth_pct": 122.6,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 9.0,
          "signals": [
            "PCR 1.16 ABOVE 1.0 \u2014 put writers dominant",
            "PCR surging +0.10",
            "Del 1.02x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 2.13,
          "price_sign": 1,
          "pcr_d1": 1.06,
          "pcr_d2": 1.16,
          "pcr_chg": 0.1,
          "fut_oi_chg_pct": -0.92,
          "oi_sign": -1,
          "avg_del": 1.015,
          "peak_del": 1.26,
          "del_chg": 0.49,
          "avg_vol": 0.855,
          "call_oi_growth_pct": -9.45,
          "put_oi_growth_pct": -0.62,
          "opt_oi_growth_pct": -4.91,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.16,
          "pcr": 0.93,
          "pcr_chg_1d": -0.03,
          "fut_oi": 26859600,
          "oi_chg_pct": 1.83,
          "delivery": 1.27,
          "volume": 1.26,
          "call_oi": 1920000,
          "put_oi": 1791600
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.01,
          "pcr": 1.06,
          "pcr_chg_1d": 0.05,
          "fut_oi": 26437200,
          "oi_chg_pct": 0.91,
          "delivery": 0.77,
          "volume": 0.72,
          "call_oi": 4011600,
          "put_oi": 4250400
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.13,
          "pcr": 1.16,
          "pcr_chg_1d": 0.1,
          "fut_oi": 26194800,
          "oi_chg_pct": -0.92,
          "delivery": 1.26,
          "volume": 0.99,
          "call_oi": 3632400,
          "put_oi": 4224000
        }
      ]
    },
    {
      "symbol": "FEDERALBNK",
      "rank": 29,
      "days_available": 3,
      "latest_score": 9.0,
      "latest_tier": "TIER 1 \u2014 STRONG ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -0.5,
          9.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.03,
        "pcr_first": 1.03,
        "pcr_last": 1.09,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -4.88,
        "cumulative_price_chg_pct_window": 2.56,
        "persistence_score": 5.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -0.5,
          "signals": [
            "PCR 0.93 approaching bullish zone"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.4,
          "price_sign": -1,
          "pcr_d1": 1.03,
          "pcr_d2": 0.93,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -3.37,
          "oi_sign": -1,
          "avg_del": 0.59,
          "peak_del": 0.68,
          "del_chg": -0.18,
          "avg_vol": 0.635,
          "call_oi_growth_pct": 72.7,
          "put_oi_growth_pct": 54.82,
          "opt_oi_growth_pct": 63.62,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 9.0,
          "signals": [
            "PCR 1.09 ABOVE 1.0 \u2014 put writers dominant",
            "PCR surging +0.16"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 2.97,
          "price_sign": 1,
          "pcr_d1": 0.93,
          "pcr_d2": 1.09,
          "pcr_chg": 0.16,
          "fut_oi_chg_pct": -1.56,
          "oi_sign": -1,
          "avg_del": 0.89,
          "peak_del": 1.28,
          "del_chg": 0.78,
          "avg_vol": 0.895,
          "call_oi_growth_pct": 5.06,
          "put_oi_growth_pct": 24.23,
          "opt_oi_growth_pct": 14.27,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.16,
          "pcr": 1.03,
          "pcr_chg_1d": 0.03,
          "fut_oi": 82455000,
          "oi_chg_pct": 0.54,
          "delivery": 0.68,
          "volume": 0.72,
          "call_oi": 13625000,
          "put_oi": 14065000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.4,
          "pcr": 0.93,
          "pcr_chg_1d": 0.0,
          "fut_oi": 79675000,
          "oi_chg_pct": -0.16,
          "delivery": 0.5,
          "volume": 0.55,
          "call_oi": 23530000,
          "put_oi": 21775000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.97,
          "pcr": 1.09,
          "pcr_chg_1d": 0.16,
          "fut_oi": 78430000,
          "oi_chg_pct": -1.56,
          "delivery": 1.28,
          "volume": 1.24,
          "call_oi": 24720000,
          "put_oi": 27050000
        }
      ]
    },
    {
      "symbol": "VEDL",
      "rank": 30,
      "days_available": 3,
      "latest_score": 8.5,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          10.5,
          8.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.075,
        "pcr_first": 0.78,
        "pcr_last": 0.93,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 12.11,
        "cumulative_price_chg_pct_window": 3.29,
        "persistence_score": 9.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 10.5,
          "signals": [
            "PCR 0.94 approaching bullish zone",
            "PCR rising +0.06",
            "\u2605 NEW LONGS: FutOI +9.9% + Price +2.2%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 2.16,
          "price_sign": 1,
          "pcr_d1": 0.78,
          "pcr_d2": 0.94,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": 9.86,
          "oi_sign": 1,
          "avg_del": 0.91,
          "peak_del": 1.02,
          "del_chg": 0.22,
          "avg_vol": 0.925,
          "call_oi_growth_pct": 17.67,
          "put_oi_growth_pct": 40.59,
          "opt_oi_growth_pct": 27.75,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 8.5,
          "signals": [
            "PCR 0.93 approaching bullish zone",
            "\u2605 NEW LONGS: FutOI +2.1% + Price +1.1%",
            "Del 1.00x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.11,
          "price_sign": 1,
          "pcr_d1": 0.94,
          "pcr_d2": 0.93,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": 2.05,
          "oi_sign": 1,
          "avg_del": 1.005,
          "peak_del": 1.02,
          "del_chg": -0.03,
          "avg_vol": 0.935,
          "call_oi_growth_pct": 2.14,
          "put_oi_growth_pct": 1.8,
          "opt_oi_growth_pct": 1.98,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.42,
          "pcr": 0.78,
          "pcr_chg_1d": 0.03,
          "fut_oi": 47759500,
          "oi_chg_pct": -6.29,
          "delivery": 0.8,
          "volume": 0.92,
          "call_oi": 20742550,
          "put_oi": 16270200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 2.16,
          "pcr": 0.94,
          "pcr_chg_1d": 0.06,
          "fut_oi": 52467600,
          "oi_chg_pct": 5.37,
          "delivery": 1.02,
          "volume": 0.93,
          "call_oi": 24408750,
          "put_oi": 22874650
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.11,
          "pcr": 0.93,
          "pcr_chg_1d": -0.01,
          "fut_oi": 53545150,
          "oi_chg_pct": 2.05,
          "delivery": 0.99,
          "volume": 0.94,
          "call_oi": 24932000,
          "put_oi": 23287500
        }
      ]
    },
    {
      "symbol": "VBL",
      "rank": 31,
      "days_available": 3,
      "latest_score": 8.5,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.0,
          8.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.065,
        "pcr_first": 0.63,
        "pcr_last": 0.76,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 6.87,
        "cumulative_price_chg_pct_window": 2.3,
        "persistence_score": 7.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 4.0,
          "signals": [
            "PCR 0.69 neutral"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.24,
          "price_sign": 0,
          "pcr_d1": 0.63,
          "pcr_d2": 0.69,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 4.9,
          "oi_sign": 1,
          "avg_del": 0.875,
          "peak_del": 1.15,
          "del_chg": 0.55,
          "avg_vol": 0.94,
          "call_oi_growth_pct": 24.11,
          "put_oi_growth_pct": 35.57,
          "opt_oi_growth_pct": 28.54,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 8.5,
          "signals": [
            "PCR 0.76 neutral-to-bullish",
            "PCR rising +0.07",
            "Del 1.25x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 2.06,
          "price_sign": 1,
          "pcr_d1": 0.69,
          "pcr_d2": 0.76,
          "pcr_chg": 0.07,
          "fut_oi_chg_pct": 1.87,
          "oi_sign": 1,
          "avg_del": 1.255,
          "peak_del": 1.36,
          "del_chg": 0.21,
          "avg_vol": 1.185,
          "call_oi_growth_pct": 1.68,
          "put_oi_growth_pct": 11.78,
          "opt_oi_growth_pct": 5.8,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.61,
          "pcr": 0.63,
          "pcr_chg_1d": -0.11,
          "fut_oi": 43583625,
          "oi_chg_pct": 1.07,
          "delivery": 0.6,
          "volume": 0.71,
          "call_oi": 8259750,
          "put_oi": 5206500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.24,
          "pcr": 0.69,
          "pcr_chg_1d": 0.03,
          "fut_oi": 45721125,
          "oi_chg_pct": 3.38,
          "delivery": 1.15,
          "volume": 1.17,
          "call_oi": 10251000,
          "put_oi": 7058250
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.06,
          "pcr": 0.76,
          "pcr_chg_1d": 0.07,
          "fut_oi": 46577250,
          "oi_chg_pct": 1.87,
          "delivery": 1.36,
          "volume": 1.2,
          "call_oi": 10423125,
          "put_oi": 7889625
        }
      ]
    },
    {
      "symbol": "BOSCHLTD",
      "rank": 32,
      "days_available": 3,
      "latest_score": 8.5,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          8.5,
          8.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.02,
        "pcr_first": 0.71,
        "pcr_last": 0.75,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 23.57,
        "cumulative_price_chg_pct_window": 3.88,
        "persistence_score": 8.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 8.5,
          "signals": [
            "PCR 0.71 neutral",
            "PCR rising +0.08",
            "\u2605 NEW LONGS: FutOI +33.4% + Price +2.3%",
            "Del 2.42x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 2.32,
          "price_sign": 1,
          "pcr_d1": 0.71,
          "pcr_d2": 0.71,
          "pcr_chg": 0.08,
          "fut_oi_chg_pct": 33.39,
          "oi_sign": 1,
          "avg_del": 2.42,
          "peak_del": 3.04,
          "del_chg": 1.24,
          "avg_vol": 2.945,
          "call_oi_growth_pct": 196.35,
          "put_oi_growth_pct": 195.64,
          "opt_oi_growth_pct": 196.05,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 8.5,
          "signals": [
            "PCR 0.75 neutral-to-bullish",
            "PCR rising +0.04",
            "Del 1.98x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.52,
          "price_sign": 1,
          "pcr_d1": 0.71,
          "pcr_d2": 0.75,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": -7.37,
          "oi_sign": -1,
          "avg_del": 1.98,
          "peak_del": 3.04,
          "del_chg": -2.12,
          "avg_vol": 2.06,
          "call_oi_growth_pct": 0.16,
          "put_oi_growth_pct": 6.5,
          "opt_oi_growth_pct": 2.78,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 6.58,
          "pcr": 0.71,
          "pcr_chg_1d": -0.4,
          "fut_oi": 274300,
          "oi_chg_pct": 30.32,
          "delivery": 1.8,
          "volume": 2.49,
          "call_oi": 88300,
          "put_oi": 62450
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 2.32,
          "pcr": 0.71,
          "pcr_chg_1d": 0.08,
          "fut_oi": 365900,
          "oi_chg_pct": 0.6,
          "delivery": 3.04,
          "volume": 3.4,
          "call_oi": 261675,
          "put_oi": 184625
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.52,
          "pcr": 0.75,
          "pcr_chg_1d": 0.04,
          "fut_oi": 338950,
          "oi_chg_pct": -7.37,
          "delivery": 0.92,
          "volume": 0.72,
          "call_oi": 262100,
          "put_oi": 196625
        }
      ]
    },
    {
      "symbol": "LICI",
      "rank": 33,
      "days_available": 3,
      "latest_score": 8.5,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.0,
          8.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.025,
        "pcr_first": 0.71,
        "pcr_last": 0.66,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 10.88,
        "cumulative_price_chg_pct_window": 0.58,
        "persistence_score": 5.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -2.0,
          "signals": [
            "PCR 0.65 neutral",
            "PCR rising +0.04"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.04,
          "price_sign": 0,
          "pcr_d1": 0.71,
          "pcr_d2": 0.65,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": 9.71,
          "oi_sign": 1,
          "avg_del": 0.84,
          "peak_del": 1.19,
          "del_chg": 0.7,
          "avg_vol": 0.78,
          "call_oi_growth_pct": 101.81,
          "put_oi_growth_pct": 83.17,
          "opt_oi_growth_pct": 94.06,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 8.5,
          "signals": [
            "PCR 0.66 neutral",
            "Del 1.39x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.62,
          "price_sign": 1,
          "pcr_d1": 0.65,
          "pcr_d2": 0.66,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 1.07,
          "oi_sign": 1,
          "avg_del": 1.385,
          "peak_del": 1.58,
          "del_chg": 0.39,
          "avg_vol": 1.115,
          "call_oi_growth_pct": 5.68,
          "put_oi_growth_pct": 8.65,
          "opt_oi_growth_pct": 6.85,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.8,
          "pcr": 0.71,
          "pcr_chg_1d": -0.04,
          "fut_oi": 8373400,
          "oi_chg_pct": 0.45,
          "delivery": 0.49,
          "volume": 0.59,
          "call_oi": 2166500,
          "put_oi": 1542800
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.04,
          "pcr": 0.65,
          "pcr_chg_1d": 0.04,
          "fut_oi": 9186100,
          "oi_chg_pct": 3.4,
          "delivery": 1.19,
          "volume": 0.97,
          "call_oi": 4372200,
          "put_oi": 2825900
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.62,
          "pcr": 0.66,
          "pcr_chg_1d": 0.01,
          "fut_oi": 9284800,
          "oi_chg_pct": 1.07,
          "delivery": 1.58,
          "volume": 1.26,
          "call_oi": 4620700,
          "put_oi": 3070200
        }
      ]
    },
    {
      "symbol": "DIVISLAB",
      "rank": 34,
      "days_available": 3,
      "latest_score": 8.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          12.0,
          8.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.07,
        "pcr_first": 0.96,
        "pcr_last": 1.1,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 7.85,
        "cumulative_price_chg_pct_window": 3.99,
        "persistence_score": 9.33,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 12.0,
          "signals": [
            "PCR 1.06 ABOVE 1.0 \u2014 put writers dominant",
            "PCR rising +0.07",
            "\u2605 NEW LONGS: FutOI +7.8% + Price +1.2%",
            "Del 1.02x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.2,
          "price_sign": 1,
          "pcr_d1": 0.96,
          "pcr_d2": 1.06,
          "pcr_chg": 0.07,
          "fut_oi_chg_pct": 7.79,
          "oi_sign": 1,
          "avg_del": 1.015,
          "peak_del": 1.47,
          "del_chg": -0.91,
          "avg_vol": 1.075,
          "call_oi_growth_pct": 71.16,
          "put_oi_growth_pct": 89.69,
          "opt_oi_growth_pct": 80.24,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 8.0,
          "signals": [
            "PCR 1.10 ABOVE 1.0 \u2014 put writers dominant",
            "PCR rising +0.04"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 2.76,
          "price_sign": 1,
          "pcr_d1": 1.06,
          "pcr_d2": 1.1,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": 0.05,
          "oi_sign": 1,
          "avg_del": 0.705,
          "peak_del": 0.85,
          "del_chg": 0.29,
          "avg_vol": 0.77,
          "call_oi_growth_pct": -2.1,
          "put_oi_growth_pct": 1.36,
          "opt_oi_growth_pct": -0.32,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.68,
          "pcr": 0.96,
          "pcr_chg_1d": -0.01,
          "fut_oi": 2702500,
          "oi_chg_pct": 1.39,
          "delivery": 1.47,
          "volume": 1.57,
          "call_oi": 367900,
          "put_oi": 353200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.2,
          "pcr": 1.06,
          "pcr_chg_1d": 0.07,
          "fut_oi": 2913100,
          "oi_chg_pct": 0.81,
          "delivery": 0.56,
          "volume": 0.58,
          "call_oi": 629700,
          "put_oi": 670000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.76,
          "pcr": 1.1,
          "pcr_chg_1d": 0.04,
          "fut_oi": 2914700,
          "oi_chg_pct": 0.05,
          "delivery": 0.85,
          "volume": 0.96,
          "call_oi": 616500,
          "put_oi": 679100
        }
      ]
    },
    {
      "symbol": "AMBUJACEM",
      "rank": 35,
      "days_available": 3,
      "latest_score": 8.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -3.5,
          8.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.04,
        "pcr_first": 1.0,
        "pcr_last": 0.92,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -3.48,
        "cumulative_price_chg_pct_window": -0.34,
        "persistence_score": 4.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -3.5,
          "signals": [
            "PCR 0.87 approaching bullish zone",
            "PCR easing -0.05"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -2.84,
          "price_sign": -1,
          "pcr_d1": 1.0,
          "pcr_d2": 0.87,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": -0.88,
          "oi_sign": -1,
          "avg_del": 0.85,
          "peak_del": 1.11,
          "del_chg": 0.52,
          "avg_vol": 0.995,
          "call_oi_growth_pct": 30.65,
          "put_oi_growth_pct": 13.7,
          "opt_oi_growth_pct": 22.17,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 8.0,
          "signals": [
            "PCR 0.92 approaching bullish zone",
            "PCR rising +0.05",
            "Del 1.10x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 2.57,
          "price_sign": 1,
          "pcr_d1": 0.87,
          "pcr_d2": 0.92,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": -2.63,
          "oi_sign": -1,
          "avg_del": 1.105,
          "peak_del": 1.11,
          "del_chg": -0.01,
          "avg_vol": 1.075,
          "call_oi_growth_pct": 0.38,
          "put_oi_growth_pct": 6.24,
          "opt_oi_growth_pct": 3.11,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.76,
          "pcr": 1.0,
          "pcr_chg_1d": -0.04,
          "fut_oi": 61251750,
          "oi_chg_pct": 1.42,
          "delivery": 0.59,
          "volume": 0.71,
          "call_oi": 8032500,
          "put_oi": 8046150
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.84,
          "pcr": 0.87,
          "pcr_chg_1d": -0.05,
          "fut_oi": 60715200,
          "oi_chg_pct": 0.35,
          "delivery": 1.11,
          "volume": 1.28,
          "call_oi": 10494750,
          "put_oi": 9148650
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.57,
          "pcr": 0.92,
          "pcr_chg_1d": 0.05,
          "fut_oi": 59120250,
          "oi_chg_pct": -2.63,
          "delivery": 1.1,
          "volume": 0.87,
          "call_oi": 10534650,
          "put_oi": 9719850
        }
      ]
    },
    {
      "symbol": "SAMMAANCAP",
      "rank": 36,
      "days_available": 3,
      "latest_score": 8.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          7.0,
          8.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.065,
        "pcr_first": 0.9,
        "pcr_last": 1.03,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -10.12,
        "cumulative_price_chg_pct_window": 2.06,
        "persistence_score": 7.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 7.0,
          "signals": [
            "PCR 1.05 ABOVE 1.0 \u2014 put writers dominant"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.56,
          "price_sign": 1,
          "pcr_d1": 0.9,
          "pcr_d2": 1.05,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": -6.47,
          "oi_sign": -1,
          "avg_del": 0.775,
          "peak_del": 0.86,
          "del_chg": -0.17,
          "avg_vol": 0.685,
          "call_oi_growth_pct": 1.96,
          "put_oi_growth_pct": 17.83,
          "opt_oi_growth_pct": 9.5,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 8.0,
          "signals": [
            "PCR 1.03 ABOVE 1.0 \u2014 put writers dominant",
            "Del 1.02x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.49,
          "price_sign": 1,
          "pcr_d1": 1.05,
          "pcr_d2": 1.03,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": -3.91,
          "oi_sign": -1,
          "avg_del": 1.02,
          "peak_del": 1.35,
          "del_chg": 0.66,
          "avg_vol": 0.935,
          "call_oi_growth_pct": -4.82,
          "put_oi_growth_pct": -6.33,
          "opt_oi_growth_pct": -5.59,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -1.91,
          "pcr": 0.9,
          "pcr_chg_1d": -0.1,
          "fut_oi": 114242400,
          "oi_chg_pct": 2.15,
          "delivery": 0.86,
          "volume": 0.78,
          "call_oi": 19504800,
          "put_oi": 17651500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.56,
          "pcr": 1.05,
          "pcr_chg_1d": 0.02,
          "fut_oi": 106855000,
          "oi_chg_pct": -1.0,
          "delivery": 0.69,
          "volume": 0.59,
          "call_oi": 19887500,
          "put_oi": 20799100
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.49,
          "pcr": 1.03,
          "pcr_chg_1d": -0.02,
          "fut_oi": 102675400,
          "oi_chg_pct": -3.91,
          "delivery": 1.35,
          "volume": 1.28,
          "call_oi": 18928600,
          "put_oi": 19483300
        }
      ]
    },
    {
      "symbol": "LAURUSLABS",
      "rank": 37,
      "days_available": 3,
      "latest_score": 8.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -0.5,
          8.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.025,
        "pcr_first": 0.89,
        "pcr_last": 0.84,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -5.23,
        "cumulative_price_chg_pct_window": 1.47,
        "persistence_score": 5.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -0.5,
          "signals": [
            "PCR 0.78 neutral-to-bullish"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.12,
          "price_sign": 0,
          "pcr_d1": 0.89,
          "pcr_d2": 0.78,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -6.02,
          "oi_sign": -1,
          "avg_del": 0.615,
          "peak_del": 0.82,
          "del_chg": -0.41,
          "avg_vol": 0.725,
          "call_oi_growth_pct": 33.66,
          "put_oi_growth_pct": 17.35,
          "opt_oi_growth_pct": 25.97,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 8.0,
          "signals": [
            "PCR 0.84 neutral-to-bullish",
            "PCR rising +0.06"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.35,
          "price_sign": 1,
          "pcr_d1": 0.78,
          "pcr_d2": 0.84,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": 0.84,
          "oi_sign": 1,
          "avg_del": 0.8,
          "peak_del": 1.19,
          "del_chg": 0.78,
          "avg_vol": 0.725,
          "call_oi_growth_pct": 1.91,
          "put_oi_growth_pct": 9.89,
          "opt_oi_growth_pct": 5.41,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.64,
          "pcr": 0.89,
          "pcr_chg_1d": 0.11,
          "fut_oi": 18388050,
          "oi_chg_pct": -0.73,
          "delivery": 0.82,
          "volume": 0.98,
          "call_oi": 3669450,
          "put_oi": 3273350
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.12,
          "pcr": 0.78,
          "pcr_chg_1d": -0.01,
          "fut_oi": 17280500,
          "oi_chg_pct": -0.11,
          "delivery": 0.41,
          "volume": 0.47,
          "call_oi": 4904500,
          "put_oi": 3841150
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.35,
          "pcr": 0.84,
          "pcr_chg_1d": 0.06,
          "fut_oi": 17425850,
          "oi_chg_pct": 0.84,
          "delivery": 1.19,
          "volume": 0.98,
          "call_oi": 4998000,
          "put_oi": 4221100
        }
      ]
    },
    {
      "symbol": "AMBER",
      "rank": 38,
      "days_available": 3,
      "latest_score": 8.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -5.5,
          8.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.105,
        "pcr_first": 0.47,
        "pcr_last": 0.68,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 21.62,
        "cumulative_price_chg_pct_window": 4.34,
        "persistence_score": 3.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -5.5,
          "signals": [
            "PCR 0.64 neutral",
            "\u26a0 NEW SHORTS: FutOI +21.0% + Price -0.8%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.8,
          "price_sign": -1,
          "pcr_d1": 0.47,
          "pcr_d2": 0.64,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 20.96,
          "oi_sign": 1,
          "avg_del": 0.875,
          "peak_del": 1.18,
          "del_chg": 0.61,
          "avg_vol": 0.895,
          "call_oi_growth_pct": 109.36,
          "put_oi_growth_pct": 186.12,
          "opt_oi_growth_pct": 133.89,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 8.0,
          "signals": [
            "PCR 0.68 neutral",
            "PCR rising +0.04",
            "Del 1.21x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 5.18,
          "price_sign": 1,
          "pcr_d1": 0.64,
          "pcr_d2": 0.68,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": 0.54,
          "oi_sign": 1,
          "avg_del": 1.21,
          "peak_del": 1.24,
          "del_chg": 0.06,
          "avg_vol": 1.18,
          "call_oi_growth_pct": 15.8,
          "put_oi_growth_pct": 22.94,
          "opt_oi_growth_pct": 18.59,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.47,
          "pcr": 0.47,
          "pcr_chg_1d": -0.08,
          "fut_oi": 1002200,
          "oi_chg_pct": -1.79,
          "delivery": 0.57,
          "volume": 0.75,
          "call_oi": 242400,
          "put_oi": 113800
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.8,
          "pcr": 0.64,
          "pcr_chg_1d": 0.01,
          "fut_oi": 1212300,
          "oi_chg_pct": 7.65,
          "delivery": 1.18,
          "volume": 1.04,
          "call_oi": 507500,
          "put_oi": 325600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 5.18,
          "pcr": 0.68,
          "pcr_chg_1d": 0.04,
          "fut_oi": 1218900,
          "oi_chg_pct": 0.54,
          "delivery": 1.24,
          "volume": 1.32,
          "call_oi": 587700,
          "put_oi": 400300
        }
      ]
    },
    {
      "symbol": "UNITDSPR",
      "rank": 39,
      "days_available": 3,
      "latest_score": 8.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.5,
          8.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.1,
        "pcr_first": 0.84,
        "pcr_last": 0.64,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 6.18,
        "cumulative_price_chg_pct_window": 1.55,
        "persistence_score": 5.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 1.5,
          "signals": [
            "PCR 0.61 neutral",
            "PCR easing -0.04"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.07,
          "price_sign": 0,
          "pcr_d1": 0.84,
          "pcr_d2": 0.61,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 5.6,
          "oi_sign": 1,
          "avg_del": 1.93,
          "peak_del": 2.98,
          "del_chg": -2.1,
          "avg_vol": 1.505,
          "call_oi_growth_pct": 59.05,
          "put_oi_growth_pct": 14.4,
          "opt_oi_growth_pct": 38.61,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 8.0,
          "signals": [
            "PCR 0.64 neutral",
            "Del 1.40x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.48,
          "price_sign": 1,
          "pcr_d1": 0.61,
          "pcr_d2": 0.64,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 0.55,
          "oi_sign": 1,
          "avg_del": 1.395,
          "peak_del": 1.91,
          "del_chg": 1.03,
          "avg_vol": 1.305,
          "call_oi_growth_pct": 1.53,
          "put_oi_growth_pct": 7.46,
          "opt_oi_growth_pct": 3.77,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.5,
          "pcr": 0.84,
          "pcr_chg_1d": -0.08,
          "fut_oi": 12140000,
          "oi_chg_pct": 0.81,
          "delivery": 2.98,
          "volume": 2.2,
          "call_oi": 2280800,
          "put_oi": 1925600
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.07,
          "pcr": 0.61,
          "pcr_chg_1d": -0.04,
          "fut_oi": 12819600,
          "oi_chg_pct": 2.33,
          "delivery": 0.88,
          "volume": 0.81,
          "call_oi": 3627600,
          "put_oi": 2202800
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.48,
          "pcr": 0.64,
          "pcr_chg_1d": 0.03,
          "fut_oi": 12890000,
          "oi_chg_pct": 0.55,
          "delivery": 1.91,
          "volume": 1.8,
          "call_oi": 3683200,
          "put_oi": 2367200
        }
      ]
    },
    {
      "symbol": "LODHA",
      "rank": 40,
      "days_available": 3,
      "latest_score": 7.5,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          6.5,
          7.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.155,
        "pcr_first": 0.48,
        "pcr_last": 0.79,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.21,
        "cumulative_price_chg_pct_window": 6.12,
        "persistence_score": 7.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 6.5,
          "signals": [
            "PCR 0.75 neutral-to-bullish",
            "PCR rising +0.06",
            "\u2605 NEW LONGS: FutOI +6.1% + Price +1.4%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": 1.37,
          "price_sign": 1,
          "pcr_d1": 0.48,
          "pcr_d2": 0.75,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": 6.09,
          "oi_sign": 1,
          "avg_del": 0.495,
          "peak_del": 0.56,
          "del_chg": 0.13,
          "avg_vol": 0.555,
          "call_oi_growth_pct": 4.28,
          "put_oi_growth_pct": 63.04,
          "opt_oi_growth_pct": 23.38,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.5,
          "signals": [
            "PCR 0.79 neutral-to-bullish",
            "PCR rising +0.04"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 4.69,
          "price_sign": 1,
          "pcr_d1": 0.75,
          "pcr_d2": 0.79,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": -5.54,
          "oi_sign": -1,
          "avg_del": 0.97,
          "peak_del": 1.38,
          "del_chg": 0.82,
          "avg_vol": 1.175,
          "call_oi_growth_pct": 8.92,
          "put_oi_growth_pct": 14.16,
          "opt_oi_growth_pct": 11.17,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.23,
          "pcr": 0.48,
          "pcr_chg_1d": -0.16,
          "fut_oi": 22219200,
          "oi_chg_pct": 2.33,
          "delivery": 0.43,
          "volume": 0.52,
          "call_oi": 5641650,
          "put_oi": 2715300
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.37,
          "pcr": 0.75,
          "pcr_chg_1d": 0.06,
          "fut_oi": 23573250,
          "oi_chg_pct": -1.57,
          "delivery": 0.56,
          "volume": 0.59,
          "call_oi": 5883300,
          "put_oi": 4427100
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 4.69,
          "pcr": 0.79,
          "pcr_chg_1d": 0.04,
          "fut_oi": 22266450,
          "oi_chg_pct": -5.54,
          "delivery": 1.38,
          "volume": 1.76,
          "call_oi": 6408000,
          "put_oi": 5053950
        }
      ]
    },
    {
      "symbol": "BHEL",
      "rank": 41,
      "days_available": 3,
      "latest_score": 7.5,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          9.5,
          7.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.065,
        "pcr_first": 0.76,
        "pcr_last": 0.89,
        "days_delivery_institutional": 3,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -4.07,
        "cumulative_price_chg_pct_window": 7.16,
        "persistence_score": 8.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 9.5,
          "signals": [
            "PCR 0.81 neutral-to-bullish",
            "Del 1.77x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 4.33,
          "price_sign": 1,
          "pcr_d1": 0.76,
          "pcr_d2": 0.81,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -3.23,
          "oi_sign": -1,
          "avg_del": 1.765,
          "peak_del": 1.92,
          "del_chg": 0.31,
          "avg_vol": 1.945,
          "call_oi_growth_pct": 64.87,
          "put_oi_growth_pct": 75.68,
          "opt_oi_growth_pct": 69.54,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.5,
          "signals": [
            "PCR 0.89 approaching bullish zone",
            "PCR rising +0.08",
            "Del 1.51x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 2.71,
          "price_sign": 1,
          "pcr_d1": 0.81,
          "pcr_d2": 0.89,
          "pcr_chg": 0.08,
          "fut_oi_chg_pct": -0.86,
          "oi_sign": -1,
          "avg_del": 1.51,
          "peak_del": 1.92,
          "del_chg": -0.82,
          "avg_vol": 1.59,
          "call_oi_growth_pct": -3.85,
          "put_oi_growth_pct": 5.47,
          "opt_oi_growth_pct": 0.33,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.58,
          "pcr": 0.76,
          "pcr_chg_1d": 0.02,
          "fut_oi": 101653125,
          "oi_chg_pct": -8.57,
          "delivery": 1.61,
          "volume": 1.58,
          "call_oi": 19052250,
          "put_oi": 14518875
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 4.33,
          "pcr": 0.81,
          "pcr_chg_1d": 0.0,
          "fut_oi": 98366625,
          "oi_chg_pct": -0.36,
          "delivery": 1.92,
          "volume": 2.31,
          "call_oi": 31410750,
          "put_oi": 25507125
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.71,
          "pcr": 0.89,
          "pcr_chg_1d": 0.08,
          "fut_oi": 97516125,
          "oi_chg_pct": -0.86,
          "delivery": 1.1,
          "volume": 0.87,
          "call_oi": 30200625,
          "put_oi": 26903625
        }
      ]
    },
    {
      "symbol": "VOLTAS",
      "rank": 42,
      "days_available": 3,
      "latest_score": 7.5,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          11.0,
          7.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.055,
        "pcr_first": 0.51,
        "pcr_last": 0.62,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 5.21,
        "cumulative_price_chg_pct_window": 4.02,
        "persistence_score": 8.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 11.0,
          "signals": [
            "PCR 0.62 neutral",
            "PCR surging +0.09",
            "\u2605 NEW LONGS: FutOI +2.4% + Price +1.5%",
            "Del 1.81x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.51,
          "price_sign": 1,
          "pcr_d1": 0.51,
          "pcr_d2": 0.62,
          "pcr_chg": 0.09,
          "fut_oi_chg_pct": 2.37,
          "oi_sign": 1,
          "avg_del": 1.815,
          "peak_del": 2.26,
          "del_chg": -0.89,
          "avg_vol": 1.495,
          "call_oi_growth_pct": 28.52,
          "put_oi_growth_pct": 55.81,
          "opt_oi_growth_pct": 37.78,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.5,
          "signals": [
            "PCR 0.62 neutral",
            "\u2605 NEW LONGS: FutOI +2.8% + Price +2.5%",
            "Del 1.03x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 2.47,
          "price_sign": 1,
          "pcr_d1": 0.62,
          "pcr_d2": 0.62,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": 2.78,
          "oi_sign": 1,
          "avg_del": 1.03,
          "peak_del": 1.37,
          "del_chg": -0.68,
          "avg_vol": 0.995,
          "call_oi_growth_pct": 6.04,
          "put_oi_growth_pct": 6.2,
          "opt_oi_growth_pct": 6.1,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -1.81,
          "pcr": 0.51,
          "pcr_chg_1d": -0.15,
          "fut_oi": 12702375,
          "oi_chg_pct": 6.94,
          "delivery": 2.26,
          "volume": 1.86,
          "call_oi": 3681750,
          "put_oi": 1891500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.51,
          "pcr": 0.62,
          "pcr_chg_1d": 0.09,
          "fut_oi": 13003500,
          "oi_chg_pct": -0.64,
          "delivery": 1.37,
          "volume": 1.13,
          "call_oi": 4731750,
          "put_oi": 2947125
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.47,
          "pcr": 0.62,
          "pcr_chg_1d": 0.0,
          "fut_oi": 13364625,
          "oi_chg_pct": 2.78,
          "delivery": 0.69,
          "volume": 0.86,
          "call_oi": 5017500,
          "put_oi": 3129750
        }
      ]
    },
    {
      "symbol": "INDIANB",
      "rank": 43,
      "days_available": 3,
      "latest_score": 7.5,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -5.5,
          7.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.0,
        "pcr_first": 0.8,
        "pcr_last": 0.8,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -2.93,
        "cumulative_price_chg_pct_window": 1.18,
        "persistence_score": 3.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -5.5,
          "signals": [
            "PCR 0.75 neutral-to-bullish",
            "PCR easing -0.08"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.53,
          "price_sign": -1,
          "pcr_d1": 0.8,
          "pcr_d2": 0.75,
          "pcr_chg": -0.08,
          "fut_oi_chg_pct": 0.27,
          "oi_sign": 1,
          "avg_del": 0.915,
          "peak_del": 0.97,
          "del_chg": -0.11,
          "avg_vol": 0.96,
          "call_oi_growth_pct": 37.46,
          "put_oi_growth_pct": 29.01,
          "opt_oi_growth_pct": 33.7,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.5,
          "signals": [
            "PCR 0.80 neutral-to-bullish",
            "PCR rising +0.05",
            "Del 1.12x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 2.75,
          "price_sign": 1,
          "pcr_d1": 0.75,
          "pcr_d2": 0.8,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": -3.19,
          "oi_sign": -1,
          "avg_del": 1.125,
          "peak_del": 1.39,
          "del_chg": 0.53,
          "avg_vol": 1.015,
          "call_oi_growth_pct": -2.42,
          "put_oi_growth_pct": 3.84,
          "opt_oi_growth_pct": 0.27,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 5.0,
          "pcr": 0.8,
          "pcr_chg_1d": -0.01,
          "fut_oi": 9316000,
          "oi_chg_pct": 5.64,
          "delivery": 0.97,
          "volume": 0.93,
          "call_oi": 2317000,
          "put_oi": 1858000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.53,
          "pcr": 0.75,
          "pcr_chg_1d": -0.08,
          "fut_oi": 9341000,
          "oi_chg_pct": -2.76,
          "delivery": 0.86,
          "volume": 0.99,
          "call_oi": 3185000,
          "put_oi": 2397000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.75,
          "pcr": 0.8,
          "pcr_chg_1d": 0.05,
          "fut_oi": 9043000,
          "oi_chg_pct": -3.19,
          "delivery": 1.39,
          "volume": 1.04,
          "call_oi": 3108000,
          "put_oi": 2489000
        }
      ]
    },
    {
      "symbol": "ASHOKLEY",
      "rank": 44,
      "days_available": 3,
      "latest_score": 7.5,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -9.5,
          7.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.05,
        "pcr_first": 0.69,
        "pcr_last": 0.79,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -12.91,
        "cumulative_price_chg_pct_window": 3.21,
        "persistence_score": 1.83,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -9.5,
          "signals": [
            "PCR 0.69 neutral",
            "PCR easing -0.07",
            "Del 2.01x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -1.22,
          "price_sign": -1,
          "pcr_d1": 0.69,
          "pcr_d2": 0.69,
          "pcr_chg": -0.07,
          "fut_oi_chg_pct": -7.81,
          "oi_sign": -1,
          "avg_del": 2.01,
          "peak_del": 3.45,
          "del_chg": -2.88,
          "avg_vol": 2.09,
          "call_oi_growth_pct": 40.09,
          "put_oi_growth_pct": 40.0,
          "opt_oi_growth_pct": 40.05,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.5,
          "signals": [
            "PCR 0.79 neutral-to-bullish",
            "PCR surging +0.10"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 4.48,
          "price_sign": 1,
          "pcr_d1": 0.69,
          "pcr_d2": 0.79,
          "pcr_chg": 0.1,
          "fut_oi_chg_pct": -5.54,
          "oi_sign": -1,
          "avg_del": 0.83,
          "peak_del": 1.09,
          "del_chg": 0.52,
          "avg_vol": 0.78,
          "call_oi_growth_pct": -4.29,
          "put_oi_growth_pct": 9.53,
          "opt_oi_growth_pct": 1.37,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -3.26,
          "pcr": 0.69,
          "pcr_chg_1d": -0.03,
          "fut_oi": 161030000,
          "oi_chg_pct": 16.97,
          "delivery": 3.45,
          "volume": 3.54,
          "call_oi": 59880000,
          "put_oi": 41615000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.22,
          "pcr": 0.69,
          "pcr_chg_1d": -0.07,
          "fut_oi": 148460000,
          "oi_chg_pct": 1.6,
          "delivery": 0.57,
          "volume": 0.64,
          "call_oi": 83885000,
          "put_oi": 58260000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 4.48,
          "pcr": 0.79,
          "pcr_chg_1d": 0.1,
          "fut_oi": 140240000,
          "oi_chg_pct": -5.54,
          "delivery": 1.09,
          "volume": 0.92,
          "call_oi": 80285000,
          "put_oi": 63810000
        }
      ]
    },
    {
      "symbol": "RECLTD",
      "rank": 45,
      "days_available": 3,
      "latest_score": 7.5,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          3.5,
          7.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.135,
        "pcr_first": 1.18,
        "pcr_last": 0.91,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -2.17,
        "cumulative_price_chg_pct_window": 2.09,
        "persistence_score": 6.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 3.5,
          "signals": [
            "PCR 0.89 approaching bullish zone"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.21,
          "price_sign": 1,
          "pcr_d1": 1.18,
          "pcr_d2": 0.89,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -2.52,
          "oi_sign": -1,
          "avg_del": 0.75,
          "peak_del": 0.93,
          "del_chg": -0.36,
          "avg_vol": 0.85,
          "call_oi_growth_pct": 43.12,
          "put_oi_growth_pct": 8.07,
          "opt_oi_growth_pct": 24.16,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.5,
          "signals": [
            "PCR 0.91 approaching bullish zone"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.87,
          "price_sign": 1,
          "pcr_d1": 0.89,
          "pcr_d2": 0.91,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": 0.36,
          "oi_sign": 1,
          "avg_del": 0.74,
          "peak_del": 0.91,
          "del_chg": 0.34,
          "avg_vol": 0.85,
          "call_oi_growth_pct": 2.83,
          "put_oi_growth_pct": 5.35,
          "opt_oi_growth_pct": 4.02,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 5.57,
          "pcr": 1.18,
          "pcr_chg_1d": -0.01,
          "fut_oi": 71659000,
          "oi_chg_pct": -8.36,
          "delivery": 0.93,
          "volume": 0.9,
          "call_oi": 14581000,
          "put_oi": 17176600
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.21,
          "pcr": 0.89,
          "pcr_chg_1d": -0.01,
          "fut_oi": 69851600,
          "oi_chg_pct": 0.38,
          "delivery": 0.57,
          "volume": 0.8,
          "call_oi": 20868400,
          "put_oi": 18562600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.87,
          "pcr": 0.91,
          "pcr_chg_1d": 0.02,
          "fut_oi": 70106400,
          "oi_chg_pct": 0.36,
          "delivery": 0.91,
          "volume": 0.9,
          "call_oi": 21459200,
          "put_oi": 19555200
        }
      ]
    },
    {
      "symbol": "MFSL",
      "rank": 46,
      "days_available": 3,
      "latest_score": 7.5,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          6.0,
          7.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.005,
        "pcr_first": 0.83,
        "pcr_last": 0.84,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -5.2,
        "cumulative_price_chg_pct_window": 4.29,
        "persistence_score": 7.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 6.0,
          "signals": [
            "PCR 0.78 neutral-to-bullish",
            "PCR surging +0.10",
            "Del 1.08x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 1.3,
          "price_sign": 1,
          "pcr_d1": 0.83,
          "pcr_d2": 0.78,
          "pcr_chg": 0.1,
          "fut_oi_chg_pct": -3.52,
          "oi_sign": -1,
          "avg_del": 1.08,
          "peak_del": 1.25,
          "del_chg": -0.34,
          "avg_vol": 1.14,
          "call_oi_growth_pct": 40.93,
          "put_oi_growth_pct": 31.12,
          "opt_oi_growth_pct": 36.47,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.5,
          "signals": [
            "PCR 0.84 neutral-to-bullish",
            "PCR rising +0.06",
            "Del 1.10x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 2.95,
          "price_sign": 1,
          "pcr_d1": 0.78,
          "pcr_d2": 0.84,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": -1.75,
          "oi_sign": -1,
          "avg_del": 1.1,
          "peak_del": 1.29,
          "del_chg": 0.38,
          "avg_vol": 1.015,
          "call_oi_growth_pct": 35.06,
          "put_oi_growth_pct": 45.67,
          "opt_oi_growth_pct": 39.69,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.89,
          "pcr": 0.83,
          "pcr_chg_1d": -0.34,
          "fut_oi": 10808000,
          "oi_chg_pct": 2.42,
          "delivery": 1.25,
          "volume": 1.33,
          "call_oi": 405600,
          "put_oi": 338000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.3,
          "pcr": 0.78,
          "pcr_chg_1d": 0.1,
          "fut_oi": 10428000,
          "oi_chg_pct": -2.66,
          "delivery": 0.91,
          "volume": 0.95,
          "call_oi": 571600,
          "put_oi": 443200
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.95,
          "pcr": 0.84,
          "pcr_chg_1d": 0.06,
          "fut_oi": 10246000,
          "oi_chg_pct": -1.75,
          "delivery": 1.29,
          "volume": 1.08,
          "call_oi": 772000,
          "put_oi": 645600
        }
      ]
    },
    {
      "symbol": "TATAPOWER",
      "rank": 47,
      "days_available": 3,
      "latest_score": 7.5,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.5,
          7.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.045,
        "pcr_first": 0.79,
        "pcr_last": 0.7,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 3.25,
        "cumulative_price_chg_pct_window": 1.12,
        "persistence_score": 4.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -2.5,
          "signals": [
            "PCR 0.70 neutral"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.06,
          "price_sign": 0,
          "pcr_d1": 0.79,
          "pcr_d2": 0.7,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 2.49,
          "oi_sign": 1,
          "avg_del": 1.12,
          "peak_del": 1.75,
          "del_chg": 1.26,
          "avg_vol": 0.925,
          "call_oi_growth_pct": 29.66,
          "put_oi_growth_pct": 14.4,
          "opt_oi_growth_pct": 22.92,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.5,
          "signals": [
            "PCR 0.70 neutral",
            "Del 1.28x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.18,
          "price_sign": 1,
          "pcr_d1": 0.7,
          "pcr_d2": 0.7,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": 0.74,
          "oi_sign": 1,
          "avg_del": 1.285,
          "peak_del": 1.75,
          "del_chg": -0.93,
          "avg_vol": 1.05,
          "call_oi_growth_pct": 6.21,
          "put_oi_growth_pct": 6.9,
          "opt_oi_growth_pct": 6.5,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.38,
          "pcr": 0.79,
          "pcr_chg_1d": -0.03,
          "fut_oi": 54625850,
          "oi_chg_pct": -0.09,
          "delivery": 0.49,
          "volume": 0.59,
          "call_oi": 23143450,
          "put_oi": 18287400
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.06,
          "pcr": 0.7,
          "pcr_chg_1d": 0.01,
          "fut_oi": 55985950,
          "oi_chg_pct": 3.94,
          "delivery": 1.75,
          "volume": 1.26,
          "call_oi": 30007750,
          "put_oi": 20920600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.18,
          "pcr": 0.7,
          "pcr_chg_1d": 0.0,
          "fut_oi": 56402100,
          "oi_chg_pct": 0.74,
          "delivery": 0.82,
          "volume": 0.84,
          "call_oi": 31872450,
          "put_oi": 22364800
        }
      ]
    },
    {
      "symbol": "MAXHEALTH",
      "rank": 48,
      "days_available": 3,
      "latest_score": -7.0,
      "latest_tier": "TIER 2 \u2014 DISTRIBUTION",
      "latest_sign": "bearish",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild short build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (short)",
        "direction": "short",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          5.5,
          -7.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.12,
        "pcr_first": 0.77,
        "pcr_last": 0.53,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 14.87,
        "cumulative_price_chg_pct_window": 1.3,
        "persistence_score": -2.83,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": 5.5,
          "signals": [
            "PCR 0.65 neutral",
            "PCR rising +0.05",
            "\u2605 NEW LONGS: FutOI +9.7% + Price +1.5%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.47,
          "price_sign": 1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.65,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": 9.72,
          "oi_sign": 1,
          "avg_del": 0.89,
          "peak_del": 1.04,
          "del_chg": 0.3,
          "avg_vol": 0.92,
          "call_oi_growth_pct": 113.16,
          "put_oi_growth_pct": 80.52,
          "opt_oi_growth_pct": 98.97,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -7.0,
          "signals": [
            "PCR 0.53 call writers dominant",
            "PCR collapsing -0.12"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.17,
          "price_sign": 0,
          "pcr_d1": 0.65,
          "pcr_d2": 0.53,
          "pcr_chg": -0.12,
          "fut_oi_chg_pct": 4.7,
          "oi_sign": 1,
          "avg_del": 1.115,
          "peak_del": 1.19,
          "del_chg": 0.15,
          "avg_vol": 1.095,
          "call_oi_growth_pct": 56.89,
          "put_oi_growth_pct": 27.81,
          "opt_oi_growth_pct": 45.42,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.35,
          "pcr": 0.77,
          "pcr_chg_1d": 0.06,
          "fut_oi": 13169625,
          "oi_chg_pct": 2.07,
          "delivery": 0.74,
          "volume": 0.78,
          "call_oi": 1184925,
          "put_oi": 910875
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.47,
          "pcr": 0.65,
          "pcr_chg_1d": 0.05,
          "fut_oi": 14449575,
          "oi_chg_pct": -0.4,
          "delivery": 1.04,
          "volume": 1.06,
          "call_oi": 2525775,
          "put_oi": 1644300
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.17,
          "pcr": 0.53,
          "pcr_chg_1d": -0.12,
          "fut_oi": 15128400,
          "oi_chg_pct": 4.7,
          "delivery": 1.19,
          "volume": 1.13,
          "call_oi": 3962700,
          "put_oi": 2101575
        }
      ]
    },
    {
      "symbol": "TVSMOTOR",
      "rank": 49,
      "days_available": 3,
      "latest_score": 7.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          3.5,
          7.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.015,
        "pcr_first": 0.81,
        "pcr_last": 0.78,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.27,
        "cumulative_price_chg_pct_window": 3.74,
        "persistence_score": 5.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 3.5,
          "signals": [
            "PCR 0.77 neutral-to-bullish"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.69,
          "price_sign": 1,
          "pcr_d1": 0.81,
          "pcr_d2": 0.77,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": 1.72,
          "oi_sign": 1,
          "avg_del": 0.91,
          "peak_del": 1.19,
          "del_chg": -0.56,
          "avg_vol": 0.95,
          "call_oi_growth_pct": 39.63,
          "put_oi_growth_pct": 32.29,
          "opt_oi_growth_pct": 36.35,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.0,
          "signals": [
            "PCR 0.78 neutral-to-bullish",
            "Del 1.21x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 3.03,
          "price_sign": 1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.78,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": -1.42,
          "oi_sign": -1,
          "avg_del": 1.21,
          "peak_del": 1.79,
          "del_chg": 1.16,
          "avg_vol": 1.07,
          "call_oi_growth_pct": 10.28,
          "put_oi_growth_pct": 11.84,
          "opt_oi_growth_pct": 10.96,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.84,
          "pcr": 0.81,
          "pcr_chg_1d": -0.03,
          "fut_oi": 8343650,
          "oi_chg_pct": 2.85,
          "delivery": 1.19,
          "volume": 1.14,
          "call_oi": 853125,
          "put_oi": 690550
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.69,
          "pcr": 0.77,
          "pcr_chg_1d": 0.0,
          "fut_oi": 8487500,
          "oi_chg_pct": 0.64,
          "delivery": 0.63,
          "volume": 0.76,
          "call_oi": 1191225,
          "put_oi": 913500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.03,
          "pcr": 0.78,
          "pcr_chg_1d": 0.01,
          "fut_oi": 8366575,
          "oi_chg_pct": -1.42,
          "delivery": 1.79,
          "volume": 1.38,
          "call_oi": 1313725,
          "put_oi": 1021650
        }
      ]
    },
    {
      "symbol": "JINDALSTEL",
      "rank": 50,
      "days_available": 3,
      "latest_score": 7.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.5,
          7.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.02,
        "pcr_first": 1.07,
        "pcr_last": 1.03,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 25.35,
        "cumulative_price_chg_pct_window": 0.5,
        "persistence_score": 3.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -2.5,
          "signals": [
            "PCR 1.05 ABOVE 1.0 \u2014 put writers dominant",
            "PCR rising +0.05",
            "\u26a0 NEW SHORTS: FutOI +23.3% + Price -1.1%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.11,
          "price_sign": -1,
          "pcr_d1": 1.07,
          "pcr_d2": 1.05,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": 23.29,
          "oi_sign": 1,
          "avg_del": 0.99,
          "peak_del": 1.2,
          "del_chg": -0.42,
          "avg_vol": 0.9,
          "call_oi_growth_pct": 55.92,
          "put_oi_growth_pct": 52.78,
          "opt_oi_growth_pct": 54.29,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.0,
          "signals": [
            "PCR 1.03 ABOVE 1.0 \u2014 put writers dominant"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.63,
          "price_sign": 1,
          "pcr_d1": 1.05,
          "pcr_d2": 1.03,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 1.67,
          "oi_sign": 1,
          "avg_del": 0.785,
          "peak_del": 0.79,
          "del_chg": 0.01,
          "avg_vol": 0.77,
          "call_oi_growth_pct": 3.29,
          "put_oi_growth_pct": 1.0,
          "opt_oi_growth_pct": 2.12,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.18,
          "pcr": 1.07,
          "pcr_chg_1d": -0.19,
          "fut_oi": 10130000,
          "oi_chg_pct": 1.94,
          "delivery": 1.2,
          "volume": 0.98,
          "call_oi": 1716875,
          "put_oi": 1842500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.11,
          "pcr": 1.05,
          "pcr_chg_1d": 0.05,
          "fut_oi": 12489375,
          "oi_chg_pct": 1.11,
          "delivery": 0.78,
          "volume": 0.82,
          "call_oi": 2676875,
          "put_oi": 2815000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.63,
          "pcr": 1.03,
          "pcr_chg_1d": -0.02,
          "fut_oi": 12697500,
          "oi_chg_pct": 1.67,
          "delivery": 0.79,
          "volume": 0.72,
          "call_oi": 2765000,
          "put_oi": 2843125
        }
      ]
    },
    {
      "symbol": "SIEMENS",
      "rank": 51,
      "days_available": 3,
      "latest_score": 7.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          0.0,
          7.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.04,
        "pcr_first": 0.53,
        "pcr_last": 0.61,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 5.04,
        "cumulative_price_chg_pct_window": 5.03,
        "persistence_score": 4.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 0.0,
          "signals": [
            "PCR 0.69 neutral"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.11,
          "price_sign": 0,
          "pcr_d1": 0.53,
          "pcr_d2": 0.69,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 0.66,
          "oi_sign": 1,
          "avg_del": 0.77,
          "peak_del": 1.02,
          "del_chg": 0.5,
          "avg_vol": 0.75,
          "call_oi_growth_pct": 46.02,
          "put_oi_growth_pct": 89.04,
          "opt_oi_growth_pct": 61.0,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.0,
          "signals": [
            "PCR 0.61 neutral",
            "PCR easing -0.08",
            "\u2605 NEW LONGS: FutOI +4.4% + Price +5.2%",
            "Del 1.53x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 5.15,
          "price_sign": 1,
          "pcr_d1": 0.69,
          "pcr_d2": 0.61,
          "pcr_chg": -0.08,
          "fut_oi_chg_pct": 4.35,
          "oi_sign": 1,
          "avg_del": 1.53,
          "peak_del": 2.04,
          "del_chg": 1.02,
          "avg_vol": 1.505,
          "call_oi_growth_pct": 73.26,
          "put_oi_growth_pct": 54.06,
          "opt_oi_growth_pct": 65.41,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.79,
          "pcr": 0.53,
          "pcr_chg_1d": -0.02,
          "fut_oi": 2583700,
          "oi_chg_pct": -0.45,
          "delivery": 0.52,
          "volume": 0.57,
          "call_oi": 373800,
          "put_oi": 199675
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.11,
          "pcr": 0.69,
          "pcr_chg_1d": 0.03,
          "fut_oi": 2600675,
          "oi_chg_pct": -0.08,
          "delivery": 1.02,
          "volume": 0.93,
          "call_oi": 545825,
          "put_oi": 377475
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 5.15,
          "pcr": 0.61,
          "pcr_chg_1d": -0.08,
          "fut_oi": 2713900,
          "oi_chg_pct": 4.35,
          "delivery": 2.04,
          "volume": 2.08,
          "call_oi": 945700,
          "put_oi": 581525
        }
      ]
    },
    {
      "symbol": "SUZLON",
      "rank": 52,
      "days_available": 3,
      "latest_score": 7.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -3.0,
          7.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.035,
        "pcr_first": 0.61,
        "pcr_last": 0.54,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 8.79,
        "cumulative_price_chg_pct_window": 2.46,
        "persistence_score": 3.67,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -3.0,
          "signals": [
            "PCR 0.46 call writers dominant"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.0,
          "price_sign": 0,
          "pcr_d1": 0.61,
          "pcr_d2": 0.46,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": 6.01,
          "oi_sign": 1,
          "avg_del": 0.915,
          "peak_del": 1.21,
          "del_chg": 0.59,
          "avg_vol": 0.965,
          "call_oi_growth_pct": 75.87,
          "put_oi_growth_pct": 31.17,
          "opt_oi_growth_pct": 58.87,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.0,
          "signals": [
            "PCR 0.54 call writers dominant",
            "PCR rising +0.08",
            "\u2605 NEW LONGS: FutOI +2.6% + Price +2.5%",
            "Del 1.14x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 2.46,
          "price_sign": 1,
          "pcr_d1": 0.46,
          "pcr_d2": 0.54,
          "pcr_chg": 0.08,
          "fut_oi_chg_pct": 2.62,
          "oi_sign": 1,
          "avg_del": 1.14,
          "peak_del": 1.21,
          "del_chg": -0.14,
          "avg_vol": 1.09,
          "call_oi_growth_pct": 6.0,
          "put_oi_growth_pct": 24.84,
          "opt_oi_growth_pct": 11.91,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.94,
          "pcr": 0.61,
          "pcr_chg_1d": -0.01,
          "fut_oi": 282085400,
          "oi_chg_pct": -0.62,
          "delivery": 0.62,
          "volume": 0.71,
          "call_oi": 67696525,
          "put_oi": 41524025
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.0,
          "pcr": 0.46,
          "pcr_chg_1d": -0.01,
          "fut_oi": 299034350,
          "oi_chg_pct": 1.59,
          "delivery": 1.21,
          "volume": 1.22,
          "call_oi": 119057800,
          "put_oi": 54465875
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.46,
          "pcr": 0.54,
          "pcr_chg_1d": 0.08,
          "fut_oi": 306868050,
          "oi_chg_pct": 2.62,
          "delivery": 1.07,
          "volume": 0.96,
          "call_oi": 126196575,
          "put_oi": 67994350
        }
      ]
    },
    {
      "symbol": "EICHERMOT",
      "rank": 53,
      "days_available": 3,
      "latest_score": 7.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          5.5,
          7.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.02,
        "pcr_first": 0.92,
        "pcr_last": 0.96,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 16.47,
        "cumulative_price_chg_pct_window": 4.11,
        "persistence_score": 6.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 5.5,
          "signals": [
            "PCR 0.88 approaching bullish zone",
            "PCR surging +0.10"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.23,
          "price_sign": 0,
          "pcr_d1": 0.92,
          "pcr_d2": 0.88,
          "pcr_chg": 0.1,
          "fut_oi_chg_pct": 16.4,
          "oi_sign": 1,
          "avg_del": 1.075,
          "peak_del": 1.49,
          "del_chg": -0.83,
          "avg_vol": 0.95,
          "call_oi_growth_pct": 99.6,
          "put_oi_growth_pct": 91.0,
          "opt_oi_growth_pct": 95.48,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.0,
          "signals": [
            "PCR 0.96 approaching bullish zone",
            "PCR rising +0.08"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": 3.87,
          "price_sign": 1,
          "pcr_d1": 0.88,
          "pcr_d2": 0.96,
          "pcr_chg": 0.08,
          "fut_oi_chg_pct": 0.06,
          "oi_sign": 1,
          "avg_del": 0.635,
          "peak_del": 0.66,
          "del_chg": -0.05,
          "avg_vol": 0.77,
          "call_oi_growth_pct": 6.27,
          "put_oi_growth_pct": 15.42,
          "opt_oi_growth_pct": 10.55,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.64,
          "pcr": 0.92,
          "pcr_chg_1d": -0.01,
          "fut_oi": 3586700,
          "oi_chg_pct": 1.45,
          "delivery": 1.49,
          "volume": 1.17,
          "call_oi": 702300,
          "put_oi": 645700
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.23,
          "pcr": 0.88,
          "pcr_chg_1d": 0.1,
          "fut_oi": 4174800,
          "oi_chg_pct": -1.97,
          "delivery": 0.66,
          "volume": 0.73,
          "call_oi": 1401800,
          "put_oi": 1233300
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.87,
          "pcr": 0.96,
          "pcr_chg_1d": 0.08,
          "fut_oi": 4177300,
          "oi_chg_pct": 0.06,
          "delivery": 0.61,
          "volume": 0.81,
          "call_oi": 1489700,
          "put_oi": 1423500
        }
      ]
    },
    {
      "symbol": "KALYANKJIL",
      "rank": 54,
      "days_available": 3,
      "latest_score": 7.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.0,
          7.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.08,
        "pcr_first": 0.77,
        "pcr_last": 0.93,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -0.04,
        "cumulative_price_chg_pct_window": 0.8,
        "persistence_score": 6.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 4.0,
          "signals": [
            "PCR 0.92 approaching bullish zone"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.12,
          "price_sign": 0,
          "pcr_d1": 0.77,
          "pcr_d2": 0.92,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": -0.13,
          "oi_sign": -1,
          "avg_del": 0.905,
          "peak_del": 1.0,
          "del_chg": 0.19,
          "avg_vol": 0.71,
          "call_oi_growth_pct": 89.07,
          "put_oi_growth_pct": 128.2,
          "opt_oi_growth_pct": 106.04,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.0,
          "signals": [
            "PCR 0.93 approaching bullish zone"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.68,
          "price_sign": 1,
          "pcr_d1": 0.92,
          "pcr_d2": 0.93,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 0.09,
          "oi_sign": 1,
          "avg_del": 0.885,
          "peak_del": 1.0,
          "del_chg": -0.23,
          "avg_vol": 0.6,
          "call_oi_growth_pct": 7.62,
          "put_oi_growth_pct": 7.78,
          "opt_oi_growth_pct": 7.7,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.98,
          "pcr": 0.77,
          "pcr_chg_1d": 0.05,
          "fut_oi": 24250825,
          "oi_chg_pct": 0.88,
          "delivery": 0.81,
          "volume": 0.71,
          "call_oi": 3042075,
          "put_oi": 2328850
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.12,
          "pcr": 0.92,
          "pcr_chg_1d": -0.02,
          "fut_oi": 24219100,
          "oi_chg_pct": 1.25,
          "delivery": 1.0,
          "volume": 0.71,
          "call_oi": 5751625,
          "put_oi": 5314525
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.68,
          "pcr": 0.93,
          "pcr_chg_1d": 0.01,
          "fut_oi": 24241425,
          "oi_chg_pct": 0.09,
          "delivery": 0.77,
          "volume": 0.49,
          "call_oi": 6189900,
          "put_oi": 5728125
        }
      ]
    },
    {
      "symbol": "TRENT",
      "rank": 55,
      "days_available": 3,
      "latest_score": 7.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.0,
          7.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.035,
        "pcr_first": 0.9,
        "pcr_last": 0.97,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 21.17,
        "cumulative_price_chg_pct_window": 0.3,
        "persistence_score": 3.33,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -4.0,
          "signals": [
            "PCR 0.89 approaching bullish zone",
            "\u26a0 NEW SHORTS: FutOI +19.9% + Price -1.4%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -1.39,
          "price_sign": -1,
          "pcr_d1": 0.9,
          "pcr_d2": 0.89,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 19.92,
          "oi_sign": 1,
          "avg_del": 0.695,
          "peak_del": 1.06,
          "del_chg": -0.73,
          "avg_vol": 0.84,
          "call_oi_growth_pct": 58.09,
          "put_oi_growth_pct": 57.67,
          "opt_oi_growth_pct": 57.89,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.0,
          "signals": [
            "PCR 0.97 approaching bullish zone",
            "PCR rising +0.08"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": 1.71,
          "price_sign": 1,
          "pcr_d1": 0.89,
          "pcr_d2": 0.97,
          "pcr_chg": 0.08,
          "fut_oi_chg_pct": 1.04,
          "oi_sign": 1,
          "avg_del": 0.54,
          "peak_del": 0.75,
          "del_chg": 0.42,
          "avg_vol": 0.46,
          "call_oi_growth_pct": -3.95,
          "put_oi_growth_pct": 3.81,
          "opt_oi_growth_pct": -0.29,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 7.0,
          "pcr": 0.9,
          "pcr_chg_1d": 0.01,
          "fut_oi": 6533700,
          "oi_chg_pct": -1.28,
          "delivery": 1.06,
          "volume": 1.34,
          "call_oi": 1516500,
          "put_oi": 1358200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.39,
          "pcr": 0.89,
          "pcr_chg_1d": 0.01,
          "fut_oi": 7835400,
          "oi_chg_pct": 2.73,
          "delivery": 0.33,
          "volume": 0.34,
          "call_oi": 2397400,
          "put_oi": 2141500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.71,
          "pcr": 0.97,
          "pcr_chg_1d": 0.08,
          "fut_oi": 7916600,
          "oi_chg_pct": 1.04,
          "delivery": 0.75,
          "volume": 0.58,
          "call_oi": 2302800,
          "put_oi": 2223000
        }
      ]
    },
    {
      "symbol": "HINDPETRO",
      "rank": 56,
      "days_available": 3,
      "latest_score": 7.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -6.5,
          7.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.035,
        "pcr_first": 0.96,
        "pcr_last": 0.89,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -9.9,
        "cumulative_price_chg_pct_window": -1.0,
        "persistence_score": 2.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -6.5,
          "signals": [
            "PCR 0.89 approaching bullish zone",
            "Del 1.15x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -1.72,
          "price_sign": -1,
          "pcr_d1": 0.96,
          "pcr_d2": 0.89,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -6.46,
          "oi_sign": -1,
          "avg_del": 1.145,
          "peak_del": 1.51,
          "del_chg": 0.73,
          "avg_vol": 0.965,
          "call_oi_growth_pct": 50.68,
          "put_oi_growth_pct": 38.47,
          "opt_oi_growth_pct": 44.69,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.0,
          "signals": [
            "PCR 0.89 approaching bullish zone",
            "Del 1.06x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.73,
          "price_sign": 1,
          "pcr_d1": 0.89,
          "pcr_d2": 0.89,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -3.68,
          "oi_sign": -1,
          "avg_del": 1.065,
          "peak_del": 1.51,
          "del_chg": -0.89,
          "avg_vol": 0.82,
          "call_oi_growth_pct": 2.24,
          "put_oi_growth_pct": 2.98,
          "opt_oi_growth_pct": 2.59,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.04,
          "pcr": 0.96,
          "pcr_chg_1d": -0.14,
          "fut_oi": 47012400,
          "oi_chg_pct": -5.06,
          "delivery": 0.78,
          "volume": 0.8,
          "call_oi": 11702475,
          "put_oi": 11281275
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.72,
          "pcr": 0.89,
          "pcr_chg_1d": -0.01,
          "fut_oi": 43976925,
          "oi_chg_pct": 0.04,
          "delivery": 1.51,
          "volume": 1.13,
          "call_oi": 17633700,
          "put_oi": 15620850
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.73,
          "pcr": 0.89,
          "pcr_chg_1d": 0.0,
          "fut_oi": 42356925,
          "oi_chg_pct": -3.68,
          "delivery": 0.62,
          "volume": 0.51,
          "call_oi": 18028575,
          "put_oi": 16086600
        }
      ]
    },
    {
      "symbol": "ADANIENT",
      "rank": 57,
      "days_available": 3,
      "latest_score": 7.0,
      "latest_tier": "TIER 2 \u2014 ACCUMULATION",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -1.0,
          7.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.06,
        "pcr_first": 1.02,
        "pcr_last": 0.9,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 1.29,
        "cumulative_price_chg_pct_window": 2.11,
        "persistence_score": 4.33,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -1.0,
          "signals": [
            "PCR 0.88 approaching bullish zone"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.16,
          "price_sign": 0,
          "pcr_d1": 1.02,
          "pcr_d2": 0.88,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 1.12,
          "oi_sign": 1,
          "avg_del": 0.845,
          "peak_del": 1.34,
          "del_chg": 0.99,
          "avg_vol": 0.745,
          "call_oi_growth_pct": 47.2,
          "put_oi_growth_pct": 27.53,
          "opt_oi_growth_pct": 37.29,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 7.0,
          "signals": [
            "PCR 0.90 approaching bullish zone",
            "Del 1.03x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 2.27,
          "price_sign": 1,
          "pcr_d1": 0.88,
          "pcr_d2": 0.9,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": 0.17,
          "oi_sign": 1,
          "avg_del": 1.03,
          "peak_del": 1.34,
          "del_chg": -0.62,
          "avg_vol": 0.795,
          "call_oi_growth_pct": -0.17,
          "put_oi_growth_pct": 2.57,
          "opt_oi_growth_pct": 1.11,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.76,
          "pcr": 1.02,
          "pcr_chg_1d": -0.01,
          "fut_oi": 16370820,
          "oi_chg_pct": -10.73,
          "delivery": 0.35,
          "volume": 0.54,
          "call_oi": 4217232,
          "put_oi": 4284903
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.16,
          "pcr": 0.88,
          "pcr_chg_1d": 0.03,
          "fut_oi": 16554366,
          "oi_chg_pct": -2.08,
          "delivery": 1.34,
          "volume": 0.95,
          "call_oi": 6207810,
          "put_oi": 5464665
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.27,
          "pcr": 0.9,
          "pcr_chg_1d": 0.02,
          "fut_oi": 16582176,
          "oi_chg_pct": 0.17,
          "delivery": 0.72,
          "volume": 0.64,
          "call_oi": 6196995,
          "put_oi": 5605260
        }
      ]
    },
    {
      "symbol": "WIPRO",
      "rank": 58,
      "days_available": 3,
      "latest_score": 6.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.0,
          6.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.115,
        "pcr_first": 0.8,
        "pcr_last": 0.57,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 15.24,
        "cumulative_price_chg_pct_window": 0.72,
        "persistence_score": 3.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -2.0,
          "signals": [
            "PCR 0.73 neutral",
            "PCR rising +0.04"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.27,
          "price_sign": 0,
          "pcr_d1": 0.8,
          "pcr_d2": 0.73,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": 8.26,
          "oi_sign": 1,
          "avg_del": 0.705,
          "peak_del": 0.98,
          "del_chg": 0.55,
          "avg_vol": 0.69,
          "call_oi_growth_pct": 53.85,
          "put_oi_growth_pct": 40.96,
          "opt_oi_growth_pct": 48.13,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.5,
          "signals": [
            "PCR 0.57 neutral",
            "PCR collapsing -0.16",
            "\u2605 NEW LONGS: FutOI +6.4% + Price +1.0%",
            "Del 1.72x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 0.99,
          "price_sign": 1,
          "pcr_d1": 0.73,
          "pcr_d2": 0.57,
          "pcr_chg": -0.16,
          "fut_oi_chg_pct": 6.45,
          "oi_sign": 1,
          "avg_del": 1.715,
          "peak_del": 2.45,
          "del_chg": 1.47,
          "avg_vol": 1.635,
          "call_oi_growth_pct": 48.97,
          "put_oi_growth_pct": 17.07,
          "opt_oi_growth_pct": 35.5,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.89,
          "pcr": 0.8,
          "pcr_chg_1d": -0.02,
          "fut_oi": 207312000,
          "oi_chg_pct": -0.76,
          "delivery": 0.43,
          "volume": 0.64,
          "call_oi": 34506000,
          "put_oi": 27546000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.27,
          "pcr": 0.73,
          "pcr_chg_1d": 0.04,
          "fut_oi": 224436000,
          "oi_chg_pct": 1.24,
          "delivery": 0.98,
          "volume": 0.74,
          "call_oi": 53088000,
          "put_oi": 38829000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.99,
          "pcr": 0.57,
          "pcr_chg_1d": -0.16,
          "fut_oi": 238902000,
          "oi_chg_pct": 6.45,
          "delivery": 2.45,
          "volume": 2.53,
          "call_oi": 79086000,
          "put_oi": 45459000
        }
      ]
    },
    {
      "symbol": "ULTRACEMCO",
      "rank": 59,
      "days_available": 3,
      "latest_score": 6.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -3.5,
          6.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.065,
        "pcr_first": 0.65,
        "pcr_last": 0.78,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 1.35,
        "cumulative_price_chg_pct_window": -0.13,
        "persistence_score": 3.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -3.5,
          "signals": [
            "PCR 0.73 neutral",
            "PCR easing -0.06"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.34,
          "price_sign": -1,
          "pcr_d1": 0.65,
          "pcr_d2": 0.73,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": 1.95,
          "oi_sign": 1,
          "avg_del": 0.815,
          "peak_del": 0.88,
          "del_chg": -0.13,
          "avg_vol": 0.84,
          "call_oi_growth_pct": 43.65,
          "put_oi_growth_pct": 62.99,
          "opt_oi_growth_pct": 51.25,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.5,
          "signals": [
            "PCR 0.78 neutral-to-bullish",
            "PCR rising +0.05",
            "Del 1.02x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.23,
          "price_sign": 1,
          "pcr_d1": 0.73,
          "pcr_d2": 0.78,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": -0.59,
          "oi_sign": -1,
          "avg_del": 1.025,
          "peak_del": 1.3,
          "del_chg": 0.55,
          "avg_vol": 0.96,
          "call_oi_growth_pct": 0.64,
          "put_oi_growth_pct": 6.31,
          "opt_oi_growth_pct": 3.04,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.29,
          "pcr": 0.65,
          "pcr_chg_1d": 0.03,
          "fut_oi": 2428800,
          "oi_chg_pct": 5.23,
          "delivery": 0.88,
          "volume": 0.86,
          "call_oi": 314200,
          "put_oi": 203350
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.34,
          "pcr": 0.73,
          "pcr_chg_1d": -0.06,
          "fut_oi": 2476150,
          "oi_chg_pct": 1.83,
          "delivery": 0.75,
          "volume": 0.82,
          "call_oi": 451350,
          "put_oi": 331450
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.23,
          "pcr": 0.78,
          "pcr_chg_1d": 0.05,
          "fut_oi": 2461550,
          "oi_chg_pct": -0.59,
          "delivery": 1.3,
          "volume": 1.1,
          "call_oi": 454250,
          "put_oi": 352350
        }
      ]
    },
    {
      "symbol": "TMPV",
      "rank": 60,
      "days_available": 3,
      "latest_score": 6.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -1.5,
          6.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.08,
        "pcr_first": 0.73,
        "pcr_last": 0.89,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -5.09,
        "cumulative_price_chg_pct_window": 2.35,
        "persistence_score": 3.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -1.5,
          "signals": [
            "PCR 0.81 neutral-to-bullish",
            "PCR easing -0.08"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -0.45,
          "price_sign": -1,
          "pcr_d1": 0.73,
          "pcr_d2": 0.81,
          "pcr_chg": -0.08,
          "fut_oi_chg_pct": -3.24,
          "oi_sign": -1,
          "avg_del": 0.925,
          "peak_del": 1.12,
          "del_chg": 0.39,
          "avg_vol": 0.87,
          "call_oi_growth_pct": 25.93,
          "put_oi_growth_pct": 39.74,
          "opt_oi_growth_pct": 31.74,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.5,
          "signals": [
            "PCR 0.89 approaching bullish zone",
            "PCR rising +0.08",
            "Del 1.14x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 2.81,
          "price_sign": 1,
          "pcr_d1": 0.81,
          "pcr_d2": 0.89,
          "pcr_chg": 0.08,
          "fut_oi_chg_pct": -1.9,
          "oi_sign": -1,
          "avg_del": 1.135,
          "peak_del": 1.15,
          "del_chg": 0.03,
          "avg_vol": 0.99,
          "call_oi_growth_pct": -3.89,
          "put_oi_growth_pct": 5.6,
          "opt_oi_growth_pct": 0.34,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.28,
          "pcr": 0.73,
          "pcr_chg_1d": 0.0,
          "fut_oi": 61304800,
          "oi_chg_pct": 0.31,
          "delivery": 0.73,
          "volume": 0.71,
          "call_oi": 21826400,
          "put_oi": 15847200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.45,
          "pcr": 0.81,
          "pcr_chg_1d": -0.08,
          "fut_oi": 59316000,
          "oi_chg_pct": -0.5,
          "delivery": 1.12,
          "volume": 1.03,
          "call_oi": 27486400,
          "put_oi": 22145600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.81,
          "pcr": 0.89,
          "pcr_chg_1d": 0.08,
          "fut_oi": 58187200,
          "oi_chg_pct": -1.9,
          "delivery": 1.15,
          "volume": 0.95,
          "call_oi": 26416800,
          "put_oi": 23386400
        }
      ]
    },
    {
      "symbol": "NATIONALUM",
      "rank": 61,
      "days_available": 3,
      "latest_score": 6.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.0,
          6.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.035,
        "pcr_first": 0.91,
        "pcr_last": 0.84,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 6.08,
        "cumulative_price_chg_pct_window": 4.21,
        "persistence_score": 5.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 4.0,
          "signals": [
            "PCR 0.82 neutral-to-bullish",
            "PCR collapsing -0.14",
            "\u2605 NEW LONGS: FutOI +3.4% + Price +3.0%",
            "Del 1.15x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 3.05,
          "price_sign": 1,
          "pcr_d1": 0.91,
          "pcr_d2": 0.82,
          "pcr_chg": -0.14,
          "fut_oi_chg_pct": 3.42,
          "oi_sign": 1,
          "avg_del": 1.15,
          "peak_del": 1.29,
          "del_chg": -0.28,
          "avg_vol": 1.035,
          "call_oi_growth_pct": 71.54,
          "put_oi_growth_pct": 53.75,
          "opt_oi_growth_pct": 63.06,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.5,
          "signals": [
            "PCR 0.84 neutral-to-bullish",
            "\u2605 NEW LONGS: FutOI +2.6% + Price +1.1%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.13,
          "price_sign": 1,
          "pcr_d1": 0.82,
          "pcr_d2": 0.84,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": 2.57,
          "oi_sign": 1,
          "avg_del": 0.95,
          "peak_del": 1.01,
          "del_chg": -0.12,
          "avg_vol": 0.915,
          "call_oi_growth_pct": 0.2,
          "put_oi_growth_pct": 2.82,
          "opt_oi_growth_pct": 1.38,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.46,
          "pcr": 0.91,
          "pcr_chg_1d": 0.04,
          "fut_oi": 49608750,
          "oi_chg_pct": -14.89,
          "delivery": 1.29,
          "volume": 1.08,
          "call_oi": 20505000,
          "put_oi": 18697500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 3.05,
          "pcr": 0.82,
          "pcr_chg_1d": -0.14,
          "fut_oi": 51307500,
          "oi_chg_pct": 0.12,
          "delivery": 1.01,
          "volume": 0.99,
          "call_oi": 35175000,
          "put_oi": 28747500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.13,
          "pcr": 0.84,
          "pcr_chg_1d": 0.02,
          "fut_oi": 52623750,
          "oi_chg_pct": 2.57,
          "delivery": 0.89,
          "volume": 0.84,
          "call_oi": 35246250,
          "put_oi": 29557500
        }
      ]
    },
    {
      "symbol": "LUPIN",
      "rank": 62,
      "days_available": 3,
      "latest_score": 6.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          3.5,
          6.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.065,
        "pcr_first": 0.97,
        "pcr_last": 0.84,
        "days_delivery_institutional": 3,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 7.55,
        "cumulative_price_chg_pct_window": 1.73,
        "persistence_score": 5.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 3.5,
          "signals": [
            "PCR 0.78 neutral-to-bullish"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.04,
          "price_sign": 0,
          "pcr_d1": 0.97,
          "pcr_d2": 0.78,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": 7.65,
          "oi_sign": 1,
          "avg_del": 1.93,
          "peak_del": 2.09,
          "del_chg": -0.32,
          "avg_vol": 1.685,
          "call_oi_growth_pct": 29.63,
          "put_oi_growth_pct": 4.53,
          "opt_oi_growth_pct": 17.31,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.5,
          "signals": [
            "PCR 0.84 neutral-to-bullish",
            "PCR rising +0.06",
            "Del 1.46x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 1.69,
          "price_sign": 1,
          "pcr_d1": 0.78,
          "pcr_d2": 0.84,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": -0.1,
          "oi_sign": -1,
          "avg_del": 1.46,
          "peak_del": 1.77,
          "del_chg": -0.62,
          "avg_vol": 1.335,
          "call_oi_growth_pct": -1.35,
          "put_oi_growth_pct": 6.09,
          "opt_oi_growth_pct": 1.91,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -1.69,
          "pcr": 0.97,
          "pcr_chg_1d": -0.03,
          "fut_oi": 6092800,
          "oi_chg_pct": 2.84,
          "delivery": 2.09,
          "volume": 1.66,
          "call_oi": 1534675,
          "put_oi": 1481125
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.04,
          "pcr": 0.78,
          "pcr_chg_1d": -0.01,
          "fut_oi": 6559025,
          "oi_chg_pct": 3.38,
          "delivery": 1.77,
          "volume": 1.71,
          "call_oi": 1989425,
          "put_oi": 1548275
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.69,
          "pcr": 0.84,
          "pcr_chg_1d": 0.06,
          "fut_oi": 6552650,
          "oi_chg_pct": -0.1,
          "delivery": 1.15,
          "volume": 0.96,
          "call_oi": 1962650,
          "put_oi": 1642625
        }
      ]
    },
    {
      "symbol": "POLICYBZR",
      "rank": 63,
      "days_available": 3,
      "latest_score": 6.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -1.0,
          6.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.005,
        "pcr_first": 0.82,
        "pcr_last": 0.83,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 1.46,
        "cumulative_price_chg_pct_window": 0.75,
        "persistence_score": 4.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -1.0,
          "signals": [
            "PCR 0.91 approaching bullish zone"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.35,
          "price_sign": -1,
          "pcr_d1": 0.82,
          "pcr_d2": 0.91,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 1.28,
          "oi_sign": 1,
          "avg_del": 0.71,
          "peak_del": 0.77,
          "del_chg": -0.12,
          "avg_vol": 0.725,
          "call_oi_growth_pct": 61.46,
          "put_oi_growth_pct": 78.98,
          "opt_oi_growth_pct": 69.34,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.5,
          "signals": [
            "PCR 0.83 neutral-to-bullish",
            "PCR easing -0.08",
            "Del 1.42x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.1,
          "price_sign": 1,
          "pcr_d1": 0.91,
          "pcr_d2": 0.83,
          "pcr_chg": -0.08,
          "fut_oi_chg_pct": 0.17,
          "oi_sign": 1,
          "avg_del": 1.415,
          "peak_del": 2.18,
          "del_chg": 1.53,
          "avg_vol": 1.2,
          "call_oi_growth_pct": 11.66,
          "put_oi_growth_pct": 1.96,
          "opt_oi_growth_pct": 7.04,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.37,
          "pcr": 0.82,
          "pcr_chg_1d": -0.35,
          "fut_oi": 7768250,
          "oi_chg_pct": 0.51,
          "delivery": 0.77,
          "volume": 0.62,
          "call_oi": 623000,
          "put_oi": 509600
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.35,
          "pcr": 0.91,
          "pcr_chg_1d": 0.01,
          "fut_oi": 7868000,
          "oi_chg_pct": 2.22,
          "delivery": 0.65,
          "volume": 0.83,
          "call_oi": 1005900,
          "put_oi": 912100
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.1,
          "pcr": 0.83,
          "pcr_chg_1d": -0.08,
          "fut_oi": 7881650,
          "oi_chg_pct": 0.17,
          "delivery": 2.18,
          "volume": 1.57,
          "call_oi": 1123150,
          "put_oi": 929950
        }
      ]
    },
    {
      "symbol": "OFSS",
      "rank": 64,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          9.5,
          6.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.085,
        "pcr_first": 0.72,
        "pcr_last": 0.89,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -7.08,
        "cumulative_price_chg_pct_window": 1.02,
        "persistence_score": 7.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 9.5,
          "signals": [
            "PCR 0.88 approaching bullish zone",
            "PCR surging +0.17"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 0.52,
          "price_sign": 1,
          "pcr_d1": 0.72,
          "pcr_d2": 0.88,
          "pcr_chg": 0.17,
          "fut_oi_chg_pct": -6.22,
          "oi_sign": -1,
          "avg_del": 0.76,
          "peak_del": 1.08,
          "del_chg": 0.64,
          "avg_vol": 0.69,
          "call_oi_growth_pct": 46.98,
          "put_oi_growth_pct": 79.58,
          "opt_oi_growth_pct": 60.59,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.89 approaching bullish zone",
            "Del 1.18x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.5,
          "price_sign": 1,
          "pcr_d1": 0.88,
          "pcr_d2": 0.89,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": -0.92,
          "oi_sign": -1,
          "avg_del": 1.175,
          "peak_del": 1.27,
          "del_chg": 0.19,
          "avg_vol": 0.995,
          "call_oi_growth_pct": 9.29,
          "put_oi_growth_pct": 10.99,
          "opt_oi_growth_pct": 10.08,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.26,
          "pcr": 0.72,
          "pcr_chg_1d": -0.03,
          "fut_oi": 1598475,
          "oi_chg_pct": 1.67,
          "delivery": 0.44,
          "volume": 0.45,
          "call_oi": 288975,
          "put_oi": 207150
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.52,
          "pcr": 0.88,
          "pcr_chg_1d": 0.17,
          "fut_oi": 1499025,
          "oi_chg_pct": -0.53,
          "delivery": 1.08,
          "volume": 0.93,
          "call_oi": 424725,
          "put_oi": 372000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.5,
          "pcr": 0.89,
          "pcr_chg_1d": 0.01,
          "fut_oi": 1485300,
          "oi_chg_pct": -0.92,
          "delivery": 1.27,
          "volume": 1.06,
          "call_oi": 464175,
          "put_oi": 412875
        }
      ]
    },
    {
      "symbol": "BHARATFORG",
      "rank": 65,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -10.5,
          6.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.03,
        "pcr_first": 0.51,
        "pcr_last": 0.57,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 6.06,
        "cumulative_price_chg_pct_window": 0.97,
        "persistence_score": 0.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -10.5,
          "signals": [
            "PCR 0.54 call writers dominant",
            "PCR easing -0.05",
            "\u26a0 NEW SHORTS: FutOI +8.6% + Price -2.4%",
            "Del 1.07x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -2.36,
          "price_sign": -1,
          "pcr_d1": 0.51,
          "pcr_d2": 0.54,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": 8.6,
          "oi_sign": 1,
          "avg_del": 1.07,
          "peak_del": 1.66,
          "del_chg": 1.18,
          "avg_vol": 1.015,
          "call_oi_growth_pct": 26.66,
          "put_oi_growth_pct": 32.61,
          "opt_oi_growth_pct": 28.68,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.57 neutral",
            "Del 1.29x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 3.41,
          "price_sign": 1,
          "pcr_d1": 0.54,
          "pcr_d2": 0.57,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -2.35,
          "oi_sign": -1,
          "avg_del": 1.29,
          "peak_del": 1.66,
          "del_chg": -0.74,
          "avg_vol": 1.23,
          "call_oi_growth_pct": 1.31,
          "put_oi_growth_pct": 8.2,
          "opt_oi_growth_pct": 3.71,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.37,
          "pcr": 0.51,
          "pcr_chg_1d": -0.4,
          "fut_oi": 7594500,
          "oi_chg_pct": 1.54,
          "delivery": 0.48,
          "volume": 0.57,
          "call_oi": 2325500,
          "put_oi": 1191500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.36,
          "pcr": 0.54,
          "pcr_chg_1d": -0.05,
          "fut_oi": 8248000,
          "oi_chg_pct": 2.52,
          "delivery": 1.66,
          "volume": 1.46,
          "call_oi": 2945500,
          "put_oi": 1580000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.41,
          "pcr": 0.57,
          "pcr_chg_1d": 0.03,
          "fut_oi": 8054500,
          "oi_chg_pct": -2.35,
          "delivery": 0.92,
          "volume": 1.0,
          "call_oi": 2984000,
          "put_oi": 1709500
        }
      ]
    },
    {
      "symbol": "PNBHOUSING",
      "rank": 66,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.5,
          6.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.22,
        "pcr_first": 1.36,
        "pcr_last": 0.92,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 4.13,
        "cumulative_price_chg_pct_window": -0.98,
        "persistence_score": 3.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -2.5,
          "signals": [
            "PCR 0.87 approaching bullish zone",
            "PCR surging +0.09",
            "\u26a0 NEW SHORTS: FutOI +3.8% + Price -1.2%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.19,
          "price_sign": -1,
          "pcr_d1": 1.36,
          "pcr_d2": 0.87,
          "pcr_chg": 0.09,
          "fut_oi_chg_pct": 3.85,
          "oi_sign": 1,
          "avg_del": 0.86,
          "peak_del": 0.96,
          "del_chg": -0.2,
          "avg_vol": 0.89,
          "call_oi_growth_pct": 126.05,
          "put_oi_growth_pct": 43.56,
          "opt_oi_growth_pct": 78.46,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.92 approaching bullish zone",
            "PCR rising +0.05"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.21,
          "price_sign": 0,
          "pcr_d1": 0.87,
          "pcr_d2": 0.92,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": 0.27,
          "oi_sign": 1,
          "avg_del": 0.555,
          "peak_del": 0.76,
          "del_chg": -0.41,
          "avg_vol": 0.625,
          "call_oi_growth_pct": 2.91,
          "put_oi_growth_pct": 9.46,
          "opt_oi_growth_pct": 5.95,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.31,
          "pcr": 1.36,
          "pcr_chg_1d": 0.0,
          "fut_oi": 12999350,
          "oi_chg_pct": 2.65,
          "delivery": 0.96,
          "volume": 1.02,
          "call_oi": 544050,
          "put_oi": 741650
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.19,
          "pcr": 0.87,
          "pcr_chg_1d": 0.09,
          "fut_oi": 13499200,
          "oi_chg_pct": -0.6,
          "delivery": 0.76,
          "volume": 0.76,
          "call_oi": 1229800,
          "put_oi": 1064700
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.21,
          "pcr": 0.92,
          "pcr_chg_1d": 0.05,
          "fut_oi": 13535600,
          "oi_chg_pct": 0.27,
          "delivery": 0.35,
          "volume": 0.49,
          "call_oi": 1265550,
          "put_oi": 1165450
        }
      ]
    },
    {
      "symbol": "RVNL",
      "rank": 67,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -7.5,
          6.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.08,
        "pcr_first": 0.86,
        "pcr_last": 0.7,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 10.52,
        "cumulative_price_chg_pct_window": 0.02,
        "persistence_score": 1.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -7.5,
          "signals": [
            "PCR 0.71 neutral",
            "\u26a0 NEW SHORTS: FutOI +5.9% + Price -0.8%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.77,
          "price_sign": -1,
          "pcr_d1": 0.86,
          "pcr_d2": 0.71,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 5.88,
          "oi_sign": 1,
          "avg_del": 0.785,
          "peak_del": 1.07,
          "del_chg": 0.57,
          "avg_vol": 0.965,
          "call_oi_growth_pct": 40.47,
          "put_oi_growth_pct": 16.64,
          "opt_oi_growth_pct": 29.46,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.70 neutral",
            "\u2605 NEW LONGS: FutOI +4.4% + Price +0.8%",
            "Del 1.18x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 0.8,
          "price_sign": 1,
          "pcr_d1": 0.71,
          "pcr_d2": 0.7,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": 4.39,
          "oi_sign": 1,
          "avg_del": 1.18,
          "peak_del": 1.29,
          "del_chg": 0.22,
          "avg_vol": 1.09,
          "call_oi_growth_pct": 8.61,
          "put_oi_growth_pct": 6.99,
          "opt_oi_growth_pct": 7.93,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 5.19,
          "pcr": 0.86,
          "pcr_chg_1d": -0.04,
          "fut_oi": 47517475,
          "oi_chg_pct": -8.05,
          "delivery": 0.5,
          "volume": 0.8,
          "call_oi": 10746675,
          "put_oi": 9235400
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.77,
          "pcr": 0.71,
          "pcr_chg_1d": -0.02,
          "fut_oi": 50309750,
          "oi_chg_pct": 0.93,
          "delivery": 1.07,
          "volume": 1.13,
          "call_oi": 15095975,
          "put_oi": 10772600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.8,
          "pcr": 0.7,
          "pcr_chg_1d": -0.01,
          "fut_oi": 52516425,
          "oi_chg_pct": 4.39,
          "delivery": 1.29,
          "volume": 1.05,
          "call_oi": 16395275,
          "put_oi": 11525950
        }
      ]
    },
    {
      "symbol": "HAL",
      "rank": 68,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          5.5,
          6.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.02,
        "pcr_first": 0.95,
        "pcr_last": 0.91,
        "days_delivery_institutional": 3,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -7.25,
        "cumulative_price_chg_pct_window": 5.24,
        "persistence_score": 5.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 5.5,
          "signals": [
            "PCR 0.87 approaching bullish zone",
            "PCR easing -0.04",
            "Del 1.24x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 3.21,
          "price_sign": 1,
          "pcr_d1": 0.95,
          "pcr_d2": 0.87,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": -5.71,
          "oi_sign": -1,
          "avg_del": 1.24,
          "peak_del": 1.42,
          "del_chg": 0.36,
          "avg_vol": 1.585,
          "call_oi_growth_pct": 33.9,
          "put_oi_growth_pct": 22.43,
          "opt_oi_growth_pct": 28.31,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.91 approaching bullish zone",
            "PCR rising +0.04",
            "Del 1.27x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.97,
          "price_sign": 1,
          "pcr_d1": 0.87,
          "pcr_d2": 0.91,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": -1.63,
          "oi_sign": -1,
          "avg_del": 1.27,
          "peak_del": 1.42,
          "del_chg": -0.3,
          "avg_vol": 1.335,
          "call_oi_growth_pct": -4.02,
          "put_oi_growth_pct": 0.78,
          "opt_oi_growth_pct": -1.78,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 5.26,
          "pcr": 0.95,
          "pcr_chg_1d": -0.09,
          "fut_oi": 8368500,
          "oi_chg_pct": 0.17,
          "delivery": 1.06,
          "volume": 1.3,
          "call_oi": 2437800,
          "put_oi": 2317650
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 3.21,
          "pcr": 0.87,
          "pcr_chg_1d": -0.04,
          "fut_oi": 7890900,
          "oi_chg_pct": -2.14,
          "delivery": 1.42,
          "volume": 1.87,
          "call_oi": 3264300,
          "put_oi": 2837550
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.97,
          "pcr": 0.91,
          "pcr_chg_1d": 0.04,
          "fut_oi": 7762200,
          "oi_chg_pct": -1.63,
          "delivery": 1.12,
          "volume": 0.8,
          "call_oi": 3133200,
          "put_oi": 2859750
        }
      ]
    },
    {
      "symbol": "IREDA",
      "rank": 69,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.5,
          6.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.035,
        "pcr_first": 0.94,
        "pcr_last": 0.87,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 3.78,
        "cumulative_price_chg_pct_window": 1.03,
        "persistence_score": 5.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 4.5,
          "signals": [
            "PCR 0.91 approaching bullish zone"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.55,
          "price_sign": 1,
          "pcr_d1": 0.94,
          "pcr_d2": 0.91,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -0.47,
          "oi_sign": -1,
          "avg_del": 0.78,
          "peak_del": 1.07,
          "del_chg": 0.58,
          "avg_vol": 0.995,
          "call_oi_growth_pct": 14.79,
          "put_oi_growth_pct": 10.52,
          "opt_oi_growth_pct": 12.72,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.87 approaching bullish zone",
            "PCR easing -0.04",
            "Del 1.08x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.48,
          "price_sign": 1,
          "pcr_d1": 0.91,
          "pcr_d2": 0.87,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 4.28,
          "oi_sign": 1,
          "avg_del": 1.08,
          "peak_del": 1.09,
          "del_chg": 0.02,
          "avg_vol": 1.12,
          "call_oi_growth_pct": 9.06,
          "put_oi_growth_pct": 4.62,
          "opt_oi_growth_pct": 6.95,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.39,
          "pcr": 0.94,
          "pcr_chg_1d": -0.17,
          "fut_oi": 50269950,
          "oi_chg_pct": -4.28,
          "delivery": 0.49,
          "volume": 0.78,
          "call_oi": 14231250,
          "put_oi": 13441200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.55,
          "pcr": 0.91,
          "pcr_chg_1d": 0.0,
          "fut_oi": 50031900,
          "oi_chg_pct": 2.81,
          "delivery": 1.07,
          "volume": 1.21,
          "call_oi": 16335750,
          "put_oi": 14855700
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.48,
          "pcr": 0.87,
          "pcr_chg_1d": -0.04,
          "fut_oi": 52170900,
          "oi_chg_pct": 4.28,
          "delivery": 1.09,
          "volume": 1.03,
          "call_oi": 17815800,
          "put_oi": 15542250
        }
      ]
    },
    {
      "symbol": "JIOFIN",
      "rank": 70,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -5.5,
          6.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.04,
        "pcr_first": 0.95,
        "pcr_last": 0.87,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -1.33,
        "cumulative_price_chg_pct_window": -1.48,
        "persistence_score": 2.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -5.5,
          "signals": [
            "PCR 0.83 neutral-to-bullish",
            "PCR easing -0.04",
            "Del 1.21x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -3.25,
          "price_sign": -1,
          "pcr_d1": 0.95,
          "pcr_d2": 0.83,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": -0.57,
          "oi_sign": -1,
          "avg_del": 1.215,
          "peak_del": 1.46,
          "del_chg": 0.49,
          "avg_vol": 1.135,
          "call_oi_growth_pct": 38.04,
          "put_oi_growth_pct": 20.4,
          "opt_oi_growth_pct": 29.43,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.87 approaching bullish zone",
            "PCR rising +0.04",
            "Del 1.08x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.83,
          "price_sign": 1,
          "pcr_d1": 0.83,
          "pcr_d2": 0.87,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": -0.76,
          "oi_sign": -1,
          "avg_del": 1.08,
          "peak_del": 1.46,
          "del_chg": -0.76,
          "avg_vol": 0.925,
          "call_oi_growth_pct": -2.61,
          "put_oi_growth_pct": 1.53,
          "opt_oi_growth_pct": -0.73,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.49,
          "pcr": 0.95,
          "pcr_chg_1d": -0.05,
          "fut_oi": 153854500,
          "oi_chg_pct": -2.15,
          "delivery": 0.97,
          "volume": 1.09,
          "call_oi": 29372650,
          "put_oi": 28009650
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -3.25,
          "pcr": 0.83,
          "pcr_chg_1d": -0.04,
          "fut_oi": 152973250,
          "oi_chg_pct": 0.46,
          "delivery": 1.46,
          "volume": 1.18,
          "call_oi": 40546900,
          "put_oi": 33722500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.83,
          "pcr": 0.87,
          "pcr_chg_1d": 0.04,
          "fut_oi": 151814700,
          "oi_chg_pct": -0.76,
          "delivery": 0.7,
          "volume": 0.67,
          "call_oi": 39487050,
          "put_oi": 34239500
        }
      ]
    },
    {
      "symbol": "UPL",
      "rank": 71,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          5.0,
          6.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.025,
        "pcr_first": 0.67,
        "pcr_last": 0.72,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 6.39,
        "cumulative_price_chg_pct_window": 0.71,
        "persistence_score": 5.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 5.0,
          "signals": [
            "PCR 0.69 neutral"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.27,
          "price_sign": 0,
          "pcr_d1": 0.67,
          "pcr_d2": 0.69,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 6.36,
          "oi_sign": 1,
          "avg_del": 1.015,
          "peak_del": 1.37,
          "del_chg": 0.71,
          "avg_vol": 1.125,
          "call_oi_growth_pct": 27.47,
          "put_oi_growth_pct": 31.72,
          "opt_oi_growth_pct": 29.17,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.72 neutral",
            "Del 1.27x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.44,
          "price_sign": 1,
          "pcr_d1": 0.69,
          "pcr_d2": 0.72,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 0.02,
          "oi_sign": 1,
          "avg_del": 1.275,
          "peak_del": 1.37,
          "del_chg": -0.19,
          "avg_vol": 1.3,
          "call_oi_growth_pct": 2.2,
          "put_oi_growth_pct": 7.49,
          "opt_oi_growth_pct": 4.36,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.67,
          "pcr": 0.67,
          "pcr_chg_1d": 0.04,
          "fut_oi": 27617610,
          "oi_chg_pct": -1.34,
          "delivery": 0.66,
          "volume": 0.71,
          "call_oi": 7296675,
          "put_oi": 4861740
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.27,
          "pcr": 0.69,
          "pcr_chg_1d": 0.03,
          "fut_oi": 29375045,
          "oi_chg_pct": 1.32,
          "delivery": 1.37,
          "volume": 1.54,
          "call_oi": 9300720,
          "put_oi": 6403730
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.44,
          "pcr": 0.72,
          "pcr_chg_1d": 0.03,
          "fut_oi": 29381820,
          "oi_chg_pct": 0.02,
          "delivery": 1.18,
          "volume": 1.06,
          "call_oi": 9505325,
          "put_oi": 6883400
        }
      ]
    },
    {
      "symbol": "JSWSTEEL",
      "rank": 72,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.5,
          6.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.015,
        "pcr_first": 0.89,
        "pcr_last": 0.86,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -0.83,
        "cumulative_price_chg_pct_window": 1.72,
        "persistence_score": 4.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 1.5,
          "signals": [
            "PCR 0.83 neutral-to-bullish"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.29,
          "price_sign": 1,
          "pcr_d1": 0.89,
          "pcr_d2": 0.83,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -1.01,
          "oi_sign": -1,
          "avg_del": 0.96,
          "peak_del": 0.97,
          "del_chg": -0.02,
          "avg_vol": 0.975,
          "call_oi_growth_pct": 110.5,
          "put_oi_growth_pct": 97.51,
          "opt_oi_growth_pct": 104.4,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.86 approaching bullish zone"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.42,
          "price_sign": 1,
          "pcr_d1": 0.83,
          "pcr_d2": 0.86,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 0.18,
          "oi_sign": 1,
          "avg_del": 0.815,
          "peak_del": 0.95,
          "del_chg": -0.27,
          "avg_vol": 0.815,
          "call_oi_growth_pct": -5.35,
          "put_oi_growth_pct": -2.5,
          "opt_oi_growth_pct": -4.05,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.59,
          "pcr": 0.89,
          "pcr_chg_1d": -0.26,
          "fut_oi": 51325650,
          "oi_chg_pct": 1.85,
          "delivery": 0.97,
          "volume": 0.96,
          "call_oi": 3238650,
          "put_oi": 2872800
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.29,
          "pcr": 0.83,
          "pcr_chg_1d": -0.01,
          "fut_oi": 50805225,
          "oi_chg_pct": -0.35,
          "delivery": 0.95,
          "volume": 0.99,
          "call_oi": 6817500,
          "put_oi": 5674050
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.42,
          "pcr": 0.86,
          "pcr_chg_1d": 0.03,
          "fut_oi": 50899050,
          "oi_chg_pct": 0.18,
          "delivery": 0.68,
          "volume": 0.64,
          "call_oi": 6453000,
          "put_oi": 5532300
        }
      ]
    },
    {
      "symbol": "ASTRAL",
      "rank": 73,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          6.0,
          6.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.115,
        "pcr_first": 0.83,
        "pcr_last": 0.6,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 4.86,
        "cumulative_price_chg_pct_window": 6.85,
        "persistence_score": 6.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 6.0,
          "signals": [
            "PCR 0.67 neutral",
            "Del 1.08x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 2.5,
          "price_sign": 1,
          "pcr_d1": 0.83,
          "pcr_d2": 0.67,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": 0.79,
          "oi_sign": 1,
          "avg_del": 1.08,
          "peak_del": 1.54,
          "del_chg": 0.92,
          "avg_vol": 0.88,
          "call_oi_growth_pct": 107.4,
          "put_oi_growth_pct": 66.76,
          "opt_oi_growth_pct": 88.92,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.60 neutral",
            "PCR easing -0.07",
            "\u2605 NEW LONGS: FutOI +4.0% + Price +4.2%",
            "Del 1.56x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 4.24,
          "price_sign": 1,
          "pcr_d1": 0.67,
          "pcr_d2": 0.6,
          "pcr_chg": -0.07,
          "fut_oi_chg_pct": 4.04,
          "oi_sign": 1,
          "avg_del": 1.555,
          "peak_del": 1.57,
          "del_chg": 0.03,
          "avg_vol": 1.095,
          "call_oi_growth_pct": 17.82,
          "put_oi_growth_pct": 6.2,
          "opt_oi_growth_pct": 13.15,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -1.79,
          "pcr": 0.83,
          "pcr_chg_1d": -0.05,
          "fut_oi": 9029975,
          "oi_chg_pct": 0.78,
          "delivery": 0.62,
          "volume": 0.73,
          "call_oi": 907375,
          "put_oi": 756925
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 2.5,
          "pcr": 0.67,
          "pcr_chg_1d": 0.0,
          "fut_oi": 9101375,
          "oi_chg_pct": 3.13,
          "delivery": 1.54,
          "volume": 1.03,
          "call_oi": 1881900,
          "put_oi": 1262250
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 4.24,
          "pcr": 0.6,
          "pcr_chg_1d": -0.07,
          "fut_oi": 9469000,
          "oi_chg_pct": 4.04,
          "delivery": 1.57,
          "volume": 1.16,
          "call_oi": 2217225,
          "put_oi": 1340450
        }
      ]
    },
    {
      "symbol": "BLUESTARCO",
      "rank": 74,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          11.0,
          6.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.13,
        "pcr_first": 0.39,
        "pcr_last": 0.65,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 22.67,
        "cumulative_price_chg_pct_window": 4.37,
        "persistence_score": 7.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 11.0,
          "signals": [
            "PCR 0.59 neutral",
            "PCR rising +0.04",
            "\u2605 NEW LONGS: FutOI +14.8% + Price +2.2%",
            "Del 1.19x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 2.24,
          "price_sign": 1,
          "pcr_d1": 0.39,
          "pcr_d2": 0.59,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": 14.81,
          "oi_sign": 1,
          "avg_del": 1.19,
          "peak_del": 1.87,
          "del_chg": -1.36,
          "avg_vol": 1.35,
          "call_oi_growth_pct": 29.74,
          "put_oi_growth_pct": 97.94,
          "opt_oi_growth_pct": 48.86,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.65 neutral",
            "PCR rising +0.06",
            "\u2605 NEW LONGS: FutOI +6.8% + Price +2.1%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": 2.08,
          "price_sign": 1,
          "pcr_d1": 0.59,
          "pcr_d2": 0.65,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": 6.85,
          "oi_sign": 1,
          "avg_del": 0.465,
          "peak_del": 0.51,
          "del_chg": -0.09,
          "avg_vol": 0.535,
          "call_oi_growth_pct": 5.0,
          "put_oi_growth_pct": 14.54,
          "opt_oi_growth_pct": 8.55,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -3.38,
          "pcr": 0.39,
          "pcr_chg_1d": -0.15,
          "fut_oi": 2475850,
          "oi_chg_pct": 7.89,
          "delivery": 1.87,
          "volume": 2.13,
          "call_oi": 811850,
          "put_oi": 316225
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 2.24,
          "pcr": 0.59,
          "pcr_chg_1d": 0.04,
          "fut_oi": 2842450,
          "oi_chg_pct": 10.11,
          "delivery": 0.51,
          "volume": 0.57,
          "call_oi": 1053325,
          "put_oi": 625950
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.08,
          "pcr": 0.65,
          "pcr_chg_1d": 0.06,
          "fut_oi": 3037125,
          "oi_chg_pct": 6.85,
          "delivery": 0.42,
          "volume": 0.5,
          "call_oi": 1105975,
          "put_oi": 716950
        }
      ]
    },
    {
      "symbol": "GMRAIRPORT",
      "rank": 75,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -6.5,
          6.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.1,
        "pcr_first": 0.99,
        "pcr_last": 0.79,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -1.39,
        "cumulative_price_chg_pct_window": -0.6,
        "persistence_score": 1.83,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -6.5,
          "signals": [
            "PCR 0.77 neutral-to-bullish",
            "PCR collapsing -0.09"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": -1.35,
          "price_sign": -1,
          "pcr_d1": 0.99,
          "pcr_d2": 0.77,
          "pcr_chg": -0.09,
          "fut_oi_chg_pct": 0.2,
          "oi_sign": 1,
          "avg_del": 0.68,
          "peak_del": 0.88,
          "del_chg": 0.4,
          "avg_vol": 0.805,
          "call_oi_growth_pct": 41.08,
          "put_oi_growth_pct": 10.1,
          "opt_oi_growth_pct": 25.71,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.79 neutral-to-bullish",
            "Del 1.35x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.76,
          "price_sign": 1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.79,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": -1.59,
          "oi_sign": -1,
          "avg_del": 1.35,
          "peak_del": 1.82,
          "del_chg": 0.94,
          "avg_vol": 1.215,
          "call_oi_growth_pct": 0.02,
          "put_oi_growth_pct": 3.28,
          "opt_oi_growth_pct": 1.44,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 5.36,
          "pcr": 0.99,
          "pcr_chg_1d": 0.01,
          "fut_oi": 140895000,
          "oi_chg_pct": 0.97,
          "delivery": 0.48,
          "volume": 0.74,
          "call_oi": 21936375,
          "put_oi": 21608550
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.35,
          "pcr": 0.77,
          "pcr_chg_1d": -0.09,
          "fut_oi": 141174000,
          "oi_chg_pct": 0.56,
          "delivery": 0.88,
          "volume": 0.87,
          "call_oi": 30948075,
          "put_oi": 23791725
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.76,
          "pcr": 0.79,
          "pcr_chg_1d": 0.02,
          "fut_oi": 138935025,
          "oi_chg_pct": -1.59,
          "delivery": 1.82,
          "volume": 1.56,
          "call_oi": 30955050,
          "put_oi": 24572925
        }
      ]
    },
    {
      "symbol": "ONGC",
      "rank": 76,
      "days_available": 3,
      "latest_score": -6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING SHORT",
      "latest_sign": "bearish",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild short build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (SHORT)",
        "direction": "short",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.5,
          -6.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.17,
        "pcr_first": 0.81,
        "pcr_last": 0.47,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 2.87,
        "cumulative_price_chg_pct_window": 0.35,
        "persistence_score": -3.5,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": 1.5,
          "signals": [
            "PCR 0.54 call writers dominant",
            "\u2605 NEW LONGS: FutOI +2.5% + Price +1.1%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.09,
          "price_sign": 1,
          "pcr_d1": 0.81,
          "pcr_d2": 0.54,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 2.45,
          "oi_sign": 1,
          "avg_del": 0.795,
          "peak_del": 1.16,
          "del_chg": -0.73,
          "avg_vol": 0.73,
          "call_oi_growth_pct": 116.62,
          "put_oi_growth_pct": 44.93,
          "opt_oi_growth_pct": 84.65,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -6.0,
          "signals": [
            "PCR 0.47 call writers dominant",
            "PCR easing -0.07"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": -0.73,
          "price_sign": -1,
          "pcr_d1": 0.54,
          "pcr_d2": 0.47,
          "pcr_chg": -0.07,
          "fut_oi_chg_pct": 0.4,
          "oi_sign": 1,
          "avg_del": 0.47,
          "peak_del": 0.51,
          "del_chg": 0.08,
          "avg_vol": 0.5,
          "call_oi_growth_pct": 15.43,
          "put_oi_growth_pct": 0.41,
          "opt_oi_growth_pct": 10.17,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.19,
          "pcr": 0.81,
          "pcr_chg_1d": -0.01,
          "fut_oi": 94137750,
          "oi_chg_pct": -1.74,
          "delivery": 1.16,
          "volume": 0.98,
          "call_oi": 30933000,
          "put_oi": 24903000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.09,
          "pcr": 0.54,
          "pcr_chg_1d": 0.03,
          "fut_oi": 96448500,
          "oi_chg_pct": -0.03,
          "delivery": 0.43,
          "volume": 0.48,
          "call_oi": 67007250,
          "put_oi": 36092250
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.73,
          "pcr": 0.47,
          "pcr_chg_1d": -0.07,
          "fut_oi": 96835500,
          "oi_chg_pct": 0.4,
          "delivery": 0.51,
          "volume": 0.52,
          "call_oi": 77346000,
          "put_oi": 36238500
        }
      ]
    },
    {
      "symbol": "GAIL",
      "rank": 77,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          0.0,
          6.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.03,
        "pcr_first": 1.05,
        "pcr_last": 1.11,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -7.17,
        "cumulative_price_chg_pct_window": 0.51,
        "persistence_score": 4.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 0.0,
          "signals": [
            "PCR 1.11 ABOVE 1.0 \u2014 put writers dominant"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.7,
          "price_sign": -1,
          "pcr_d1": 1.05,
          "pcr_d2": 1.11,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -6.08,
          "oi_sign": -1,
          "avg_del": 0.71,
          "peak_del": 0.81,
          "del_chg": -0.2,
          "avg_vol": 0.71,
          "call_oi_growth_pct": 10.36,
          "put_oi_growth_pct": 17.15,
          "opt_oi_growth_pct": 13.83,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 1.11 ABOVE 1.0 \u2014 put writers dominant"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.22,
          "price_sign": 1,
          "pcr_d1": 1.11,
          "pcr_d2": 1.11,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -1.16,
          "oi_sign": -1,
          "avg_del": 0.845,
          "peak_del": 1.08,
          "del_chg": 0.47,
          "avg_vol": 0.8,
          "call_oi_growth_pct": 0.92,
          "put_oi_growth_pct": 0.91,
          "opt_oi_growth_pct": 0.91,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.15,
          "pcr": 1.05,
          "pcr_chg_1d": 0.0,
          "fut_oi": 86675400,
          "oi_chg_pct": -2.2,
          "delivery": 0.81,
          "volume": 0.78,
          "call_oi": 24292800,
          "put_oi": 25445700
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.7,
          "pcr": 1.11,
          "pcr_chg_1d": 0.0,
          "fut_oi": 81405450,
          "oi_chg_pct": -0.73,
          "delivery": 0.61,
          "volume": 0.64,
          "call_oi": 26809650,
          "put_oi": 29808450
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.22,
          "pcr": 1.11,
          "pcr_chg_1d": 0.0,
          "fut_oi": 80457300,
          "oi_chg_pct": -1.16,
          "delivery": 1.08,
          "volume": 0.96,
          "call_oi": 27055350,
          "put_oi": 30079350
        }
      ]
    },
    {
      "symbol": "YESBANK",
      "rank": 78,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -0.5,
          6.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.015,
        "pcr_first": 0.86,
        "pcr_last": 0.89,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.31,
        "cumulative_price_chg_pct_window": 0.21,
        "persistence_score": 3.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -0.5,
          "signals": [
            "PCR 0.86 approaching bullish zone"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": -0.58,
          "price_sign": -1,
          "pcr_d1": 0.86,
          "pcr_d2": 0.86,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 1.29,
          "oi_sign": 1,
          "avg_del": 0.67,
          "peak_del": 0.85,
          "del_chg": 0.36,
          "avg_vol": 0.765,
          "call_oi_growth_pct": 23.59,
          "put_oi_growth_pct": 24.07,
          "opt_oi_growth_pct": 23.81,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.89 approaching bullish zone",
            "Del 1.04x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.79,
          "price_sign": 1,
          "pcr_d1": 0.86,
          "pcr_d2": 0.89,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -0.97,
          "oi_sign": -1,
          "avg_del": 1.04,
          "peak_del": 1.23,
          "del_chg": 0.38,
          "avg_vol": 0.87,
          "call_oi_growth_pct": -0.02,
          "put_oi_growth_pct": 2.59,
          "opt_oi_growth_pct": 1.19,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.83,
          "pcr": 0.86,
          "pcr_chg_1d": -0.08,
          "fut_oi": 1139379600,
          "oi_chg_pct": -0.7,
          "delivery": 0.49,
          "volume": 0.67,
          "call_oi": 226936700,
          "put_oi": 195214700
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.58,
          "pcr": 0.86,
          "pcr_chg_1d": -0.02,
          "fut_oi": 1154089900,
          "oi_chg_pct": 0.2,
          "delivery": 0.85,
          "volume": 0.86,
          "call_oi": 280459800,
          "put_oi": 242206800
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.79,
          "pcr": 0.89,
          "pcr_chg_1d": 0.03,
          "fut_oi": 1142925000,
          "oi_chg_pct": -0.97,
          "delivery": 1.23,
          "volume": 0.88,
          "call_oi": 280397600,
          "put_oi": 248489000
        }
      ]
    },
    {
      "symbol": "OBEROIRLTY",
      "rank": 79,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          13.0,
          6.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.025,
        "pcr_first": 0.82,
        "pcr_last": 0.77,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 10.83,
        "cumulative_price_chg_pct_window": 2.19,
        "persistence_score": 8.33,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 13.0,
          "signals": [
            "PCR 0.90 approaching bullish zone",
            "\u2605 NEW LONGS: FutOI +8.1% + Price +1.1%",
            "Del 1.34x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.08,
          "price_sign": 1,
          "pcr_d1": 0.82,
          "pcr_d2": 0.9,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": 8.1,
          "oi_sign": 1,
          "avg_del": 1.345,
          "peak_del": 1.71,
          "del_chg": 0.73,
          "avg_vol": 1.29,
          "call_oi_growth_pct": 81.51,
          "put_oi_growth_pct": 99.42,
          "opt_oi_growth_pct": 89.55,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.77 neutral-to-bullish",
            "PCR collapsing -0.13",
            "\u2605 NEW LONGS: FutOI +2.5% + Price +1.1%",
            "Del 1.28x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.1,
          "price_sign": 1,
          "pcr_d1": 0.9,
          "pcr_d2": 0.77,
          "pcr_chg": -0.13,
          "fut_oi_chg_pct": 2.52,
          "oi_sign": 1,
          "avg_del": 1.285,
          "peak_del": 1.71,
          "del_chg": -0.85,
          "avg_vol": 1.21,
          "call_oi_growth_pct": 21.45,
          "put_oi_growth_pct": 4.86,
          "opt_oi_growth_pct": 13.61,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.91,
          "pcr": 0.82,
          "pcr_chg_1d": -0.03,
          "fut_oi": 8522500,
          "oi_chg_pct": 0.32,
          "delivery": 0.98,
          "volume": 1.02,
          "call_oi": 518700,
          "put_oi": 422800
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.08,
          "pcr": 0.9,
          "pcr_chg_1d": -0.01,
          "fut_oi": 9212700,
          "oi_chg_pct": 8.18,
          "delivery": 1.71,
          "volume": 1.56,
          "call_oi": 941500,
          "put_oi": 843150
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.1,
          "pcr": 0.77,
          "pcr_chg_1d": -0.13,
          "fut_oi": 9445100,
          "oi_chg_pct": 2.52,
          "delivery": 0.86,
          "volume": 0.86,
          "call_oi": 1143450,
          "put_oi": 884100
        }
      ]
    },
    {
      "symbol": "BSE",
      "rank": 80,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          12.0,
          6.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.035,
        "pcr_first": 1.02,
        "pcr_last": 1.09,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 12.54,
        "cumulative_price_chg_pct_window": 3.71,
        "persistence_score": 8.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 12.0,
          "signals": [
            "PCR 1.08 ABOVE 1.0 \u2014 put writers dominant",
            "\u2605 NEW LONGS: FutOI +14.5% + Price +3.0%",
            "Del 1.06x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 2.96,
          "price_sign": 1,
          "pcr_d1": 1.02,
          "pcr_d2": 1.08,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 14.53,
          "oi_sign": 1,
          "avg_del": 1.065,
          "peak_del": 1.09,
          "del_chg": -0.05,
          "avg_vol": 1.25,
          "call_oi_growth_pct": 85.86,
          "put_oi_growth_pct": 97.65,
          "opt_oi_growth_pct": 91.81,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 1.09 ABOVE 1.0 \u2014 put writers dominant"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.73,
          "price_sign": 1,
          "pcr_d1": 1.08,
          "pcr_d2": 1.09,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": -1.74,
          "oi_sign": -1,
          "avg_del": 0.945,
          "peak_del": 1.04,
          "del_chg": -0.19,
          "avg_vol": 1.195,
          "call_oi_growth_pct": 10.45,
          "put_oi_growth_pct": 10.94,
          "opt_oi_growth_pct": 10.7,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 6.86,
          "pcr": 1.02,
          "pcr_chg_1d": 0.08,
          "fut_oi": 7002750,
          "oi_chg_pct": 1.8,
          "delivery": 1.09,
          "volume": 1.22,
          "call_oi": 3127125,
          "put_oi": 3180375
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 2.96,
          "pcr": 1.08,
          "pcr_chg_1d": 0.03,
          "fut_oi": 8020125,
          "oi_chg_pct": 8.58,
          "delivery": 1.04,
          "volume": 1.28,
          "call_oi": 5812125,
          "put_oi": 6286125
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.73,
          "pcr": 1.09,
          "pcr_chg_1d": 0.01,
          "fut_oi": 7880625,
          "oi_chg_pct": -1.74,
          "delivery": 0.85,
          "volume": 1.11,
          "call_oi": 6419250,
          "put_oi": 6973875
        }
      ]
    },
    {
      "symbol": "CGPOWER",
      "rank": 81,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -8.5,
          6.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.0,
        "pcr_first": 0.75,
        "pcr_last": 0.75,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 6.4,
        "cumulative_price_chg_pct_window": 0.67,
        "persistence_score": 1.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -8.5,
          "signals": [
            "PCR 0.71 neutral",
            "PCR easing -0.04",
            "\u26a0 NEW SHORTS: FutOI +6.5% + Price -0.8%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.78,
          "price_sign": -1,
          "pcr_d1": 0.75,
          "pcr_d2": 0.71,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 6.48,
          "oi_sign": 1,
          "avg_del": 0.87,
          "peak_del": 1.07,
          "del_chg": 0.4,
          "avg_vol": 0.88,
          "call_oi_growth_pct": 81.92,
          "put_oi_growth_pct": 72.12,
          "opt_oi_growth_pct": 77.73,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.75 neutral-to-bullish",
            "PCR rising +0.04",
            "Del 1.02x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.46,
          "price_sign": 1,
          "pcr_d1": 0.71,
          "pcr_d2": 0.75,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": -0.08,
          "oi_sign": -1,
          "avg_del": 1.025,
          "peak_del": 1.07,
          "del_chg": -0.09,
          "avg_vol": 0.985,
          "call_oi_growth_pct": 5.47,
          "put_oi_growth_pct": 12.31,
          "opt_oi_growth_pct": 8.31,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.85,
          "pcr": 0.75,
          "pcr_chg_1d": -0.03,
          "fut_oi": 17903550,
          "oi_chg_pct": 0.98,
          "delivery": 0.67,
          "volume": 0.64,
          "call_oi": 1528300,
          "put_oi": 1143250
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.78,
          "pcr": 0.71,
          "pcr_chg_1d": -0.04,
          "fut_oi": 19063800,
          "oi_chg_pct": 1.45,
          "delivery": 1.07,
          "volume": 1.12,
          "call_oi": 2780350,
          "put_oi": 1967750
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.46,
          "pcr": 0.75,
          "pcr_chg_1d": 0.04,
          "fut_oi": 19049350,
          "oi_chg_pct": -0.08,
          "delivery": 0.98,
          "volume": 0.85,
          "call_oi": 2932500,
          "put_oi": 2210000
        }
      ]
    },
    {
      "symbol": "CHOLAFIN",
      "rank": 82,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -0.5,
          6.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.03,
        "pcr_first": 0.82,
        "pcr_last": 0.88,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -2.5,
        "cumulative_price_chg_pct_window": 1.74,
        "persistence_score": 3.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -0.5,
          "signals": [
            "PCR 0.85 approaching bullish zone"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.36,
          "price_sign": -1,
          "pcr_d1": 0.82,
          "pcr_d2": 0.85,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": 0.0,
          "oi_sign": 1,
          "avg_del": 0.815,
          "peak_del": 0.84,
          "del_chg": -0.05,
          "avg_vol": 0.79,
          "call_oi_growth_pct": 146.76,
          "put_oi_growth_pct": 155.06,
          "opt_oi_growth_pct": 150.51,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.88 approaching bullish zone"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 3.14,
          "price_sign": 1,
          "pcr_d1": 0.85,
          "pcr_d2": 0.88,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -2.5,
          "oi_sign": -1,
          "avg_del": 0.87,
          "peak_del": 0.95,
          "del_chg": 0.16,
          "avg_vol": 0.825,
          "call_oi_growth_pct": 8.95,
          "put_oi_growth_pct": 13.05,
          "opt_oi_growth_pct": 10.83,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.4,
          "pcr": 0.82,
          "pcr_chg_1d": -0.08,
          "fut_oi": 19386250,
          "oi_chg_pct": -0.14,
          "delivery": 0.84,
          "volume": 0.78,
          "call_oi": 1410000,
          "put_oi": 1160000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.36,
          "pcr": 0.85,
          "pcr_chg_1d": 0.02,
          "fut_oi": 19386875,
          "oi_chg_pct": -3.62,
          "delivery": 0.79,
          "volume": 0.8,
          "call_oi": 3479375,
          "put_oi": 2958750
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.14,
          "pcr": 0.88,
          "pcr_chg_1d": 0.03,
          "fut_oi": 18901250,
          "oi_chg_pct": -2.5,
          "delivery": 0.95,
          "volume": 0.85,
          "call_oi": 3790625,
          "put_oi": 3345000
        }
      ]
    },
    {
      "symbol": "LTF",
      "rank": 83,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -1.0,
          6.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.085,
        "pcr_first": 0.63,
        "pcr_last": 0.8,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -7.14,
        "cumulative_price_chg_pct_window": 1.08,
        "persistence_score": 3.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -1.0,
          "signals": [
            "PCR 0.80 neutral-to-bullish"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -1.19,
          "price_sign": -1,
          "pcr_d1": 0.63,
          "pcr_d2": 0.8,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -7.61,
          "oi_sign": -1,
          "avg_del": 0.655,
          "peak_del": 0.66,
          "del_chg": -0.01,
          "avg_vol": 0.68,
          "call_oi_growth_pct": 4.6,
          "put_oi_growth_pct": 31.58,
          "opt_oi_growth_pct": 15.06,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.80 neutral-to-bullish"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 2.3,
          "price_sign": 1,
          "pcr_d1": 0.8,
          "pcr_d2": 0.8,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": 0.51,
          "oi_sign": 1,
          "avg_del": 0.9,
          "peak_del": 1.15,
          "del_chg": 0.5,
          "avg_vol": 0.735,
          "call_oi_growth_pct": 0.42,
          "put_oi_growth_pct": 1.05,
          "opt_oi_growth_pct": 0.7,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.85,
          "pcr": 0.63,
          "pcr_chg_1d": -0.01,
          "fut_oi": 58594500,
          "oi_chg_pct": -3.52,
          "delivery": 0.66,
          "volume": 0.71,
          "call_oi": 17718750,
          "put_oi": 11214000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.19,
          "pcr": 0.8,
          "pcr_chg_1d": 0.03,
          "fut_oi": 54135000,
          "oi_chg_pct": 2.38,
          "delivery": 0.65,
          "volume": 0.65,
          "call_oi": 18533250,
          "put_oi": 14755500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.3,
          "pcr": 0.8,
          "pcr_chg_1d": 0.0,
          "fut_oi": 54409500,
          "oi_chg_pct": 0.51,
          "delivery": 1.15,
          "volume": 0.82,
          "call_oi": 18612000,
          "put_oi": 14910750
        }
      ]
    },
    {
      "symbol": "KAYNES",
      "rank": 84,
      "days_available": 3,
      "latest_score": 6.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.5,
          6.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.04,
        "pcr_first": 0.68,
        "pcr_last": 0.76,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -1.24,
        "cumulative_price_chg_pct_window": -0.39,
        "persistence_score": 2.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -4.5,
          "signals": [
            "PCR 0.73 neutral",
            "PCR collapsing -0.09",
            "Del 1.15x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -1.53,
          "price_sign": -1,
          "pcr_d1": 0.68,
          "pcr_d2": 0.73,
          "pcr_chg": -0.09,
          "fut_oi_chg_pct": -1.98,
          "oi_sign": -1,
          "avg_del": 1.145,
          "peak_del": 1.27,
          "del_chg": -0.25,
          "avg_vol": 1.035,
          "call_oi_growth_pct": 24.28,
          "put_oi_growth_pct": 33.65,
          "opt_oi_growth_pct": 28.08,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 6.0,
          "signals": [
            "PCR 0.76 neutral-to-bullish"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.16,
          "price_sign": 1,
          "pcr_d1": 0.73,
          "pcr_d2": 0.76,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 0.76,
          "oi_sign": 1,
          "avg_del": 0.885,
          "peak_del": 1.02,
          "del_chg": -0.27,
          "avg_vol": 0.76,
          "call_oi_growth_pct": 6.9,
          "put_oi_growth_pct": 10.44,
          "opt_oi_growth_pct": 8.4,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.22,
          "pcr": 0.68,
          "pcr_chg_1d": -0.16,
          "fut_oi": 3450600,
          "oi_chg_pct": -6.11,
          "delivery": 1.27,
          "volume": 1.21,
          "call_oi": 991400,
          "put_oi": 676400
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.53,
          "pcr": 0.73,
          "pcr_chg_1d": -0.09,
          "fut_oi": 3382200,
          "oi_chg_pct": 6.04,
          "delivery": 1.02,
          "volume": 0.86,
          "call_oi": 1232100,
          "put_oi": 904000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.16,
          "pcr": 0.76,
          "pcr_chg_1d": 0.03,
          "fut_oi": 3407900,
          "oi_chg_pct": 0.76,
          "delivery": 0.75,
          "volume": 0.66,
          "call_oi": 1317100,
          "put_oi": 998400
        }
      ]
    },
    {
      "symbol": "ETERNAL",
      "rank": 85,
      "days_available": 3,
      "latest_score": 5.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -6.5,
          5.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.075,
        "pcr_first": 0.85,
        "pcr_last": 0.7,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 8.97,
        "cumulative_price_chg_pct_window": -1.39,
        "persistence_score": 1.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -6.5,
          "signals": [
            "PCR 0.69 neutral",
            "PCR easing -0.07",
            "\u26a0 NEW SHORTS: FutOI +6.3% + Price -2.4%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": -2.35,
          "price_sign": -1,
          "pcr_d1": 0.85,
          "pcr_d2": 0.69,
          "pcr_chg": -0.07,
          "fut_oi_chg_pct": 6.28,
          "oi_sign": 1,
          "avg_del": 0.69,
          "peak_del": 0.8,
          "del_chg": 0.22,
          "avg_vol": 0.705,
          "call_oi_growth_pct": 61.71,
          "put_oi_growth_pct": 31.51,
          "opt_oi_growth_pct": 47.83,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.5,
          "signals": [
            "PCR 0.70 neutral",
            "\u2605 NEW LONGS: FutOI +2.5% + Price +1.0%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.98,
          "price_sign": 1,
          "pcr_d1": 0.69,
          "pcr_d2": 0.7,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 2.53,
          "oi_sign": 1,
          "avg_del": 0.845,
          "peak_del": 0.89,
          "del_chg": 0.09,
          "avg_vol": 0.825,
          "call_oi_growth_pct": 0.75,
          "put_oi_growth_pct": 2.3,
          "opt_oi_growth_pct": 1.39,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.29,
          "pcr": 0.85,
          "pcr_chg_1d": -0.09,
          "fut_oi": 189651975,
          "oi_chg_pct": -11.68,
          "delivery": 0.58,
          "volume": 0.6,
          "call_oi": 35184325,
          "put_oi": 29946325
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.35,
          "pcr": 0.69,
          "pcr_chg_1d": -0.07,
          "fut_oi": 201558725,
          "oi_chg_pct": 0.36,
          "delivery": 0.8,
          "volume": 0.81,
          "call_oi": 56897775,
          "put_oi": 39382000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.98,
          "pcr": 0.7,
          "pcr_chg_1d": 0.01,
          "fut_oi": 206660925,
          "oi_chg_pct": 2.53,
          "delivery": 0.89,
          "volume": 0.84,
          "call_oi": 57327000,
          "put_oi": 40286525
        }
      ]
    },
    {
      "symbol": "PAYTM",
      "rank": 86,
      "days_available": 3,
      "latest_score": 5.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -6.0,
          5.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.045,
        "pcr_first": 0.74,
        "pcr_last": 0.83,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -11.69,
        "cumulative_price_chg_pct_window": 0.98,
        "persistence_score": 1.67,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -6.0,
          "signals": [
            "PCR 0.80 neutral-to-bullish",
            "PCR easing -0.06",
            "Del 1.30x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -1.35,
          "price_sign": -1,
          "pcr_d1": 0.74,
          "pcr_d2": 0.8,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": -10.37,
          "oi_sign": -1,
          "avg_del": 1.3,
          "peak_del": 1.88,
          "del_chg": 1.16,
          "avg_vol": 1.24,
          "call_oi_growth_pct": 106.47,
          "put_oi_growth_pct": 123.17,
          "opt_oi_growth_pct": 113.59,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.5,
          "signals": [
            "PCR 0.83 neutral-to-bullish",
            "Del 1.41x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 2.36,
          "price_sign": 1,
          "pcr_d1": 0.8,
          "pcr_d2": 0.83,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -1.47,
          "oi_sign": -1,
          "avg_del": 1.41,
          "peak_del": 1.88,
          "del_chg": -0.94,
          "avg_vol": 1.22,
          "call_oi_growth_pct": 2.29,
          "put_oi_growth_pct": 6.32,
          "opt_oi_growth_pct": 4.09,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.97,
          "pcr": 0.74,
          "pcr_chg_1d": -0.07,
          "fut_oi": 18994275,
          "oi_chg_pct": -1.5,
          "delivery": 0.72,
          "volume": 0.83,
          "call_oi": 2800675,
          "put_oi": 2080750
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.35,
          "pcr": 0.8,
          "pcr_chg_1d": -0.06,
          "fut_oi": 17025175,
          "oi_chg_pct": -3.81,
          "delivery": 1.88,
          "volume": 1.65,
          "call_oi": 5782600,
          "put_oi": 4643625
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.36,
          "pcr": 0.83,
          "pcr_chg_1d": 0.03,
          "fut_oi": 16774325,
          "oi_chg_pct": -1.47,
          "delivery": 0.94,
          "volume": 0.79,
          "call_oi": 5915275,
          "put_oi": 4937250
        }
      ]
    },
    {
      "symbol": "ICICIBANK",
      "rank": 87,
      "days_available": 3,
      "latest_score": 5.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.0,
          5.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.045,
        "pcr_first": 0.85,
        "pcr_last": 0.94,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -8.89,
        "cumulative_price_chg_pct_window": 0.97,
        "persistence_score": 2.33,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -4.0,
          "signals": [
            "PCR 0.86 approaching bullish zone",
            "PCR collapsing -0.13",
            "Del 1.14x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -2.13,
          "price_sign": -1,
          "pcr_d1": 0.85,
          "pcr_d2": 0.86,
          "pcr_chg": -0.13,
          "fut_oi_chg_pct": -8.18,
          "oi_sign": -1,
          "avg_del": 1.135,
          "peak_del": 1.45,
          "del_chg": -0.63,
          "avg_vol": 1.155,
          "call_oi_growth_pct": 21.87,
          "put_oi_growth_pct": 23.79,
          "opt_oi_growth_pct": 22.76,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.5,
          "signals": [
            "PCR 0.94 approaching bullish zone",
            "PCR rising +0.08"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 3.17,
          "price_sign": 1,
          "pcr_d1": 0.86,
          "pcr_d2": 0.94,
          "pcr_chg": 0.08,
          "fut_oi_chg_pct": -0.77,
          "oi_sign": -1,
          "avg_del": 0.885,
          "peak_del": 0.95,
          "del_chg": 0.13,
          "avg_vol": 0.97,
          "call_oi_growth_pct": -1.35,
          "put_oi_growth_pct": 7.85,
          "opt_oi_growth_pct": 2.92,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.56,
          "pcr": 0.85,
          "pcr_chg_1d": -0.16,
          "fut_oi": 129082100,
          "oi_chg_pct": 1.28,
          "delivery": 1.45,
          "volume": 1.24,
          "call_oi": 15234100,
          "put_oi": 12950000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.13,
          "pcr": 0.86,
          "pcr_chg_1d": -0.13,
          "fut_oi": 118518400,
          "oi_chg_pct": -0.1,
          "delivery": 0.82,
          "volume": 1.07,
          "call_oi": 18566100,
          "put_oi": 16031400
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.17,
          "pcr": 0.94,
          "pcr_chg_1d": 0.08,
          "fut_oi": 117610500,
          "oi_chg_pct": -0.77,
          "delivery": 0.95,
          "volume": 0.87,
          "call_oi": 18316200,
          "put_oi": 17290000
        }
      ]
    },
    {
      "symbol": "M&M",
      "rank": 88,
      "days_available": 3,
      "latest_score": 5.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.5,
          5.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.045,
        "pcr_first": 0.76,
        "pcr_last": 0.85,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 3.7,
        "cumulative_price_chg_pct_window": 1.55,
        "persistence_score": 2.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -4.5,
          "signals": [
            "PCR 0.80 neutral-to-bullish",
            "PCR collapsing -0.10",
            "\u26a0 NEW SHORTS: FutOI +4.5% + Price -1.4%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.35,
          "price_sign": -1,
          "pcr_d1": 0.76,
          "pcr_d2": 0.8,
          "pcr_chg": -0.1,
          "fut_oi_chg_pct": 4.45,
          "oi_sign": 1,
          "avg_del": 0.88,
          "peak_del": 0.95,
          "del_chg": -0.14,
          "avg_vol": 0.925,
          "call_oi_growth_pct": 18.91,
          "put_oi_growth_pct": 24.77,
          "opt_oi_growth_pct": 21.44,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.5,
          "signals": [
            "PCR 0.85 approaching bullish zone",
            "PCR rising +0.05"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 2.94,
          "price_sign": 1,
          "pcr_d1": 0.8,
          "pcr_d2": 0.85,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": -0.72,
          "oi_sign": -1,
          "avg_del": 0.845,
          "peak_del": 0.88,
          "del_chg": 0.07,
          "avg_vol": 0.935,
          "call_oi_growth_pct": -0.51,
          "put_oi_growth_pct": 6.19,
          "opt_oi_growth_pct": 2.47,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.6,
          "pcr": 0.76,
          "pcr_chg_1d": -0.03,
          "fut_oi": 19166400,
          "oi_chg_pct": -0.91,
          "delivery": 0.95,
          "volume": 0.89,
          "call_oi": 3333200,
          "put_oi": 2539000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.35,
          "pcr": 0.8,
          "pcr_chg_1d": -0.1,
          "fut_oi": 20020200,
          "oi_chg_pct": -0.05,
          "delivery": 0.81,
          "volume": 0.96,
          "call_oi": 3963400,
          "put_oi": 3167800
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.94,
          "pcr": 0.85,
          "pcr_chg_1d": 0.05,
          "fut_oi": 19876200,
          "oi_chg_pct": -0.72,
          "delivery": 0.88,
          "volume": 0.91,
          "call_oi": 3943200,
          "put_oi": 3363800
        }
      ]
    },
    {
      "symbol": "HINDUNILVR",
      "rank": 89,
      "days_available": 3,
      "latest_score": 5.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -6.5,
          5.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.095,
        "pcr_first": 0.95,
        "pcr_last": 0.76,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 10.03,
        "cumulative_price_chg_pct_window": 0.45,
        "persistence_score": 1.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -6.5,
          "signals": [
            "PCR 0.77 neutral-to-bullish",
            "PCR easing -0.06",
            "\u26a0 NEW SHORTS: FutOI +5.4% + Price -0.6%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.58,
          "price_sign": -1,
          "pcr_d1": 0.95,
          "pcr_d2": 0.77,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": 5.37,
          "oi_sign": 1,
          "avg_del": 0.97,
          "peak_del": 1.03,
          "del_chg": 0.12,
          "avg_vol": 0.975,
          "call_oi_growth_pct": 63.62,
          "put_oi_growth_pct": 32.42,
          "opt_oi_growth_pct": 48.38,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.5,
          "signals": [
            "PCR 0.76 neutral-to-bullish",
            "\u2605 NEW LONGS: FutOI +4.4% + Price +1.0%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.04,
          "price_sign": 1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.76,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": 4.42,
          "oi_sign": 1,
          "avg_del": 0.99,
          "peak_del": 1.03,
          "del_chg": -0.08,
          "avg_vol": 0.985,
          "call_oi_growth_pct": 7.43,
          "put_oi_growth_pct": 6.22,
          "opt_oi_growth_pct": 6.9,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.46,
          "pcr": 0.95,
          "pcr_chg_1d": -0.15,
          "fut_oi": 16236300,
          "oi_chg_pct": 2.37,
          "delivery": 0.91,
          "volume": 0.87,
          "call_oi": 2638500,
          "put_oi": 2519100
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.58,
          "pcr": 0.77,
          "pcr_chg_1d": -0.06,
          "fut_oi": 17107800,
          "oi_chg_pct": 1.92,
          "delivery": 1.03,
          "volume": 1.08,
          "call_oi": 4317000,
          "put_oi": 3335700
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.04,
          "pcr": 0.76,
          "pcr_chg_1d": -0.01,
          "fut_oi": 17864100,
          "oi_chg_pct": 4.42,
          "delivery": 0.95,
          "volume": 0.89,
          "call_oi": 4637700,
          "put_oi": 3543300
        }
      ]
    },
    {
      "symbol": "BAJFINANCE",
      "rank": 90,
      "days_available": 3,
      "latest_score": 5.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.5,
          5.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.035,
        "pcr_first": 0.93,
        "pcr_last": 0.86,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -1.73,
        "cumulative_price_chg_pct_window": 1.04,
        "persistence_score": 2.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -2.5,
          "signals": [
            "PCR 0.83 neutral-to-bullish"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -1.29,
          "price_sign": -1,
          "pcr_d1": 0.93,
          "pcr_d2": 0.83,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": -0.89,
          "oi_sign": -1,
          "avg_del": 0.83,
          "peak_del": 0.93,
          "del_chg": -0.2,
          "avg_vol": 0.84,
          "call_oi_growth_pct": 47.73,
          "put_oi_growth_pct": 31.6,
          "opt_oi_growth_pct": 39.94,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.5,
          "signals": [
            "PCR 0.86 approaching bullish zone"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 2.36,
          "price_sign": 1,
          "pcr_d1": 0.83,
          "pcr_d2": 0.86,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -0.85,
          "oi_sign": -1,
          "avg_del": 0.88,
          "peak_del": 1.03,
          "del_chg": 0.3,
          "avg_vol": 0.8,
          "call_oi_growth_pct": 1.83,
          "put_oi_growth_pct": 5.3,
          "opt_oi_growth_pct": 3.4,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.96,
          "pcr": 0.93,
          "pcr_chg_1d": -0.04,
          "fut_oi": 72608250,
          "oi_chg_pct": 0.82,
          "delivery": 0.93,
          "volume": 0.92,
          "call_oi": 12056250,
          "put_oi": 11262000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.29,
          "pcr": 0.83,
          "pcr_chg_1d": 0.01,
          "fut_oi": 71964000,
          "oi_chg_pct": 0.77,
          "delivery": 0.73,
          "volume": 0.76,
          "call_oi": 17810250,
          "put_oi": 14820750
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.36,
          "pcr": 0.86,
          "pcr_chg_1d": 0.03,
          "fut_oi": 71355000,
          "oi_chg_pct": -0.85,
          "delivery": 1.03,
          "volume": 0.84,
          "call_oi": 18135750,
          "put_oi": 15606000
        }
      ]
    },
    {
      "symbol": "MCX",
      "rank": 91,
      "days_available": 3,
      "latest_score": 5.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          10.5,
          5.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.095,
        "pcr_first": 0.72,
        "pcr_last": 0.91,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 9.45,
        "cumulative_price_chg_pct_window": 2.82,
        "persistence_score": 7.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 10.5,
          "signals": [
            "PCR 0.92 approaching bullish zone",
            "PCR rising +0.08",
            "\u2605 NEW LONGS: FutOI +6.4% + Price +2.4%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 2.36,
          "price_sign": 1,
          "pcr_d1": 0.72,
          "pcr_d2": 0.92,
          "pcr_chg": 0.08,
          "fut_oi_chg_pct": 6.42,
          "oi_sign": 1,
          "avg_del": 0.87,
          "peak_del": 1.02,
          "del_chg": 0.3,
          "avg_vol": 0.9,
          "call_oi_growth_pct": 48.87,
          "put_oi_growth_pct": 88.3,
          "opt_oi_growth_pct": 65.44,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.5,
          "signals": [
            "PCR 0.91 approaching bullish zone"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.45,
          "price_sign": 1,
          "pcr_d1": 0.92,
          "pcr_d2": 0.91,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": 2.85,
          "oi_sign": 1,
          "avg_del": 0.935,
          "peak_del": 1.02,
          "del_chg": -0.17,
          "avg_vol": 0.97,
          "call_oi_growth_pct": 8.42,
          "put_oi_growth_pct": 7.71,
          "opt_oi_growth_pct": 8.08,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.36,
          "pcr": 0.72,
          "pcr_chg_1d": 0.0,
          "fut_oi": 12155000,
          "oi_chg_pct": -0.29,
          "delivery": 0.72,
          "volume": 0.73,
          "call_oi": 3885000,
          "put_oi": 2815000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 2.36,
          "pcr": 0.92,
          "pcr_chg_1d": 0.08,
          "fut_oi": 12935000,
          "oi_chg_pct": 1.03,
          "delivery": 1.02,
          "volume": 1.07,
          "call_oi": 5783750,
          "put_oi": 5300625
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.45,
          "pcr": 0.91,
          "pcr_chg_1d": -0.01,
          "fut_oi": 13303750,
          "oi_chg_pct": 2.85,
          "delivery": 0.85,
          "volume": 0.87,
          "call_oi": 6270625,
          "put_oi": 5709375
        }
      ]
    },
    {
      "symbol": "HDFCAMC",
      "rank": 92,
      "days_available": 3,
      "latest_score": 5.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.5,
          5.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.02,
        "pcr_first": 0.74,
        "pcr_last": 0.78,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -4.92,
        "cumulative_price_chg_pct_window": 3.15,
        "persistence_score": 2.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -2.5,
          "signals": [
            "PCR 0.77 neutral-to-bullish",
            "PCR easing -0.06"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -0.96,
          "price_sign": -1,
          "pcr_d1": 0.74,
          "pcr_d2": 0.77,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": -6.39,
          "oi_sign": -1,
          "avg_del": 0.815,
          "peak_del": 1.02,
          "del_chg": -0.41,
          "avg_vol": 0.92,
          "call_oi_growth_pct": 72.63,
          "put_oi_growth_pct": 80.83,
          "opt_oi_growth_pct": 76.11,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.5,
          "signals": [
            "PCR 0.78 neutral-to-bullish"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": 4.15,
          "price_sign": 1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.78,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 1.56,
          "oi_sign": 1,
          "avg_del": 0.64,
          "peak_del": 0.67,
          "del_chg": 0.06,
          "avg_vol": 0.73,
          "call_oi_growth_pct": 20.87,
          "put_oi_growth_pct": 22.99,
          "opt_oi_growth_pct": 21.79,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 5.6,
          "pcr": 0.74,
          "pcr_chg_1d": 0.05,
          "fut_oi": 6304800,
          "oi_chg_pct": -2.75,
          "delivery": 1.02,
          "volume": 1.16,
          "call_oi": 529500,
          "put_oi": 389700
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.96,
          "pcr": 0.77,
          "pcr_chg_1d": -0.06,
          "fut_oi": 5902200,
          "oi_chg_pct": 1.87,
          "delivery": 0.61,
          "volume": 0.68,
          "call_oi": 914100,
          "put_oi": 704700
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 4.15,
          "pcr": 0.78,
          "pcr_chg_1d": 0.01,
          "fut_oi": 5994300,
          "oi_chg_pct": 1.56,
          "delivery": 0.67,
          "volume": 0.78,
          "call_oi": 1104900,
          "put_oi": 866700
        }
      ]
    },
    {
      "symbol": "SUPREMEIND",
      "rank": 93,
      "days_available": 3,
      "latest_score": 5.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.0,
          5.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.055,
        "pcr_first": 0.53,
        "pcr_last": 0.64,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -0.47,
        "cumulative_price_chg_pct_window": 0.39,
        "persistence_score": 2.33,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -4.0,
          "signals": [
            "PCR 0.64 neutral",
            "PCR collapsing -0.15"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -0.42,
          "price_sign": -1,
          "pcr_d1": 0.53,
          "pcr_d2": 0.64,
          "pcr_chg": -0.15,
          "fut_oi_chg_pct": -2.86,
          "oi_sign": -1,
          "avg_del": 0.81,
          "peak_del": 1.22,
          "del_chg": 0.82,
          "avg_vol": 0.735,
          "call_oi_growth_pct": 117.28,
          "put_oi_growth_pct": 163.55,
          "opt_oi_growth_pct": 133.29,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.5,
          "signals": [
            "PCR 0.64 neutral",
            "\u2605 NEW LONGS: FutOI +2.5% + Price +0.8%",
            "Del 1.17x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 0.81,
          "price_sign": 1,
          "pcr_d1": 0.64,
          "pcr_d2": 0.64,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": 2.46,
          "oi_sign": 1,
          "avg_del": 1.17,
          "peak_del": 1.22,
          "del_chg": -0.1,
          "avg_vol": 0.855,
          "call_oi_growth_pct": 7.95,
          "put_oi_growth_pct": 6.94,
          "opt_oi_growth_pct": 7.56,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -2.32,
          "pcr": 0.53,
          "pcr_chg_1d": -0.31,
          "fut_oi": 2045575,
          "oi_chg_pct": 3.82,
          "delivery": 0.4,
          "volume": 0.55,
          "call_oi": 236950,
          "put_oi": 125300
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.42,
          "pcr": 0.64,
          "pcr_chg_1d": -0.15,
          "fut_oi": 1987125,
          "oi_chg_pct": 2.1,
          "delivery": 1.22,
          "volume": 0.92,
          "call_oi": 514850,
          "put_oi": 330225
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.81,
          "pcr": 0.64,
          "pcr_chg_1d": 0.0,
          "fut_oi": 2035950,
          "oi_chg_pct": 2.46,
          "delivery": 1.12,
          "volume": 0.79,
          "call_oi": 555800,
          "put_oi": 353150
        }
      ]
    },
    {
      "symbol": "PHOENIXLTD",
      "rank": 94,
      "days_available": 3,
      "latest_score": 5.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.0,
          5.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.15,
        "pcr_first": 1.31,
        "pcr_last": 1.01,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.98,
        "cumulative_price_chg_pct_window": 2.93,
        "persistence_score": 4.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 1.0,
          "signals": [
            "PCR 1.29 ABOVE 1.0 \u2014 put writers dominant",
            "PCR easing -0.04"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.19,
          "price_sign": 0,
          "pcr_d1": 1.31,
          "pcr_d2": 1.29,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": -0.41,
          "oi_sign": -1,
          "avg_del": 0.99,
          "peak_del": 1.22,
          "del_chg": 0.46,
          "avg_vol": 0.985,
          "call_oi_growth_pct": 104.87,
          "put_oi_growth_pct": 101.66,
          "opt_oi_growth_pct": 103.05,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.5,
          "signals": [
            "PCR 1.01 ABOVE 1.0 \u2014 put writers dominant",
            "PCR collapsing -0.28",
            "Del 1.29x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 3.13,
          "price_sign": 1,
          "pcr_d1": 1.29,
          "pcr_d2": 1.01,
          "pcr_chg": -0.28,
          "fut_oi_chg_pct": 1.4,
          "oi_sign": 1,
          "avg_del": 1.29,
          "peak_del": 1.36,
          "del_chg": 0.14,
          "avg_vol": 1.185,
          "call_oi_growth_pct": 28.99,
          "put_oi_growth_pct": 0.38,
          "opt_oi_growth_pct": 12.86,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.75,
          "pcr": 1.31,
          "pcr_chg_1d": -0.47,
          "fut_oi": 3847550,
          "oi_chg_pct": 3.93,
          "delivery": 0.76,
          "volume": 0.87,
          "call_oi": 208600,
          "put_oi": 274050
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.19,
          "pcr": 1.29,
          "pcr_chg_1d": -0.04,
          "fut_oi": 3831800,
          "oi_chg_pct": -1.5,
          "delivery": 1.22,
          "volume": 1.1,
          "call_oi": 427350,
          "put_oi": 552650
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.13,
          "pcr": 1.01,
          "pcr_chg_1d": -0.28,
          "fut_oi": 3885350,
          "oi_chg_pct": 1.4,
          "delivery": 1.36,
          "volume": 1.27,
          "call_oi": 551250,
          "put_oi": 554750
        }
      ]
    },
    {
      "symbol": "ADANIPORTS",
      "rank": 95,
      "days_available": 3,
      "latest_score": 5.5,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -6.0,
          5.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.385,
        "pcr_first": 1.45,
        "pcr_last": 0.68,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 3.12,
        "cumulative_price_chg_pct_window": 1.51,
        "persistence_score": 1.67,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -6.0,
          "signals": [
            "PCR 0.63 neutral",
            "PCR rising +0.06",
            "Del 1.01x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.41,
          "price_sign": -1,
          "pcr_d1": 1.45,
          "pcr_d2": 0.63,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": 3.9,
          "oi_sign": 1,
          "avg_del": 1.01,
          "peak_del": 1.25,
          "del_chg": -0.48,
          "avg_vol": 1.085,
          "call_oi_growth_pct": 111.3,
          "put_oi_growth_pct": -7.25,
          "opt_oi_growth_pct": 41.22,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.5,
          "signals": [
            "PCR 0.68 neutral",
            "PCR rising +0.05",
            "Del 1.02x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.93,
          "price_sign": 1,
          "pcr_d1": 0.63,
          "pcr_d2": 0.68,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": -0.75,
          "oi_sign": -1,
          "avg_del": 1.015,
          "peak_del": 1.26,
          "del_chg": 0.49,
          "avg_vol": 0.97,
          "call_oi_growth_pct": 0.42,
          "put_oi_growth_pct": 7.69,
          "opt_oi_growth_pct": 3.24,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 5.55,
          "pcr": 1.45,
          "pcr_chg_1d": -0.19,
          "fut_oi": 20140475,
          "oi_chg_pct": 0.41,
          "delivery": 1.25,
          "volume": 1.33,
          "call_oi": 4185225,
          "put_oi": 6050075
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.41,
          "pcr": 0.63,
          "pcr_chg_1d": 0.06,
          "fut_oi": 20925175,
          "oi_chg_pct": 0.47,
          "delivery": 0.77,
          "volume": 0.84,
          "call_oi": 8843550,
          "put_oi": 5611175
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.93,
          "pcr": 0.68,
          "pcr_chg_1d": 0.05,
          "fut_oi": 20768425,
          "oi_chg_pct": -0.75,
          "delivery": 1.26,
          "volume": 1.1,
          "call_oi": 8880600,
          "put_oi": 6042475
        }
      ]
    },
    {
      "symbol": "CROMPTON",
      "rank": 96,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.5,
          5.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.005,
        "pcr_first": 0.72,
        "pcr_last": 0.73,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -3.58,
        "cumulative_price_chg_pct_window": -1.75,
        "persistence_score": 1.83,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -4.5,
          "signals": [
            "PCR 0.75 neutral-to-bullish",
            "PCR collapsing -0.15",
            "Del 1.42x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -3.31,
          "price_sign": -1,
          "pcr_d1": 0.72,
          "pcr_d2": 0.75,
          "pcr_chg": -0.15,
          "fut_oi_chg_pct": -1.46,
          "oi_sign": -1,
          "avg_del": 1.42,
          "peak_del": 1.79,
          "del_chg": 0.74,
          "avg_vol": 1.465,
          "call_oi_growth_pct": 60.23,
          "put_oi_growth_pct": 68.2,
          "opt_oi_growth_pct": 63.56,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 0.73 neutral",
            "Del 1.34x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.61,
          "price_sign": 1,
          "pcr_d1": 0.75,
          "pcr_d2": 0.73,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": -2.15,
          "oi_sign": -1,
          "avg_del": 1.345,
          "peak_del": 1.79,
          "del_chg": -0.89,
          "avg_vol": 1.405,
          "call_oi_growth_pct": 5.27,
          "put_oi_growth_pct": 2.09,
          "opt_oi_growth_pct": 3.9,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.02,
          "pcr": 0.72,
          "pcr_chg_1d": -0.15,
          "fut_oi": 47350800,
          "oi_chg_pct": -0.45,
          "delivery": 1.05,
          "volume": 1.12,
          "call_oi": 4629600,
          "put_oi": 3322800
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -3.31,
          "pcr": 0.75,
          "pcr_chg_1d": -0.15,
          "fut_oi": 46659600,
          "oi_chg_pct": -1.31,
          "delivery": 1.79,
          "volume": 1.81,
          "call_oi": 7417800,
          "put_oi": 5589000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.61,
          "pcr": 0.73,
          "pcr_chg_1d": -0.02,
          "fut_oi": 45655200,
          "oi_chg_pct": -2.15,
          "delivery": 0.9,
          "volume": 1.0,
          "call_oi": 7808400,
          "put_oi": 5706000
        }
      ]
    },
    {
      "symbol": "CIPLA",
      "rank": 97,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          5.0,
          5.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.005,
        "pcr_first": 0.84,
        "pcr_last": 0.83,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 10.05,
        "cumulative_price_chg_pct_window": 1.12,
        "persistence_score": 5.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 5.0,
          "signals": [
            "PCR 0.78 neutral-to-bullish",
            "PCR easing -0.04",
            "\u2605 NEW LONGS: FutOI +10.1% + Price +0.7%",
            "Del 1.31x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 0.7,
          "price_sign": 1,
          "pcr_d1": 0.84,
          "pcr_d2": 0.78,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 10.14,
          "oi_sign": 1,
          "avg_del": 1.31,
          "peak_del": 1.45,
          "del_chg": -0.28,
          "avg_vol": 1.22,
          "call_oi_growth_pct": 66.35,
          "put_oi_growth_pct": 54.17,
          "opt_oi_growth_pct": 60.79,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 0.83 neutral-to-bullish",
            "PCR rising +0.05",
            "Del 1.03x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.42,
          "price_sign": 1,
          "pcr_d1": 0.78,
          "pcr_d2": 0.83,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": -0.07,
          "oi_sign": -1,
          "avg_del": 1.03,
          "peak_del": 1.17,
          "del_chg": -0.28,
          "avg_vol": 0.95,
          "call_oi_growth_pct": -7.02,
          "put_oi_growth_pct": -1.01,
          "opt_oi_growth_pct": -4.39,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -2.31,
          "pcr": 0.84,
          "pcr_chg_1d": -0.04,
          "fut_oi": 13534500,
          "oi_chg_pct": 4.14,
          "delivery": 1.45,
          "volume": 1.38,
          "call_oi": 2695875,
          "put_oi": 2263875
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.7,
          "pcr": 0.78,
          "pcr_chg_1d": -0.04,
          "fut_oi": 14906250,
          "oi_chg_pct": -0.27,
          "delivery": 1.17,
          "volume": 1.06,
          "call_oi": 4484625,
          "put_oi": 3490125
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.42,
          "pcr": 0.83,
          "pcr_chg_1d": 0.05,
          "fut_oi": 14895375,
          "oi_chg_pct": -0.07,
          "delivery": 0.89,
          "volume": 0.84,
          "call_oi": 4169625,
          "put_oi": 3454875
        }
      ]
    },
    {
      "symbol": "SOLARINDS",
      "rank": 98,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          8.0,
          5.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.005,
        "pcr_first": 0.81,
        "pcr_last": 0.8,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 2.82,
        "cumulative_price_chg_pct_window": 3.01,
        "persistence_score": 6.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 8.0,
          "signals": [
            "PCR 0.82 neutral-to-bullish",
            "\u2605 NEW LONGS: FutOI +2.2% + Price +1.9%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.95,
          "price_sign": 1,
          "pcr_d1": 0.81,
          "pcr_d2": 0.82,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 2.17,
          "oi_sign": 1,
          "avg_del": 0.8,
          "peak_del": 0.89,
          "del_chg": 0.18,
          "avg_vol": 1.02,
          "call_oi_growth_pct": 42.34,
          "put_oi_growth_pct": 42.37,
          "opt_oi_growth_pct": 42.35,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 0.80 neutral-to-bullish"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.04,
          "price_sign": 1,
          "pcr_d1": 0.82,
          "pcr_d2": 0.8,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 0.64,
          "oi_sign": 1,
          "avg_del": 0.8,
          "peak_del": 0.89,
          "del_chg": -0.18,
          "avg_vol": 0.835,
          "call_oi_growth_pct": 3.63,
          "put_oi_growth_pct": 1.36,
          "opt_oi_growth_pct": 2.61,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 6.05,
          "pcr": 0.81,
          "pcr_chg_1d": -0.15,
          "fut_oi": 755850,
          "oi_chg_pct": 2.04,
          "delivery": 0.71,
          "volume": 1.01,
          "call_oi": 155650,
          "put_oi": 126850
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.95,
          "pcr": 0.82,
          "pcr_chg_1d": -0.02,
          "fut_oi": 772250,
          "oi_chg_pct": 0.71,
          "delivery": 0.89,
          "volume": 1.03,
          "call_oi": 221550,
          "put_oi": 180600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.04,
          "pcr": 0.8,
          "pcr_chg_1d": -0.02,
          "fut_oi": 777200,
          "oi_chg_pct": 0.64,
          "delivery": 0.71,
          "volume": 0.64,
          "call_oi": 229600,
          "put_oi": 183050
        }
      ]
    },
    {
      "symbol": "ADANIGREEN",
      "rank": 99,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.5,
          5.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.08,
        "pcr_first": 1.05,
        "pcr_last": 0.89,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -5.04,
        "cumulative_price_chg_pct_window": 5.42,
        "persistence_score": 4.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 4.5,
          "signals": [
            "PCR 0.87 approaching bullish zone",
            "PCR surging +0.12"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 1.45,
          "price_sign": 1,
          "pcr_d1": 1.05,
          "pcr_d2": 0.87,
          "pcr_chg": 0.12,
          "fut_oi_chg_pct": -1.17,
          "oi_sign": -1,
          "avg_del": 0.93,
          "peak_del": 1.42,
          "del_chg": -0.98,
          "avg_vol": 0.91,
          "call_oi_growth_pct": 113.74,
          "put_oi_growth_pct": 78.12,
          "opt_oi_growth_pct": 95.52,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 0.89 approaching bullish zone"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 3.91,
          "price_sign": 1,
          "pcr_d1": 0.87,
          "pcr_d2": 0.89,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": -3.91,
          "oi_sign": -1,
          "avg_del": 0.545,
          "peak_del": 0.65,
          "del_chg": 0.21,
          "avg_vol": 0.69,
          "call_oi_growth_pct": 4.43,
          "put_oi_growth_pct": 6.2,
          "opt_oi_growth_pct": 5.25,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 5.58,
          "pcr": 1.05,
          "pcr_chg_1d": 0.13,
          "fut_oi": 21601200,
          "oi_chg_pct": -1.29,
          "delivery": 1.42,
          "volume": 1.19,
          "call_oi": 2759400,
          "put_oi": 2890200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.45,
          "pcr": 0.87,
          "pcr_chg_1d": 0.12,
          "fut_oi": 21348000,
          "oi_chg_pct": -3.54,
          "delivery": 0.44,
          "volume": 0.63,
          "call_oi": 5898000,
          "put_oi": 5148000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.91,
          "pcr": 0.89,
          "pcr_chg_1d": 0.02,
          "fut_oi": 20512800,
          "oi_chg_pct": -3.91,
          "delivery": 0.65,
          "volume": 0.75,
          "call_oi": 6159000,
          "put_oi": 5467200
        }
      ]
    },
    {
      "symbol": "BPCL",
      "rank": 100,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          5.5,
          5.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.095,
        "pcr_first": 0.64,
        "pcr_last": 0.83,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -6.25,
        "cumulative_price_chg_pct_window": 0.42,
        "persistence_score": 5.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 5.5,
          "signals": [
            "PCR 0.82 neutral-to-bullish",
            "PCR surging +0.19"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": -0.25,
          "price_sign": 0,
          "pcr_d1": 0.64,
          "pcr_d2": 0.82,
          "pcr_chg": 0.19,
          "fut_oi_chg_pct": -2.99,
          "oi_sign": -1,
          "avg_del": 1.14,
          "peak_del": 1.35,
          "del_chg": 0.42,
          "avg_vol": 0.97,
          "call_oi_growth_pct": 30.22,
          "put_oi_growth_pct": 68.44,
          "opt_oi_growth_pct": 45.1,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 0.83 neutral-to-bullish",
            "Del 1.18x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.67,
          "price_sign": 1,
          "pcr_d1": 0.82,
          "pcr_d2": 0.83,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": -3.36,
          "oi_sign": -1,
          "avg_del": 1.18,
          "peak_del": 1.35,
          "del_chg": -0.34,
          "avg_vol": 0.94,
          "call_oi_growth_pct": 2.63,
          "put_oi_growth_pct": 3.7,
          "opt_oi_growth_pct": 3.12,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.09,
          "pcr": 0.64,
          "pcr_chg_1d": -0.11,
          "fut_oi": 53775300,
          "oi_chg_pct": -4.39,
          "delivery": 0.93,
          "volume": 0.88,
          "call_oi": 15102825,
          "put_oi": 9626150
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.25,
          "pcr": 0.82,
          "pcr_chg_1d": 0.19,
          "fut_oi": 52167650,
          "oi_chg_pct": 0.58,
          "delivery": 1.35,
          "volume": 1.06,
          "call_oi": 19667050,
          "put_oi": 16214750
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.67,
          "pcr": 0.83,
          "pcr_chg_1d": 0.01,
          "fut_oi": 50415825,
          "oi_chg_pct": -3.36,
          "delivery": 1.01,
          "volume": 0.82,
          "call_oi": 20184500,
          "put_oi": 16815150
        }
      ]
    },
    {
      "symbol": "INDHOTEL",
      "rank": 101,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.5,
          5.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.005,
        "pcr_first": 1.03,
        "pcr_last": 1.04,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -0.91,
        "cumulative_price_chg_pct_window": 0.81,
        "persistence_score": 3.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 1.5,
          "signals": [
            "PCR 1.04 ABOVE 1.0 \u2014 put writers dominant",
            "PCR rising +0.05"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.14,
          "price_sign": -1,
          "pcr_d1": 1.03,
          "pcr_d2": 1.04,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": 0.63,
          "oi_sign": 1,
          "avg_del": 0.86,
          "peak_del": 1.13,
          "del_chg": -0.54,
          "avg_vol": 0.88,
          "call_oi_growth_pct": 25.88,
          "put_oi_growth_pct": 26.23,
          "opt_oi_growth_pct": 26.06,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 1.04 ABOVE 1.0 \u2014 put writers dominant"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.97,
          "price_sign": 1,
          "pcr_d1": 1.04,
          "pcr_d2": 1.04,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -1.53,
          "oi_sign": -1,
          "avg_del": 0.685,
          "peak_del": 0.78,
          "del_chg": 0.19,
          "avg_vol": 0.615,
          "call_oi_growth_pct": 5.39,
          "put_oi_growth_pct": 5.63,
          "opt_oi_growth_pct": 5.51,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.5,
          "pcr": 1.03,
          "pcr_chg_1d": -0.07,
          "fut_oi": 22027000,
          "oi_chg_pct": 4.24,
          "delivery": 1.13,
          "volume": 1.19,
          "call_oi": 3937000,
          "put_oi": 4068000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.14,
          "pcr": 1.04,
          "pcr_chg_1d": 0.05,
          "fut_oi": 22166000,
          "oi_chg_pct": 1.31,
          "delivery": 0.59,
          "volume": 0.57,
          "call_oi": 4956000,
          "put_oi": 5135000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.97,
          "pcr": 1.04,
          "pcr_chg_1d": 0.0,
          "fut_oi": 21826000,
          "oi_chg_pct": -1.53,
          "delivery": 0.78,
          "volume": 0.66,
          "call_oi": 5223000,
          "put_oi": 5424000
        }
      ]
    },
    {
      "symbol": "PREMIERENE",
      "rank": 102,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -5.5,
          5.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.12,
        "pcr_first": 0.66,
        "pcr_last": 0.9,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 6.27,
        "cumulative_price_chg_pct_window": 1.62,
        "persistence_score": 1.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -5.5,
          "signals": [
            "PCR 0.84 neutral-to-bullish",
            "PCR easing -0.06",
            "Del 2.47x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.33,
          "price_sign": -1,
          "pcr_d1": 0.66,
          "pcr_d2": 0.84,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": 7.52,
          "oi_sign": 1,
          "avg_del": 2.47,
          "peak_del": 3.81,
          "del_chg": -2.68,
          "avg_vol": 1.615,
          "call_oi_growth_pct": 73.63,
          "put_oi_growth_pct": 122.82,
          "opt_oi_growth_pct": 93.15,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 0.90 approaching bullish zone",
            "PCR rising +0.06"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 1.96,
          "price_sign": 1,
          "pcr_d1": 0.84,
          "pcr_d2": 0.9,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": -1.16,
          "oi_sign": -1,
          "avg_del": 0.935,
          "peak_del": 1.13,
          "del_chg": -0.39,
          "avg_vol": 0.865,
          "call_oi_growth_pct": -3.19,
          "put_oi_growth_pct": 2.79,
          "opt_oi_growth_pct": -0.45,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 5.16,
          "pcr": 0.66,
          "pcr_chg_1d": 0.02,
          "fut_oi": 9829050,
          "oi_chg_pct": 9.74,
          "delivery": 3.81,
          "volume": 2.22,
          "call_oi": 1194850,
          "put_oi": 786025
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.33,
          "pcr": 0.84,
          "pcr_chg_1d": -0.06,
          "fut_oi": 10568500,
          "oi_chg_pct": 2.0,
          "delivery": 1.13,
          "volume": 1.01,
          "call_oi": 2074600,
          "put_oi": 1751450
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.96,
          "pcr": 0.9,
          "pcr_chg_1d": 0.06,
          "fut_oi": 10445450,
          "oi_chg_pct": -1.16,
          "delivery": 0.74,
          "volume": 0.72,
          "call_oi": 2008475,
          "put_oi": 1800325
        }
      ]
    },
    {
      "symbol": "NESTLEIND",
      "rank": 103,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          5.0,
          5.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.075,
        "pcr_first": 0.87,
        "pcr_last": 0.72,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 5.12,
        "cumulative_price_chg_pct_window": 2.94,
        "persistence_score": 5.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 5.0,
          "signals": [
            "PCR 0.73 neutral",
            "\u2605 NEW LONGS: FutOI +4.2% + Price +1.2%",
            "Del 1.11x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.24,
          "price_sign": 1,
          "pcr_d1": 0.87,
          "pcr_d2": 0.73,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": 4.21,
          "oi_sign": 1,
          "avg_del": 1.11,
          "peak_del": 1.47,
          "del_chg": -0.72,
          "avg_vol": 1.085,
          "call_oi_growth_pct": 105.66,
          "put_oi_growth_pct": 71.51,
          "opt_oi_growth_pct": 89.76,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 0.72 neutral"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.68,
          "price_sign": 1,
          "pcr_d1": 0.73,
          "pcr_d2": 0.72,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": 0.88,
          "oi_sign": 1,
          "avg_del": 0.91,
          "peak_del": 1.07,
          "del_chg": 0.32,
          "avg_vol": 0.88,
          "call_oi_growth_pct": 1.0,
          "put_oi_growth_pct": 0.51,
          "opt_oi_growth_pct": 0.8,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.51,
          "pcr": 0.87,
          "pcr_chg_1d": -0.27,
          "fut_oi": 17474500,
          "oi_chg_pct": 2.3,
          "delivery": 1.47,
          "volume": 1.36,
          "call_oi": 1114000,
          "put_oi": 970500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.24,
          "pcr": 0.73,
          "pcr_chg_1d": 0.02,
          "fut_oi": 18209500,
          "oi_chg_pct": -1.05,
          "delivery": 0.75,
          "volume": 0.81,
          "call_oi": 2291000,
          "put_oi": 1664500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.68,
          "pcr": 0.72,
          "pcr_chg_1d": -0.01,
          "fut_oi": 18369000,
          "oi_chg_pct": 0.88,
          "delivery": 1.07,
          "volume": 0.95,
          "call_oi": 2314000,
          "put_oi": 1673000
        }
      ]
    },
    {
      "symbol": "DRREDDY",
      "rank": 104,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          8.0,
          5.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.1,
        "pcr_first": 0.97,
        "pcr_last": 0.77,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 17.39,
        "cumulative_price_chg_pct_window": 3.43,
        "persistence_score": 6.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 8.0,
          "signals": [
            "PCR 0.77 neutral-to-bullish",
            "\u2605 NEW LONGS: FutOI +18.9% + Price +1.7%",
            "Del 1.17x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.72,
          "price_sign": 1,
          "pcr_d1": 0.97,
          "pcr_d2": 0.77,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 18.91,
          "oi_sign": 1,
          "avg_del": 1.17,
          "peak_del": 1.5,
          "del_chg": 0.66,
          "avg_vol": 1.12,
          "call_oi_growth_pct": 200.13,
          "put_oi_growth_pct": 137.81,
          "opt_oi_growth_pct": 169.5,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 0.77 neutral-to-bullish",
            "Del 1.25x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.68,
          "price_sign": 1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.77,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -1.28,
          "oi_sign": -1,
          "avg_del": 1.245,
          "peak_del": 1.5,
          "del_chg": -0.51,
          "avg_vol": 1.02,
          "call_oi_growth_pct": 2.45,
          "put_oi_growth_pct": 2.61,
          "opt_oi_growth_pct": 2.52,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -3.61,
          "pcr": 0.97,
          "pcr_chg_1d": -0.22,
          "fut_oi": 11279375,
          "oi_chg_pct": 4.71,
          "delivery": 0.84,
          "volume": 1.02,
          "call_oi": 1896875,
          "put_oi": 1833125
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.72,
          "pcr": 0.77,
          "pcr_chg_1d": -0.02,
          "fut_oi": 13411875,
          "oi_chg_pct": -2.17,
          "delivery": 1.5,
          "volume": 1.22,
          "call_oi": 5693125,
          "put_oi": 4359375
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.68,
          "pcr": 0.77,
          "pcr_chg_1d": 0.0,
          "fut_oi": 13240625,
          "oi_chg_pct": -1.28,
          "delivery": 0.99,
          "volume": 0.82,
          "call_oi": 5832500,
          "put_oi": 4473125
        }
      ]
    },
    {
      "symbol": "INOXWIND",
      "rank": 105,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.0,
          5.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.005,
        "pcr_first": 1.07,
        "pcr_last": 1.08,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -2.31,
        "cumulative_price_chg_pct_window": 0.43,
        "persistence_score": 3.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 1.0,
          "signals": [
            "PCR 1.08 ABOVE 1.0 \u2014 put writers dominant",
            "PCR easing -0.04"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -1.29,
          "price_sign": -1,
          "pcr_d1": 1.07,
          "pcr_d2": 1.08,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": -1.21,
          "oi_sign": -1,
          "avg_del": 0.595,
          "peak_del": 0.79,
          "del_chg": 0.39,
          "avg_vol": 0.735,
          "call_oi_growth_pct": 8.9,
          "put_oi_growth_pct": 9.04,
          "opt_oi_growth_pct": 8.97,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 1.08 ABOVE 1.0 \u2014 put writers dominant"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.74,
          "price_sign": 1,
          "pcr_d1": 1.08,
          "pcr_d2": 1.08,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -1.11,
          "oi_sign": -1,
          "avg_del": 0.78,
          "peak_del": 0.79,
          "del_chg": -0.02,
          "avg_vol": 0.74,
          "call_oi_growth_pct": 0.94,
          "put_oi_growth_pct": 1.75,
          "opt_oi_growth_pct": 1.36,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 6.68,
          "pcr": 1.07,
          "pcr_chg_1d": -0.11,
          "fut_oi": 102627525,
          "oi_chg_pct": -1.98,
          "delivery": 0.4,
          "volume": 0.69,
          "call_oi": 16394950,
          "put_oi": 17606875
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.29,
          "pcr": 1.08,
          "pcr_chg_1d": -0.04,
          "fut_oi": 101383425,
          "oi_chg_pct": 0.43,
          "delivery": 0.79,
          "volume": 0.78,
          "call_oi": 17853550,
          "put_oi": 19197750
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.74,
          "pcr": 1.08,
          "pcr_chg_1d": 0.0,
          "fut_oi": 100260875,
          "oi_chg_pct": -1.11,
          "delivery": 0.77,
          "volume": 0.7,
          "call_oi": 18021575,
          "put_oi": 19533800
        }
      ]
    },
    {
      "symbol": "DLF",
      "rank": 106,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.5,
          5.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.015,
        "pcr_first": 0.93,
        "pcr_last": 0.96,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.09,
        "cumulative_price_chg_pct_window": -0.57,
        "persistence_score": 3.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 1.5,
          "signals": [
            "PCR 0.99 approaching bullish zone"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -1.73,
          "price_sign": -1,
          "pcr_d1": 0.93,
          "pcr_d2": 0.99,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": -0.23,
          "oi_sign": -1,
          "avg_del": 0.77,
          "peak_del": 1.12,
          "del_chg": -0.7,
          "avg_vol": 0.81,
          "call_oi_growth_pct": 40.68,
          "put_oi_growth_pct": 49.27,
          "opt_oi_growth_pct": 44.82,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 0.96 approaching bullish zone"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.18,
          "price_sign": 1,
          "pcr_d1": 0.99,
          "pcr_d2": 0.96,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": 0.32,
          "oi_sign": 1,
          "avg_del": 0.56,
          "peak_del": 0.7,
          "del_chg": 0.28,
          "avg_vol": 0.68,
          "call_oi_growth_pct": 4.85,
          "put_oi_growth_pct": 1.72,
          "opt_oi_growth_pct": 3.3,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.12,
          "pcr": 0.93,
          "pcr_chg_1d": -0.09,
          "fut_oi": 54503625,
          "oi_chg_pct": 4.38,
          "delivery": 1.12,
          "volume": 1.08,
          "call_oi": 6779025,
          "put_oi": 6301350
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.73,
          "pcr": 0.99,
          "pcr_chg_1d": -0.02,
          "fut_oi": 54379050,
          "oi_chg_pct": 0.05,
          "delivery": 0.42,
          "volume": 0.54,
          "call_oi": 9537000,
          "put_oi": 9405825
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.18,
          "pcr": 0.96,
          "pcr_chg_1d": -0.03,
          "fut_oi": 54551475,
          "oi_chg_pct": 0.32,
          "delivery": 0.7,
          "volume": 0.82,
          "call_oi": 9999825,
          "put_oi": 9567525
        }
      ]
    },
    {
      "symbol": "CANBK",
      "rank": 107,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          0.5,
          5.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.035,
        "pcr_first": 0.86,
        "pcr_last": 0.93,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -3.69,
        "cumulative_price_chg_pct_window": 0.69,
        "persistence_score": 3.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 0.5,
          "signals": [
            "PCR 0.90 approaching bullish zone",
            "PCR easing -0.04"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.92,
          "price_sign": -1,
          "pcr_d1": 0.86,
          "pcr_d2": 0.9,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": -0.94,
          "oi_sign": -1,
          "avg_del": 0.9,
          "peak_del": 0.96,
          "del_chg": -0.12,
          "avg_vol": 0.92,
          "call_oi_growth_pct": 28.5,
          "put_oi_growth_pct": 35.25,
          "opt_oi_growth_pct": 31.61,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 0.93 approaching bullish zone"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.62,
          "price_sign": 1,
          "pcr_d1": 0.9,
          "pcr_d2": 0.93,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -2.78,
          "oi_sign": -1,
          "avg_del": 0.915,
          "peak_del": 0.99,
          "del_chg": 0.15,
          "avg_vol": 0.825,
          "call_oi_growth_pct": 0.0,
          "put_oi_growth_pct": 3.49,
          "opt_oi_growth_pct": 1.65,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.12,
          "pcr": 0.86,
          "pcr_chg_1d": -0.07,
          "fut_oi": 205983000,
          "oi_chg_pct": 0.37,
          "delivery": 0.96,
          "volume": 1.0,
          "call_oi": 50753250,
          "put_oi": 43510500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.92,
          "pcr": 0.9,
          "pcr_chg_1d": -0.04,
          "fut_oi": 204052500,
          "oi_chg_pct": 0.85,
          "delivery": 0.84,
          "volume": 0.84,
          "call_oi": 65218500,
          "put_oi": 58846500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.62,
          "pcr": 0.93,
          "pcr_chg_1d": 0.03,
          "fut_oi": 198382500,
          "oi_chg_pct": -2.78,
          "delivery": 0.99,
          "volume": 0.81,
          "call_oi": 65218500,
          "put_oi": 60898500
        }
      ]
    },
    {
      "symbol": "TORNTPHARM",
      "rank": 108,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.5,
          5.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.48,
        "pcr_first": 1.73,
        "pcr_last": 0.77,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 12.37,
        "cumulative_price_chg_pct_window": 3.12,
        "persistence_score": 3.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 1.5,
          "signals": [
            "PCR 0.68 neutral",
            "PCR collapsing -0.15",
            "\u2605 NEW LONGS: FutOI +13.1% + Price +1.6%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.62,
          "price_sign": 1,
          "pcr_d1": 1.73,
          "pcr_d2": 0.68,
          "pcr_chg": -0.15,
          "fut_oi_chg_pct": 13.1,
          "oi_sign": 1,
          "avg_del": 0.825,
          "peak_del": 1.02,
          "del_chg": -0.39,
          "avg_vol": 0.89,
          "call_oi_growth_pct": 176.97,
          "put_oi_growth_pct": 8.91,
          "opt_oi_growth_pct": 70.51,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 0.77 neutral-to-bullish",
            "PCR surging +0.09"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 1.48,
          "price_sign": 1,
          "pcr_d1": 0.68,
          "pcr_d2": 0.77,
          "pcr_chg": 0.09,
          "fut_oi_chg_pct": -0.64,
          "oi_sign": -1,
          "avg_del": 0.715,
          "peak_del": 0.8,
          "del_chg": 0.17,
          "avg_vol": 0.705,
          "call_oi_growth_pct": -12.53,
          "put_oi_growth_pct": -0.81,
          "opt_oi_growth_pct": -7.79,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -2.58,
          "pcr": 1.73,
          "pcr_chg_1d": -0.35,
          "fut_oi": 2826500,
          "oi_chg_pct": 3.9,
          "delivery": 1.02,
          "volume": 1.08,
          "call_oi": 229000,
          "put_oi": 395750
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.62,
          "pcr": 0.68,
          "pcr_chg_1d": -0.15,
          "fut_oi": 3196750,
          "oi_chg_pct": 1.73,
          "delivery": 0.63,
          "volume": 0.7,
          "call_oi": 634250,
          "put_oi": 431000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.48,
          "pcr": 0.77,
          "pcr_chg_1d": 0.09,
          "fut_oi": 3176250,
          "oi_chg_pct": -0.64,
          "delivery": 0.8,
          "volume": 0.71,
          "call_oi": 554750,
          "put_oi": 427500
        }
      ]
    },
    {
      "symbol": "TITAN",
      "rank": 109,
      "days_available": 3,
      "latest_score": 5.0,
      "latest_tier": "TIER 3 \u2014 BUILDING LONG",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -6.5,
          5.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.115,
        "pcr_first": 1.03,
        "pcr_last": 0.8,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -0.23,
        "cumulative_price_chg_pct_window": 0.28,
        "persistence_score": 1.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -6.5,
          "signals": [
            "PCR 0.74 neutral",
            "PCR easing -0.04"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": -1.17,
          "price_sign": -1,
          "pcr_d1": 1.03,
          "pcr_d2": 0.74,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 1.4,
          "oi_sign": 1,
          "avg_del": 0.685,
          "peak_del": 0.85,
          "del_chg": 0.33,
          "avg_vol": 0.67,
          "call_oi_growth_pct": 234.08,
          "put_oi_growth_pct": 141.72,
          "opt_oi_growth_pct": 187.31,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 5.0,
          "signals": [
            "PCR 0.80 neutral-to-bullish",
            "PCR rising +0.06"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 1.47,
          "price_sign": 1,
          "pcr_d1": 0.74,
          "pcr_d2": 0.8,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": -1.61,
          "oi_sign": -1,
          "avg_del": 0.84,
          "peak_del": 0.85,
          "del_chg": -0.02,
          "avg_vol": 0.775,
          "call_oi_growth_pct": 3.65,
          "put_oi_growth_pct": 11.43,
          "opt_oi_growth_pct": 6.96,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.89,
          "pcr": 1.03,
          "pcr_chg_1d": -0.02,
          "fut_oi": 9675575,
          "oi_chg_pct": 0.99,
          "delivery": 0.52,
          "volume": 0.59,
          "call_oi": 982275,
          "put_oi": 1007650
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.17,
          "pcr": 0.74,
          "pcr_chg_1d": -0.04,
          "fut_oi": 9811375,
          "oi_chg_pct": -0.29,
          "delivery": 0.85,
          "volume": 0.75,
          "call_oi": 3281600,
          "put_oi": 2435650
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.47,
          "pcr": 0.8,
          "pcr_chg_1d": 0.06,
          "fut_oi": 9653000,
          "oi_chg_pct": -1.61,
          "delivery": 0.83,
          "volume": 0.8,
          "call_oi": 3401300,
          "put_oi": 2714075
        }
      ]
    },
    {
      "symbol": "CDSL",
      "rank": 110,
      "days_available": 3,
      "latest_score": 4.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -6.0,
          4.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.13,
        "pcr_first": 1.09,
        "pcr_last": 0.83,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 13.62,
        "cumulative_price_chg_pct_window": 1.24,
        "persistence_score": 1.0,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -6.0,
          "signals": [
            "PCR 0.80 neutral-to-bullish",
            "\u26a0 NEW SHORTS: FutOI +17.6% + Price -0.6%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.63,
          "price_sign": -1,
          "pcr_d1": 1.09,
          "pcr_d2": 0.8,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": 17.6,
          "oi_sign": 1,
          "avg_del": 0.755,
          "peak_del": 0.9,
          "del_chg": 0.29,
          "avg_vol": 0.955,
          "call_oi_growth_pct": 67.84,
          "put_oi_growth_pct": 23.59,
          "opt_oi_growth_pct": 44.73,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.5,
          "signals": [
            "PCR 0.83 neutral-to-bullish"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.88,
          "price_sign": 1,
          "pcr_d1": 0.8,
          "pcr_d2": 0.83,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -3.39,
          "oi_sign": -1,
          "avg_del": 0.99,
          "peak_del": 1.08,
          "del_chg": 0.18,
          "avg_vol": 1.03,
          "call_oi_growth_pct": 0.68,
          "put_oi_growth_pct": 3.8,
          "opt_oi_growth_pct": 2.07,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 5.66,
          "pcr": 1.09,
          "pcr_chg_1d": -0.05,
          "fut_oi": 10234350,
          "oi_chg_pct": -0.91,
          "delivery": 0.61,
          "volume": 0.82,
          "call_oi": 2590650,
          "put_oi": 2831475
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.63,
          "pcr": 0.8,
          "pcr_chg_1d": -0.03,
          "fut_oi": 12035550,
          "oi_chg_pct": 3.52,
          "delivery": 0.9,
          "volume": 1.09,
          "call_oi": 4348150,
          "put_oi": 3499325
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.88,
          "pcr": 0.83,
          "pcr_chg_1d": 0.03,
          "fut_oi": 11628000,
          "oi_chg_pct": -3.39,
          "delivery": 1.08,
          "volume": 0.97,
          "call_oi": 4377600,
          "put_oi": 3632325
        }
      ]
    },
    {
      "symbol": "HDFCLIFE",
      "rank": 111,
      "days_available": 3,
      "latest_score": 4.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -9.0,
          4.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.0,
        "pcr_first": 0.7,
        "pcr_last": 0.7,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 2.94,
        "cumulative_price_chg_pct_window": 0.97,
        "persistence_score": 0.0,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -9.0,
          "signals": [
            "PCR 0.62 neutral",
            "\u26a0 NEW SHORTS: FutOI +6.7% + Price -1.2%",
            "Del 1.49x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_short",
          "price_chg_pct": -1.19,
          "price_sign": -1,
          "pcr_d1": 0.7,
          "pcr_d2": 0.62,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 6.74,
          "oi_sign": 1,
          "avg_del": 1.485,
          "peak_del": 2.29,
          "del_chg": -1.61,
          "avg_vol": 1.47,
          "call_oi_growth_pct": 56.8,
          "put_oi_growth_pct": 38.87,
          "opt_oi_growth_pct": 49.4,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.5,
          "signals": [
            "PCR 0.70 neutral",
            "PCR rising +0.08"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 2.19,
          "price_sign": 1,
          "pcr_d1": 0.62,
          "pcr_d2": 0.7,
          "pcr_chg": 0.08,
          "fut_oi_chg_pct": -3.56,
          "oi_sign": -1,
          "avg_del": 0.81,
          "peak_del": 0.94,
          "del_chg": 0.26,
          "avg_vol": 0.795,
          "call_oi_growth_pct": -1.2,
          "put_oi_growth_pct": 11.38,
          "opt_oi_growth_pct": 3.63,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -2.99,
          "pcr": 0.7,
          "pcr_chg_1d": -0.14,
          "fut_oi": 42851600,
          "oi_chg_pct": 11.19,
          "delivery": 2.29,
          "volume": 2.28,
          "call_oi": 7117000,
          "put_oi": 5002800
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.19,
          "pcr": 0.62,
          "pcr_chg_1d": 0.03,
          "fut_oi": 45740200,
          "oi_chg_pct": 1.22,
          "delivery": 0.68,
          "volume": 0.66,
          "call_oi": 11159500,
          "put_oi": 6947600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.19,
          "pcr": 0.7,
          "pcr_chg_1d": 0.08,
          "fut_oi": 44113300,
          "oi_chg_pct": -3.56,
          "delivery": 0.94,
          "volume": 0.93,
          "call_oi": 11025300,
          "put_oi": 7738500
        }
      ]
    },
    {
      "symbol": "GODFRYPHLP",
      "rank": 112,
      "days_available": 3,
      "latest_score": 4.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "phase_2_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.5,
          4.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.13,
        "pcr_first": 0.2,
        "pcr_last": 0.46,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 1281.89,
        "cumulative_price_chg_pct_window": 4.79,
        "persistence_score": 4.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 4.5,
          "signals": [
            "PCR 0.50 call writers dominant",
            "PCR collapsing -0.49",
            "\u2605 NEW LONGS: FutOI +724.4% + Price +1.5%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.46,
          "price_sign": 1,
          "pcr_d1": 0.2,
          "pcr_d2": 0.5,
          "pcr_chg": -0.49,
          "fut_oi_chg_pct": 724.41,
          "oi_sign": 1,
          "avg_del": 0.94,
          "peak_del": 1.29,
          "del_chg": 0.7,
          "avg_vol": 0.96,
          "call_oi_growth_pct": 1057.14,
          "put_oi_growth_pct": 2740.0,
          "opt_oi_growth_pct": 1342.37,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.5,
          "signals": [
            "PCR 0.46 call writers dominant",
            "PCR easing -0.04",
            "\u2605 NEW LONGS: FutOI +67.6% + Price +3.3%",
            "Del 1.41x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 3.28,
          "price_sign": 1,
          "pcr_d1": 0.5,
          "pcr_d2": 0.46,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 67.62,
          "oi_sign": 1,
          "avg_del": 1.41,
          "peak_del": 1.53,
          "del_chg": 0.24,
          "avg_vol": 1.65,
          "call_oi_growth_pct": 55.03,
          "put_oi_growth_pct": 42.25,
          "opt_oi_growth_pct": 50.76,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.87,
          "pcr": 0.2,
          "pcr_chg_1d": 0.0,
          "fut_oi": 34925,
          "oi_chg_pct": 0.0,
          "delivery": 0.59,
          "volume": 0.32,
          "call_oi": 13475,
          "put_oi": 2750
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.46,
          "pcr": 0.5,
          "pcr_chg_1d": -0.49,
          "fut_oi": 287925,
          "oi_chg_pct": 25.69,
          "delivery": 1.29,
          "volume": 1.6,
          "call_oi": 155925,
          "put_oi": 78100
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.28,
          "pcr": 0.46,
          "pcr_chg_1d": -0.04,
          "fut_oi": 482625,
          "oi_chg_pct": 67.62,
          "delivery": 1.53,
          "volume": 1.7,
          "call_oi": 241725,
          "put_oi": 111100
        }
      ]
    },
    {
      "symbol": "ANGELONE",
      "rank": 113,
      "days_available": 3,
      "latest_score": 4.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          8.5,
          4.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.01,
        "pcr_first": 0.84,
        "pcr_last": 0.86,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 2.28,
        "cumulative_price_chg_pct_window": 4.99,
        "persistence_score": 5.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 8.5,
          "signals": [
            "PCR 0.82 neutral-to-bullish",
            "PCR easing -0.04",
            "\u2605 NEW LONGS: FutOI +3.3% + Price +5.3%",
            "Del 2.41x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 5.3,
          "price_sign": 1,
          "pcr_d1": 0.84,
          "pcr_d2": 0.82,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 3.34,
          "oi_sign": 1,
          "avg_del": 2.41,
          "peak_del": 3.82,
          "del_chg": 2.82,
          "avg_vol": 2.37,
          "call_oi_growth_pct": 121.53,
          "put_oi_growth_pct": 116.86,
          "opt_oi_growth_pct": 119.4,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.5,
          "signals": [
            "PCR 0.86 approaching bullish zone",
            "PCR rising +0.04"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.29,
          "price_sign": 0,
          "pcr_d1": 0.82,
          "pcr_d2": 0.86,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": -1.03,
          "oi_sign": -1,
          "avg_del": 2.33,
          "peak_del": 3.82,
          "del_chg": -2.98,
          "avg_vol": 2.31,
          "call_oi_growth_pct": 1.76,
          "put_oi_growth_pct": 6.23,
          "opt_oi_growth_pct": 3.78,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 5.74,
          "pcr": 0.84,
          "pcr_chg_1d": -0.34,
          "fut_oi": 23030000,
          "oi_chg_pct": -21.13,
          "delivery": 1.0,
          "volume": 1.26,
          "call_oi": 6222500,
          "put_oi": 5235000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 5.3,
          "pcr": 0.82,
          "pcr_chg_1d": -0.04,
          "fut_oi": 23800000,
          "oi_chg_pct": 5.65,
          "delivery": 3.82,
          "volume": 3.48,
          "call_oi": 13785000,
          "put_oi": 11352500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.29,
          "pcr": 0.86,
          "pcr_chg_1d": 0.04,
          "fut_oi": 23555000,
          "oi_chg_pct": -1.03,
          "delivery": 0.84,
          "volume": 1.14,
          "call_oi": 14027500,
          "put_oi": 12060000
        }
      ]
    },
    {
      "symbol": "SBIN",
      "rank": 114,
      "days_available": 3,
      "latest_score": 4.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -9.5,
          4.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.025,
        "pcr_first": 0.77,
        "pcr_last": 0.72,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 2.42,
        "cumulative_price_chg_pct_window": 0.49,
        "persistence_score": -0.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -9.5,
          "signals": [
            "PCR 0.65 neutral",
            "PCR easing -0.06",
            "\u26a0 NEW SHORTS: FutOI +3.4% + Price -1.9%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.93,
          "price_sign": -1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.65,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": 3.4,
          "oi_sign": 1,
          "avg_del": 0.94,
          "peak_del": 1.14,
          "del_chg": 0.4,
          "avg_vol": 1.005,
          "call_oi_growth_pct": 62.88,
          "put_oi_growth_pct": 36.17,
          "opt_oi_growth_pct": 51.22,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.5,
          "signals": [
            "PCR 0.72 neutral",
            "PCR rising +0.07",
            "Del 1.02x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 2.47,
          "price_sign": 1,
          "pcr_d1": 0.65,
          "pcr_d2": 0.72,
          "pcr_chg": 0.07,
          "fut_oi_chg_pct": -0.95,
          "oi_sign": -1,
          "avg_del": 1.025,
          "peak_del": 1.14,
          "del_chg": -0.23,
          "avg_vol": 0.985,
          "call_oi_growth_pct": -3.91,
          "put_oi_growth_pct": 7.04,
          "opt_oi_growth_pct": 0.39,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.92,
          "pcr": 0.77,
          "pcr_chg_1d": -0.03,
          "fut_oi": 79499250,
          "oi_chg_pct": -1.71,
          "delivery": 0.74,
          "volume": 0.83,
          "call_oi": 25918500,
          "put_oi": 20066250
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.93,
          "pcr": 0.65,
          "pcr_chg_1d": -0.06,
          "fut_oi": 82201500,
          "oi_chg_pct": 2.93,
          "delivery": 1.14,
          "volume": 1.18,
          "call_oi": 42215250,
          "put_oi": 27324750
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.47,
          "pcr": 0.72,
          "pcr_chg_1d": 0.07,
          "fut_oi": 81423000,
          "oi_chg_pct": -0.95,
          "delivery": 0.91,
          "volume": 0.79,
          "call_oi": 40565250,
          "put_oi": 29249250
        }
      ]
    },
    {
      "symbol": "MANAPPURAM",
      "rank": 115,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -5.5,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.115,
        "pcr_first": 0.91,
        "pcr_last": 0.68,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 2.35,
        "cumulative_price_chg_pct_window": -0.72,
        "persistence_score": 0.83,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -5.5,
          "signals": [
            "PCR 0.67 neutral"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -2.45,
          "price_sign": -1,
          "pcr_d1": 0.91,
          "pcr_d2": 0.67,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": 0.86,
          "oi_sign": 1,
          "avg_del": 0.99,
          "peak_del": 1.04,
          "del_chg": 0.1,
          "avg_vol": 0.86,
          "call_oi_growth_pct": 40.06,
          "put_oi_growth_pct": 3.77,
          "opt_oi_growth_pct": 22.79,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.68 neutral"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.77,
          "price_sign": 1,
          "pcr_d1": 0.67,
          "pcr_d2": 0.68,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 1.48,
          "oi_sign": 1,
          "avg_del": 0.975,
          "peak_del": 1.04,
          "del_chg": -0.13,
          "avg_vol": 0.865,
          "call_oi_growth_pct": 2.46,
          "put_oi_growth_pct": 3.79,
          "opt_oi_growth_pct": 3.0,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.71,
          "pcr": 0.91,
          "pcr_chg_1d": -0.02,
          "fut_oi": 51360000,
          "oi_chg_pct": -2.15,
          "delivery": 0.94,
          "volume": 0.79,
          "call_oi": 9570000,
          "put_oi": 8685000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.45,
          "pcr": 0.67,
          "pcr_chg_1d": 0.0,
          "fut_oi": 51804000,
          "oi_chg_pct": 1.2,
          "delivery": 1.04,
          "volume": 0.93,
          "call_oi": 13404000,
          "put_oi": 9012000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.77,
          "pcr": 0.68,
          "pcr_chg_1d": 0.01,
          "fut_oi": 52569000,
          "oi_chg_pct": 1.48,
          "delivery": 0.91,
          "volume": 0.8,
          "call_oi": 13734000,
          "put_oi": 9354000
        }
      ]
    },
    {
      "symbol": "PNB",
      "rank": 116,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -7.0,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.05,
        "pcr_first": 0.87,
        "pcr_last": 0.77,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 2.39,
        "cumulative_price_chg_pct_window": 0.6,
        "persistence_score": 0.33,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -7.0,
          "signals": [
            "PCR 0.76 neutral-to-bullish",
            "\u26a0 NEW SHORTS: FutOI +3.2% + Price -1.4%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.39,
          "price_sign": -1,
          "pcr_d1": 0.87,
          "pcr_d2": 0.76,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": 3.17,
          "oi_sign": 1,
          "avg_del": 0.79,
          "peak_del": 0.95,
          "del_chg": 0.32,
          "avg_vol": 0.85,
          "call_oi_growth_pct": 52.62,
          "put_oi_growth_pct": 34.09,
          "opt_oi_growth_pct": 44.0,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.77 neutral-to-bullish",
            "Del 1.00x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 2.02,
          "price_sign": 1,
          "pcr_d1": 0.76,
          "pcr_d2": 0.77,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": -0.75,
          "oi_sign": -1,
          "avg_del": 1.0,
          "peak_del": 1.05,
          "del_chg": 0.1,
          "avg_vol": 0.84,
          "call_oi_growth_pct": 1.95,
          "put_oi_growth_pct": 2.92,
          "opt_oi_growth_pct": 2.37,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.42,
          "pcr": 0.87,
          "pcr_chg_1d": -0.02,
          "fut_oi": 276840000,
          "oi_chg_pct": -1.22,
          "delivery": 0.63,
          "volume": 0.77,
          "call_oi": 54368000,
          "put_oi": 47240000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.39,
          "pcr": 0.76,
          "pcr_chg_1d": -0.03,
          "fut_oi": 285616000,
          "oi_chg_pct": 2.12,
          "delivery": 0.95,
          "volume": 0.93,
          "call_oi": 82976000,
          "put_oi": 63344000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.02,
          "pcr": 0.77,
          "pcr_chg_1d": 0.01,
          "fut_oi": 283464000,
          "oi_chg_pct": -0.75,
          "delivery": 1.05,
          "volume": 0.75,
          "call_oi": 84592000,
          "put_oi": 65192000
        }
      ]
    },
    {
      "symbol": "HINDALCO",
      "rank": 117,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          8.0,
          4.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.03,
        "pcr_first": 0.65,
        "pcr_last": 0.71,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -4.37,
        "cumulative_price_chg_pct_window": 4.23,
        "persistence_score": 5.33,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 8.0,
          "signals": [
            "PCR 0.72 neutral",
            "PCR surging +0.10",
            "Del 1.04x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 3.56,
          "price_sign": 1,
          "pcr_d1": 0.65,
          "pcr_d2": 0.72,
          "pcr_chg": 0.1,
          "fut_oi_chg_pct": -4.59,
          "oi_sign": -1,
          "avg_del": 1.04,
          "peak_del": 1.17,
          "del_chg": -0.26,
          "avg_vol": 1.105,
          "call_oi_growth_pct": 56.36,
          "put_oi_growth_pct": 72.63,
          "opt_oi_growth_pct": 62.77,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.71 neutral"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.65,
          "price_sign": 1,
          "pcr_d1": 0.72,
          "pcr_d2": 0.71,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": 0.23,
          "oi_sign": 1,
          "avg_del": 0.87,
          "peak_del": 0.91,
          "del_chg": -0.08,
          "avg_vol": 0.92,
          "call_oi_growth_pct": 0.68,
          "put_oi_growth_pct": -0.78,
          "opt_oi_growth_pct": 0.07,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.28,
          "pcr": 0.65,
          "pcr_chg_1d": 0.0,
          "fut_oi": 40085500,
          "oi_chg_pct": -13.7,
          "delivery": 1.17,
          "volume": 1.07,
          "call_oi": 8314600,
          "put_oi": 5403300
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 3.56,
          "pcr": 0.72,
          "pcr_chg_1d": 0.1,
          "fut_oi": 38245900,
          "oi_chg_pct": 1.16,
          "delivery": 0.91,
          "volume": 1.14,
          "call_oi": 13001100,
          "put_oi": 9327500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.65,
          "pcr": 0.71,
          "pcr_chg_1d": -0.01,
          "fut_oi": 38332700,
          "oi_chg_pct": 0.23,
          "delivery": 0.83,
          "volume": 0.7,
          "call_oi": 13090000,
          "put_oi": 9254700
        }
      ]
    },
    {
      "symbol": "IRFC",
      "rank": 118,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -3.5,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.165,
        "pcr_first": 1.03,
        "pcr_last": 0.7,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -3.06,
        "cumulative_price_chg_pct_window": 1.37,
        "persistence_score": 1.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -3.5,
          "signals": [
            "PCR 0.74 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.42,
          "price_sign": -1,
          "pcr_d1": 1.03,
          "pcr_d2": 0.74,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -4.86,
          "oi_sign": -1,
          "avg_del": 0.73,
          "peak_del": 0.77,
          "del_chg": 0.08,
          "avg_vol": 0.905,
          "call_oi_growth_pct": 63.8,
          "put_oi_growth_pct": 18.32,
          "opt_oi_growth_pct": 40.76,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.70 neutral",
            "PCR easing -0.04",
            "Del 1.02x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.8,
          "price_sign": 1,
          "pcr_d1": 0.74,
          "pcr_d2": 0.7,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 1.89,
          "oi_sign": 1,
          "avg_del": 1.015,
          "peak_del": 1.26,
          "del_chg": 0.49,
          "avg_vol": 0.985,
          "call_oi_growth_pct": 17.8,
          "put_oi_growth_pct": 11.03,
          "opt_oi_growth_pct": 14.92,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 5.46,
          "pcr": 1.03,
          "pcr_chg_1d": 0.15,
          "fut_oi": 56355000,
          "oi_chg_pct": -2.13,
          "delivery": 0.69,
          "volume": 0.97,
          "call_oi": 20510500,
          "put_oi": 21046000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.42,
          "pcr": 0.74,
          "pcr_chg_1d": 0.03,
          "fut_oi": 53613750,
          "oi_chg_pct": 1.07,
          "delivery": 0.77,
          "volume": 0.84,
          "call_oi": 33596250,
          "put_oi": 24900750
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.8,
          "pcr": 0.7,
          "pcr_chg_1d": -0.04,
          "fut_oi": 54629500,
          "oi_chg_pct": 1.89,
          "delivery": 1.26,
          "volume": 1.13,
          "call_oi": 39576000,
          "put_oi": 27646250
        }
      ]
    },
    {
      "symbol": "COLPAL",
      "rank": 119,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.0,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.06,
        "pcr_first": 0.8,
        "pcr_last": 0.68,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 3.48,
        "cumulative_price_chg_pct_window": 1.68,
        "persistence_score": 2.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -2.0,
          "signals": [
            "PCR 0.69 neutral",
            "PCR rising +0.06"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.02,
          "price_sign": 0,
          "pcr_d1": 0.8,
          "pcr_d2": 0.69,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": 5.3,
          "oi_sign": 1,
          "avg_del": 1.29,
          "peak_del": 1.76,
          "del_chg": 0.94,
          "avg_vol": 1.225,
          "call_oi_growth_pct": 49.81,
          "put_oi_growth_pct": 29.33,
          "opt_oi_growth_pct": 40.72,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.68 neutral",
            "Del 1.52x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.7,
          "price_sign": 1,
          "pcr_d1": 0.69,
          "pcr_d2": 0.68,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -1.73,
          "oi_sign": -1,
          "avg_del": 1.525,
          "peak_del": 1.76,
          "del_chg": -0.47,
          "avg_vol": 1.4,
          "call_oi_growth_pct": -4.58,
          "put_oi_growth_pct": -6.0,
          "opt_oi_growth_pct": -5.16,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.73,
          "pcr": 0.8,
          "pcr_chg_1d": -0.02,
          "fut_oi": 6309000,
          "oi_chg_pct": 0.25,
          "delivery": 0.82,
          "volume": 0.75,
          "call_oi": 1075050,
          "put_oi": 858375
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.02,
          "pcr": 0.69,
          "pcr_chg_1d": 0.06,
          "fut_oi": 6643575,
          "oi_chg_pct": 1.46,
          "delivery": 1.76,
          "volume": 1.7,
          "call_oi": 1610550,
          "put_oi": 1110150
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.7,
          "pcr": 0.68,
          "pcr_chg_1d": -0.01,
          "fut_oi": 6528825,
          "oi_chg_pct": -1.73,
          "delivery": 1.29,
          "volume": 1.1,
          "call_oi": 1536750,
          "put_oi": 1043550
        }
      ]
    },
    {
      "symbol": "BAJAJFINSV",
      "rank": 120,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.5,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.065,
        "pcr_first": 0.95,
        "pcr_last": 1.08,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 3.16,
        "cumulative_price_chg_pct_window": 1.38,
        "persistence_score": 3.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 1.5,
          "signals": [
            "PCR 1.10 ABOVE 1.0 \u2014 put writers dominant",
            "PCR surging +0.09",
            "\u26a0 NEW SHORTS: FutOI +4.0% + Price -0.9%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.95,
          "price_sign": -1,
          "pcr_d1": 0.95,
          "pcr_d2": 1.1,
          "pcr_chg": 0.09,
          "fut_oi_chg_pct": 4.03,
          "oi_sign": 1,
          "avg_del": 0.78,
          "peak_del": 0.86,
          "del_chg": -0.16,
          "avg_vol": 0.755,
          "call_oi_growth_pct": 45.88,
          "put_oi_growth_pct": 68.58,
          "opt_oi_growth_pct": 56.95,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 1.08 ABOVE 1.0 \u2014 put writers dominant"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 2.35,
          "price_sign": 1,
          "pcr_d1": 1.1,
          "pcr_d2": 1.08,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": -0.84,
          "oi_sign": -1,
          "avg_del": 0.58,
          "peak_del": 0.7,
          "del_chg": -0.24,
          "avg_vol": 0.62,
          "call_oi_growth_pct": 3.14,
          "put_oi_growth_pct": 0.84,
          "opt_oi_growth_pct": 1.94,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.93,
          "pcr": 0.95,
          "pcr_chg_1d": 0.0,
          "fut_oi": 11296750,
          "oi_chg_pct": 1.41,
          "delivery": 0.86,
          "volume": 0.77,
          "call_oi": 2091000,
          "put_oi": 1990750
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.95,
          "pcr": 1.1,
          "pcr_chg_1d": 0.09,
          "fut_oi": 11751750,
          "oi_chg_pct": 1.07,
          "delivery": 0.7,
          "volume": 0.74,
          "call_oi": 3050250,
          "put_oi": 3356000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.35,
          "pcr": 1.08,
          "pcr_chg_1d": -0.02,
          "fut_oi": 11653500,
          "oi_chg_pct": -0.84,
          "delivery": 0.46,
          "volume": 0.5,
          "call_oi": 3146000,
          "put_oi": 3384250
        }
      ]
    },
    {
      "symbol": "AXISBANK",
      "rank": 121,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -1.5,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.06,
        "pcr_first": 0.81,
        "pcr_last": 0.93,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -4.04,
        "cumulative_price_chg_pct_window": 1.33,
        "persistence_score": 2.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -1.5,
          "signals": [
            "PCR 0.90 approaching bullish zone",
            "PCR collapsing -0.10"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -1.09,
          "price_sign": -1,
          "pcr_d1": 0.81,
          "pcr_d2": 0.9,
          "pcr_chg": -0.1,
          "fut_oi_chg_pct": -2.69,
          "oi_sign": -1,
          "avg_del": 0.55,
          "peak_del": 0.59,
          "del_chg": -0.08,
          "avg_vol": 0.665,
          "call_oi_growth_pct": 81.74,
          "put_oi_growth_pct": 101.41,
          "opt_oi_growth_pct": 90.53,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.93 approaching bullish zone"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 2.45,
          "price_sign": 1,
          "pcr_d1": 0.9,
          "pcr_d2": 0.93,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -1.38,
          "oi_sign": -1,
          "avg_del": 0.655,
          "peak_del": 0.8,
          "del_chg": 0.29,
          "avg_vol": 0.71,
          "call_oi_growth_pct": 9.78,
          "put_oi_growth_pct": 13.9,
          "opt_oi_growth_pct": 11.73,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.74,
          "pcr": 0.81,
          "pcr_chg_1d": 0.02,
          "fut_oi": 70797500,
          "oi_chg_pct": 1.26,
          "delivery": 0.59,
          "volume": 0.63,
          "call_oi": 6778750,
          "put_oi": 5481250
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.09,
          "pcr": 0.9,
          "pcr_chg_1d": -0.1,
          "fut_oi": 68890000,
          "oi_chg_pct": -0.03,
          "delivery": 0.51,
          "volume": 0.7,
          "call_oi": 12319375,
          "put_oi": 11040000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.45,
          "pcr": 0.93,
          "pcr_chg_1d": 0.03,
          "fut_oi": 67940000,
          "oi_chg_pct": -1.38,
          "delivery": 0.8,
          "volume": 0.72,
          "call_oi": 13524375,
          "put_oi": 12574375
        }
      ]
    },
    {
      "symbol": "ZYDUSLIFE",
      "rank": 122,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          5.5,
          4.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.02,
        "pcr_first": 0.77,
        "pcr_last": 0.81,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -4.9,
        "cumulative_price_chg_pct_window": 2.68,
        "persistence_score": 4.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 5.5,
          "signals": [
            "PCR 0.78 neutral-to-bullish",
            "PCR easing -0.08",
            "Del 1.01x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.2,
          "price_sign": 1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.78,
          "pcr_chg": -0.08,
          "fut_oi_chg_pct": -3.42,
          "oi_sign": -1,
          "avg_del": 1.01,
          "peak_del": 1.16,
          "del_chg": 0.3,
          "avg_vol": 0.985,
          "call_oi_growth_pct": 35.12,
          "put_oi_growth_pct": 36.8,
          "opt_oi_growth_pct": 35.85,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.81 neutral-to-bullish",
            "Del 1.19x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.46,
          "price_sign": 1,
          "pcr_d1": 0.78,
          "pcr_d2": 0.81,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -1.54,
          "oi_sign": -1,
          "avg_del": 1.19,
          "peak_del": 1.22,
          "del_chg": 0.06,
          "avg_vol": 0.89,
          "call_oi_growth_pct": -1.03,
          "put_oi_growth_pct": 1.93,
          "opt_oi_growth_pct": 0.27,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.92,
          "pcr": 0.77,
          "pcr_chg_1d": -0.25,
          "fut_oi": 9347400,
          "oi_chg_pct": 4.15,
          "delivery": 0.86,
          "volume": 1.03,
          "call_oi": 1935000,
          "put_oi": 1496700
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.2,
          "pcr": 0.78,
          "pcr_chg_1d": -0.08,
          "fut_oi": 9027900,
          "oi_chg_pct": -1.77,
          "delivery": 1.16,
          "volume": 0.94,
          "call_oi": 2614500,
          "put_oi": 2047500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.46,
          "pcr": 0.81,
          "pcr_chg_1d": 0.03,
          "fut_oi": 8889300,
          "oi_chg_pct": -1.54,
          "delivery": 1.22,
          "volume": 0.84,
          "call_oi": 2587500,
          "put_oi": 2087100
        }
      ]
    },
    {
      "symbol": "HINDZINC",
      "rank": 123,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          2.5,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.04,
        "pcr_first": 0.77,
        "pcr_last": 0.85,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -10.51,
        "cumulative_price_chg_pct_window": 0.94,
        "persistence_score": 3.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 2.5,
          "signals": [
            "PCR 0.82 neutral-to-bullish"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.15,
          "price_sign": 0,
          "pcr_d1": 0.77,
          "pcr_d2": 0.82,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": -8.99,
          "oi_sign": -1,
          "avg_del": 0.64,
          "peak_del": 0.77,
          "del_chg": -0.26,
          "avg_vol": 0.665,
          "call_oi_growth_pct": 15.08,
          "put_oi_growth_pct": 22.34,
          "opt_oi_growth_pct": 18.25,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.85 approaching bullish zone"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.09,
          "price_sign": 1,
          "pcr_d1": 0.82,
          "pcr_d2": 0.85,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -1.67,
          "oi_sign": -1,
          "avg_del": 0.665,
          "peak_del": 0.82,
          "del_chg": 0.31,
          "avg_vol": 0.65,
          "call_oi_growth_pct": 0.26,
          "put_oi_growth_pct": 3.38,
          "opt_oi_growth_pct": 1.67,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.44,
          "pcr": 0.77,
          "pcr_chg_1d": -0.01,
          "fut_oi": 41324150,
          "oi_chg_pct": 2.23,
          "delivery": 0.77,
          "volume": 0.8,
          "call_oi": 13858425,
          "put_oi": 10727325
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.15,
          "pcr": 0.82,
          "pcr_chg_1d": 0.01,
          "fut_oi": 37607500,
          "oi_chg_pct": -1.69,
          "delivery": 0.51,
          "volume": 0.53,
          "call_oi": 15948275,
          "put_oi": 13123425
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.09,
          "pcr": 0.85,
          "pcr_chg_1d": 0.03,
          "fut_oi": 36980300,
          "oi_chg_pct": -1.67,
          "delivery": 0.82,
          "volume": 0.77,
          "call_oi": 15989925,
          "put_oi": 13566875
        }
      ]
    },
    {
      "symbol": "NMDC",
      "rank": 124,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.5,
          4.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.01,
        "pcr_first": 0.6,
        "pcr_last": 0.62,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.01,
        "cumulative_price_chg_pct_window": 2.61,
        "persistence_score": 4.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 4.5,
          "signals": [
            "PCR 0.61 neutral",
            "Del 1.16x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.85,
          "price_sign": 1,
          "pcr_d1": 0.6,
          "pcr_d2": 0.61,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": -0.18,
          "oi_sign": -1,
          "avg_del": 1.155,
          "peak_del": 1.36,
          "del_chg": -0.41,
          "avg_vol": 0.975,
          "call_oi_growth_pct": 61.2,
          "put_oi_growth_pct": 65.38,
          "opt_oi_growth_pct": 62.77,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.62 neutral"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.75,
          "price_sign": 1,
          "pcr_d1": 0.61,
          "pcr_d2": 0.62,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 0.19,
          "oi_sign": 1,
          "avg_del": 0.935,
          "peak_del": 0.95,
          "del_chg": -0.03,
          "avg_vol": 0.845,
          "call_oi_growth_pct": 0.24,
          "put_oi_growth_pct": 0.52,
          "opt_oi_growth_pct": 0.35,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.49,
          "pcr": 0.6,
          "pcr_chg_1d": -0.05,
          "fut_oi": 332093250,
          "oi_chg_pct": 0.46,
          "delivery": 1.36,
          "volume": 1.08,
          "call_oi": 41613750,
          "put_oi": 24921000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.85,
          "pcr": 0.61,
          "pcr_chg_1d": 0.01,
          "fut_oi": 331506000,
          "oi_chg_pct": 0.86,
          "delivery": 0.95,
          "volume": 0.87,
          "call_oi": 67081500,
          "put_oi": 41215500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.75,
          "pcr": 0.62,
          "pcr_chg_1d": 0.01,
          "fut_oi": 332140500,
          "oi_chg_pct": 0.19,
          "delivery": 0.92,
          "volume": 0.82,
          "call_oi": 67243500,
          "put_oi": 41431500
        }
      ]
    },
    {
      "symbol": "IDFCFIRSTB",
      "rank": 125,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -0.5,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.02,
        "pcr_first": 0.84,
        "pcr_last": 0.88,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -3.95,
        "cumulative_price_chg_pct_window": 0.51,
        "persistence_score": 2.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -0.5,
          "signals": [
            "PCR 0.84 neutral-to-bullish"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.9,
          "price_sign": -1,
          "pcr_d1": 0.84,
          "pcr_d2": 0.84,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -2.63,
          "oi_sign": -1,
          "avg_del": 0.625,
          "peak_del": 0.73,
          "del_chg": -0.21,
          "avg_vol": 0.695,
          "call_oi_growth_pct": 17.28,
          "put_oi_growth_pct": 17.58,
          "opt_oi_growth_pct": 17.42,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.88 approaching bullish zone",
            "PCR rising +0.04"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.42,
          "price_sign": 1,
          "pcr_d1": 0.84,
          "pcr_d2": 0.88,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": -1.35,
          "oi_sign": -1,
          "avg_del": 0.555,
          "peak_del": 0.59,
          "del_chg": 0.07,
          "avg_vol": 0.635,
          "call_oi_growth_pct": -0.12,
          "put_oi_growth_pct": 3.87,
          "opt_oi_growth_pct": 1.7,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.26,
          "pcr": 0.84,
          "pcr_chg_1d": -0.1,
          "fut_oi": 426223350,
          "oi_chg_pct": -4.39,
          "delivery": 0.73,
          "volume": 0.79,
          "call_oi": 97127800,
          "put_oi": 81620000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.9,
          "pcr": 0.84,
          "pcr_chg_1d": -0.01,
          "fut_oi": 415000600,
          "oi_chg_pct": 0.65,
          "delivery": 0.52,
          "volume": 0.6,
          "call_oi": 113915550,
          "put_oi": 95968425
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.42,
          "pcr": 0.88,
          "pcr_chg_1d": 0.04,
          "fut_oi": 409398500,
          "oi_chg_pct": -1.35,
          "delivery": 0.59,
          "volume": 0.67,
          "call_oi": 113776425,
          "put_oi": 99678425
        }
      ]
    },
    {
      "symbol": "LT",
      "rank": 126,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -8.0,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.045,
        "pcr_first": 0.89,
        "pcr_last": 0.8,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -4.96,
        "cumulative_price_chg_pct_window": -1.15,
        "persistence_score": 0.0,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -8.0,
          "signals": [
            "PCR 0.74 neutral",
            "PCR collapsing -0.11"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -2.74,
          "price_sign": -1,
          "pcr_d1": 0.89,
          "pcr_d2": 0.74,
          "pcr_chg": -0.11,
          "fut_oi_chg_pct": -3.04,
          "oi_sign": -1,
          "avg_del": 0.865,
          "peak_del": 0.93,
          "del_chg": 0.13,
          "avg_vol": 0.92,
          "call_oi_growth_pct": 52.78,
          "put_oi_growth_pct": 26.44,
          "opt_oi_growth_pct": 40.35,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.80 neutral-to-bullish",
            "PCR rising +0.06"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 1.63,
          "price_sign": 1,
          "pcr_d1": 0.74,
          "pcr_d2": 0.8,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": -1.98,
          "oi_sign": -1,
          "avg_del": 0.785,
          "peak_del": 0.93,
          "del_chg": -0.29,
          "avg_vol": 0.815,
          "call_oi_growth_pct": -3.27,
          "put_oi_growth_pct": 4.14,
          "opt_oi_growth_pct": -0.12,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.95,
          "pcr": 0.89,
          "pcr_chg_1d": -0.06,
          "fut_oi": 16194675,
          "oi_chg_pct": -0.39,
          "delivery": 0.8,
          "volume": 0.84,
          "call_oi": 5426925,
          "put_oi": 4846450
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.74,
          "pcr": 0.74,
          "pcr_chg_1d": -0.11,
          "fut_oi": 15702925,
          "oi_chg_pct": 3.2,
          "delivery": 0.93,
          "volume": 1.0,
          "call_oi": 8291150,
          "put_oi": 6127975
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.63,
          "pcr": 0.8,
          "pcr_chg_1d": 0.06,
          "fut_oi": 15391425,
          "oi_chg_pct": -1.98,
          "delivery": 0.64,
          "volume": 0.63,
          "call_oi": 8019725,
          "put_oi": 6381725
        }
      ]
    },
    {
      "symbol": "GRASIM",
      "rank": 127,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.5,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.06,
        "pcr_first": 0.94,
        "pcr_last": 0.82,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -2.43,
        "cumulative_price_chg_pct_window": -0.49,
        "persistence_score": 1.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -4.5,
          "signals": [
            "PCR 0.73 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.57,
          "price_sign": -1,
          "pcr_d1": 0.94,
          "pcr_d2": 0.73,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -1.92,
          "oi_sign": -1,
          "avg_del": 0.815,
          "peak_del": 1.32,
          "del_chg": 1.01,
          "avg_vol": 0.75,
          "call_oi_growth_pct": 217.15,
          "put_oi_growth_pct": 146.62,
          "opt_oi_growth_pct": 182.96,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.82 neutral-to-bullish",
            "PCR surging +0.09"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 0.08,
          "price_sign": 0,
          "pcr_d1": 0.73,
          "pcr_d2": 0.82,
          "pcr_chg": 0.09,
          "fut_oi_chg_pct": -0.52,
          "oi_sign": -1,
          "avg_del": 1.14,
          "peak_del": 1.32,
          "del_chg": -0.36,
          "avg_vol": 1.03,
          "call_oi_growth_pct": -7.61,
          "put_oi_growth_pct": 3.62,
          "opt_oi_growth_pct": -2.86,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.37,
          "pcr": 0.94,
          "pcr_chg_1d": -0.58,
          "fut_oi": 14370000,
          "oi_chg_pct": -0.02,
          "delivery": 0.31,
          "volume": 0.32,
          "call_oi": 526250,
          "put_oi": 495000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.57,
          "pcr": 0.73,
          "pcr_chg_1d": -0.01,
          "fut_oi": 14093750,
          "oi_chg_pct": -0.74,
          "delivery": 1.32,
          "volume": 1.18,
          "call_oi": 1669000,
          "put_oi": 1220750
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.08,
          "pcr": 0.82,
          "pcr_chg_1d": 0.09,
          "fut_oi": 14020250,
          "oi_chg_pct": -0.52,
          "delivery": 0.96,
          "volume": 0.88,
          "call_oi": 1542000,
          "put_oi": 1265000
        }
      ]
    },
    {
      "symbol": "BANKBARODA",
      "rank": 128,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -0.5,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.0,
        "pcr_first": 0.92,
        "pcr_last": 0.92,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -1.71,
        "cumulative_price_chg_pct_window": 0.08,
        "persistence_score": 2.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -0.5,
          "signals": [
            "PCR 0.93 approaching bullish zone",
            "PCR easing -0.04"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.63,
          "price_sign": -1,
          "pcr_d1": 0.92,
          "pcr_d2": 0.93,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": -0.18,
          "oi_sign": -1,
          "avg_del": 0.94,
          "peak_del": 1.12,
          "del_chg": 0.36,
          "avg_vol": 0.89,
          "call_oi_growth_pct": 30.33,
          "put_oi_growth_pct": 31.27,
          "opt_oi_growth_pct": 30.78,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.92 approaching bullish zone"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.71,
          "price_sign": 1,
          "pcr_d1": 0.93,
          "pcr_d2": 0.92,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -1.53,
          "oi_sign": -1,
          "avg_del": 0.905,
          "peak_del": 1.12,
          "del_chg": -0.43,
          "avg_vol": 0.83,
          "call_oi_growth_pct": 2.67,
          "put_oi_growth_pct": 2.13,
          "opt_oi_growth_pct": 2.41,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.79,
          "pcr": 0.92,
          "pcr_chg_1d": -0.05,
          "fut_oi": 106996500,
          "oi_chg_pct": -5.24,
          "delivery": 0.76,
          "volume": 0.81,
          "call_oi": 27328275,
          "put_oi": 25207650
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.63,
          "pcr": 0.93,
          "pcr_chg_1d": -0.04,
          "fut_oi": 106800525,
          "oi_chg_pct": 0.91,
          "delivery": 1.12,
          "volume": 0.97,
          "call_oi": 35617725,
          "put_oi": 33090525
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.71,
          "pcr": 0.92,
          "pcr_chg_1d": -0.01,
          "fut_oi": 105162525,
          "oi_chg_pct": -1.53,
          "delivery": 0.69,
          "volume": 0.69,
          "call_oi": 36568350,
          "put_oi": 33795450
        }
      ]
    },
    {
      "symbol": "DALBHARAT",
      "rank": 129,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.5,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.115,
        "pcr_first": 1.02,
        "pcr_last": 1.25,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 22.15,
        "cumulative_price_chg_pct_window": 2.4,
        "persistence_score": 3.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 1.5,
          "signals": [
            "PCR 1.36 ABOVE 1.0 \u2014 put writers dominant",
            "\u26a0 NEW SHORTS: FutOI +20.7% + Price -0.6%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": -0.62,
          "price_sign": -1,
          "pcr_d1": 1.02,
          "pcr_d2": 1.36,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 20.74,
          "oi_sign": 1,
          "avg_del": 0.405,
          "peak_del": 0.6,
          "del_chg": -0.39,
          "avg_vol": 0.5,
          "call_oi_growth_pct": 126.66,
          "put_oi_growth_pct": 203.65,
          "opt_oi_growth_pct": 165.48,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 1.25 ABOVE 1.0 \u2014 put writers dominant",
            "PCR collapsing -0.11"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 3.04,
          "price_sign": 1,
          "pcr_d1": 1.36,
          "pcr_d2": 1.25,
          "pcr_chg": -0.11,
          "fut_oi_chg_pct": 1.17,
          "oi_sign": 1,
          "avg_del": 0.52,
          "peak_del": 0.83,
          "del_chg": 0.62,
          "avg_vol": 0.55,
          "call_oi_growth_pct": 20.2,
          "put_oi_growth_pct": 10.24,
          "opt_oi_growth_pct": 14.45,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.51,
          "pcr": 1.02,
          "pcr_chg_1d": -0.15,
          "fut_oi": 2122900,
          "oi_chg_pct": 1.26,
          "delivery": 0.6,
          "volume": 0.68,
          "call_oi": 288925,
          "put_oi": 293800
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.62,
          "pcr": 1.36,
          "pcr_chg_1d": -0.02,
          "fut_oi": 2563275,
          "oi_chg_pct": 0.56,
          "delivery": 0.21,
          "volume": 0.32,
          "call_oi": 654875,
          "put_oi": 892125
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.04,
          "pcr": 1.25,
          "pcr_chg_1d": -0.11,
          "fut_oi": 2593175,
          "oi_chg_pct": 1.17,
          "delivery": 0.83,
          "volume": 0.78,
          "call_oi": 787150,
          "put_oi": 983450
        }
      ]
    },
    {
      "symbol": "AUBANK",
      "rank": 130,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.5,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.045,
        "pcr_first": 0.81,
        "pcr_last": 0.9,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -1.54,
        "cumulative_price_chg_pct_window": 1.44,
        "persistence_score": 3.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 1.5,
          "signals": [
            "PCR 0.89 approaching bullish zone",
            "PCR rising +0.06"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.5,
          "price_sign": -1,
          "pcr_d1": 0.81,
          "pcr_d2": 0.89,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": 0.45,
          "oi_sign": 1,
          "avg_del": 0.63,
          "peak_del": 0.7,
          "del_chg": -0.14,
          "avg_vol": 0.66,
          "call_oi_growth_pct": 70.16,
          "put_oi_growth_pct": 87.59,
          "opt_oi_growth_pct": 77.96,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.90 approaching bullish zone"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.95,
          "price_sign": 1,
          "pcr_d1": 0.89,
          "pcr_d2": 0.9,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": -1.98,
          "oi_sign": -1,
          "avg_del": 0.64,
          "peak_del": 0.72,
          "del_chg": 0.16,
          "avg_vol": 0.675,
          "call_oi_growth_pct": 10.64,
          "put_oi_growth_pct": 11.79,
          "opt_oi_growth_pct": 11.18,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.82,
          "pcr": 0.81,
          "pcr_chg_1d": -0.16,
          "fut_oi": 25209000,
          "oi_chg_pct": -0.67,
          "delivery": 0.7,
          "volume": 0.71,
          "call_oi": 3143000,
          "put_oi": 2546000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.5,
          "pcr": 0.89,
          "pcr_chg_1d": 0.06,
          "fut_oi": 25322000,
          "oi_chg_pct": 0.65,
          "delivery": 0.56,
          "volume": 0.61,
          "call_oi": 5348000,
          "put_oi": 4776000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.95,
          "pcr": 0.9,
          "pcr_chg_1d": 0.01,
          "fut_oi": 24820000,
          "oi_chg_pct": -1.98,
          "delivery": 0.72,
          "volume": 0.74,
          "call_oi": 5917000,
          "put_oi": 5339000
        }
      ]
    },
    {
      "symbol": "IDEA",
      "rank": 131,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -8.5,
          4.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.015,
        "pcr_first": 0.59,
        "pcr_last": 0.56,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 2.29,
        "cumulative_price_chg_pct_window": 0.55,
        "persistence_score": -0.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -8.5,
          "signals": [
            "PCR 0.56 neutral",
            "\u26a0 NEW SHORTS: FutOI +2.5% + Price -0.9%",
            "Del 1.23x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -0.87,
          "price_sign": -1,
          "pcr_d1": 0.59,
          "pcr_d2": 0.56,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 2.5,
          "oi_sign": 1,
          "avg_del": 1.23,
          "peak_del": 1.95,
          "del_chg": -1.44,
          "avg_vol": 0.96,
          "call_oi_growth_pct": 25.33,
          "put_oi_growth_pct": 17.85,
          "opt_oi_growth_pct": 22.55,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 0.56 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.43,
          "price_sign": 1,
          "pcr_d1": 0.56,
          "pcr_d2": 0.56,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -0.2,
          "oi_sign": -1,
          "avg_del": 0.755,
          "peak_del": 1.0,
          "del_chg": 0.49,
          "avg_vol": 0.725,
          "call_oi_growth_pct": 4.92,
          "put_oi_growth_pct": 5.65,
          "opt_oi_growth_pct": 5.18,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.29,
          "pcr": 0.59,
          "pcr_chg_1d": -0.03,
          "fut_oi": 6482782500,
          "oi_chg_pct": 0.91,
          "delivery": 1.95,
          "volume": 1.28,
          "call_oi": 1071910575,
          "put_oi": 632696700
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.87,
          "pcr": 0.56,
          "pcr_chg_1d": -0.02,
          "fut_oi": 6645030750,
          "oi_chg_pct": 0.64,
          "delivery": 0.51,
          "volume": 0.64,
          "call_oi": 1343372625,
          "put_oi": 745627200
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.43,
          "pcr": 0.56,
          "pcr_chg_1d": 0.0,
          "fut_oi": 6631450500,
          "oi_chg_pct": -0.2,
          "delivery": 1.0,
          "volume": 0.81,
          "call_oi": 1409487000,
          "put_oi": 787725975
        }
      ]
    },
    {
      "symbol": "TATACONSUM",
      "rank": 132,
      "days_available": 3,
      "latest_score": 4.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          12.0,
          4.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.015,
        "pcr_first": 1.43,
        "pcr_last": 1.46,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 2.79,
        "cumulative_price_chg_pct_window": 2.36,
        "persistence_score": 6.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 12.0,
          "signals": [
            "PCR 1.56 ABOVE 1.0 \u2014 put writers dominant",
            "PCR rising +0.04",
            "\u2605 NEW LONGS: FutOI +5.3% + Price +0.9%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.89,
          "price_sign": 1,
          "pcr_d1": 1.43,
          "pcr_d2": 1.56,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": 5.35,
          "oi_sign": 1,
          "avg_del": 0.975,
          "peak_del": 1.21,
          "del_chg": 0.47,
          "avg_vol": 0.96,
          "call_oi_growth_pct": 70.63,
          "put_oi_growth_pct": 86.48,
          "opt_oi_growth_pct": 79.96,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 4.0,
          "signals": [
            "PCR 1.46 ABOVE 1.0 \u2014 put writers dominant",
            "PCR collapsing -0.10",
            "Del 1.06x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.46,
          "price_sign": 1,
          "pcr_d1": 1.56,
          "pcr_d2": 1.46,
          "pcr_chg": -0.1,
          "fut_oi_chg_pct": -2.43,
          "oi_sign": -1,
          "avg_del": 1.06,
          "peak_del": 1.21,
          "del_chg": -0.3,
          "avg_vol": 0.965,
          "call_oi_growth_pct": 12.74,
          "put_oi_growth_pct": 5.03,
          "opt_oi_growth_pct": 8.04,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.89,
          "pcr": 1.43,
          "pcr_chg_1d": 0.32,
          "fut_oi": 13028950,
          "oi_chg_pct": 1.24,
          "delivery": 0.74,
          "volume": 0.76,
          "call_oi": 799700,
          "put_oi": 1143450
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.89,
          "pcr": 1.56,
          "pcr_chg_1d": 0.04,
          "fut_oi": 13725800,
          "oi_chg_pct": 2.39,
          "delivery": 1.21,
          "volume": 1.16,
          "call_oi": 1364550,
          "put_oi": 2132350
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.46,
          "pcr": 1.46,
          "pcr_chg_1d": -0.1,
          "fut_oi": 13391950,
          "oi_chg_pct": -2.43,
          "delivery": 0.91,
          "volume": 0.77,
          "call_oi": 1538350,
          "put_oi": 2239600
        }
      ]
    },
    {
      "symbol": "JUBLFOOD",
      "rank": 133,
      "days_available": 3,
      "latest_score": 3.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -6.5,
          3.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.015,
        "pcr_first": 0.71,
        "pcr_last": 0.68,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 64.55,
        "cumulative_price_chg_pct_window": 2.13,
        "persistence_score": 0.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -6.5,
          "signals": [
            "PCR 0.66 neutral",
            "\u26a0 NEW SHORTS: FutOI +59.2% + Price -1.8%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -1.81,
          "price_sign": -1,
          "pcr_d1": 0.71,
          "pcr_d2": 0.66,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 59.17,
          "oi_sign": 1,
          "avg_del": 0.63,
          "peak_del": 0.92,
          "del_chg": -0.58,
          "avg_vol": 0.675,
          "call_oi_growth_pct": 166.78,
          "put_oi_growth_pct": 150.51,
          "opt_oi_growth_pct": 160.04,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.5,
          "signals": [
            "PCR 0.68 neutral",
            "\u2605 NEW LONGS: FutOI +3.4% + Price +4.0%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": 4.01,
          "price_sign": 1,
          "pcr_d1": 0.66,
          "pcr_d2": 0.68,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": 3.38,
          "oi_sign": 1,
          "avg_del": 0.41,
          "peak_del": 0.48,
          "del_chg": 0.14,
          "avg_vol": 0.345,
          "call_oi_growth_pct": -5.07,
          "put_oi_growth_pct": -3.14,
          "opt_oi_growth_pct": -4.3,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.21,
          "pcr": 0.71,
          "pcr_chg_1d": -0.08,
          "fut_oi": 25372500,
          "oi_chg_pct": 4.84,
          "delivery": 0.92,
          "volume": 1.03,
          "call_oi": 5727500,
          "put_oi": 4048750
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.81,
          "pcr": 0.66,
          "pcr_chg_1d": 0.01,
          "fut_oi": 40385000,
          "oi_chg_pct": 5.86,
          "delivery": 0.34,
          "volume": 0.32,
          "call_oi": 15280000,
          "put_oi": 10142500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 4.01,
          "pcr": 0.68,
          "pcr_chg_1d": 0.02,
          "fut_oi": 41751250,
          "oi_chg_pct": 3.38,
          "delivery": 0.48,
          "volume": 0.37,
          "call_oi": 14505000,
          "put_oi": 9823750
        }
      ]
    },
    {
      "symbol": "NBCC",
      "rank": 134,
      "days_available": 3,
      "latest_score": 3.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -6.0,
          3.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.04,
        "pcr_first": 0.88,
        "pcr_last": 0.8,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.08,
        "cumulative_price_chg_pct_window": 0.51,
        "persistence_score": 0.33,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -6.0,
          "signals": [
            "PCR 0.83 neutral-to-bullish",
            "PCR easing -0.06"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.01,
          "price_sign": -1,
          "pcr_d1": 0.88,
          "pcr_d2": 0.83,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": 0.64,
          "oi_sign": 1,
          "avg_del": 0.85,
          "peak_del": 0.92,
          "del_chg": 0.14,
          "avg_vol": 1.085,
          "call_oi_growth_pct": 28.77,
          "put_oi_growth_pct": 21.75,
          "opt_oi_growth_pct": 25.49,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.5,
          "signals": [
            "PCR 0.80 neutral-to-bullish",
            "Del 1.01x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.54,
          "price_sign": 1,
          "pcr_d1": 0.83,
          "pcr_d2": 0.8,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": -0.56,
          "oi_sign": -1,
          "avg_del": 1.005,
          "peak_del": 1.09,
          "del_chg": 0.17,
          "avg_vol": 0.89,
          "call_oi_growth_pct": 5.27,
          "put_oi_growth_pct": 1.79,
          "opt_oi_growth_pct": 3.69,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 6.8,
          "pcr": 0.88,
          "pcr_chg_1d": 0.08,
          "fut_oi": 77818000,
          "oi_chg_pct": -0.94,
          "delivery": 0.78,
          "volume": 1.23,
          "call_oi": 11882000,
          "put_oi": 10458500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.01,
          "pcr": 0.83,
          "pcr_chg_1d": -0.06,
          "fut_oi": 78318500,
          "oi_chg_pct": -0.19,
          "delivery": 0.92,
          "volume": 0.94,
          "call_oi": 15301000,
          "put_oi": 12733500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.54,
          "pcr": 0.8,
          "pcr_chg_1d": -0.03,
          "fut_oi": 77876500,
          "oi_chg_pct": -0.56,
          "delivery": 1.09,
          "volume": 0.84,
          "call_oi": 16107000,
          "put_oi": 12961000
        }
      ]
    },
    {
      "symbol": "ICICIPRULI",
      "rank": 135,
      "days_available": 3,
      "latest_score": 3.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          3.0,
          3.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.05,
        "pcr_first": 0.95,
        "pcr_last": 0.85,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.56,
        "cumulative_price_chg_pct_window": 0.99,
        "persistence_score": 3.33,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 3.0,
          "signals": [
            "PCR 0.92 approaching bullish zone",
            "PCR easing -0.06"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.06,
          "price_sign": 0,
          "pcr_d1": 0.95,
          "pcr_d2": 0.92,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": 0.42,
          "oi_sign": 1,
          "avg_del": 1.195,
          "peak_del": 1.45,
          "del_chg": -0.51,
          "avg_vol": 1.15,
          "call_oi_growth_pct": 27.77,
          "put_oi_growth_pct": 23.99,
          "opt_oi_growth_pct": 25.93,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.5,
          "signals": [
            "PCR 0.85 approaching bullish zone",
            "PCR easing -0.07"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.93,
          "price_sign": 1,
          "pcr_d1": 0.92,
          "pcr_d2": 0.85,
          "pcr_chg": -0.07,
          "fut_oi_chg_pct": 0.14,
          "oi_sign": 1,
          "avg_del": 0.855,
          "peak_del": 0.94,
          "del_chg": -0.17,
          "avg_vol": 0.93,
          "call_oi_growth_pct": 25.98,
          "put_oi_growth_pct": 16.17,
          "opt_oi_growth_pct": 21.28,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.75,
          "pcr": 0.95,
          "pcr_chg_1d": 0.03,
          "fut_oi": 18591575,
          "oi_chg_pct": 5.07,
          "delivery": 1.45,
          "volume": 1.35,
          "call_oi": 1312575,
          "put_oi": 1241350
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.06,
          "pcr": 0.92,
          "pcr_chg_1d": -0.06,
          "fut_oi": 18669275,
          "oi_chg_pct": 0.22,
          "delivery": 0.94,
          "volume": 0.95,
          "call_oi": 1677025,
          "put_oi": 1539200
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.93,
          "pcr": 0.85,
          "pcr_chg_1d": -0.07,
          "fut_oi": 18696100,
          "oi_chg_pct": 0.14,
          "delivery": 0.77,
          "volume": 0.91,
          "call_oi": 2112700,
          "put_oi": 1788025
        }
      ]
    },
    {
      "symbol": "EXIDEIND",
      "rank": 136,
      "days_available": 3,
      "latest_score": 3.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -3.0,
          3.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.005,
        "pcr_first": 0.88,
        "pcr_last": 0.89,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 1.8,
        "cumulative_price_chg_pct_window": 3.3,
        "persistence_score": 1.33,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -3.0,
          "signals": [
            "PCR 0.97 approaching bullish zone",
            "PCR surging +0.12",
            "\u26a0 NEW SHORTS: FutOI +2.5% + Price -0.9%",
            "Del 1.24x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_short",
          "price_chg_pct": -0.92,
          "price_sign": -1,
          "pcr_d1": 0.88,
          "pcr_d2": 0.97,
          "pcr_chg": 0.12,
          "fut_oi_chg_pct": 2.45,
          "oi_sign": 1,
          "avg_del": 1.24,
          "peak_del": 1.94,
          "del_chg": 1.4,
          "avg_vol": 1.395,
          "call_oi_growth_pct": 52.54,
          "put_oi_growth_pct": 68.64,
          "opt_oi_growth_pct": 60.06,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.5,
          "signals": [
            "PCR 0.89 approaching bullish zone",
            "PCR easing -0.08",
            "Del 1.89x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 4.26,
          "price_sign": 1,
          "pcr_d1": 0.97,
          "pcr_d2": 0.89,
          "pcr_chg": -0.08,
          "fut_oi_chg_pct": -0.64,
          "oi_sign": -1,
          "avg_del": 1.885,
          "peak_del": 1.94,
          "del_chg": -0.11,
          "avg_vol": 2.005,
          "call_oi_growth_pct": 20.14,
          "put_oi_growth_pct": 10.64,
          "opt_oi_growth_pct": 15.47,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.15,
          "pcr": 0.88,
          "pcr_chg_1d": 0.02,
          "fut_oi": 28675800,
          "oi_chg_pct": -0.52,
          "delivery": 0.54,
          "volume": 0.67,
          "call_oi": 7335000,
          "put_oi": 6427800
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.92,
          "pcr": 0.97,
          "pcr_chg_1d": 0.12,
          "fut_oi": 29379600,
          "oi_chg_pct": 0.83,
          "delivery": 1.94,
          "volume": 2.12,
          "call_oi": 11188800,
          "put_oi": 10839600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 4.26,
          "pcr": 0.89,
          "pcr_chg_1d": -0.08,
          "fut_oi": 29190600,
          "oi_chg_pct": -0.64,
          "delivery": 1.83,
          "volume": 1.89,
          "call_oi": 13442400,
          "put_oi": 11993400
        }
      ]
    },
    {
      "symbol": "DELHIVERY",
      "rank": 137,
      "days_available": 3,
      "latest_score": -3.5,
      "latest_tier": "WATCH (mild bearish)",
      "latest_sign": "bearish",
      "latest_phase": "pre_phase_1_short",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u25cb NONE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          9.0,
          -3.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.03,
        "pcr_first": 0.44,
        "pcr_last": 0.5,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 7.77,
        "cumulative_price_chg_pct_window": 2.23,
        "persistence_score": 0.67,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": 9.0,
          "signals": [
            "PCR 0.56 neutral",
            "PCR rising +0.05",
            "\u2605 NEW LONGS: FutOI +9.5% + Price +2.2%",
            "Del 1.20x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 2.17,
          "price_sign": 1,
          "pcr_d1": 0.44,
          "pcr_d2": 0.56,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": 9.53,
          "oi_sign": 1,
          "avg_del": 1.195,
          "peak_del": 1.31,
          "del_chg": -0.23,
          "avg_vol": 1.285,
          "call_oi_growth_pct": 94.7,
          "put_oi_growth_pct": 148.2,
          "opt_oi_growth_pct": 110.99,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -3.5,
          "signals": [
            "PCR 0.50 call writers dominant",
            "PCR easing -0.06"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": 0.06,
          "price_sign": 0,
          "pcr_d1": 0.56,
          "pcr_d2": 0.5,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": -1.6,
          "oi_sign": -1,
          "avg_del": 0.86,
          "peak_del": 1.08,
          "del_chg": -0.44,
          "avg_vol": 0.93,
          "call_oi_growth_pct": 13.94,
          "put_oi_growth_pct": 1.4,
          "opt_oi_growth_pct": 9.45,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.53,
          "pcr": 0.44,
          "pcr_chg_1d": 0.02,
          "fut_oi": 26943875,
          "oi_chg_pct": 0.72,
          "delivery": 1.31,
          "volume": 1.26,
          "call_oi": 3676900,
          "put_oi": 1610200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 2.17,
          "pcr": 0.56,
          "pcr_chg_1d": 0.05,
          "fut_oi": 29510650,
          "oi_chg_pct": -3.44,
          "delivery": 1.08,
          "volume": 1.31,
          "call_oi": 7158750,
          "put_oi": 3996450
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.06,
          "pcr": 0.5,
          "pcr_chg_1d": -0.06,
          "fut_oi": 29037550,
          "oi_chg_pct": -1.6,
          "delivery": 0.64,
          "volume": 0.55,
          "call_oi": 8156825,
          "put_oi": 4052475
        }
      ]
    },
    {
      "symbol": "DIXON",
      "rank": 138,
      "days_available": 3,
      "latest_score": 3.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.0,
          3.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.04,
        "pcr_first": 0.8,
        "pcr_last": 0.72,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 16.0,
        "cumulative_price_chg_pct_window": 0.38,
        "persistence_score": 1.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -2.0,
          "signals": [
            "PCR 0.77 neutral-to-bullish"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.1,
          "price_sign": 0,
          "pcr_d1": 0.8,
          "pcr_d2": 0.77,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 11.24,
          "oi_sign": 1,
          "avg_del": 0.795,
          "peak_del": 0.89,
          "del_chg": -0.19,
          "avg_vol": 0.915,
          "call_oi_growth_pct": 65.61,
          "put_oi_growth_pct": 60.28,
          "opt_oi_growth_pct": 63.25,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.5,
          "signals": [
            "PCR 0.72 neutral",
            "PCR easing -0.05"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.48,
          "price_sign": 1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.72,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": 4.28,
          "oi_sign": 1,
          "avg_del": 0.85,
          "peak_del": 1.0,
          "del_chg": 0.3,
          "avg_vol": 0.855,
          "call_oi_growth_pct": 10.83,
          "put_oi_growth_pct": 2.75,
          "opt_oi_growth_pct": 7.3,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 6.01,
          "pcr": 0.8,
          "pcr_chg_1d": 0.05,
          "fut_oi": 2728850,
          "oi_chg_pct": 2.71,
          "delivery": 0.89,
          "volume": 1.06,
          "call_oi": 988450,
          "put_oi": 788600
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.1,
          "pcr": 0.77,
          "pcr_chg_1d": 0.03,
          "fut_oi": 3035500,
          "oi_chg_pct": 1.33,
          "delivery": 0.7,
          "volume": 0.77,
          "call_oi": 1636950,
          "put_oi": 1264000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.48,
          "pcr": 0.72,
          "pcr_chg_1d": -0.05,
          "fut_oi": 3165350,
          "oi_chg_pct": 4.28,
          "delivery": 1.0,
          "volume": 0.94,
          "call_oi": 1814150,
          "put_oi": 1298700
        }
      ]
    },
    {
      "symbol": "MUTHOOTFIN",
      "rank": 139,
      "days_available": 3,
      "latest_score": 3.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -5.5,
          3.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.1,
        "pcr_first": 0.92,
        "pcr_last": 0.72,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -9.6,
        "cumulative_price_chg_pct_window": 2.02,
        "persistence_score": 0.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -5.5,
          "signals": [
            "PCR 0.69 neutral"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.8,
          "price_sign": -1,
          "pcr_d1": 0.92,
          "pcr_d2": 0.69,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -8.85,
          "oi_sign": -1,
          "avg_del": 0.66,
          "peak_del": 0.98,
          "del_chg": 0.64,
          "avg_vol": 0.67,
          "call_oi_growth_pct": 75.87,
          "put_oi_growth_pct": 32.11,
          "opt_oi_growth_pct": 54.92,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.5,
          "signals": [
            "PCR 0.72 neutral",
            "Del 1.02x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 2.84,
          "price_sign": 1,
          "pcr_d1": 0.69,
          "pcr_d2": 0.72,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -0.82,
          "oi_sign": -1,
          "avg_del": 1.02,
          "peak_del": 1.06,
          "del_chg": 0.08,
          "avg_vol": 1.0,
          "call_oi_growth_pct": 1.54,
          "put_oi_growth_pct": 5.63,
          "opt_oi_growth_pct": 3.21,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.03,
          "pcr": 0.92,
          "pcr_chg_1d": 0.04,
          "fut_oi": 3892075,
          "oi_chg_pct": -0.06,
          "delivery": 0.34,
          "volume": 0.37,
          "call_oi": 1047200,
          "put_oi": 961675
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.8,
          "pcr": 0.69,
          "pcr_chg_1d": 0.03,
          "fut_oi": 3547500,
          "oi_chg_pct": -0.07,
          "delivery": 0.98,
          "volume": 0.97,
          "call_oi": 1841675,
          "put_oi": 1270500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.84,
          "pcr": 0.72,
          "pcr_chg_1d": 0.03,
          "fut_oi": 3518350,
          "oi_chg_pct": -0.82,
          "delivery": 1.06,
          "volume": 1.03,
          "call_oi": 1870000,
          "put_oi": 1342000
        }
      ]
    },
    {
      "symbol": "PPLPHARMA",
      "rank": 140,
      "days_available": 3,
      "latest_score": -3.5,
      "latest_tier": "WATCH (mild bearish)",
      "latest_sign": "bearish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -8.0,
          -3.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 2,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.155,
        "pcr_first": 0.81,
        "pcr_last": 0.5,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.04,
        "cumulative_price_chg_pct_window": 1.54,
        "persistence_score": -5.0,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -8.0,
          "signals": [
            "PCR 0.60 neutral",
            "PCR collapsing -0.10"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": -0.57,
          "price_sign": -1,
          "pcr_d1": 0.81,
          "pcr_d2": 0.6,
          "pcr_chg": -0.1,
          "fut_oi_chg_pct": 1.69,
          "oi_sign": 1,
          "avg_del": 0.58,
          "peak_del": 0.74,
          "del_chg": 0.32,
          "avg_vol": 0.55,
          "call_oi_growth_pct": 68.08,
          "put_oi_growth_pct": 23.89,
          "opt_oi_growth_pct": 48.27,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -3.5,
          "signals": [
            "PCR 0.50 call writers dominant",
            "PCR collapsing -0.10"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 2.12,
          "price_sign": 1,
          "pcr_d1": 0.6,
          "pcr_d2": 0.5,
          "pcr_chg": -0.1,
          "fut_oi_chg_pct": -1.62,
          "oi_sign": -1,
          "avg_del": 0.875,
          "peak_del": 1.01,
          "del_chg": 0.27,
          "avg_vol": 0.845,
          "call_oi_growth_pct": 33.06,
          "put_oi_growth_pct": 10.01,
          "opt_oi_growth_pct": 24.43,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.37,
          "pcr": 0.81,
          "pcr_chg_1d": 0.0,
          "fut_oi": 13064625,
          "oi_chg_pct": -1.62,
          "delivery": 0.42,
          "volume": 0.44,
          "call_oi": 2475375,
          "put_oi": 2010750
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.57,
          "pcr": 0.6,
          "pcr_chg_1d": -0.1,
          "fut_oi": 13285125,
          "oi_chg_pct": 2.26,
          "delivery": 0.74,
          "volume": 0.66,
          "call_oi": 4160625,
          "put_oi": 2491125
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.12,
          "pcr": 0.5,
          "pcr_chg_1d": -0.1,
          "fut_oi": 13069875,
          "oi_chg_pct": -1.62,
          "delivery": 1.01,
          "volume": 1.03,
          "call_oi": 5536125,
          "put_oi": 2740500
        }
      ]
    },
    {
      "symbol": "BAJAJHLDNG",
      "rank": 141,
      "days_available": 3,
      "latest_score": 3.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.0,
          3.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.01,
        "pcr_first": 0.62,
        "pcr_last": 0.64,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 9.05,
        "cumulative_price_chg_pct_window": 0.28,
        "persistence_score": 1.0,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -4.0,
          "signals": [
            "PCR 0.67 neutral",
            "\u26a0 NEW SHORTS: FutOI +9.0% + Price -0.6%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.58,
          "price_sign": -1,
          "pcr_d1": 0.62,
          "pcr_d2": 0.67,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": 9.01,
          "oi_sign": 1,
          "avg_del": 0.87,
          "peak_del": 0.88,
          "del_chg": -0.02,
          "avg_vol": 0.895,
          "call_oi_growth_pct": 70.28,
          "put_oi_growth_pct": 84.05,
          "opt_oi_growth_pct": 75.54,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.5,
          "signals": [
            "PCR 0.64 neutral"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.86,
          "price_sign": 1,
          "pcr_d1": 0.67,
          "pcr_d2": 0.64,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": 0.04,
          "oi_sign": 1,
          "avg_del": 0.805,
          "peak_del": 0.86,
          "del_chg": -0.11,
          "avg_vol": 0.78,
          "call_oi_growth_pct": 5.29,
          "put_oi_growth_pct": 1.32,
          "opt_oi_growth_pct": 3.7,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.84,
          "pcr": 0.62,
          "pcr_chg_1d": 0.12,
          "fut_oi": 260300,
          "oi_chg_pct": -1.61,
          "delivery": 0.88,
          "volume": 0.94,
          "call_oi": 29950,
          "put_oi": 18500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.58,
          "pcr": 0.67,
          "pcr_chg_1d": 0.0,
          "fut_oi": 283750,
          "oi_chg_pct": 2.94,
          "delivery": 0.86,
          "volume": 0.85,
          "call_oi": 51000,
          "put_oi": 34050
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.86,
          "pcr": 0.64,
          "pcr_chg_1d": -0.03,
          "fut_oi": 283850,
          "oi_chg_pct": 0.04,
          "delivery": 0.75,
          "volume": 0.71,
          "call_oi": 53700,
          "put_oi": 34500
        }
      ]
    },
    {
      "symbol": "ADANIPOWER",
      "rank": 142,
      "days_available": 3,
      "latest_score": 3.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          7.5,
          3.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.03,
        "pcr_first": 0.36,
        "pcr_last": 0.42,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 401.59,
        "cumulative_price_chg_pct_window": 3.84,
        "persistence_score": 4.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 7.5,
          "signals": [
            "PCR 0.36 heavy call writing",
            "PCR rising +0.06",
            "\u2605 NEW LONGS: FutOI +363.3% + Price +1.8%",
            "Del 1.39x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.78,
          "price_sign": 1,
          "pcr_d1": 0.36,
          "pcr_d2": 0.36,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": 363.29,
          "oi_sign": 1,
          "avg_del": 1.39,
          "peak_del": 2.38,
          "del_chg": -1.98,
          "avg_vol": 1.265,
          "call_oi_growth_pct": 996.54,
          "put_oi_growth_pct": 1018.06,
          "opt_oi_growth_pct": 1002.19,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.5,
          "signals": [
            "PCR 0.42 call writers dominant",
            "PCR rising +0.06",
            "\u2605 NEW LONGS: FutOI +8.3% + Price +2.0%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": 2.02,
          "price_sign": 1,
          "pcr_d1": 0.36,
          "pcr_d2": 0.42,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": 8.27,
          "oi_sign": 1,
          "avg_del": 0.425,
          "peak_del": 0.45,
          "del_chg": 0.05,
          "avg_vol": 0.71,
          "call_oi_growth_pct": -0.18,
          "put_oi_growth_pct": 15.84,
          "opt_oi_growth_pct": 4.08,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.44,
          "pcr": 0.36,
          "pcr_chg_1d": 0.0,
          "fut_oi": 11594300,
          "oi_chg_pct": 0.0,
          "delivery": 2.38,
          "volume": 1.9,
          "call_oi": 1437750,
          "put_oi": 511200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.78,
          "pcr": 0.36,
          "pcr_chg_1d": 0.06,
          "fut_oi": 53715050,
          "oi_chg_pct": 2.17,
          "delivery": 0.4,
          "volume": 0.63,
          "call_oi": 15765550,
          "put_oi": 5715500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.02,
          "pcr": 0.42,
          "pcr_chg_1d": 0.06,
          "fut_oi": 58156100,
          "oi_chg_pct": 8.27,
          "delivery": 0.45,
          "volume": 0.79,
          "call_oi": 15737150,
          "put_oi": 6620750
        }
      ]
    },
    {
      "symbol": "PFC",
      "rank": 143,
      "days_available": 3,
      "latest_score": 3.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          6.5,
          3.5
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.02,
        "pcr_first": 0.77,
        "pcr_last": 0.73,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 3.35,
        "cumulative_price_chg_pct_window": 4.13,
        "persistence_score": 4.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 6.5,
          "signals": [
            "PCR 0.75 neutral-to-bullish",
            "\u2605 NEW LONGS: FutOI +2.1% + Price +2.5%",
            "Del 1.02x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 2.49,
          "price_sign": 1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.75,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": 2.13,
          "oi_sign": 1,
          "avg_del": 1.025,
          "peak_del": 1.15,
          "del_chg": -0.25,
          "avg_vol": 1.145,
          "call_oi_growth_pct": 52.18,
          "put_oi_growth_pct": 47.07,
          "opt_oi_growth_pct": 49.96,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.5,
          "signals": [
            "PCR 0.73 neutral"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.6,
          "price_sign": 1,
          "pcr_d1": 0.75,
          "pcr_d2": 0.73,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 1.2,
          "oi_sign": 1,
          "avg_del": 0.95,
          "peak_del": 1.0,
          "del_chg": 0.1,
          "avg_vol": 1.18,
          "call_oi_growth_pct": 6.61,
          "put_oi_growth_pct": 3.7,
          "opt_oi_growth_pct": 5.36,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.8,
          "pcr": 0.77,
          "pcr_chg_1d": -0.01,
          "fut_oi": 55179800,
          "oi_chg_pct": -9.38,
          "delivery": 1.15,
          "volume": 1.02,
          "call_oi": 12478700,
          "put_oi": 9633000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 2.49,
          "pcr": 0.75,
          "pcr_chg_1d": 0.0,
          "fut_oi": 56355000,
          "oi_chg_pct": 2.96,
          "delivery": 0.9,
          "volume": 1.27,
          "call_oi": 18990400,
          "put_oi": 14167400
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.6,
          "pcr": 0.73,
          "pcr_chg_1d": -0.02,
          "fut_oi": 57031000,
          "oi_chg_pct": 1.2,
          "delivery": 1.0,
          "volume": 1.09,
          "call_oi": 20244900,
          "put_oi": 14691300
        }
      ]
    },
    {
      "symbol": "KFINTECH",
      "rank": 144,
      "days_available": 3,
      "latest_score": 3.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -15.0,
          3.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.27,
        "pcr_first": 1.03,
        "pcr_last": 0.49,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 68.22,
        "cumulative_price_chg_pct_window": -0.86,
        "persistence_score": -2.67,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -15.0,
          "signals": [
            "PCR 0.51 call writers dominant",
            "PCR collapsing -0.11",
            "\u26a0 NEW SHORTS: FutOI +68.1% + Price -3.0%",
            "Del 1.46x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -2.95,
          "price_sign": -1,
          "pcr_d1": 1.03,
          "pcr_d2": 0.51,
          "pcr_chg": -0.11,
          "fut_oi_chg_pct": 68.07,
          "oi_sign": 1,
          "avg_del": 1.46,
          "peak_del": 2.57,
          "del_chg": 2.22,
          "avg_vol": 1.14,
          "call_oi_growth_pct": 423.47,
          "put_oi_growth_pct": 160.23,
          "opt_oi_growth_pct": 289.81,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.5,
          "signals": [
            "PCR 0.49 call writers dominant",
            "Del 1.88x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 2.15,
          "price_sign": 1,
          "pcr_d1": 0.51,
          "pcr_d2": 0.49,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 0.09,
          "oi_sign": 1,
          "avg_del": 1.88,
          "peak_del": 2.57,
          "del_chg": -1.38,
          "avg_vol": 1.43,
          "call_oi_growth_pct": 7.69,
          "put_oi_growth_pct": 1.98,
          "opt_oi_growth_pct": 5.75,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.02,
          "pcr": 1.03,
          "pcr_chg_1d": -0.02,
          "fut_oi": 2010500,
          "oi_chg_pct": -0.96,
          "delivery": 0.35,
          "volume": 0.44,
          "call_oi": 253500,
          "put_oi": 261500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.95,
          "pcr": 0.51,
          "pcr_chg_1d": -0.11,
          "fut_oi": 3379000,
          "oi_chg_pct": 12.07,
          "delivery": 2.57,
          "volume": 1.84,
          "call_oi": 1327000,
          "put_oi": 680500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.15,
          "pcr": 0.49,
          "pcr_chg_1d": -0.02,
          "fut_oi": 3382000,
          "oi_chg_pct": 0.09,
          "delivery": 1.19,
          "volume": 1.02,
          "call_oi": 1429000,
          "put_oi": 694000
        }
      ]
    },
    {
      "symbol": "INDIGO",
      "rank": 145,
      "days_available": 3,
      "latest_score": 3.5,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -10.5,
          3.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.02,
        "pcr_first": 0.67,
        "pcr_last": 0.63,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -1.28,
        "cumulative_price_chg_pct_window": -1.34,
        "persistence_score": -1.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -10.5,
          "signals": [
            "PCR 0.58 neutral",
            "PCR easing -0.05",
            "\u26a0 NEW SHORTS: FutOI +2.8% + Price -3.6%",
            "Del 1.16x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -3.61,
          "price_sign": -1,
          "pcr_d1": 0.67,
          "pcr_d2": 0.58,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": 2.81,
          "oi_sign": 1,
          "avg_del": 1.155,
          "peak_del": 1.52,
          "del_chg": -0.73,
          "avg_vol": 1.265,
          "call_oi_growth_pct": 85.94,
          "put_oi_growth_pct": 61.21,
          "opt_oi_growth_pct": 76.06,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.5,
          "signals": [
            "PCR 0.63 neutral",
            "PCR rising +0.05"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 2.36,
          "price_sign": 1,
          "pcr_d1": 0.58,
          "pcr_d2": 0.63,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": -3.98,
          "oi_sign": -1,
          "avg_del": 0.68,
          "peak_del": 0.79,
          "del_chg": -0.22,
          "avg_vol": 0.56,
          "call_oi_growth_pct": -2.92,
          "put_oi_growth_pct": 5.26,
          "opt_oi_growth_pct": 0.07,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 6.02,
          "pcr": 0.67,
          "pcr_chg_1d": -0.09,
          "fut_oi": 7338150,
          "oi_chg_pct": -9.9,
          "delivery": 1.52,
          "volume": 1.91,
          "call_oi": 3097200,
          "put_oi": 2060850
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -3.61,
          "pcr": 0.58,
          "pcr_chg_1d": -0.05,
          "fut_oi": 7544400,
          "oi_chg_pct": 3.35,
          "delivery": 0.79,
          "volume": 0.62,
          "call_oi": 5758950,
          "put_oi": 3322200
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.36,
          "pcr": 0.63,
          "pcr_chg_1d": 0.05,
          "fut_oi": 7244250,
          "oi_chg_pct": -3.98,
          "delivery": 0.57,
          "volume": 0.5,
          "call_oi": 5590950,
          "put_oi": 3496800
        }
      ]
    },
    {
      "symbol": "PAGEIND",
      "rank": 146,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u25cb NONE",
        "direction": "none",
        "count": 0
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          8.5,
          3.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.2,
        "pcr_first": 0.49,
        "pcr_last": 0.89,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 13.88,
        "cumulative_price_chg_pct_window": 2.07,
        "persistence_score": 4.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 8.5,
          "signals": [
            "PCR 0.89 approaching bullish zone",
            "PCR rising +0.07",
            "\u2605 NEW LONGS: FutOI +16.2% + Price +1.8%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": 1.77,
          "price_sign": 1,
          "pcr_d1": 0.49,
          "pcr_d2": 0.89,
          "pcr_chg": 0.07,
          "fut_oi_chg_pct": 16.21,
          "oi_sign": 1,
          "avg_del": 0.665,
          "peak_del": 0.8,
          "del_chg": 0.27,
          "avg_vol": 0.685,
          "call_oi_growth_pct": 88.08,
          "put_oi_growth_pct": 245.83,
          "opt_oi_growth_pct": 139.63,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.89 approaching bullish zone"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 0
          },
          "phase": "no_signal",
          "price_chg_pct": 0.29,
          "price_sign": 0,
          "pcr_d1": 0.89,
          "pcr_d2": 0.89,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -2.0,
          "oi_sign": -1,
          "avg_del": 1.285,
          "peak_del": 1.77,
          "del_chg": 0.97,
          "avg_vol": 1.0,
          "call_oi_growth_pct": 2.73,
          "put_oi_growth_pct": 2.72,
          "opt_oi_growth_pct": 2.73,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.66,
          "pcr": 0.49,
          "pcr_chg_1d": 0.14,
          "fut_oi": 312765,
          "oi_chg_pct": 3.1,
          "delivery": 0.53,
          "volume": 0.67,
          "call_oi": 31830,
          "put_oi": 15450
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.77,
          "pcr": 0.89,
          "pcr_chg_1d": 0.07,
          "fut_oi": 363465,
          "oi_chg_pct": 1.38,
          "delivery": 0.8,
          "volume": 0.7,
          "call_oi": 59865,
          "put_oi": 53430
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.29,
          "pcr": 0.89,
          "pcr_chg_1d": 0.0,
          "fut_oi": 356190,
          "oi_chg_pct": -2.0,
          "delivery": 1.77,
          "volume": 1.3,
          "call_oi": 61500,
          "put_oi": 54885
        }
      ]
    },
    {
      "symbol": "BHARTIARTL",
      "rank": 147,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          2.0,
          3.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.065,
        "pcr_first": 0.76,
        "pcr_last": 0.89,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.31,
        "cumulative_price_chg_pct_window": 0.45,
        "persistence_score": 2.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 2.0,
          "signals": [
            "PCR 0.88 approaching bullish zone"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.12,
          "price_sign": 0,
          "pcr_d1": 0.76,
          "pcr_d2": 0.88,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 0.99,
          "oi_sign": 1,
          "avg_del": 0.74,
          "peak_del": 0.84,
          "del_chg": -0.2,
          "avg_vol": 0.895,
          "call_oi_growth_pct": 25.56,
          "put_oi_growth_pct": 44.68,
          "opt_oi_growth_pct": 33.83,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.89 approaching bullish zone"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.57,
          "price_sign": 1,
          "pcr_d1": 0.88,
          "pcr_d2": 0.89,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": -0.68,
          "oi_sign": -1,
          "avg_del": 0.605,
          "peak_del": 0.64,
          "del_chg": -0.07,
          "avg_vol": 0.78,
          "call_oi_growth_pct": -1.34,
          "put_oi_growth_pct": 0.11,
          "opt_oi_growth_pct": -0.66,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.03,
          "pcr": 0.76,
          "pcr_chg_1d": -0.05,
          "fut_oi": 58444950,
          "oi_chg_pct": 2.73,
          "delivery": 0.84,
          "volume": 0.81,
          "call_oi": 6972050,
          "put_oi": 5309075
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.12,
          "pcr": 0.88,
          "pcr_chg_1d": 0.01,
          "fut_oi": 59022550,
          "oi_chg_pct": -0.05,
          "delivery": 0.64,
          "volume": 0.98,
          "call_oi": 8754250,
          "put_oi": 7681225
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.57,
          "pcr": 0.89,
          "pcr_chg_1d": 0.01,
          "fut_oi": 58623550,
          "oi_chg_pct": -0.68,
          "delivery": 0.57,
          "volume": 0.58,
          "call_oi": 8636925,
          "put_oi": 7689775
        }
      ]
    },
    {
      "symbol": "HUDCO",
      "rank": 148,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -0.5,
          3.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.05,
        "pcr_first": 0.89,
        "pcr_last": 0.79,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -3.89,
        "cumulative_price_chg_pct_window": 1.0,
        "persistence_score": 1.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -0.5,
          "signals": [
            "PCR 0.84 neutral-to-bullish"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.12,
          "price_sign": 0,
          "pcr_d1": 0.89,
          "pcr_d2": 0.84,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -4.13,
          "oi_sign": -1,
          "avg_del": 0.585,
          "peak_del": 0.64,
          "del_chg": 0.11,
          "avg_vol": 0.735,
          "call_oi_growth_pct": 57.39,
          "put_oi_growth_pct": 49.39,
          "opt_oi_growth_pct": 53.62,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.79 neutral-to-bullish",
            "PCR easing -0.05"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.12,
          "price_sign": 1,
          "pcr_d1": 0.84,
          "pcr_d2": 0.79,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": 0.25,
          "oi_sign": 1,
          "avg_del": 0.725,
          "peak_del": 0.81,
          "del_chg": 0.17,
          "avg_vol": 0.76,
          "call_oi_growth_pct": 12.22,
          "put_oi_growth_pct": 4.99,
          "opt_oi_growth_pct": 8.91,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 5.3,
          "pcr": 0.89,
          "pcr_chg_1d": 0.03,
          "fut_oi": 29878425,
          "oi_chg_pct": -2.71,
          "delivery": 0.53,
          "volume": 0.65,
          "call_oi": 5106000,
          "put_oi": 4539900
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.12,
          "pcr": 0.84,
          "pcr_chg_1d": -0.01,
          "fut_oi": 28643550,
          "oi_chg_pct": -1.37,
          "delivery": 0.64,
          "volume": 0.82,
          "call_oi": 8036400,
          "put_oi": 6782100
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.12,
          "pcr": 0.79,
          "pcr_chg_1d": -0.05,
          "fut_oi": 28715700,
          "oi_chg_pct": 0.25,
          "delivery": 0.81,
          "volume": 0.7,
          "call_oi": 9018750,
          "put_oi": 7120650
        }
      ]
    },
    {
      "symbol": "SHRIRAMFIN",
      "rank": 149,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -6.5,
          3.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.04,
        "pcr_first": 0.8,
        "pcr_last": 0.72,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -4.55,
        "cumulative_price_chg_pct_window": 0.43,
        "persistence_score": -0.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -6.5,
          "signals": [
            "PCR 0.70 neutral",
            "PCR easing -0.05"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -2.63,
          "price_sign": -1,
          "pcr_d1": 0.8,
          "pcr_d2": 0.7,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": -3.31,
          "oi_sign": -1,
          "avg_del": 0.755,
          "peak_del": 0.83,
          "del_chg": 0.15,
          "avg_vol": 0.875,
          "call_oi_growth_pct": 37.7,
          "put_oi_growth_pct": 19.62,
          "opt_oi_growth_pct": 29.65,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.72 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 3.14,
          "price_sign": 1,
          "pcr_d1": 0.7,
          "pcr_d2": 0.72,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": -1.29,
          "oi_sign": -1,
          "avg_del": 0.89,
          "peak_del": 0.95,
          "del_chg": 0.12,
          "avg_vol": 0.845,
          "call_oi_growth_pct": 10.39,
          "put_oi_growth_pct": 14.64,
          "opt_oi_growth_pct": 12.13,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.26,
          "pcr": 0.8,
          "pcr_chg_1d": -0.05,
          "fut_oi": 44167200,
          "oi_chg_pct": 0.76,
          "delivery": 0.68,
          "volume": 0.96,
          "call_oi": 8537925,
          "put_oi": 6858225
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.63,
          "pcr": 0.7,
          "pcr_chg_1d": -0.05,
          "fut_oi": 42706950,
          "oi_chg_pct": -1.14,
          "delivery": 0.83,
          "volume": 0.79,
          "call_oi": 11757075,
          "put_oi": 8203800
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.14,
          "pcr": 0.72,
          "pcr_chg_1d": 0.02,
          "fut_oi": 42157500,
          "oi_chg_pct": -1.29,
          "delivery": 0.95,
          "volume": 0.9,
          "call_oi": 12978075,
          "put_oi": 9405000
        }
      ]
    },
    {
      "symbol": "GLENMARK",
      "rank": 150,
      "days_available": 3,
      "latest_score": -3.0,
      "latest_tier": "WATCH (mild bearish)",
      "latest_sign": "bearish",
      "latest_phase": "pre_phase_1_short",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u25cb NONE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          2.5,
          -3.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.07,
        "pcr_first": 0.38,
        "pcr_last": 0.52,
        "days_delivery_institutional": 3,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -8.2,
        "cumulative_price_chg_pct_window": -0.47,
        "persistence_score": -1.17,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": 2.5,
          "signals": [
            "PCR 0.59 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.2,
          "price_sign": 0,
          "pcr_d1": 0.38,
          "pcr_d2": 0.59,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": -8.03,
          "oi_sign": -1,
          "avg_del": 1.295,
          "peak_del": 1.44,
          "del_chg": -0.29,
          "avg_vol": 1.2,
          "call_oi_growth_pct": 26.61,
          "put_oi_growth_pct": 96.74,
          "opt_oi_growth_pct": 45.8,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -3.0,
          "signals": [
            "PCR 0.52 call writers dominant",
            "PCR easing -0.07"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -0.27,
          "price_sign": 0,
          "pcr_d1": 0.59,
          "pcr_d2": 0.52,
          "pcr_chg": -0.07,
          "fut_oi_chg_pct": -0.18,
          "oi_sign": -1,
          "avg_del": 1.26,
          "peak_del": 1.37,
          "del_chg": 0.22,
          "avg_vol": 0.98,
          "call_oi_growth_pct": 14.2,
          "put_oi_growth_pct": 1.84,
          "opt_oi_growth_pct": 9.63,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -1.44,
          "pcr": 0.38,
          "pcr_chg_1d": -0.01,
          "fut_oi": 11350125,
          "oi_chg_pct": 0.4,
          "delivery": 1.44,
          "volume": 1.52,
          "call_oi": 1128750,
          "put_oi": 425250
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.2,
          "pcr": 0.59,
          "pcr_chg_1d": 0.02,
          "fut_oi": 10438875,
          "oi_chg_pct": -2.39,
          "delivery": 1.15,
          "volume": 0.88,
          "call_oi": 1429125,
          "put_oi": 836625
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.27,
          "pcr": 0.52,
          "pcr_chg_1d": -0.07,
          "fut_oi": 10419750,
          "oi_chg_pct": -0.18,
          "delivery": 1.37,
          "volume": 1.08,
          "call_oi": 1632000,
          "put_oi": 852000
        }
      ]
    },
    {
      "symbol": "TATASTEEL",
      "rank": 151,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          8.5,
          3.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.015,
        "pcr_first": 0.77,
        "pcr_last": 0.8,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 3.25,
        "cumulative_price_chg_pct_window": 1.19,
        "persistence_score": 4.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 8.5,
          "signals": [
            "PCR 0.78 neutral-to-bullish",
            "Del 1.00x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.5,
          "price_sign": 1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.78,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 4.94,
          "oi_sign": 1,
          "avg_del": 1.005,
          "peak_del": 1.15,
          "del_chg": 0.29,
          "avg_vol": 1.03,
          "call_oi_growth_pct": 67.62,
          "put_oi_growth_pct": 69.16,
          "opt_oi_growth_pct": 68.29,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.80 neutral-to-bullish"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.69,
          "price_sign": 1,
          "pcr_d1": 0.78,
          "pcr_d2": 0.8,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": -1.61,
          "oi_sign": -1,
          "avg_del": 0.99,
          "peak_del": 1.15,
          "del_chg": -0.32,
          "avg_vol": 1.015,
          "call_oi_growth_pct": -0.66,
          "put_oi_growth_pct": 2.12,
          "opt_oi_growth_pct": 0.56,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.43,
          "pcr": 0.77,
          "pcr_chg_1d": -0.09,
          "fut_oi": 181643000,
          "oi_chg_pct": -6.69,
          "delivery": 0.86,
          "volume": 0.91,
          "call_oi": 63118000,
          "put_oi": 48664000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.5,
          "pcr": 0.78,
          "pcr_chg_1d": 0.03,
          "fut_oi": 190619000,
          "oi_chg_pct": 4.05,
          "delivery": 1.15,
          "volume": 1.15,
          "call_oi": 105798000,
          "put_oi": 82318500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.69,
          "pcr": 0.8,
          "pcr_chg_1d": 0.02,
          "fut_oi": 187544500,
          "oi_chg_pct": -1.61,
          "delivery": 0.83,
          "volume": 0.88,
          "call_oi": 105105000,
          "put_oi": 84062000
        }
      ]
    },
    {
      "symbol": "MAZDOCK",
      "rank": 152,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          10.5,
          3.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.035,
        "pcr_first": 0.81,
        "pcr_last": 0.74,
        "days_delivery_institutional": 3,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 4.61,
        "cumulative_price_chg_pct_window": 3.13,
        "persistence_score": 5.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 10.5,
          "signals": [
            "PCR 0.82 neutral-to-bullish",
            "\u2605 NEW LONGS: FutOI +3.5% + Price +1.7%",
            "Del 1.54x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.69,
          "price_sign": 1,
          "pcr_d1": 0.81,
          "pcr_d2": 0.82,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 3.45,
          "oi_sign": 1,
          "avg_del": 1.545,
          "peak_del": 1.92,
          "del_chg": -0.75,
          "avg_vol": 2.655,
          "call_oi_growth_pct": 15.83,
          "put_oi_growth_pct": 17.64,
          "opt_oi_growth_pct": 16.64,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.74 neutral",
            "PCR easing -0.08",
            "Del 1.14x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.42,
          "price_sign": 1,
          "pcr_d1": 0.82,
          "pcr_d2": 0.74,
          "pcr_chg": -0.08,
          "fut_oi_chg_pct": 1.12,
          "oi_sign": 1,
          "avg_del": 1.135,
          "peak_del": 1.17,
          "del_chg": -0.07,
          "avg_vol": 0.86,
          "call_oi_growth_pct": 17.94,
          "put_oi_growth_pct": 6.45,
          "opt_oi_growth_pct": 12.75,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 12.25,
          "pcr": 0.81,
          "pcr_chg_1d": 0.04,
          "fut_oi": 4365200,
          "oi_chg_pct": -11.6,
          "delivery": 1.92,
          "volume": 4.48,
          "call_oi": 2238200,
          "put_oi": 1811000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.69,
          "pcr": 0.82,
          "pcr_chg_1d": 0.03,
          "fut_oi": 4515800,
          "oi_chg_pct": 1.75,
          "delivery": 1.17,
          "volume": 0.83,
          "call_oi": 2592600,
          "put_oi": 2130400
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.42,
          "pcr": 0.74,
          "pcr_chg_1d": -0.08,
          "fut_oi": 4566400,
          "oi_chg_pct": 1.12,
          "delivery": 1.1,
          "volume": 0.89,
          "call_oi": 3057600,
          "put_oi": 2267800
        }
      ]
    },
    {
      "symbol": "APOLLOHOSP",
      "rank": 153,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          6.0,
          3.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.08,
        "pcr_first": 1.02,
        "pcr_last": 0.86,
        "days_delivery_institutional": 3,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 1.37,
        "cumulative_price_chg_pct_window": 1.48,
        "persistence_score": 4.0,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 6.0,
          "signals": [
            "PCR 0.92 approaching bullish zone",
            "Del 1.15x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.08,
          "price_sign": 1,
          "pcr_d1": 1.02,
          "pcr_d2": 0.92,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 1.42,
          "oi_sign": 1,
          "avg_del": 1.145,
          "peak_del": 1.23,
          "del_chg": -0.17,
          "avg_vol": 1.055,
          "call_oi_growth_pct": 62.02,
          "put_oi_growth_pct": 45.57,
          "opt_oi_growth_pct": 53.7,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.86 approaching bullish zone",
            "PCR easing -0.06",
            "Del 1.20x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.4,
          "price_sign": 1,
          "pcr_d1": 0.92,
          "pcr_d2": 0.86,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": -0.05,
          "oi_sign": -1,
          "avg_del": 1.195,
          "peak_del": 1.33,
          "del_chg": 0.27,
          "avg_vol": 1.12,
          "call_oi_growth_pct": 12.6,
          "put_oi_growth_pct": 5.46,
          "opt_oi_growth_pct": 9.18,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -1.53,
          "pcr": 1.02,
          "pcr_chg_1d": -0.35,
          "fut_oi": 2479000,
          "oi_chg_pct": 3.2,
          "delivery": 1.23,
          "volume": 1.08,
          "call_oi": 430500,
          "put_oi": 440250
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.08,
          "pcr": 0.92,
          "pcr_chg_1d": -0.02,
          "fut_oi": 2514250,
          "oi_chg_pct": -0.78,
          "delivery": 1.06,
          "volume": 1.03,
          "call_oi": 697500,
          "put_oi": 640875
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.4,
          "pcr": 0.86,
          "pcr_chg_1d": -0.06,
          "fut_oi": 2513000,
          "oi_chg_pct": -0.05,
          "delivery": 1.33,
          "volume": 1.21,
          "call_oi": 785375,
          "put_oi": 675875
        }
      ]
    },
    {
      "symbol": "IOC",
      "rank": 154,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.5,
          3.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.04,
        "pcr_first": 0.75,
        "pcr_last": 0.67,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -1.26,
        "cumulative_price_chg_pct_window": -0.27,
        "persistence_score": 0.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -4.5,
          "signals": [
            "PCR 0.69 neutral",
            "PCR rising +0.07"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.17,
          "price_sign": -1,
          "pcr_d1": 0.75,
          "pcr_d2": 0.69,
          "pcr_chg": 0.07,
          "fut_oi_chg_pct": 0.87,
          "oi_sign": 1,
          "avg_del": 0.955,
          "peak_del": 0.99,
          "del_chg": 0.07,
          "avg_vol": 0.885,
          "call_oi_growth_pct": 68.14,
          "put_oi_growth_pct": 55.2,
          "opt_oi_growth_pct": 62.6,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.67 neutral"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.91,
          "price_sign": 1,
          "pcr_d1": 0.69,
          "pcr_d2": 0.67,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": -2.11,
          "oi_sign": -1,
          "avg_del": 0.805,
          "peak_del": 0.99,
          "del_chg": -0.37,
          "avg_vol": 0.64,
          "call_oi_growth_pct": 2.24,
          "put_oi_growth_pct": -0.56,
          "opt_oi_growth_pct": 1.1,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.24,
          "pcr": 0.75,
          "pcr_chg_1d": -0.2,
          "fut_oi": 109063500,
          "oi_chg_pct": 2.99,
          "delivery": 0.92,
          "volume": 0.99,
          "call_oi": 36421125,
          "put_oi": 27270750
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.17,
          "pcr": 0.69,
          "pcr_chg_1d": 0.07,
          "fut_oi": 110009250,
          "oi_chg_pct": -1.65,
          "delivery": 0.99,
          "volume": 0.78,
          "call_oi": 61239750,
          "put_oi": 42324750
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.91,
          "pcr": 0.67,
          "pcr_chg_1d": -0.02,
          "fut_oi": 107683875,
          "oi_chg_pct": -2.11,
          "delivery": 0.62,
          "volume": 0.5,
          "call_oi": 62614500,
          "put_oi": 42085875
        }
      ]
    },
    {
      "symbol": "NYKAA",
      "rank": 155,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (LONG)",
        "direction": "long",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          5.0,
          3.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.08,
        "pcr_first": 0.77,
        "pcr_last": 0.61,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 6.48,
        "cumulative_price_chg_pct_window": 2.14,
        "persistence_score": 3.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 5.0,
          "signals": [
            "PCR 0.59 neutral",
            "Del 1.13x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.34,
          "price_sign": 1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.59,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": 6.27,
          "oi_sign": 1,
          "avg_del": 1.13,
          "peak_del": 1.68,
          "del_chg": -1.1,
          "avg_vol": 1.035,
          "call_oi_growth_pct": 375.4,
          "put_oi_growth_pct": 264.95,
          "opt_oi_growth_pct": 327.35,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.61 neutral"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": 1.79,
          "price_sign": 1,
          "pcr_d1": 0.59,
          "pcr_d2": 0.61,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": 0.2,
          "oi_sign": 1,
          "avg_del": 0.56,
          "peak_del": 0.58,
          "del_chg": -0.04,
          "avg_vol": 0.545,
          "call_oi_growth_pct": -4.51,
          "put_oi_growth_pct": -1.2,
          "opt_oi_growth_pct": -3.28,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.11,
          "pcr": 0.77,
          "pcr_chg_1d": 0.06,
          "fut_oi": 43353125,
          "oi_chg_pct": 2.05,
          "delivery": 1.68,
          "volume": 1.48,
          "call_oi": 1575000,
          "put_oi": 1212500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.34,
          "pcr": 0.59,
          "pcr_chg_1d": -0.03,
          "fut_oi": 46071875,
          "oi_chg_pct": -1.67,
          "delivery": 0.58,
          "volume": 0.59,
          "call_oi": 7487500,
          "put_oi": 4425000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.79,
          "pcr": 0.61,
          "pcr_chg_1d": 0.02,
          "fut_oi": 46162500,
          "oi_chg_pct": 0.2,
          "delivery": 0.54,
          "volume": 0.5,
          "call_oi": 7150000,
          "put_oi": 4371875
        }
      ]
    },
    {
      "symbol": "RBLBANK",
      "rank": 156,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -5.0,
          3.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.035,
        "pcr_first": 1.06,
        "pcr_last": 0.99,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -7.61,
        "cumulative_price_chg_pct_window": -0.22,
        "persistence_score": 0.33,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -5.0,
          "signals": [
            "PCR 1.05 ABOVE 1.0 \u2014 put writers dominant",
            "Del 1.39x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -1.6,
          "price_sign": -1,
          "pcr_d1": 1.06,
          "pcr_d2": 1.05,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": -6.95,
          "oi_sign": -1,
          "avg_del": 1.39,
          "peak_del": 2.47,
          "del_chg": -2.16,
          "avg_vol": 1.005,
          "call_oi_growth_pct": 58.14,
          "put_oi_growth_pct": 56.15,
          "opt_oi_growth_pct": 57.12,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.99 approaching bullish zone",
            "PCR easing -0.06"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.4,
          "price_sign": 1,
          "pcr_d1": 1.05,
          "pcr_d2": 0.99,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": -0.71,
          "oi_sign": -1,
          "avg_del": 0.6,
          "peak_del": 0.89,
          "del_chg": 0.58,
          "avg_vol": 0.45,
          "call_oi_growth_pct": 4.46,
          "put_oi_growth_pct": -1.11,
          "opt_oi_growth_pct": 1.61,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.11,
          "pcr": 1.06,
          "pcr_chg_1d": -0.43,
          "fut_oi": 69370575,
          "oi_chg_pct": -4.06,
          "delivery": 2.47,
          "volume": 1.65,
          "call_oi": 17497425,
          "put_oi": 18580100
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.6,
          "pcr": 1.05,
          "pcr_chg_1d": -0.02,
          "fut_oi": 64547750,
          "oi_chg_pct": -1.48,
          "delivery": 0.31,
          "volume": 0.36,
          "call_oi": 27670125,
          "put_oi": 29013150
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.4,
          "pcr": 0.99,
          "pcr_chg_1d": -0.06,
          "fut_oi": 64090550,
          "oi_chg_pct": -0.71,
          "delivery": 0.89,
          "volume": 0.54,
          "call_oi": 28905200,
          "put_oi": 28692475
        }
      ]
    },
    {
      "symbol": "MARUTI",
      "rank": 157,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.0,
          3.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.005,
        "pcr_first": 0.66,
        "pcr_last": 0.65,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -6.35,
        "cumulative_price_chg_pct_window": 0.78,
        "persistence_score": 1.33,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": -2.0,
          "signals": [
            "PCR 0.63 neutral",
            "PCR easing -0.06"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -0.1,
          "price_sign": 0,
          "pcr_d1": 0.66,
          "pcr_d2": 0.63,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": -5.0,
          "oi_sign": -1,
          "avg_del": 0.71,
          "peak_del": 0.8,
          "del_chg": 0.18,
          "avg_vol": 0.92,
          "call_oi_growth_pct": 88.53,
          "put_oi_growth_pct": 80.81,
          "opt_oi_growth_pct": 85.46,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.65 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.88,
          "price_sign": 1,
          "pcr_d1": 0.63,
          "pcr_d2": 0.65,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": -1.43,
          "oi_sign": -1,
          "avg_del": 0.86,
          "peak_del": 0.92,
          "del_chg": 0.12,
          "avg_vol": 0.94,
          "call_oi_growth_pct": 4.26,
          "put_oi_growth_pct": 7.79,
          "opt_oi_growth_pct": 5.63,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.65,
          "pcr": 0.66,
          "pcr_chg_1d": -0.04,
          "fut_oi": 3525500,
          "oi_chg_pct": -1.25,
          "delivery": 0.62,
          "volume": 0.82,
          "call_oi": 784900,
          "put_oi": 517550
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.1,
          "pcr": 0.63,
          "pcr_chg_1d": -0.06,
          "fut_oi": 3349350,
          "oi_chg_pct": -1.48,
          "delivery": 0.8,
          "volume": 1.02,
          "call_oi": 1479750,
          "put_oi": 935800
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.88,
          "pcr": 0.65,
          "pcr_chg_1d": 0.02,
          "fut_oi": 3301500,
          "oi_chg_pct": -1.43,
          "delivery": 0.92,
          "volume": 0.86,
          "call_oi": 1542800,
          "put_oi": 1008700
        }
      ]
    },
    {
      "symbol": "DABUR",
      "rank": 158,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          3.5,
          3.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.07,
        "pcr_first": 0.86,
        "pcr_last": 0.72,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -1.12,
        "cumulative_price_chg_pct_window": 1.98,
        "persistence_score": 3.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 3.5,
          "signals": [
            "PCR 0.75 neutral-to-bullish"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": 0.5,
          "price_sign": 1,
          "pcr_d1": 0.86,
          "pcr_d2": 0.75,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": 0.28,
          "oi_sign": 1,
          "avg_del": 0.69,
          "peak_del": 1.02,
          "del_chg": 0.66,
          "avg_vol": 0.715,
          "call_oi_growth_pct": 103.39,
          "put_oi_growth_pct": 77.29,
          "opt_oi_growth_pct": 91.31,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.72 neutral",
            "Del 1.22x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.47,
          "price_sign": 1,
          "pcr_d1": 0.75,
          "pcr_d2": 0.72,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": -1.39,
          "oi_sign": -1,
          "avg_del": 1.22,
          "peak_del": 1.42,
          "del_chg": 0.4,
          "avg_vol": 1.085,
          "call_oi_growth_pct": 10.8,
          "put_oi_growth_pct": 6.7,
          "opt_oi_growth_pct": 9.04,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.1,
          "pcr": 0.86,
          "pcr_chg_1d": 0.02,
          "fut_oi": 31365000,
          "oi_chg_pct": 0.73,
          "delivery": 0.36,
          "volume": 0.4,
          "call_oi": 3871250,
          "put_oi": 3335000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.5,
          "pcr": 0.75,
          "pcr_chg_1d": 0.02,
          "fut_oi": 31452500,
          "oi_chg_pct": -0.71,
          "delivery": 1.02,
          "volume": 1.03,
          "call_oi": 7873750,
          "put_oi": 5912500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.47,
          "pcr": 0.72,
          "pcr_chg_1d": -0.03,
          "fut_oi": 31013750,
          "oi_chg_pct": -1.39,
          "delivery": 1.42,
          "volume": 1.14,
          "call_oi": 8723750,
          "put_oi": 6308750
        }
      ]
    },
    {
      "symbol": "FORCEMOT",
      "rank": 159,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.0,
          3.0
        ],
        "bullish_windows": 2,
        "bearish_windows": 0,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": 0.21,
        "pcr_first": 0.13,
        "pcr_last": 0.55,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 1168.18,
        "cumulative_price_chg_pct_window": 2.46,
        "persistence_score": 3.33,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 4.0,
          "signals": [
            "PCR 0.52 call writers dominant"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.42,
          "price_sign": 1,
          "pcr_d1": 0.13,
          "pcr_d2": 0.52,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": 1190.53,
          "oi_sign": 1,
          "avg_del": 0.87,
          "peak_del": 1.13,
          "del_chg": -0.52,
          "avg_vol": 1.135,
          "call_oi_growth_pct": 2251.61,
          "put_oi_growth_pct": 9425.0,
          "opt_oi_growth_pct": 3071.43,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.55 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 2.03,
          "price_sign": 1,
          "pcr_d1": 0.52,
          "pcr_d2": 0.55,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -1.73,
          "oi_sign": -1,
          "avg_del": 0.715,
          "peak_del": 0.82,
          "del_chg": 0.21,
          "avg_vol": 0.91,
          "call_oi_growth_pct": 10.43,
          "put_oi_growth_pct": 17.06,
          "opt_oi_growth_pct": 12.7,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 6.84,
          "pcr": 0.13,
          "pcr_chg_1d": 0.0,
          "fut_oi": 6600,
          "oi_chg_pct": 0.0,
          "delivery": 1.13,
          "volume": 1.33,
          "call_oi": 1550,
          "put_oi": 200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.42,
          "pcr": 0.52,
          "pcr_chg_1d": 0.0,
          "fut_oi": 85175,
          "oi_chg_pct": 0.24,
          "delivery": 0.61,
          "volume": 0.94,
          "call_oi": 36450,
          "put_oi": 19050
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.03,
          "pcr": 0.55,
          "pcr_chg_1d": 0.03,
          "fut_oi": 83700,
          "oi_chg_pct": -1.73,
          "delivery": 0.82,
          "volume": 0.88,
          "call_oi": 40250,
          "put_oi": 22300
        }
      ]
    },
    {
      "symbol": "BRITANNIA",
      "rank": 160,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -9.5,
          3.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.15,
        "pcr_first": 1.26,
        "pcr_last": 0.96,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 11.98,
        "cumulative_price_chg_pct_window": -0.66,
        "persistence_score": -1.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -9.5,
          "signals": [
            "PCR 1.12 ABOVE 1.0 \u2014 put writers dominant",
            "PCR collapsing -0.20",
            "\u26a0 NEW SHORTS: FutOI +12.9% + Price -2.1%",
            "Del 1.15x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -2.14,
          "price_sign": -1,
          "pcr_d1": 1.26,
          "pcr_d2": 1.12,
          "pcr_chg": -0.2,
          "fut_oi_chg_pct": 12.93,
          "oi_sign": 1,
          "avg_del": 1.15,
          "peak_del": 1.75,
          "del_chg": 1.2,
          "avg_vol": 1.235,
          "call_oi_growth_pct": 172.77,
          "put_oi_growth_pct": 142.19,
          "opt_oi_growth_pct": 155.69,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.96 approaching bullish zone",
            "PCR collapsing -0.16",
            "Del 1.29x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.51,
          "price_sign": 1,
          "pcr_d1": 1.12,
          "pcr_d2": 0.96,
          "pcr_chg": -0.16,
          "fut_oi_chg_pct": -0.84,
          "oi_sign": -1,
          "avg_del": 1.295,
          "peak_del": 1.75,
          "del_chg": -0.91,
          "avg_vol": 1.4,
          "call_oi_growth_pct": 15.9,
          "put_oi_growth_pct": -0.77,
          "opt_oi_growth_pct": 7.08,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.94,
          "pcr": 1.26,
          "pcr_chg_1d": 0.34,
          "fut_oi": 2597750,
          "oi_chg_pct": 1.95,
          "delivery": 0.55,
          "volume": 0.53,
          "call_oi": 190500,
          "put_oi": 240875
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.14,
          "pcr": 1.12,
          "pcr_chg_1d": -0.2,
          "fut_oi": 2933750,
          "oi_chg_pct": 4.73,
          "delivery": 1.75,
          "volume": 1.94,
          "call_oi": 519625,
          "put_oi": 583375
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.51,
          "pcr": 0.96,
          "pcr_chg_1d": -0.16,
          "fut_oi": 2909000,
          "oi_chg_pct": -0.84,
          "delivery": 0.84,
          "volume": 0.86,
          "call_oi": 602250,
          "put_oi": 578875
        }
      ]
    },
    {
      "symbol": "MANKIND",
      "rank": 161,
      "days_available": 3,
      "latest_score": -3.0,
      "latest_tier": "WATCH (mild bearish)",
      "latest_sign": "bearish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.5,
          -3.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.085,
        "pcr_first": 0.67,
        "pcr_last": 0.5,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 3.02,
        "cumulative_price_chg_pct_window": 1.82,
        "persistence_score": -0.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": 4.5,
          "signals": [
            "PCR 0.56 neutral",
            "\u2605 NEW LONGS: FutOI +3.7% + Price +0.6%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.6,
          "price_sign": 1,
          "pcr_d1": 0.67,
          "pcr_d2": 0.56,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": 3.69,
          "oi_sign": 1,
          "avg_del": 0.895,
          "peak_del": 1.53,
          "del_chg": -1.27,
          "avg_vol": 0.915,
          "call_oi_growth_pct": 39.89,
          "put_oi_growth_pct": 16.22,
          "opt_oi_growth_pct": 30.4,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -3.0,
          "signals": [
            "PCR 0.50 call writers dominant",
            "PCR easing -0.06"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.21,
          "price_sign": 1,
          "pcr_d1": 0.56,
          "pcr_d2": 0.5,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": -0.65,
          "oi_sign": -1,
          "avg_del": 0.47,
          "peak_del": 0.68,
          "del_chg": 0.42,
          "avg_vol": 0.55,
          "call_oi_growth_pct": 16.24,
          "put_oi_growth_pct": 3.74,
          "opt_oi_growth_pct": 11.77,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.22,
          "pcr": 0.67,
          "pcr_chg_1d": 0.01,
          "fut_oi": 2707425,
          "oi_chg_pct": 2.42,
          "delivery": 1.53,
          "volume": 1.43,
          "call_oi": 317025,
          "put_oi": 212175
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.6,
          "pcr": 0.56,
          "pcr_chg_1d": 0.02,
          "fut_oi": 2807325,
          "oi_chg_pct": 1.8,
          "delivery": 0.26,
          "volume": 0.4,
          "call_oi": 443475,
          "put_oi": 246600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.21,
          "pcr": 0.5,
          "pcr_chg_1d": -0.06,
          "fut_oi": 2789100,
          "oi_chg_pct": -0.65,
          "delivery": 0.68,
          "volume": 0.7,
          "call_oi": 515475,
          "put_oi": 255825
        }
      ]
    },
    {
      "symbol": "NHPC",
      "rank": 162,
      "days_available": 3,
      "latest_score": -3.0,
      "latest_tier": "WATCH (mild bearish)",
      "latest_sign": "bearish",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild short build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (short)",
        "direction": "short",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          7.0,
          -3.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.025,
        "pcr_first": 0.63,
        "pcr_last": 0.58,
        "days_delivery_institutional": 3,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 14.26,
        "cumulative_price_chg_pct_window": 0.5,
        "persistence_score": 0.33,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": 7.0,
          "signals": [
            "PCR 0.59 neutral",
            "PCR easing -0.08",
            "\u2605 NEW LONGS: FutOI +8.2% + Price +0.5%",
            "Del 1.60x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 0.53,
          "price_sign": 1,
          "pcr_d1": 0.63,
          "pcr_d2": 0.59,
          "pcr_chg": -0.08,
          "fut_oi_chg_pct": 8.22,
          "oi_sign": 1,
          "avg_del": 1.605,
          "peak_del": 2.02,
          "del_chg": 0.83,
          "avg_vol": 2.1,
          "call_oi_growth_pct": 95.45,
          "put_oi_growth_pct": 81.72,
          "opt_oi_growth_pct": 90.14,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -3.0,
          "signals": [
            "PCR 0.58 neutral"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.03,
          "price_sign": 0,
          "pcr_d1": 0.59,
          "pcr_d2": 0.58,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": 5.58,
          "oi_sign": 1,
          "avg_del": 1.84,
          "peak_del": 2.02,
          "del_chg": -0.36,
          "avg_vol": 2.26,
          "call_oi_growth_pct": 5.79,
          "put_oi_growth_pct": 4.75,
          "opt_oi_growth_pct": 5.4,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.27,
          "pcr": 0.63,
          "pcr_chg_1d": 0.15,
          "fut_oi": 66400000,
          "oi_chg_pct": 2.65,
          "delivery": 1.19,
          "volume": 1.04,
          "call_oi": 21664000,
          "put_oi": 13651200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.53,
          "pcr": 0.59,
          "pcr_chg_1d": -0.08,
          "fut_oi": 71859200,
          "oi_chg_pct": 3.78,
          "delivery": 2.02,
          "volume": 3.16,
          "call_oi": 42342400,
          "put_oi": 24806400
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.03,
          "pcr": 0.58,
          "pcr_chg_1d": -0.01,
          "fut_oi": 75865600,
          "oi_chg_pct": 5.58,
          "delivery": 1.66,
          "volume": 1.36,
          "call_oi": 44793600,
          "put_oi": 25984000
        }
      ]
    },
    {
      "symbol": "SRF",
      "rank": 163,
      "days_available": 3,
      "latest_score": 3.0,
      "latest_tier": "WATCH (mild bullish)",
      "latest_sign": "bullish",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -8.5,
          3.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 1,
        "neutral_windows": 0,
        "total_windows": 2,
        "pcr_slope_7d": -0.165,
        "pcr_first": 1.03,
        "pcr_last": 0.7,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 19.61,
        "cumulative_price_chg_pct_window": 1.58,
        "persistence_score": -0.83,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -8.5,
          "signals": [
            "PCR 0.67 neutral",
            "PCR easing -0.05",
            "\u26a0 NEW SHORTS: FutOI +24.6% + Price -1.4%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -1.45,
          "price_sign": -1,
          "pcr_d1": 1.03,
          "pcr_d2": 0.67,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": 24.55,
          "oi_sign": 1,
          "avg_del": 0.75,
          "peak_del": 0.75,
          "del_chg": 0.0,
          "avg_vol": 0.825,
          "call_oi_growth_pct": 212.64,
          "put_oi_growth_pct": 103.47,
          "opt_oi_growth_pct": 157.29,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 3.0,
          "signals": [
            "PCR 0.70 neutral"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 3.07,
          "price_sign": 1,
          "pcr_d1": 0.67,
          "pcr_d2": 0.7,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -3.97,
          "oi_sign": -1,
          "avg_del": 0.875,
          "peak_del": 1.0,
          "del_chg": 0.25,
          "avg_vol": 0.86,
          "call_oi_growth_pct": -1.52,
          "put_oi_growth_pct": 3.41,
          "opt_oi_growth_pct": 0.46,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.81,
          "pcr": 1.03,
          "pcr_chg_1d": 0.04,
          "fut_oi": 3514400,
          "oi_chg_pct": 0.18,
          "delivery": 0.75,
          "volume": 0.78,
          "call_oi": 493600,
          "put_oi": 507600
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.45,
          "pcr": 0.67,
          "pcr_chg_1d": -0.05,
          "fut_oi": 4377200,
          "oi_chg_pct": 6.69,
          "delivery": 0.75,
          "volume": 0.87,
          "call_oi": 1543200,
          "put_oi": 1032800
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 3.07,
          "pcr": 0.7,
          "pcr_chg_1d": 0.03,
          "fut_oi": 4203600,
          "oi_chg_pct": -3.97,
          "delivery": 1.0,
          "volume": 0.85,
          "call_oi": 1519800,
          "put_oi": 1068000
        }
      ]
    },
    {
      "symbol": "PIIND",
      "rank": 164,
      "days_available": 3,
      "latest_score": 2.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          2.5,
          2.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 0,
        "neutral_windows": 2,
        "total_windows": 2,
        "pcr_slope_7d": -0.11,
        "pcr_first": 1.13,
        "pcr_last": 0.91,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -7.2,
        "cumulative_price_chg_pct_window": 2.61,
        "persistence_score": 2.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": 2.5,
          "signals": [
            "PCR 0.97 approaching bullish zone",
            "PCR rising +0.08"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 0.13,
          "price_sign": 0,
          "pcr_d1": 1.13,
          "pcr_d2": 0.97,
          "pcr_chg": 0.08,
          "fut_oi_chg_pct": -6.85,
          "oi_sign": -1,
          "avg_del": 1.245,
          "peak_del": 1.51,
          "del_chg": 0.53,
          "avg_vol": 1.21,
          "call_oi_growth_pct": 137.95,
          "put_oi_growth_pct": 103.87,
          "opt_oi_growth_pct": 119.9,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 2.5,
          "signals": [
            "PCR 0.91 approaching bullish zone",
            "PCR easing -0.06"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 2.48,
          "price_sign": 1,
          "pcr_d1": 0.97,
          "pcr_d2": 0.91,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": -0.38,
          "oi_sign": -1,
          "avg_del": 0.95,
          "peak_del": 1.51,
          "del_chg": -1.12,
          "avg_vol": 1.03,
          "call_oi_growth_pct": 47.57,
          "put_oi_growth_pct": 38.34,
          "opt_oi_growth_pct": 43.03,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.64,
          "pcr": 1.13,
          "pcr_chg_1d": 0.15,
          "fut_oi": 2797025,
          "oi_chg_pct": -0.48,
          "delivery": 0.98,
          "volume": 0.84,
          "call_oi": 208425,
          "put_oi": 234850
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.13,
          "pcr": 0.97,
          "pcr_chg_1d": 0.08,
          "fut_oi": 2605400,
          "oi_chg_pct": -2.44,
          "delivery": 1.51,
          "volume": 1.58,
          "call_oi": 495950,
          "put_oi": 478800
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.48,
          "pcr": 0.91,
          "pcr_chg_1d": -0.06,
          "fut_oi": 2595600,
          "oi_chg_pct": -0.38,
          "delivery": 0.39,
          "volume": 0.48,
          "call_oi": 731850,
          "put_oi": 662375
        }
      ]
    },
    {
      "symbol": "LTM",
      "rank": 165,
      "days_available": 3,
      "latest_score": -2.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u26a0 NEW SHORTS (Bearish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605\u2605 TC (SHORT)",
        "direction": "short",
        "count": 3
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.5,
          -2.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.04,
        "pcr_first": 0.99,
        "pcr_last": 0.91,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 13.3,
        "cumulative_price_chg_pct_window": -0.43,
        "persistence_score": -0.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 4.5,
          "signals": [
            "PCR 0.92 approaching bullish zone",
            "\u2605 NEW LONGS: FutOI +8.0% + Price +1.1%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": 1.08,
          "price_sign": 1,
          "pcr_d1": 0.99,
          "pcr_d2": 0.92,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 7.95,
          "oi_sign": 1,
          "avg_del": 0.595,
          "peak_del": 0.68,
          "del_chg": 0.17,
          "avg_vol": 0.685,
          "call_oi_growth_pct": 48.19,
          "put_oi_growth_pct": 37.72,
          "opt_oi_growth_pct": 42.97,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -2.5,
          "signals": [
            "PCR 0.91 approaching bullish zone",
            "\u26a0 NEW SHORTS: FutOI +5.0% + Price -1.5%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": -1.49,
          "price_sign": -1,
          "pcr_d1": 0.92,
          "pcr_d2": 0.91,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": 4.96,
          "oi_sign": 1,
          "avg_del": 0.695,
          "peak_del": 0.71,
          "del_chg": 0.03,
          "avg_vol": 0.86,
          "call_oi_growth_pct": 2.06,
          "put_oi_growth_pct": 1.11,
          "opt_oi_growth_pct": 1.6,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.32,
          "pcr": 0.99,
          "pcr_chg_1d": 0.03,
          "fut_oi": 3667650,
          "oi_chg_pct": 0.24,
          "delivery": 0.51,
          "volume": 0.54,
          "call_oi": 584550,
          "put_oi": 580200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.08,
          "pcr": 0.92,
          "pcr_chg_1d": 0.01,
          "fut_oi": 3959250,
          "oi_chg_pct": 1.81,
          "delivery": 0.68,
          "volume": 0.83,
          "call_oi": 866250,
          "put_oi": 799050
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -1.49,
          "pcr": 0.91,
          "pcr_chg_1d": -0.01,
          "fut_oi": 4155450,
          "oi_chg_pct": 4.96,
          "delivery": 0.71,
          "volume": 0.89,
          "call_oi": 884100,
          "put_oi": 807900
        }
      ]
    },
    {
      "symbol": "SWIGGY",
      "rank": 166,
      "days_available": 3,
      "latest_score": -2.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -7.5,
          -2.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.085,
        "pcr_first": 0.73,
        "pcr_last": 0.56,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.74,
        "cumulative_price_chg_pct_window": -0.95,
        "persistence_score": -4.17,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -7.5,
          "signals": [
            "PCR 0.65 neutral",
            "PCR easing -0.05",
            "\u26a0 NEW SHORTS: FutOI +3.1% + Price -2.1%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -2.07,
          "price_sign": -1,
          "pcr_d1": 0.73,
          "pcr_d2": 0.65,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": 3.11,
          "oi_sign": 1,
          "avg_del": 0.8,
          "peak_del": 1.2,
          "del_chg": -0.8,
          "avg_vol": 0.88,
          "call_oi_growth_pct": 54.17,
          "put_oi_growth_pct": 36.7,
          "opt_oi_growth_pct": 46.79,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -2.5,
          "signals": [
            "PCR 0.56 neutral",
            "PCR collapsing -0.09"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.14,
          "price_sign": 1,
          "pcr_d1": 0.65,
          "pcr_d2": 0.56,
          "pcr_chg": -0.09,
          "fut_oi_chg_pct": -2.3,
          "oi_sign": -1,
          "avg_del": 0.455,
          "peak_del": 0.51,
          "del_chg": 0.11,
          "avg_vol": 0.625,
          "call_oi_growth_pct": 26.99,
          "put_oi_growth_pct": 10.57,
          "opt_oi_growth_pct": 20.53,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.02,
          "pcr": 0.73,
          "pcr_chg_1d": -0.01,
          "fut_oi": 50785800,
          "oi_chg_pct": 2.89,
          "delivery": 1.2,
          "volume": 1.15,
          "call_oi": 4033900,
          "put_oi": 2951000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.07,
          "pcr": 0.65,
          "pcr_chg_1d": -0.05,
          "fut_oi": 52366600,
          "oi_chg_pct": 0.32,
          "delivery": 0.4,
          "volume": 0.61,
          "call_oi": 6219200,
          "put_oi": 4033900
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.14,
          "pcr": 0.56,
          "pcr_chg_1d": -0.09,
          "fut_oi": 51160200,
          "oi_chg_pct": -2.3,
          "delivery": 0.51,
          "volume": 0.64,
          "call_oi": 7897500,
          "put_oi": 4460300
        }
      ]
    },
    {
      "symbol": "MPHASIS",
      "rank": 167,
      "days_available": 3,
      "latest_score": -2.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "phase_1_short",
      "latest_interpretation": "Mild short build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          7.5,
          -2.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.12,
        "pcr_first": 0.7,
        "pcr_last": 0.94,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.75,
        "cumulative_price_chg_pct_window": -1.03,
        "persistence_score": 0.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 7.5,
          "signals": [
            "PCR 0.91 approaching bullish zone",
            "PCR surging +0.13"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 1.47,
          "price_sign": 1,
          "pcr_d1": 0.7,
          "pcr_d2": 0.91,
          "pcr_chg": 0.13,
          "fut_oi_chg_pct": -0.56,
          "oi_sign": -1,
          "avg_del": 0.98,
          "peak_del": 1.16,
          "del_chg": -0.36,
          "avg_vol": 1.0,
          "call_oi_growth_pct": 117.7,
          "put_oi_growth_pct": 182.74,
          "opt_oi_growth_pct": 144.48,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -2.5,
          "signals": [
            "PCR 0.94 approaching bullish zone"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -2.46,
          "price_sign": -1,
          "pcr_d1": 0.91,
          "pcr_d2": 0.94,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 1.32,
          "oi_sign": 1,
          "avg_del": 0.985,
          "peak_del": 1.17,
          "del_chg": 0.37,
          "avg_vol": 1.065,
          "call_oi_growth_pct": 7.98,
          "put_oi_growth_pct": 11.68,
          "opt_oi_growth_pct": 9.74,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.07,
          "pcr": 0.7,
          "pcr_chg_1d": -0.01,
          "fut_oi": 4890600,
          "oi_chg_pct": -2.99,
          "delivery": 1.16,
          "volume": 1.16,
          "call_oi": 416350,
          "put_oi": 291500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.47,
          "pcr": 0.91,
          "pcr_chg_1d": 0.13,
          "fut_oi": 4863100,
          "oi_chg_pct": -1.02,
          "delivery": 0.8,
          "volume": 0.84,
          "call_oi": 906400,
          "put_oi": 824175
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -2.46,
          "pcr": 0.94,
          "pcr_chg_1d": 0.03,
          "fut_oi": 4927450,
          "oi_chg_pct": 1.32,
          "delivery": 1.17,
          "volume": 1.29,
          "call_oi": 978725,
          "put_oi": 920425
        }
      ]
    },
    {
      "symbol": "TATAELXSI",
      "rank": 168,
      "days_available": 3,
      "latest_score": -2.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild short build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (short)",
        "direction": "short",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.5,
          -2.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.045,
        "pcr_first": 0.63,
        "pcr_last": 0.72,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.81,
        "cumulative_price_chg_pct_window": 0.25,
        "persistence_score": -0.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 4.5,
          "signals": [
            "PCR 0.74 neutral",
            "PCR rising +0.08"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 0.4,
          "price_sign": 1,
          "pcr_d1": 0.63,
          "pcr_d2": 0.74,
          "pcr_chg": 0.08,
          "fut_oi_chg_pct": -2.71,
          "oi_sign": -1,
          "avg_del": 0.695,
          "peak_del": 0.87,
          "del_chg": 0.35,
          "avg_vol": 0.795,
          "call_oi_growth_pct": 31.39,
          "put_oi_growth_pct": 52.79,
          "opt_oi_growth_pct": 39.69,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -2.5,
          "signals": [
            "PCR 0.72 neutral"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.15,
          "price_sign": 0,
          "pcr_d1": 0.74,
          "pcr_d2": 0.72,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 3.62,
          "oi_sign": 1,
          "avg_del": 0.88,
          "peak_del": 0.89,
          "del_chg": 0.02,
          "avg_vol": 0.755,
          "call_oi_growth_pct": 7.36,
          "put_oi_growth_pct": 4.34,
          "opt_oi_growth_pct": 6.08,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.78,
          "pcr": 0.63,
          "pcr_chg_1d": -0.03,
          "fut_oi": 1738900,
          "oi_chg_pct": -1.91,
          "delivery": 0.52,
          "volume": 0.86,
          "call_oi": 449800,
          "put_oi": 285100
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.4,
          "pcr": 0.74,
          "pcr_chg_1d": 0.08,
          "fut_oi": 1691800,
          "oi_chg_pct": -0.15,
          "delivery": 0.87,
          "volume": 0.73,
          "call_oi": 591000,
          "put_oi": 435600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.15,
          "pcr": 0.72,
          "pcr_chg_1d": -0.02,
          "fut_oi": 1753000,
          "oi_chg_pct": 3.62,
          "delivery": 0.89,
          "volume": 0.78,
          "call_oi": 634500,
          "put_oi": 454500
        }
      ]
    },
    {
      "symbol": "VMM",
      "rank": 169,
      "days_available": 3,
      "latest_score": 2.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "phase_1_long",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -10.0,
          2.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.255,
        "pcr_first": 1.15,
        "pcr_last": 0.64,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 449.27,
        "cumulative_price_chg_pct_window": -1.79,
        "persistence_score": -1.67,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -10.0,
          "signals": [
            "PCR 0.78 neutral-to-bullish",
            "PCR collapsing -0.10",
            "\u26a0 NEW SHORTS: FutOI +435.3% + Price -3.9%",
            "Del 1.34x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -3.88,
          "price_sign": -1,
          "pcr_d1": 1.15,
          "pcr_d2": 0.78,
          "pcr_chg": -0.1,
          "fut_oi_chg_pct": 435.33,
          "oi_sign": 1,
          "avg_del": 1.345,
          "peak_del": 1.46,
          "del_chg": 0.23,
          "avg_vol": 1.285,
          "call_oi_growth_pct": 343.89,
          "put_oi_growth_pct": 199.61,
          "opt_oi_growth_pct": 266.6,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 2.5,
          "signals": [
            "PCR 0.64 neutral",
            "PCR collapsing -0.14",
            "\u2605 NEW LONGS: FutOI +2.6% + Price +2.2%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 2.17,
          "price_sign": 1,
          "pcr_d1": 0.78,
          "pcr_d2": 0.64,
          "pcr_chg": -0.14,
          "fut_oi_chg_pct": 2.6,
          "oi_sign": 1,
          "avg_del": 0.945,
          "peak_del": 1.46,
          "del_chg": -1.03,
          "avg_vol": 0.935,
          "call_oi_growth_pct": 21.92,
          "put_oi_growth_pct": 0.79,
          "opt_oi_growth_pct": 12.66,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.18,
          "pcr": 1.15,
          "pcr_chg_1d": 0.0,
          "fut_oi": 3652050,
          "oi_chg_pct": 0.0,
          "delivery": 1.23,
          "volume": 1.13,
          "call_oi": 1071850,
          "put_oi": 1236750
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -3.88,
          "pcr": 0.78,
          "pcr_chg_1d": -0.1,
          "fut_oi": 19550350,
          "oi_chg_pct": 7.81,
          "delivery": 1.46,
          "volume": 1.44,
          "call_oi": 4757850,
          "put_oi": 3705400
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.17,
          "pcr": 0.64,
          "pcr_chg_1d": -0.14,
          "fut_oi": 20059600,
          "oi_chg_pct": 2.6,
          "delivery": 0.43,
          "volume": 0.43,
          "call_oi": 5800600,
          "put_oi": 3734500
        }
      ]
    },
    {
      "symbol": "NUVAMA",
      "rank": 170,
      "days_available": 3,
      "latest_score": 2.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.5,
          2.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 0,
        "neutral_windows": 2,
        "total_windows": 2,
        "pcr_slope_7d": -0.005,
        "pcr_first": 0.8,
        "pcr_last": 0.79,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 4.77,
        "cumulative_price_chg_pct_window": 1.99,
        "persistence_score": 2.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": 1.5,
          "signals": [
            "PCR 0.74 neutral",
            "PCR collapsing -0.10",
            "\u2605 NEW LONGS: FutOI +5.5% + Price +1.1%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.08,
          "price_sign": 1,
          "pcr_d1": 0.8,
          "pcr_d2": 0.74,
          "pcr_chg": -0.1,
          "fut_oi_chg_pct": 5.48,
          "oi_sign": 1,
          "avg_del": 0.73,
          "peak_del": 1.0,
          "del_chg": -0.54,
          "avg_vol": 0.975,
          "call_oi_growth_pct": 59.0,
          "put_oi_growth_pct": 48.73,
          "opt_oi_growth_pct": 54.45,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 2.5,
          "signals": [
            "PCR 0.79 neutral-to-bullish",
            "PCR rising +0.05"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.9,
          "price_sign": 1,
          "pcr_d1": 0.74,
          "pcr_d2": 0.79,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": -0.67,
          "oi_sign": -1,
          "avg_del": 0.485,
          "peak_del": 0.51,
          "del_chg": 0.05,
          "avg_vol": 0.56,
          "call_oi_growth_pct": -0.94,
          "put_oi_growth_pct": 5.31,
          "opt_oi_growth_pct": 1.73,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -1.91,
          "pcr": 0.8,
          "pcr_chg_1d": -0.4,
          "fut_oi": 1899000,
          "oi_chg_pct": 13.04,
          "delivery": 1.0,
          "volume": 1.32,
          "call_oi": 469500,
          "put_oi": 373500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.08,
          "pcr": 0.74,
          "pcr_chg_1d": -0.1,
          "fut_oi": 2003000,
          "oi_chg_pct": -0.1,
          "delivery": 0.46,
          "volume": 0.63,
          "call_oi": 746500,
          "put_oi": 555500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.9,
          "pcr": 0.79,
          "pcr_chg_1d": 0.05,
          "fut_oi": 1989500,
          "oi_chg_pct": -0.67,
          "delivery": 0.51,
          "volume": 0.49,
          "call_oi": 739500,
          "put_oi": 585000
        }
      ]
    },
    {
      "symbol": "HAVELLS",
      "rank": 171,
      "days_available": 3,
      "latest_score": 2.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          8.5,
          2.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.025,
        "pcr_first": 0.77,
        "pcr_last": 0.82,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -0.27,
        "cumulative_price_chg_pct_window": 2.83,
        "persistence_score": 4.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 8.5,
          "signals": [
            "PCR 0.86 approaching bullish zone"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.85,
          "price_sign": 1,
          "pcr_d1": 0.77,
          "pcr_d2": 0.86,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": 1.3,
          "oi_sign": 1,
          "avg_del": 0.84,
          "peak_del": 1.32,
          "del_chg": 0.96,
          "avg_vol": 0.82,
          "call_oi_growth_pct": 62.45,
          "put_oi_growth_pct": 80.51,
          "opt_oi_growth_pct": 70.33,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 2.0,
          "signals": [
            "PCR 0.82 neutral-to-bullish",
            "PCR easing -0.04",
            "Del 1.09x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.96,
          "price_sign": 1,
          "pcr_d1": 0.86,
          "pcr_d2": 0.82,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": -1.55,
          "oi_sign": -1,
          "avg_del": 1.095,
          "peak_del": 1.32,
          "del_chg": -0.45,
          "avg_vol": 0.97,
          "call_oi_growth_pct": 7.63,
          "put_oi_growth_pct": 2.37,
          "opt_oi_growth_pct": 5.2,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.39,
          "pcr": 0.77,
          "pcr_chg_1d": -0.26,
          "fut_oi": 8300500,
          "oi_chg_pct": 2.71,
          "delivery": 0.36,
          "volume": 0.48,
          "call_oi": 1149000,
          "put_oi": 890000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.85,
          "pcr": 0.86,
          "pcr_chg_1d": -0.01,
          "fut_oi": 8408000,
          "oi_chg_pct": -1.01,
          "delivery": 1.32,
          "volume": 1.16,
          "call_oi": 1866500,
          "put_oi": 1606500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.96,
          "pcr": 0.82,
          "pcr_chg_1d": -0.04,
          "fut_oi": 8278000,
          "oi_chg_pct": -1.55,
          "delivery": 0.87,
          "volume": 0.78,
          "call_oi": 2009000,
          "put_oi": 1644500
        }
      ]
    },
    {
      "symbol": "BANKINDIA",
      "rank": 172,
      "days_available": 3,
      "latest_score": 2.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -0.5,
          2.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 0,
        "neutral_windows": 2,
        "total_windows": 2,
        "pcr_slope_7d": -0.05,
        "pcr_first": 1.19,
        "pcr_last": 1.09,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 8.36,
        "cumulative_price_chg_pct_window": 0.98,
        "persistence_score": 1.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -0.5,
          "signals": [
            "PCR 1.19 ABOVE 1.0 \u2014 put writers dominant",
            "PCR surging +0.15",
            "\u26a0 NEW SHORTS: FutOI +12.3% + Price -1.5%",
            "Del 1.03x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_short",
          "price_chg_pct": -1.5,
          "price_sign": -1,
          "pcr_d1": 1.19,
          "pcr_d2": 1.19,
          "pcr_chg": 0.15,
          "fut_oi_chg_pct": 12.33,
          "oi_sign": 1,
          "avg_del": 1.03,
          "peak_del": 1.28,
          "del_chg": -0.5,
          "avg_vol": 1.045,
          "call_oi_growth_pct": 96.73,
          "put_oi_growth_pct": 96.76,
          "opt_oi_growth_pct": 96.75,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 2.0,
          "signals": [
            "PCR 1.09 ABOVE 1.0 \u2014 put writers dominant",
            "PCR collapsing -0.10"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 2.52,
          "price_sign": 1,
          "pcr_d1": 1.19,
          "pcr_d2": 1.09,
          "pcr_chg": -0.1,
          "fut_oi_chg_pct": -3.53,
          "oi_sign": -1,
          "avg_del": 0.675,
          "peak_del": 0.78,
          "del_chg": -0.21,
          "avg_vol": 0.685,
          "call_oi_growth_pct": 13.38,
          "put_oi_growth_pct": 3.19,
          "opt_oi_growth_pct": 7.84,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.44,
          "pcr": 1.19,
          "pcr_chg_1d": -0.05,
          "fut_oi": 51724400,
          "oi_chg_pct": 4.43,
          "delivery": 1.28,
          "volume": 1.32,
          "call_oi": 8892000,
          "put_oi": 10602800
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.5,
          "pcr": 1.19,
          "pcr_chg_1d": 0.15,
          "fut_oi": 58099600,
          "oi_chg_pct": 3.73,
          "delivery": 0.78,
          "volume": 0.77,
          "call_oi": 17492800,
          "put_oi": 20862400
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.52,
          "pcr": 1.09,
          "pcr_chg_1d": -0.1,
          "fut_oi": 56050800,
          "oi_chg_pct": -3.53,
          "delivery": 0.57,
          "volume": 0.6,
          "call_oi": 19832800,
          "put_oi": 21528000
        }
      ]
    },
    {
      "symbol": "BDL",
      "rank": 173,
      "days_available": 3,
      "latest_score": 2.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          6.5,
          2.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.04,
        "pcr_first": 0.87,
        "pcr_last": 0.79,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -6.36,
        "cumulative_price_chg_pct_window": 4.22,
        "persistence_score": 3.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 6.5,
          "signals": [
            "PCR 0.84 neutral-to-bullish",
            "PCR rising +0.07",
            "Del 1.17x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 2.64,
          "price_sign": 1,
          "pcr_d1": 0.87,
          "pcr_d2": 0.84,
          "pcr_chg": 0.07,
          "fut_oi_chg_pct": -5.91,
          "oi_sign": -1,
          "avg_del": 1.165,
          "peak_del": 1.32,
          "del_chg": 0.31,
          "avg_vol": 1.62,
          "call_oi_growth_pct": 18.95,
          "put_oi_growth_pct": 15.63,
          "opt_oi_growth_pct": 17.41,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 2.0,
          "signals": [
            "PCR 0.79 neutral-to-bullish",
            "PCR easing -0.05",
            "Del 1.04x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.54,
          "price_sign": 1,
          "pcr_d1": 0.84,
          "pcr_d2": 0.79,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": -0.48,
          "oi_sign": -1,
          "avg_del": 1.045,
          "peak_del": 1.32,
          "del_chg": -0.55,
          "avg_vol": 1.0,
          "call_oi_growth_pct": 8.94,
          "put_oi_growth_pct": 2.84,
          "opt_oi_growth_pct": 6.15,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 9.78,
          "pcr": 0.87,
          "pcr_chg_1d": 0.07,
          "fut_oi": 4254600,
          "oi_chg_pct": -6.82,
          "delivery": 1.01,
          "volume": 1.93,
          "call_oi": 2144800,
          "put_oi": 1856750
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 2.64,
          "pcr": 0.84,
          "pcr_chg_1d": 0.07,
          "fut_oi": 4003300,
          "oi_chg_pct": 1.41,
          "delivery": 1.32,
          "volume": 1.31,
          "call_oi": 2551150,
          "put_oi": 2146900
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.54,
          "pcr": 0.79,
          "pcr_chg_1d": -0.05,
          "fut_oi": 3984050,
          "oi_chg_pct": -0.48,
          "delivery": 0.77,
          "volume": 0.69,
          "call_oi": 2779350,
          "put_oi": 2207800
        }
      ]
    },
    {
      "symbol": "INDUSTOWER",
      "rank": 174,
      "days_available": 3,
      "latest_score": 2.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u25cb NONE",
        "direction": "none",
        "count": 0
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -8.5,
          2.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.14,
        "pcr_first": 0.98,
        "pcr_last": 0.7,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 3.42,
        "cumulative_price_chg_pct_window": -0.71,
        "persistence_score": -1.5,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -8.5,
          "signals": [
            "PCR 0.70 neutral",
            "PCR collapsing -0.20",
            "\u26a0 NEW SHORTS: FutOI +4.2% + Price -0.6%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.57,
          "price_sign": -1,
          "pcr_d1": 0.98,
          "pcr_d2": 0.7,
          "pcr_chg": -0.2,
          "fut_oi_chg_pct": 4.15,
          "oi_sign": 1,
          "avg_del": 0.765,
          "peak_del": 0.77,
          "del_chg": -0.01,
          "avg_vol": 0.835,
          "call_oi_growth_pct": 146.29,
          "put_oi_growth_pct": 76.89,
          "opt_oi_growth_pct": 112.03,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 2.0,
          "signals": [
            "PCR 0.70 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 0
          },
          "phase": "no_signal",
          "price_chg_pct": -0.14,
          "price_sign": 0,
          "pcr_d1": 0.7,
          "pcr_d2": 0.7,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -0.7,
          "oi_sign": -1,
          "avg_del": 1.135,
          "peak_del": 1.51,
          "del_chg": 0.75,
          "avg_vol": 1.135,
          "call_oi_growth_pct": 6.93,
          "put_oi_growth_pct": 7.06,
          "opt_oi_growth_pct": 6.99,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.22,
          "pcr": 0.98,
          "pcr_chg_1d": -0.09,
          "fut_oi": 63075100,
          "oi_chg_pct": -0.66,
          "delivery": 0.77,
          "volume": 0.74,
          "call_oi": 5038800,
          "put_oi": 4913000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.57,
          "pcr": 0.7,
          "pcr_chg_1d": -0.2,
          "fut_oi": 65694800,
          "oi_chg_pct": 1.6,
          "delivery": 0.76,
          "volume": 0.93,
          "call_oi": 12410000,
          "put_oi": 8690400
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.14,
          "pcr": 0.7,
          "pcr_chg_1d": 0.0,
          "fut_oi": 65232400,
          "oi_chg_pct": -0.7,
          "delivery": 1.51,
          "volume": 1.34,
          "call_oi": 13270200,
          "put_oi": 9304100
        }
      ]
    },
    {
      "symbol": "CONCOR",
      "rank": 175,
      "days_available": 3,
      "latest_score": 2.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u25cb NONE",
        "direction": "none",
        "count": 0
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.5,
          2.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.15,
        "pcr_first": 1.08,
        "pcr_last": 0.78,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.61,
        "cumulative_price_chg_pct_window": 2.11,
        "persistence_score": 2.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 4.5,
          "signals": [
            "PCR 0.78 neutral-to-bullish",
            "PCR easing -0.08",
            "\u2605 NEW LONGS: FutOI +2.0% + Price +1.8%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 1.8,
          "price_sign": 1,
          "pcr_d1": 1.08,
          "pcr_d2": 0.78,
          "pcr_chg": -0.08,
          "fut_oi_chg_pct": 2.03,
          "oi_sign": 1,
          "avg_del": 0.73,
          "peak_del": 1.14,
          "del_chg": 0.82,
          "avg_vol": 0.935,
          "call_oi_growth_pct": 66.14,
          "put_oi_growth_pct": 20.1,
          "opt_oi_growth_pct": 42.24,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 2.0,
          "signals": [
            "PCR 0.78 neutral-to-bullish"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 0
          },
          "phase": "no_signal",
          "price_chg_pct": 0.3,
          "price_sign": 0,
          "pcr_d1": 0.78,
          "pcr_d2": 0.78,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -1.39,
          "oi_sign": -1,
          "avg_del": 1.19,
          "peak_del": 1.24,
          "del_chg": 0.1,
          "avg_vol": 1.255,
          "call_oi_growth_pct": -1.02,
          "put_oi_growth_pct": -1.57,
          "opt_oi_growth_pct": -1.26,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.53,
          "pcr": 1.08,
          "pcr_chg_1d": -0.08,
          "fut_oi": 25626250,
          "oi_chg_pct": 0.66,
          "delivery": 0.32,
          "volume": 0.48,
          "call_oi": 3381250,
          "put_oi": 3650000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.8,
          "pcr": 0.78,
          "pcr_chg_1d": -0.08,
          "fut_oi": 26146250,
          "oi_chg_pct": 0.37,
          "delivery": 1.14,
          "volume": 1.39,
          "call_oi": 5617500,
          "put_oi": 4383750
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.3,
          "pcr": 0.78,
          "pcr_chg_1d": 0.0,
          "fut_oi": 25782500,
          "oi_chg_pct": -1.39,
          "delivery": 1.24,
          "volume": 1.12,
          "call_oi": 5560000,
          "put_oi": 4315000
        }
      ]
    },
    {
      "symbol": "INDUSINDBK",
      "rank": 176,
      "days_available": 3,
      "latest_score": 2.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.5,
          2.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 0,
        "neutral_windows": 2,
        "total_windows": 2,
        "pcr_slope_7d": -0.115,
        "pcr_first": 1.22,
        "pcr_last": 0.99,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -3.37,
        "cumulative_price_chg_pct_window": -0.6,
        "persistence_score": 0.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -2.5,
          "signals": [
            "PCR 1.05 ABOVE 1.0 \u2014 put writers dominant"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -2.56,
          "price_sign": -1,
          "pcr_d1": 1.22,
          "pcr_d2": 1.05,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": -2.6,
          "oi_sign": -1,
          "avg_del": 0.75,
          "peak_del": 0.76,
          "del_chg": -0.02,
          "avg_vol": 0.81,
          "call_oi_growth_pct": 62.38,
          "put_oi_growth_pct": 40.52,
          "opt_oi_growth_pct": 50.38,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 2.0,
          "signals": [
            "PCR 0.99 approaching bullish zone",
            "PCR easing -0.06"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 2.01,
          "price_sign": 1,
          "pcr_d1": 1.05,
          "pcr_d2": 0.99,
          "pcr_chg": -0.06,
          "fut_oi_chg_pct": -0.79,
          "oi_sign": -1,
          "avg_del": 0.625,
          "peak_del": 0.74,
          "del_chg": -0.23,
          "avg_vol": 0.76,
          "call_oi_growth_pct": 4.36,
          "put_oi_growth_pct": -1.49,
          "opt_oi_growth_pct": 1.36,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.41,
          "pcr": 1.22,
          "pcr_chg_1d": 0.03,
          "fut_oi": 39513600,
          "oi_chg_pct": -0.24,
          "delivery": 0.76,
          "volume": 0.72,
          "call_oi": 3632300,
          "put_oi": 4421200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.56,
          "pcr": 1.05,
          "pcr_chg_1d": 0.02,
          "fut_oi": 38488100,
          "oi_chg_pct": -0.68,
          "delivery": 0.74,
          "volume": 0.9,
          "call_oi": 5898200,
          "put_oi": 6212500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.01,
          "pcr": 0.99,
          "pcr_chg_1d": -0.06,
          "fut_oi": 38182200,
          "oi_chg_pct": -0.79,
          "delivery": 0.51,
          "volume": 0.62,
          "call_oi": 6155100,
          "put_oi": 6120100
        }
      ]
    },
    {
      "symbol": "PERSISTENT",
      "rank": 177,
      "days_available": 3,
      "latest_score": -2.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          8.5,
          -2.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.035,
        "pcr_first": 0.89,
        "pcr_last": 0.96,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 2.95,
        "cumulative_price_chg_pct_window": 1.0,
        "persistence_score": 1.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 8.5,
          "signals": [
            "PCR 0.95 approaching bullish zone",
            "PCR rising +0.04",
            "\u2605 NEW LONGS: FutOI +3.6% + Price +1.8%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": 1.81,
          "price_sign": 1,
          "pcr_d1": 0.89,
          "pcr_d2": 0.95,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": 3.63,
          "oi_sign": 1,
          "avg_del": 0.695,
          "peak_del": 0.78,
          "del_chg": 0.17,
          "avg_vol": 0.74,
          "call_oi_growth_pct": 41.97,
          "put_oi_growth_pct": 51.64,
          "opt_oi_growth_pct": 46.53,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -2.0,
          "signals": [
            "PCR 0.96 approaching bullish zone",
            "Del 1.08x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.8,
          "price_sign": -1,
          "pcr_d1": 0.95,
          "pcr_d2": 0.96,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": -0.65,
          "oi_sign": -1,
          "avg_del": 1.08,
          "peak_del": 1.38,
          "del_chg": 0.6,
          "avg_vol": 1.025,
          "call_oi_growth_pct": 3.59,
          "put_oi_growth_pct": 4.62,
          "opt_oi_growth_pct": 4.09,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.52,
          "pcr": 0.89,
          "pcr_chg_1d": 0.13,
          "fut_oi": 5413700,
          "oi_chg_pct": 0.07,
          "delivery": 0.61,
          "volume": 0.67,
          "call_oi": 618100,
          "put_oi": 552300
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.81,
          "pcr": 0.95,
          "pcr_chg_1d": 0.04,
          "fut_oi": 5610100,
          "oi_chg_pct": -0.19,
          "delivery": 0.78,
          "volume": 0.81,
          "call_oi": 877500,
          "put_oi": 837500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.8,
          "pcr": 0.96,
          "pcr_chg_1d": 0.01,
          "fut_oi": 5573600,
          "oi_chg_pct": -0.65,
          "delivery": 1.38,
          "volume": 1.24,
          "call_oi": 909000,
          "put_oi": 876200
        }
      ]
    },
    {
      "symbol": "NTPC",
      "rank": 178,
      "days_available": 3,
      "latest_score": -2.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          2.0,
          -2.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 0,
        "neutral_windows": 2,
        "total_windows": 2,
        "pcr_slope_7d": -0.11,
        "pcr_first": 0.67,
        "pcr_last": 0.45,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 3.59,
        "cumulative_price_chg_pct_window": 1.6,
        "persistence_score": -0.67,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": 2.0,
          "signals": [
            "PCR 0.49 call writers dominant",
            "PCR easing -0.04",
            "\u2605 NEW LONGS: FutOI +4.2% + Price +1.2%",
            "Del 1.04x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.2,
          "price_sign": 1,
          "pcr_d1": 0.67,
          "pcr_d2": 0.49,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 4.24,
          "oi_sign": 1,
          "avg_del": 1.04,
          "peak_del": 1.04,
          "del_chg": 0.0,
          "avg_vol": 1.16,
          "call_oi_growth_pct": 105.11,
          "put_oi_growth_pct": 49.62,
          "opt_oi_growth_pct": 82.92,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -2.0,
          "signals": [
            "PCR 0.45 call writers dominant",
            "PCR easing -0.04"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.4,
          "price_sign": 1,
          "pcr_d1": 0.49,
          "pcr_d2": 0.45,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": -0.63,
          "oi_sign": -1,
          "avg_del": 0.965,
          "peak_del": 1.04,
          "del_chg": -0.15,
          "avg_vol": 1.085,
          "call_oi_growth_pct": 12.58,
          "put_oi_growth_pct": 4.16,
          "opt_oi_growth_pct": 9.83,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -1.62,
          "pcr": 0.67,
          "pcr_chg_1d": -0.16,
          "fut_oi": 84003000,
          "oi_chg_pct": 0.97,
          "delivery": 1.04,
          "volume": 1.1,
          "call_oi": 17590500,
          "put_oi": 11725500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.2,
          "pcr": 0.49,
          "pcr_chg_1d": -0.04,
          "fut_oi": 87567000,
          "oi_chg_pct": 1.55,
          "delivery": 1.04,
          "volume": 1.22,
          "call_oi": 36079500,
          "put_oi": 17544000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.4,
          "pcr": 0.45,
          "pcr_chg_1d": -0.04,
          "fut_oi": 87015000,
          "oi_chg_pct": -0.63,
          "delivery": 0.89,
          "volume": 0.95,
          "call_oi": 40618500,
          "put_oi": 18274500
        }
      ]
    },
    {
      "symbol": "HDFCBANK",
      "rank": 179,
      "days_available": 3,
      "latest_score": 2.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -3.5,
          2.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.07,
        "pcr_first": 0.49,
        "pcr_last": 0.63,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -8.05,
        "cumulative_price_chg_pct_window": -0.71,
        "persistence_score": 0.17,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -3.5,
          "signals": [
            "PCR 0.59 neutral",
            "PCR easing -0.04"
          ],
          "interpretation": "\u2193 LONG LIQUIDATION (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -2.25,
          "price_sign": -1,
          "pcr_d1": 0.49,
          "pcr_d2": 0.59,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": -7.22,
          "oi_sign": -1,
          "avg_del": 0.89,
          "peak_del": 1.14,
          "del_chg": -0.5,
          "avg_vol": 0.96,
          "call_oi_growth_pct": 7.62,
          "put_oi_growth_pct": 30.26,
          "opt_oi_growth_pct": 15.05,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 2.0,
          "signals": [
            "PCR 0.63 neutral",
            "PCR rising +0.04"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.58,
          "price_sign": 1,
          "pcr_d1": 0.59,
          "pcr_d2": 0.63,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": -0.89,
          "oi_sign": -1,
          "avg_del": 0.695,
          "peak_del": 0.75,
          "del_chg": 0.11,
          "avg_vol": 0.78,
          "call_oi_growth_pct": -3.79,
          "put_oi_growth_pct": 2.9,
          "opt_oi_growth_pct": -1.3,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.46,
          "pcr": 0.49,
          "pcr_chg_1d": -0.04,
          "fut_oi": 364433850,
          "oi_chg_pct": 1.79,
          "delivery": 1.14,
          "volume": 1.09,
          "call_oi": 66173800,
          "put_oi": 32283900
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.25,
          "pcr": 0.59,
          "pcr_chg_1d": -0.04,
          "fut_oi": 338103700,
          "oi_chg_pct": 1.75,
          "delivery": 0.64,
          "volume": 0.83,
          "call_oi": 71218400,
          "put_oi": 42053000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.58,
          "pcr": 0.63,
          "pcr_chg_1d": 0.04,
          "fut_oi": 335092450,
          "oi_chg_pct": -0.89,
          "delivery": 0.75,
          "volume": 0.73,
          "call_oi": 68522300,
          "put_oi": 43274000
        }
      ]
    },
    {
      "symbol": "LICHSGFIN",
      "rank": 180,
      "days_available": 3,
      "latest_score": 2.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u25cb NONE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          3.5,
          2.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.09,
        "pcr_first": 1.29,
        "pcr_last": 1.11,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 0,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.36,
        "cumulative_price_chg_pct_window": 0.39,
        "persistence_score": 2.5,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 3.5,
          "signals": [
            "PCR 1.16 ABOVE 1.0 \u2014 put writers dominant",
            "PCR collapsing -0.09"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.51,
          "price_sign": 1,
          "pcr_d1": 1.29,
          "pcr_d2": 1.16,
          "pcr_chg": -0.09,
          "fut_oi_chg_pct": 0.81,
          "oi_sign": 1,
          "avg_del": 0.57,
          "peak_del": 0.68,
          "del_chg": 0.22,
          "avg_vol": 0.595,
          "call_oi_growth_pct": 10.46,
          "put_oi_growth_pct": -0.86,
          "opt_oi_growth_pct": 4.08,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 2.0,
          "signals": [
            "PCR 1.11 ABOVE 1.0 \u2014 put writers dominant",
            "PCR easing -0.05"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.12,
          "price_sign": 0,
          "pcr_d1": 1.16,
          "pcr_d2": 1.11,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": -0.44,
          "oi_sign": -1,
          "avg_del": 0.645,
          "peak_del": 0.68,
          "del_chg": -0.07,
          "avg_vol": 0.72,
          "call_oi_growth_pct": 4.14,
          "put_oi_growth_pct": 0.12,
          "opt_oi_growth_pct": 1.98,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.1,
          "pcr": 1.29,
          "pcr_chg_1d": -0.05,
          "fut_oi": 33282000,
          "oi_chg_pct": 1.12,
          "delivery": 0.46,
          "volume": 0.5,
          "call_oi": 3959000,
          "put_oi": 5110000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.51,
          "pcr": 1.16,
          "pcr_chg_1d": -0.09,
          "fut_oi": 33550000,
          "oi_chg_pct": -0.33,
          "delivery": 0.68,
          "volume": 0.69,
          "call_oi": 4373000,
          "put_oi": 5066000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.12,
          "pcr": 1.11,
          "pcr_chg_1d": -0.05,
          "fut_oi": 33401000,
          "oi_chg_pct": -0.44,
          "delivery": 0.61,
          "volume": 0.75,
          "call_oi": 4554000,
          "put_oi": 5072000
        }
      ]
    },
    {
      "symbol": "BEL",
      "rank": 181,
      "days_available": 3,
      "latest_score": 2.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          3.0,
          2.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.01,
        "pcr_first": 0.67,
        "pcr_last": 0.65,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -2.55,
        "cumulative_price_chg_pct_window": 2.16,
        "persistence_score": 2.33,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 3.0,
          "signals": [
            "PCR 0.66 neutral",
            "PCR rising +0.05"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.54,
          "price_sign": 1,
          "pcr_d1": 0.67,
          "pcr_d2": 0.66,
          "pcr_chg": 0.05,
          "fut_oi_chg_pct": -2.44,
          "oi_sign": -1,
          "avg_del": 0.985,
          "peak_del": 1.11,
          "del_chg": 0.25,
          "avg_vol": 1.24,
          "call_oi_growth_pct": 26.36,
          "put_oi_growth_pct": 23.74,
          "opt_oi_growth_pct": 25.31,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 2.0,
          "signals": [
            "PCR 0.65 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.61,
          "price_sign": 1,
          "pcr_d1": 0.66,
          "pcr_d2": 0.65,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -0.11,
          "oi_sign": -1,
          "avg_del": 0.885,
          "peak_del": 1.11,
          "del_chg": -0.45,
          "avg_vol": 0.885,
          "call_oi_growth_pct": 2.24,
          "put_oi_growth_pct": 1.54,
          "opt_oi_growth_pct": 1.96,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.51,
          "pcr": 0.67,
          "pcr_chg_1d": 0.01,
          "fut_oi": 105110850,
          "oi_chg_pct": -3.96,
          "delivery": 0.86,
          "volume": 1.36,
          "call_oi": 31032225,
          "put_oi": 20796450
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.54,
          "pcr": 0.66,
          "pcr_chg_1d": 0.05,
          "fut_oi": 102547275,
          "oi_chg_pct": -1.29,
          "delivery": 1.11,
          "volume": 1.12,
          "call_oi": 39213150,
          "put_oi": 25734075
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.61,
          "pcr": 0.65,
          "pcr_chg_1d": -0.01,
          "fut_oi": 102430425,
          "oi_chg_pct": -0.11,
          "delivery": 0.66,
          "volume": 0.65,
          "call_oi": 40090950,
          "put_oi": 26131650
        }
      ]
    },
    {
      "symbol": "SBILIFE",
      "rank": 182,
      "days_available": 3,
      "latest_score": 2.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.0,
          2.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 0,
        "neutral_windows": 2,
        "total_windows": 2,
        "pcr_slope_7d": 0.055,
        "pcr_first": 1.21,
        "pcr_last": 1.32,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 1.47,
        "cumulative_price_chg_pct_window": 0.82,
        "persistence_score": 1.67,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": 1.0,
          "signals": [
            "PCR 1.50 ABOVE 1.0 \u2014 put writers dominant",
            "PCR collapsing -0.27"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.19,
          "price_sign": 0,
          "pcr_d1": 1.21,
          "pcr_d2": 1.5,
          "pcr_chg": -0.27,
          "fut_oi_chg_pct": 1.82,
          "oi_sign": 1,
          "avg_del": 0.83,
          "peak_del": 0.91,
          "del_chg": 0.16,
          "avg_vol": 0.9,
          "call_oi_growth_pct": 47.58,
          "put_oi_growth_pct": 83.37,
          "opt_oi_growth_pct": 67.18,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 2.0,
          "signals": [
            "PCR 1.32 ABOVE 1.0 \u2014 put writers dominant",
            "PCR collapsing -0.18"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.01,
          "price_sign": 1,
          "pcr_d1": 1.5,
          "pcr_d2": 1.32,
          "pcr_chg": -0.18,
          "fut_oi_chg_pct": -0.34,
          "oi_sign": -1,
          "avg_del": 0.725,
          "peak_del": 0.91,
          "del_chg": -0.37,
          "avg_vol": 0.805,
          "call_oi_growth_pct": 23.01,
          "put_oi_growth_pct": 8.38,
          "opt_oi_growth_pct": 14.22,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.74,
          "pcr": 1.21,
          "pcr_chg_1d": 0.13,
          "fut_oi": 10524375,
          "oi_chg_pct": 4.98,
          "delivery": 0.75,
          "volume": 0.77,
          "call_oi": 542250,
          "put_oi": 656250
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.19,
          "pcr": 1.5,
          "pcr_chg_1d": -0.27,
          "fut_oi": 10715625,
          "oi_chg_pct": -0.83,
          "delivery": 0.91,
          "volume": 1.03,
          "call_oi": 800250,
          "put_oi": 1203375
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.01,
          "pcr": 1.32,
          "pcr_chg_1d": -0.18,
          "fut_oi": 10679250,
          "oi_chg_pct": -0.34,
          "delivery": 0.54,
          "volume": 0.58,
          "call_oi": 984375,
          "put_oi": 1304250
        }
      ]
    },
    {
      "symbol": "JSWENERGY",
      "rank": 183,
      "days_available": 3,
      "latest_score": -1.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild short build",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -5.0,
          -1.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.02,
        "pcr_first": 0.52,
        "pcr_last": 0.56,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 3.6,
        "cumulative_price_chg_pct_window": -2.63,
        "persistence_score": -2.67,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -5.0,
          "signals": [
            "PCR 0.56 neutral",
            "\u26a0 NEW SHORTS: FutOI +2.5% + Price -2.6%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_1_short",
          "price_chg_pct": -2.57,
          "price_sign": -1,
          "pcr_d1": 0.52,
          "pcr_d2": 0.56,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": 2.5,
          "oi_sign": 1,
          "avg_del": 0.81,
          "peak_del": 1.35,
          "del_chg": 1.08,
          "avg_vol": 0.815,
          "call_oi_growth_pct": 75.53,
          "put_oi_growth_pct": 88.88,
          "opt_oi_growth_pct": 80.08,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -1.5,
          "signals": [
            "PCR 0.56 neutral"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.06,
          "price_sign": 0,
          "pcr_d1": 0.56,
          "pcr_d2": 0.56,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": 1.07,
          "oi_sign": 1,
          "avg_del": 1.05,
          "peak_del": 1.35,
          "del_chg": -0.6,
          "avg_vol": 1.015,
          "call_oi_growth_pct": 0.37,
          "put_oi_growth_pct": 0.76,
          "opt_oi_growth_pct": 0.51,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.66,
          "pcr": 0.52,
          "pcr_chg_1d": -0.03,
          "fut_oi": 26564000,
          "oi_chg_pct": -2.09,
          "delivery": 0.27,
          "volume": 0.39,
          "call_oi": 4042000,
          "put_oi": 2086000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.57,
          "pcr": 0.56,
          "pcr_chg_1d": -0.03,
          "fut_oi": 27229000,
          "oi_chg_pct": 2.89,
          "delivery": 1.35,
          "volume": 1.24,
          "call_oi": 7095000,
          "put_oi": 3940000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.06,
          "pcr": 0.56,
          "pcr_chg_1d": 0.0,
          "fut_oi": 27519000,
          "oi_chg_pct": 1.07,
          "delivery": 0.75,
          "volume": 0.79,
          "call_oi": 7121000,
          "put_oi": 3970000
        }
      ]
    },
    {
      "symbol": "IEX",
      "rank": 184,
      "days_available": 3,
      "latest_score": 1.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -1.5,
          1.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 0,
        "neutral_windows": 2,
        "total_windows": 2,
        "pcr_slope_7d": -0.055,
        "pcr_first": 0.85,
        "pcr_last": 0.74,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -3.9,
        "cumulative_price_chg_pct_window": 0.42,
        "persistence_score": 0.5,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -1.5,
          "signals": [
            "PCR 0.67 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 0
          },
          "phase": "no_signal",
          "price_chg_pct": 0.19,
          "price_sign": 0,
          "pcr_d1": 0.85,
          "pcr_d2": 0.67,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -3.45,
          "oi_sign": -1,
          "avg_del": 0.52,
          "peak_del": 0.72,
          "del_chg": 0.4,
          "avg_vol": 0.625,
          "call_oi_growth_pct": 46.6,
          "put_oi_growth_pct": 15.63,
          "opt_oi_growth_pct": 32.36,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.5,
          "signals": [
            "PCR 0.74 neutral",
            "PCR rising +0.07"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 0.23,
          "price_sign": 0,
          "pcr_d1": 0.67,
          "pcr_d2": 0.74,
          "pcr_chg": 0.07,
          "fut_oi_chg_pct": -0.47,
          "oi_sign": -1,
          "avg_del": 0.665,
          "peak_del": 0.72,
          "del_chg": -0.11,
          "avg_vol": 0.685,
          "call_oi_growth_pct": -0.84,
          "put_oi_growth_pct": 9.8,
          "opt_oi_growth_pct": 3.43,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.53,
          "pcr": 0.85,
          "pcr_chg_1d": -0.04,
          "fut_oi": 73856250,
          "oi_chg_pct": -1.7,
          "delivery": 0.32,
          "volume": 0.47,
          "call_oi": 25492500,
          "put_oi": 21712500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.19,
          "pcr": 0.67,
          "pcr_chg_1d": 0.0,
          "fut_oi": 71306250,
          "oi_chg_pct": -1.36,
          "delivery": 0.72,
          "volume": 0.78,
          "call_oi": 37372500,
          "put_oi": 25106250
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.23,
          "pcr": 0.74,
          "pcr_chg_1d": 0.07,
          "fut_oi": 70972500,
          "oi_chg_pct": -0.47,
          "delivery": 0.61,
          "volume": 0.59,
          "call_oi": 37057500,
          "put_oi": 27566250
        }
      ]
    },
    {
      "symbol": "PRESTIGE",
      "rank": 185,
      "days_available": 3,
      "latest_score": 1.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.0,
          1.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.165,
        "pcr_first": 0.95,
        "pcr_last": 0.62,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 7.03,
        "cumulative_price_chg_pct_window": 0.12,
        "persistence_score": -0.33,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -4.0,
          "signals": [
            "PCR 0.61 neutral",
            "PCR easing -0.04"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.11,
          "price_sign": 0,
          "pcr_d1": 0.95,
          "pcr_d2": 0.61,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 7.06,
          "oi_sign": 1,
          "avg_del": 1.845,
          "peak_del": 3.36,
          "del_chg": -3.03,
          "avg_vol": 1.225,
          "call_oi_growth_pct": 209.16,
          "put_oi_growth_pct": 97.63,
          "opt_oi_growth_pct": 154.82,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.5,
          "signals": [
            "PCR 0.62 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.23,
          "price_sign": 0,
          "pcr_d1": 0.61,
          "pcr_d2": 0.62,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": -0.03,
          "oi_sign": -1,
          "avg_del": 0.87,
          "peak_del": 1.41,
          "del_chg": 1.08,
          "avg_vol": 0.785,
          "call_oi_growth_pct": 8.75,
          "put_oi_growth_pct": 11.88,
          "opt_oi_growth_pct": 9.94,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.63,
          "pcr": 0.95,
          "pcr_chg_1d": -0.09,
          "fut_oi": 6446250,
          "oi_chg_pct": 3.29,
          "delivery": 3.36,
          "volume": 2.07,
          "call_oi": 540450,
          "put_oi": 513450
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.11,
          "pcr": 0.61,
          "pcr_chg_1d": -0.04,
          "fut_oi": 6901200,
          "oi_chg_pct": 2.19,
          "delivery": 0.33,
          "volume": 0.38,
          "call_oi": 1670850,
          "put_oi": 1014750
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.23,
          "pcr": 0.62,
          "pcr_chg_1d": 0.01,
          "fut_oi": 6899400,
          "oi_chg_pct": -0.03,
          "delivery": 1.41,
          "volume": 1.19,
          "call_oi": 1817100,
          "put_oi": 1135350
        }
      ]
    },
    {
      "symbol": "KEI",
      "rank": 186,
      "days_available": 3,
      "latest_score": 1.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -7.0,
          1.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.13,
        "pcr_first": 1.08,
        "pcr_last": 0.82,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 8.8,
        "cumulative_price_chg_pct_window": -1.07,
        "persistence_score": -1.33,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -7.0,
          "signals": [
            "PCR 0.85 approaching bullish zone",
            "PCR easing -0.07",
            "\u26a0 NEW SHORTS: FutOI +9.0% + Price -2.0%",
            "Del 1.03x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -2.0,
          "price_sign": -1,
          "pcr_d1": 1.08,
          "pcr_d2": 0.85,
          "pcr_chg": -0.07,
          "fut_oi_chg_pct": 9.0,
          "oi_sign": 1,
          "avg_del": 1.035,
          "peak_del": 1.18,
          "del_chg": -0.29,
          "avg_vol": 1.035,
          "call_oi_growth_pct": 103.66,
          "put_oi_growth_pct": 60.12,
          "opt_oi_growth_pct": 81.05,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.5,
          "signals": [
            "PCR 0.82 neutral-to-bullish"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.95,
          "price_sign": 1,
          "pcr_d1": 0.85,
          "pcr_d2": 0.82,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": -0.18,
          "oi_sign": -1,
          "avg_del": 0.69,
          "peak_del": 0.89,
          "del_chg": -0.4,
          "avg_vol": 0.775,
          "call_oi_growth_pct": 5.14,
          "put_oi_growth_pct": 1.91,
          "opt_oi_growth_pct": 3.65,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.4,
          "pcr": 1.08,
          "pcr_chg_1d": -0.05,
          "fut_oi": 1999375,
          "oi_chg_pct": 3.45,
          "delivery": 1.18,
          "volume": 1.16,
          "call_oi": 244125,
          "put_oi": 263725
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -2.0,
          "pcr": 0.85,
          "pcr_chg_1d": -0.07,
          "fut_oi": 2179275,
          "oi_chg_pct": -0.34,
          "delivery": 0.89,
          "volume": 0.91,
          "call_oi": 497175,
          "put_oi": 422275
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.95,
          "pcr": 0.82,
          "pcr_chg_1d": -0.03,
          "fut_oi": 2175250,
          "oi_chg_pct": -0.18,
          "delivery": 0.49,
          "volume": 0.64,
          "call_oi": 522725,
          "put_oi": 430325
        }
      ]
    },
    {
      "symbol": "TORNTPOWER",
      "rank": 187,
      "days_available": 3,
      "latest_score": 1.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.0,
          1.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 0,
        "neutral_windows": 2,
        "total_windows": 2,
        "pcr_slope_7d": -0.19,
        "pcr_first": 1.2,
        "pcr_last": 0.82,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 6.81,
        "cumulative_price_chg_pct_window": 1.61,
        "persistence_score": 0.33,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -2.0,
          "signals": [
            "PCR 0.91 approaching bullish zone",
            "PCR easing -0.04"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.17,
          "price_sign": 0,
          "pcr_d1": 1.2,
          "pcr_d2": 0.91,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 9.44,
          "oi_sign": 1,
          "avg_del": 1.305,
          "peak_del": 1.35,
          "del_chg": -0.09,
          "avg_vol": 1.205,
          "call_oi_growth_pct": 97.6,
          "put_oi_growth_pct": 50.05,
          "opt_oi_growth_pct": 71.65,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.5,
          "signals": [
            "PCR 0.82 neutral-to-bullish",
            "PCR collapsing -0.09"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.78,
          "price_sign": 1,
          "pcr_d1": 0.91,
          "pcr_d2": 0.82,
          "pcr_chg": -0.09,
          "fut_oi_chg_pct": -2.4,
          "oi_sign": -1,
          "avg_del": 0.92,
          "peak_del": 1.26,
          "del_chg": -0.68,
          "avg_vol": 0.86,
          "call_oi_growth_pct": 10.21,
          "put_oi_growth_pct": -1.26,
          "opt_oi_growth_pct": 4.73,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.4,
          "pcr": 1.2,
          "pcr_chg_1d": 0.2,
          "fut_oi": 3213850,
          "oi_chg_pct": -0.05,
          "delivery": 1.35,
          "volume": 1.29,
          "call_oi": 354025,
          "put_oi": 425425
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.17,
          "pcr": 0.91,
          "pcr_chg_1d": -0.04,
          "fut_oi": 3517300,
          "oi_chg_pct": 2.57,
          "delivery": 1.26,
          "volume": 1.12,
          "call_oi": 699550,
          "put_oi": 638350
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.78,
          "pcr": 0.82,
          "pcr_chg_1d": -0.09,
          "fut_oi": 3432725,
          "oi_chg_pct": -2.4,
          "delivery": 0.58,
          "volume": 0.6,
          "call_oi": 770950,
          "put_oi": 630275
        }
      ]
    },
    {
      "symbol": "APLAPOLLO",
      "rank": 188,
      "days_available": 3,
      "latest_score": 1.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2191 SHORT COVERING (lagging)",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -6.0,
          1.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.065,
        "pcr_first": 0.87,
        "pcr_last": 0.74,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -2.36,
        "cumulative_price_chg_pct_window": 0.83,
        "persistence_score": -1.0,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -6.0,
          "signals": [
            "PCR 0.79 neutral-to-bullish",
            "Del 1.11x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.36,
          "price_sign": -1,
          "pcr_d1": 0.87,
          "pcr_d2": 0.79,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 0.43,
          "oi_sign": 1,
          "avg_del": 1.11,
          "peak_del": 1.15,
          "del_chg": -0.08,
          "avg_vol": 1.15,
          "call_oi_growth_pct": 59.06,
          "put_oi_growth_pct": 43.91,
          "opt_oi_growth_pct": 51.99,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.5,
          "signals": [
            "PCR 0.74 neutral",
            "PCR easing -0.05"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.19,
          "price_sign": 1,
          "pcr_d1": 0.79,
          "pcr_d2": 0.74,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": -2.77,
          "oi_sign": -1,
          "avg_del": 0.88,
          "peak_del": 1.07,
          "del_chg": -0.38,
          "avg_vol": 0.825,
          "call_oi_growth_pct": 7.97,
          "put_oi_growth_pct": 0.35,
          "opt_oi_growth_pct": 4.6,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.11,
          "pcr": 0.87,
          "pcr_chg_1d": -0.28,
          "fut_oi": 4829300,
          "oi_chg_pct": 2.51,
          "delivery": 1.15,
          "volume": 1.35,
          "call_oi": 552300,
          "put_oi": 483000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.36,
          "pcr": 0.79,
          "pcr_chg_1d": 0.03,
          "fut_oi": 4849950,
          "oi_chg_pct": 1.21,
          "delivery": 1.07,
          "volume": 0.95,
          "call_oi": 878500,
          "put_oi": 695100
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.19,
          "pcr": 0.74,
          "pcr_chg_1d": -0.05,
          "fut_oi": 4715550,
          "oi_chg_pct": -2.77,
          "delivery": 0.69,
          "volume": 0.7,
          "call_oi": 948500,
          "put_oi": 697550
        }
      ]
    },
    {
      "symbol": "FORTIS",
      "rank": 189,
      "days_available": 3,
      "latest_score": -1.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild short build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (short)",
        "direction": "short",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          6.5,
          -1.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.025,
        "pcr_first": 0.62,
        "pcr_last": 0.67,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -4.03,
        "cumulative_price_chg_pct_window": 0.87,
        "persistence_score": 1.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 6.5,
          "signals": [
            "PCR 0.70 neutral",
            "PCR rising +0.06"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 1.13,
          "price_sign": 1,
          "pcr_d1": 0.62,
          "pcr_d2": 0.7,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": -4.26,
          "oi_sign": -1,
          "avg_del": 0.77,
          "peak_del": 1.08,
          "del_chg": 0.62,
          "avg_vol": 0.74,
          "call_oi_growth_pct": 68.73,
          "put_oi_growth_pct": 90.85,
          "opt_oi_growth_pct": 77.18,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -1.5,
          "signals": [
            "PCR 0.67 neutral"
          ],
          "interpretation": "Mild short build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.26,
          "price_sign": 0,
          "pcr_d1": 0.7,
          "pcr_d2": 0.67,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": 0.25,
          "oi_sign": 1,
          "avg_del": 0.805,
          "peak_del": 1.08,
          "del_chg": -0.55,
          "avg_vol": 0.715,
          "call_oi_growth_pct": 4.81,
          "put_oi_growth_pct": 0.38,
          "opt_oi_growth_pct": 2.99,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.0,
          "pcr": 0.62,
          "pcr_chg_1d": 0.02,
          "fut_oi": 12475950,
          "oi_chg_pct": 1.01,
          "delivery": 0.46,
          "volume": 0.51,
          "call_oi": 1040825,
          "put_oi": 644025
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.13,
          "pcr": 0.7,
          "pcr_chg_1d": 0.06,
          "fut_oi": 11944300,
          "oi_chg_pct": 0.52,
          "delivery": 1.08,
          "volume": 0.97,
          "call_oi": 1756150,
          "put_oi": 1229150
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.26,
          "pcr": 0.67,
          "pcr_chg_1d": -0.03,
          "fut_oi": 11973750,
          "oi_chg_pct": 0.25,
          "delivery": 0.53,
          "volume": 0.46,
          "call_oi": 1840625,
          "put_oi": 1233800
        }
      ]
    },
    {
      "symbol": "KPITTECH",
      "rank": 190,
      "days_available": 3,
      "latest_score": 1.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u25cb NONE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -6.5,
          1.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.105,
        "pcr_first": 1.0,
        "pcr_last": 0.79,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 10.47,
        "cumulative_price_chg_pct_window": -0.65,
        "persistence_score": -1.17,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -6.5,
          "signals": [
            "PCR 0.81 neutral-to-bullish",
            "\u26a0 NEW SHORTS: FutOI +11.8% + Price -0.7%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -0.71,
          "price_sign": -1,
          "pcr_d1": 1.0,
          "pcr_d2": 0.81,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 11.82,
          "oi_sign": 1,
          "avg_del": 0.94,
          "peak_del": 0.94,
          "del_chg": 0.0,
          "avg_vol": 1.03,
          "call_oi_growth_pct": 75.06,
          "put_oi_growth_pct": 42.09,
          "opt_oi_growth_pct": 58.57,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.5,
          "signals": [
            "PCR 0.79 neutral-to-bullish"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.06,
          "price_sign": 0,
          "pcr_d1": 0.81,
          "pcr_d2": 0.79,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": -1.2,
          "oi_sign": -1,
          "avg_del": 0.845,
          "peak_del": 0.94,
          "del_chg": -0.19,
          "avg_vol": 0.86,
          "call_oi_growth_pct": 2.65,
          "put_oi_growth_pct": -0.58,
          "opt_oi_growth_pct": 1.2,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 6.23,
          "pcr": 1.0,
          "pcr_chg_1d": 0.11,
          "fut_oi": 5996325,
          "oi_chg_pct": -5.18,
          "delivery": 0.94,
          "volume": 1.14,
          "call_oi": 1657925,
          "put_oi": 1659200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.71,
          "pcr": 0.81,
          "pcr_chg_1d": 0.01,
          "fut_oi": 6704800,
          "oi_chg_pct": 2.11,
          "delivery": 0.94,
          "volume": 0.92,
          "call_oi": 2902325,
          "put_oi": 2357475
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.06,
          "pcr": 0.79,
          "pcr_chg_1d": -0.02,
          "fut_oi": 6624050,
          "oi_chg_pct": -1.2,
          "delivery": 0.75,
          "volume": 0.8,
          "call_oi": 2979250,
          "put_oi": 2343875
        }
      ]
    },
    {
      "symbol": "AUROPHARMA",
      "rank": 191,
      "days_available": 3,
      "latest_score": 1.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "pre_phase_1_long",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          3.5,
          1.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.05,
        "pcr_first": 0.84,
        "pcr_last": 0.74,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 5.89,
        "cumulative_price_chg_pct_window": 1.02,
        "persistence_score": 2.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 3.5,
          "signals": [
            "PCR 0.67 neutral",
            "PCR rising +0.04"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.35,
          "price_sign": 1,
          "pcr_d1": 0.84,
          "pcr_d2": 0.67,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": 6.01,
          "oi_sign": 1,
          "avg_del": 0.895,
          "peak_del": 1.44,
          "del_chg": -1.09,
          "avg_vol": 0.875,
          "call_oi_growth_pct": 36.36,
          "put_oi_growth_pct": 8.93,
          "opt_oi_growth_pct": 23.82,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.5,
          "signals": [
            "PCR 0.74 neutral",
            "PCR rising +0.07"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "pre_phase_1_long",
          "price_chg_pct": 0.67,
          "price_sign": 1,
          "pcr_d1": 0.67,
          "pcr_d2": 0.74,
          "pcr_chg": 0.07,
          "fut_oi_chg_pct": -0.11,
          "oi_sign": -1,
          "avg_del": 0.455,
          "peak_del": 0.56,
          "del_chg": 0.21,
          "avg_vol": 0.465,
          "call_oi_growth_pct": -0.71,
          "put_oi_growth_pct": 9.53,
          "opt_oi_growth_pct": 3.41,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.89,
          "pcr": 0.84,
          "pcr_chg_1d": 0.13,
          "fut_oi": 20155850,
          "oi_chg_pct": 1.63,
          "delivery": 1.44,
          "volume": 1.32,
          "call_oi": 2606450,
          "put_oi": 2193400
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.35,
          "pcr": 0.67,
          "pcr_chg_1d": 0.04,
          "fut_oi": 21367500,
          "oi_chg_pct": 0.27,
          "delivery": 0.35,
          "volume": 0.43,
          "call_oi": 3554100,
          "put_oi": 2389200
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.67,
          "pcr": 0.74,
          "pcr_chg_1d": 0.07,
          "fut_oi": 21343850,
          "oi_chg_pct": -0.11,
          "delivery": 0.56,
          "volume": 0.5,
          "call_oi": 3528800,
          "put_oi": 2616900
        }
      ]
    },
    {
      "symbol": "OIL",
      "rank": 192,
      "days_available": 3,
      "latest_score": -1.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u25cb NONE",
        "direction": "none",
        "count": 0
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          7.0,
          -1.5
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.0,
        "pcr_first": 0.47,
        "pcr_last": 0.47,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -10.35,
        "cumulative_price_chg_pct_window": 2.69,
        "persistence_score": 1.33,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 7.0,
          "signals": [
            "PCR 0.47 call writers dominant",
            "PCR rising +0.04",
            "Del 1.23x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 2.57,
          "price_sign": 1,
          "pcr_d1": 0.47,
          "pcr_d2": 0.47,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": -7.25,
          "oi_sign": -1,
          "avg_del": 1.235,
          "peak_del": 1.76,
          "del_chg": 1.05,
          "avg_vol": 1.09,
          "call_oi_growth_pct": 29.49,
          "put_oi_growth_pct": 29.99,
          "opt_oi_growth_pct": 29.65,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -1.5,
          "signals": [
            "PCR 0.47 call writers dominant"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 0
          },
          "phase": "no_signal",
          "price_chg_pct": 0.12,
          "price_sign": 0,
          "pcr_d1": 0.47,
          "pcr_d2": 0.47,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -3.34,
          "oi_sign": -1,
          "avg_del": 0.99,
          "peak_del": 1.76,
          "del_chg": -1.54,
          "avg_vol": 0.915,
          "call_oi_growth_pct": -2.87,
          "put_oi_growth_pct": -2.0,
          "opt_oi_growth_pct": -2.59,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.43,
          "pcr": 0.47,
          "pcr_chg_1d": 0.01,
          "fut_oi": 22489600,
          "oi_chg_pct": -0.8,
          "delivery": 0.71,
          "volume": 0.63,
          "call_oi": 7382200,
          "put_oi": 3449600
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 2.57,
          "pcr": 0.47,
          "pcr_chg_1d": 0.04,
          "fut_oi": 20860000,
          "oi_chg_pct": -2.08,
          "delivery": 1.76,
          "volume": 1.55,
          "call_oi": 9559200,
          "put_oi": 4484200
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.12,
          "pcr": 0.47,
          "pcr_chg_1d": 0.0,
          "fut_oi": 20162800,
          "oi_chg_pct": -3.34,
          "delivery": 0.22,
          "volume": 0.28,
          "call_oi": 9284800,
          "put_oi": 4394600
        }
      ]
    },
    {
      "symbol": "HYUNDAI",
      "rank": 193,
      "days_available": 3,
      "latest_score": 1.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2605 NEW LONGS (Bullish)",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -11.5,
          1.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.145,
        "pcr_first": 0.92,
        "pcr_last": 0.63,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 250.41,
        "cumulative_price_chg_pct_window": 0.98,
        "persistence_score": -2.83,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -11.5,
          "signals": [
            "PCR 0.67 neutral",
            "PCR easing -0.07",
            "\u26a0 NEW SHORTS: FutOI +231.1% + Price -0.6%",
            "Del 2.63x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -0.6,
          "price_sign": -1,
          "pcr_d1": 0.92,
          "pcr_d2": 0.67,
          "pcr_chg": -0.07,
          "fut_oi_chg_pct": 231.07,
          "oi_sign": 1,
          "avg_del": 2.635,
          "peak_del": 4.72,
          "del_chg": -4.17,
          "avg_vol": 3.09,
          "call_oi_growth_pct": 312.98,
          "put_oi_growth_pct": 199.09,
          "opt_oi_growth_pct": 258.33,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.5,
          "signals": [
            "PCR 0.63 neutral",
            "PCR easing -0.04",
            "\u2605 NEW LONGS: FutOI +5.8% + Price +1.6%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.59,
          "price_sign": 1,
          "pcr_d1": 0.67,
          "pcr_d2": 0.63,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 5.84,
          "oi_sign": 1,
          "avg_del": 0.43,
          "peak_del": 0.55,
          "del_chg": -0.24,
          "avg_vol": 0.47,
          "call_oi_growth_pct": 32.63,
          "put_oi_growth_pct": 24.94,
          "opt_oi_growth_pct": 29.55,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -3.48,
          "pcr": 0.92,
          "pcr_chg_1d": 0.0,
          "fut_oi": 1535600,
          "oi_chg_pct": 0.0,
          "delivery": 4.72,
          "volume": 5.58,
          "call_oi": 163075,
          "put_oi": 150425
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.6,
          "pcr": 0.67,
          "pcr_chg_1d": -0.07,
          "fut_oi": 5083925,
          "oi_chg_pct": 16.26,
          "delivery": 0.55,
          "volume": 0.6,
          "call_oi": 673475,
          "put_oi": 449900
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.59,
          "pcr": 0.63,
          "pcr_chg_1d": -0.04,
          "fut_oi": 5380925,
          "oi_chg_pct": 5.84,
          "delivery": 0.31,
          "volume": 0.34,
          "call_oi": 893200,
          "put_oi": 562100
        }
      ]
    },
    {
      "symbol": "SHREECEM",
      "rank": 194,
      "days_available": 3,
      "latest_score": 1.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -9.0,
          1.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.04,
        "pcr_first": 0.54,
        "pcr_last": 0.62,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 5.2,
        "cumulative_price_chg_pct_window": -0.08,
        "persistence_score": -2.0,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -9.0,
          "signals": [
            "PCR 0.67 neutral",
            "PCR easing -0.04",
            "\u26a0 NEW SHORTS: FutOI +6.9% + Price -1.5%",
            "Del 1.77x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "phase_2_short",
          "price_chg_pct": -1.52,
          "price_sign": -1,
          "pcr_d1": 0.54,
          "pcr_d2": 0.67,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 6.93,
          "oi_sign": 1,
          "avg_del": 1.77,
          "peak_del": 3.1,
          "del_chg": 2.66,
          "avg_vol": 1.82,
          "call_oi_growth_pct": 213.01,
          "put_oi_growth_pct": 286.77,
          "opt_oi_growth_pct": 238.82,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.5,
          "signals": [
            "PCR 0.62 neutral",
            "PCR easing -0.05",
            "Del 2.52x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.46,
          "price_sign": 1,
          "pcr_d1": 0.67,
          "pcr_d2": 0.62,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": -1.62,
          "oi_sign": -1,
          "avg_del": 2.525,
          "peak_del": 3.1,
          "del_chg": -1.15,
          "avg_vol": 2.375,
          "call_oi_growth_pct": 19.56,
          "put_oi_growth_pct": 12.3,
          "opt_oi_growth_pct": 16.66,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.06,
          "pcr": 0.54,
          "pcr_chg_1d": -0.22,
          "fut_oi": 361700,
          "oi_chg_pct": -0.14,
          "delivery": 0.44,
          "volume": 0.44,
          "call_oi": 18250,
          "put_oi": 9825
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.52,
          "pcr": 0.67,
          "pcr_chg_1d": -0.04,
          "fut_oi": 386775,
          "oi_chg_pct": 3.87,
          "delivery": 3.1,
          "volume": 3.2,
          "call_oi": 57125,
          "put_oi": 38000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.46,
          "pcr": 0.62,
          "pcr_chg_1d": -0.05,
          "fut_oi": 380500,
          "oi_chg_pct": -1.62,
          "delivery": 1.95,
          "volume": 1.55,
          "call_oi": 68300,
          "put_oi": 42675
        }
      ]
    },
    {
      "symbol": "POWERGRID",
      "rank": 195,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          5.0,
          1.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.06,
        "pcr_first": 0.65,
        "pcr_last": 0.53,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 5.0,
        "cumulative_price_chg_pct_window": 2.68,
        "persistence_score": 2.33,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 5.0,
          "signals": [
            "PCR 0.51 call writers dominant",
            "PCR rising +0.04",
            "\u2605 NEW LONGS: FutOI +6.2% + Price +1.1%",
            "Del 1.12x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (LONG)",
            "direction": "long",
            "count": 3
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.1,
          "price_sign": 1,
          "pcr_d1": 0.65,
          "pcr_d2": 0.51,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": 6.15,
          "oi_sign": 1,
          "avg_del": 1.125,
          "peak_del": 1.47,
          "del_chg": 0.69,
          "avg_vol": 1.08,
          "call_oi_growth_pct": 45.08,
          "put_oi_growth_pct": 13.47,
          "opt_oi_growth_pct": 32.67,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 0.53 call writers dominant",
            "Del 1.35x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.56,
          "price_sign": 1,
          "pcr_d1": 0.51,
          "pcr_d2": 0.53,
          "pcr_chg": 0.02,
          "fut_oi_chg_pct": -1.08,
          "oi_sign": -1,
          "avg_del": 1.355,
          "peak_del": 1.47,
          "del_chg": -0.23,
          "avg_vol": 1.19,
          "call_oi_growth_pct": -3.74,
          "put_oi_growth_pct": 1.62,
          "opt_oi_growth_pct": -1.94,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -1.11,
          "pcr": 0.65,
          "pcr_chg_1d": -0.04,
          "fut_oi": 74728900,
          "oi_chg_pct": 3.49,
          "delivery": 0.78,
          "volume": 0.81,
          "call_oi": 20563700,
          "put_oi": 13298100
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.1,
          "pcr": 0.51,
          "pcr_chg_1d": 0.04,
          "fut_oi": 79325000,
          "oi_chg_pct": 0.46,
          "delivery": 1.47,
          "volume": 1.35,
          "call_oi": 29833800,
          "put_oi": 15089800
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.56,
          "pcr": 0.53,
          "pcr_chg_1d": 0.02,
          "fut_oi": 78466200,
          "oi_chg_pct": -1.08,
          "delivery": 1.24,
          "volume": 1.03,
          "call_oi": 28716600,
          "put_oi": 15334900
        }
      ]
    },
    {
      "symbol": "TECHM",
      "rank": 196,
      "days_available": 3,
      "latest_score": -1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          1.5,
          -1.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 0,
        "neutral_windows": 2,
        "total_windows": 2,
        "pcr_slope_7d": -0.07,
        "pcr_first": 0.96,
        "pcr_last": 0.82,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -6.63,
        "cumulative_price_chg_pct_window": -0.77,
        "persistence_score": -0.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": 1.5,
          "signals": [
            "PCR 0.79 neutral-to-bullish"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.7,
          "price_sign": 1,
          "pcr_d1": 0.96,
          "pcr_d2": 0.79,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": -6.53,
          "oi_sign": -1,
          "avg_del": 0.64,
          "peak_del": 0.77,
          "del_chg": 0.26,
          "avg_vol": 0.675,
          "call_oi_growth_pct": 72.64,
          "put_oi_growth_pct": 42.41,
          "opt_oi_growth_pct": 57.87,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -1.0,
          "signals": [
            "PCR 0.82 neutral-to-bullish"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -1.46,
          "price_sign": -1,
          "pcr_d1": 0.79,
          "pcr_d2": 0.82,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -0.1,
          "oi_sign": -1,
          "avg_del": 0.89,
          "peak_del": 1.01,
          "del_chg": 0.24,
          "avg_vol": 0.95,
          "call_oi_growth_pct": 0.27,
          "put_oi_growth_pct": 4.61,
          "opt_oi_growth_pct": 2.18,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.48,
          "pcr": 0.96,
          "pcr_chg_1d": 0.02,
          "fut_oi": 19933200,
          "oi_chg_pct": -1.32,
          "delivery": 0.51,
          "volume": 0.45,
          "call_oi": 2841600,
          "put_oi": 2713800
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.7,
          "pcr": 0.79,
          "pcr_chg_1d": -0.02,
          "fut_oi": 18630600,
          "oi_chg_pct": -2.6,
          "delivery": 0.77,
          "volume": 0.9,
          "call_oi": 4905600,
          "put_oi": 3864600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -1.46,
          "pcr": 0.82,
          "pcr_chg_1d": 0.03,
          "fut_oi": 18611400,
          "oi_chg_pct": -0.1,
          "delivery": 1.01,
          "volume": 1.0,
          "call_oi": 4918800,
          "put_oi": 4042800
        }
      ]
    },
    {
      "symbol": "SAIL",
      "rank": 197,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -5.5,
          1.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.135,
        "pcr_first": 0.47,
        "pcr_last": 0.74,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 12.77,
        "cumulative_price_chg_pct_window": 0.98,
        "persistence_score": -1.17,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -5.5,
          "signals": [
            "PCR 0.71 neutral",
            "\u26a0 NEW SHORTS: FutOI +13.1% + Price -0.6%",
            "Del 1.35x + Price\u2193 INSTITUTIONAL DISTRIBUTION"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_short",
          "price_chg_pct": -0.64,
          "price_sign": -1,
          "pcr_d1": 0.47,
          "pcr_d2": 0.71,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": 13.1,
          "oi_sign": 1,
          "avg_del": 1.35,
          "peak_del": 2.08,
          "del_chg": -1.46,
          "avg_vol": 0.965,
          "call_oi_growth_pct": 140.15,
          "put_oi_growth_pct": 268.15,
          "opt_oi_growth_pct": 180.79,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 0.74 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.63,
          "price_sign": 1,
          "pcr_d1": 0.71,
          "pcr_d2": 0.74,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -0.3,
          "oi_sign": -1,
          "avg_del": 0.595,
          "peak_del": 0.62,
          "del_chg": -0.05,
          "avg_vol": 0.645,
          "call_oi_growth_pct": -3.44,
          "put_oi_growth_pct": -0.44,
          "opt_oi_growth_pct": -2.19,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.91,
          "pcr": 0.47,
          "pcr_chg_1d": 0.0,
          "fut_oi": 184005000,
          "oi_chg_pct": 9.31,
          "delivery": 2.08,
          "volume": 1.2,
          "call_oi": 5010200,
          "put_oi": 2331200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.64,
          "pcr": 0.71,
          "pcr_chg_1d": 0.03,
          "fut_oi": 208116000,
          "oi_chg_pct": -1.73,
          "delivery": 0.62,
          "volume": 0.73,
          "call_oi": 12032000,
          "put_oi": 8582200
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.63,
          "pcr": 0.74,
          "pcr_chg_1d": 0.03,
          "fut_oi": 207500300,
          "oi_chg_pct": -0.3,
          "delivery": 0.57,
          "volume": 0.56,
          "call_oi": 11618400,
          "put_oi": 8544600
        }
      ]
    },
    {
      "symbol": "PATANJALI",
      "rank": 198,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -3.5,
          1.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.195,
        "pcr_first": 1.13,
        "pcr_last": 0.74,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -2.87,
        "cumulative_price_chg_pct_window": -0.26,
        "persistence_score": -0.5,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -3.5,
          "signals": [
            "PCR 0.74 neutral",
            "PCR easing -0.05"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -1.89,
          "price_sign": -1,
          "pcr_d1": 1.13,
          "pcr_d2": 0.74,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": -1.65,
          "oi_sign": -1,
          "avg_del": 0.585,
          "peak_del": 0.73,
          "del_chg": 0.29,
          "avg_vol": 0.71,
          "call_oi_growth_pct": 88.99,
          "put_oi_growth_pct": 23.42,
          "opt_oi_growth_pct": 54.16,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 0.74 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.66,
          "price_sign": 1,
          "pcr_d1": 0.74,
          "pcr_d2": 0.74,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -1.23,
          "oi_sign": -1,
          "avg_del": 0.575,
          "peak_del": 0.73,
          "del_chg": -0.31,
          "avg_vol": 0.59,
          "call_oi_growth_pct": 4.26,
          "put_oi_growth_pct": 4.15,
          "opt_oi_growth_pct": 4.21,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.25,
          "pcr": 1.13,
          "pcr_chg_1d": -0.13,
          "fut_oi": 34983900,
          "oi_chg_pct": -0.22,
          "delivery": 0.44,
          "volume": 0.72,
          "call_oi": 1520100,
          "put_oi": 1721700
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.89,
          "pcr": 0.74,
          "pcr_chg_1d": -0.05,
          "fut_oi": 34405200,
          "oi_chg_pct": 0.46,
          "delivery": 0.73,
          "volume": 0.7,
          "call_oi": 2872800,
          "put_oi": 2124900
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.66,
          "pcr": 0.74,
          "pcr_chg_1d": 0.0,
          "fut_oi": 33980400,
          "oi_chg_pct": -1.23,
          "delivery": 0.42,
          "volume": 0.48,
          "call_oi": 2995200,
          "put_oi": 2213100
        }
      ]
    },
    {
      "symbol": "ITC",
      "rank": 199,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.0,
          1.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 0,
        "neutral_windows": 2,
        "total_windows": 2,
        "pcr_slope_7d": -0.14,
        "pcr_first": 0.84,
        "pcr_last": 0.56,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -1.54,
        "cumulative_price_chg_pct_window": 0.59,
        "persistence_score": 0.0,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -2.0,
          "signals": [
            "PCR 0.57 neutral",
            "PCR easing -0.04"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.18,
          "price_sign": 0,
          "pcr_d1": 0.84,
          "pcr_d2": 0.57,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": -1.13,
          "oi_sign": -1,
          "avg_del": 0.81,
          "peak_del": 1.0,
          "del_chg": 0.38,
          "avg_vol": 0.76,
          "call_oi_growth_pct": 74.28,
          "put_oi_growth_pct": 17.53,
          "opt_oi_growth_pct": 48.35,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 0.56 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.41,
          "price_sign": 1,
          "pcr_d1": 0.57,
          "pcr_d2": 0.56,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -0.41,
          "oi_sign": -1,
          "avg_del": 0.97,
          "peak_del": 1.0,
          "del_chg": -0.06,
          "avg_vol": 0.855,
          "call_oi_growth_pct": 5.52,
          "put_oi_growth_pct": 4.68,
          "opt_oi_growth_pct": 5.22,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.39,
          "pcr": 0.84,
          "pcr_chg_1d": -0.04,
          "fut_oi": 162040000,
          "oi_chg_pct": 0.67,
          "delivery": 0.62,
          "volume": 0.67,
          "call_oi": 48776000,
          "put_oi": 41032000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.18,
          "pcr": 0.57,
          "pcr_chg_1d": -0.04,
          "fut_oi": 160203200,
          "oi_chg_pct": 0.21,
          "delivery": 1.0,
          "volume": 0.85,
          "call_oi": 85006400,
          "put_oi": 48224000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.41,
          "pcr": 0.56,
          "pcr_chg_1d": -0.01,
          "fut_oi": 159552000,
          "oi_chg_pct": -0.41,
          "delivery": 0.94,
          "volume": 0.86,
          "call_oi": 89702400,
          "put_oi": 50481600
        }
      ]
    },
    {
      "symbol": "ALKEM",
      "rank": 200,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          5.0,
          1.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.225,
        "pcr_first": 1.24,
        "pcr_last": 0.79,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -0.67,
        "cumulative_price_chg_pct_window": 3.69,
        "persistence_score": 2.33,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 5.0,
          "signals": [
            "PCR 0.95 approaching bullish zone",
            "PCR collapsing -0.12",
            "Del 1.09x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 2.37,
          "price_sign": 1,
          "pcr_d1": 1.24,
          "pcr_d2": 0.95,
          "pcr_chg": -0.12,
          "fut_oi_chg_pct": 0.27,
          "oi_sign": 1,
          "avg_del": 1.095,
          "peak_del": 1.28,
          "del_chg": 0.37,
          "avg_vol": 1.095,
          "call_oi_growth_pct": 150.75,
          "put_oi_growth_pct": 91.55,
          "opt_oi_growth_pct": 117.96,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 0.79 neutral-to-bullish",
            "PCR collapsing -0.16",
            "Del 1.08x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.29,
          "price_sign": 1,
          "pcr_d1": 0.95,
          "pcr_d2": 0.79,
          "pcr_chg": -0.16,
          "fut_oi_chg_pct": -0.94,
          "oi_sign": -1,
          "avg_del": 1.08,
          "peak_del": 1.28,
          "del_chg": -0.4,
          "avg_vol": 0.94,
          "call_oi_growth_pct": 19.64,
          "put_oi_growth_pct": 0.18,
          "opt_oi_growth_pct": 10.17,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -1.03,
          "pcr": 1.24,
          "pcr_chg_1d": -0.19,
          "fut_oi": 1150000,
          "oi_chg_pct": 1.69,
          "delivery": 0.91,
          "volume": 1.03,
          "call_oi": 58375,
          "put_oi": 72500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 2.37,
          "pcr": 0.95,
          "pcr_chg_1d": -0.12,
          "fut_oi": 1153125,
          "oi_chg_pct": -0.31,
          "delivery": 1.28,
          "volume": 1.16,
          "call_oi": 146375,
          "put_oi": 138875
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.29,
          "pcr": 0.79,
          "pcr_chg_1d": -0.16,
          "fut_oi": 1142250,
          "oi_chg_pct": -0.94,
          "delivery": 0.88,
          "volume": 0.72,
          "call_oi": 175125,
          "put_oi": 139125
        }
      ]
    },
    {
      "symbol": "HCLTECH",
      "rank": 201,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u25cb NONE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          7.5,
          1.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": 0.035,
        "pcr_first": 0.95,
        "pcr_last": 1.02,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 7.8,
        "cumulative_price_chg_pct_window": -0.67,
        "persistence_score": 3.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 7.5,
          "signals": [
            "PCR 1.02 ABOVE 1.0 \u2014 put writers dominant",
            "PCR rising +0.04"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.27,
          "price_sign": 0,
          "pcr_d1": 0.95,
          "pcr_d2": 1.02,
          "pcr_chg": 0.04,
          "fut_oi_chg_pct": 8.2,
          "oi_sign": 1,
          "avg_del": 0.685,
          "peak_del": 0.93,
          "del_chg": 0.49,
          "avg_vol": 0.635,
          "call_oi_growth_pct": 78.5,
          "put_oi_growth_pct": 91.52,
          "opt_oi_growth_pct": 84.84,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 1.02 ABOVE 1.0 \u2014 put writers dominant"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.94,
          "price_sign": -1,
          "pcr_d1": 1.02,
          "pcr_d2": 1.02,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": -0.37,
          "oi_sign": -1,
          "avg_del": 0.985,
          "peak_del": 1.04,
          "del_chg": 0.11,
          "avg_vol": 0.855,
          "call_oi_growth_pct": 3.64,
          "put_oi_growth_pct": 3.89,
          "opt_oi_growth_pct": 3.77,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.95,
          "pcr": 0.95,
          "pcr_chg_1d": -0.05,
          "fut_oi": 34240850,
          "oi_chg_pct": 0.17,
          "delivery": 0.44,
          "volume": 0.45,
          "call_oi": 2733850,
          "put_oi": 2589300
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.27,
          "pcr": 1.02,
          "pcr_chg_1d": 0.04,
          "fut_oi": 37048550,
          "oi_chg_pct": 0.62,
          "delivery": 0.93,
          "volume": 0.82,
          "call_oi": 4880050,
          "put_oi": 4959150
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.94,
          "pcr": 1.02,
          "pcr_chg_1d": 0.0,
          "fut_oi": 36913100,
          "oi_chg_pct": -0.37,
          "delivery": 1.04,
          "volume": 0.89,
          "call_oi": 5057850,
          "put_oi": 5152000
        }
      ]
    },
    {
      "symbol": "ICICIGI",
      "rank": 202,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          6.5,
          1.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.22,
        "pcr_first": 1.15,
        "pcr_last": 0.71,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 6.18,
        "cumulative_price_chg_pct_window": 2.02,
        "persistence_score": 2.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 6.5,
          "signals": [
            "PCR 0.80 neutral-to-bullish",
            "PCR collapsing -0.19",
            "\u2605 NEW LONGS: FutOI +6.8% + Price +1.0%",
            "Del 1.01x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_2_long",
          "price_chg_pct": 1.03,
          "price_sign": 1,
          "pcr_d1": 1.15,
          "pcr_d2": 0.8,
          "pcr_chg": -0.19,
          "fut_oi_chg_pct": 6.82,
          "oi_sign": 1,
          "avg_del": 1.01,
          "peak_del": 1.57,
          "del_chg": 1.12,
          "avg_vol": 1.01,
          "call_oi_growth_pct": 256.78,
          "put_oi_growth_pct": 147.59,
          "opt_oi_growth_pct": 198.3,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 0.71 neutral",
            "PCR collapsing -0.09",
            "Del 1.03x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.98,
          "price_sign": 1,
          "pcr_d1": 0.8,
          "pcr_d2": 0.71,
          "pcr_chg": -0.09,
          "fut_oi_chg_pct": -0.6,
          "oi_sign": -1,
          "avg_del": 1.03,
          "peak_del": 1.57,
          "del_chg": -1.08,
          "avg_vol": 1.045,
          "call_oi_growth_pct": 12.08,
          "put_oi_growth_pct": -0.57,
          "opt_oi_growth_pct": 6.46,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": -0.92,
          "pcr": 1.15,
          "pcr_chg_1d": 0.05,
          "fut_oi": 4953000,
          "oi_chg_pct": 1.91,
          "delivery": 0.45,
          "volume": 0.49,
          "call_oi": 239850,
          "put_oi": 276575
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.03,
          "pcr": 0.8,
          "pcr_chg_1d": -0.19,
          "fut_oi": 5291000,
          "oi_chg_pct": 4.57,
          "delivery": 1.57,
          "volume": 1.53,
          "call_oi": 855725,
          "put_oi": 684775
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.98,
          "pcr": 0.71,
          "pcr_chg_1d": -0.09,
          "fut_oi": 5259150,
          "oi_chg_pct": -0.6,
          "delivery": 0.49,
          "volume": 0.56,
          "call_oi": 959075,
          "put_oi": 680875
        }
      ]
    },
    {
      "symbol": "PGEL",
      "rank": 203,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -4.5,
          1.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.02,
        "pcr_first": 0.65,
        "pcr_last": 0.61,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 0,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 10.98,
        "cumulative_price_chg_pct_window": 0.91,
        "persistence_score": -0.83,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -4.5,
          "signals": [
            "PCR 0.62 neutral",
            "PCR rising +0.06",
            "\u26a0 NEW SHORTS: FutOI +11.8% + Price -0.5%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.53,
          "price_sign": -1,
          "pcr_d1": 0.65,
          "pcr_d2": 0.62,
          "pcr_chg": 0.06,
          "fut_oi_chg_pct": 11.76,
          "oi_sign": 1,
          "avg_del": 0.585,
          "peak_del": 0.63,
          "del_chg": 0.09,
          "avg_vol": 0.835,
          "call_oi_growth_pct": 78.59,
          "put_oi_growth_pct": 69.28,
          "opt_oi_growth_pct": 74.91,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 0.61 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.45,
          "price_sign": 1,
          "pcr_d1": 0.62,
          "pcr_d2": 0.61,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -0.7,
          "oi_sign": -1,
          "avg_del": 0.61,
          "peak_del": 0.63,
          "del_chg": -0.04,
          "avg_vol": 0.825,
          "call_oi_growth_pct": 1.08,
          "put_oi_growth_pct": 0.4,
          "opt_oi_growth_pct": 0.82,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.34,
          "pcr": 0.65,
          "pcr_chg_1d": -0.15,
          "fut_oi": 15766200,
          "oi_chg_pct": 2.44,
          "delivery": 0.54,
          "volume": 0.68,
          "call_oi": 5103400,
          "put_oi": 3333550
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.53,
          "pcr": 0.62,
          "pcr_chg_1d": 0.06,
          "fut_oi": 17619650,
          "oi_chg_pct": 0.53,
          "delivery": 0.63,
          "volume": 0.99,
          "call_oi": 9114300,
          "put_oi": 5643000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.45,
          "pcr": 0.61,
          "pcr_chg_1d": -0.01,
          "fut_oi": 17497100,
          "oi_chg_pct": -0.7,
          "delivery": 0.59,
          "volume": 0.66,
          "call_oi": 9213100,
          "put_oi": 5665800
        }
      ]
    },
    {
      "symbol": "BANDHANBNK",
      "rank": 204,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          3.5,
          1.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.07,
        "pcr_first": 0.87,
        "pcr_last": 0.73,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 0,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 9.62,
        "cumulative_price_chg_pct_window": 2.01,
        "persistence_score": 1.83,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 3.5,
          "signals": [
            "PCR 0.76 neutral-to-bullish",
            "\u2605 NEW LONGS: FutOI +9.2% + Price +0.7%"
          ],
          "interpretation": "\u2605 NEW LONGS (Bullish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.72,
          "price_sign": 1,
          "pcr_d1": 0.87,
          "pcr_d2": 0.76,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": 9.23,
          "oi_sign": 1,
          "avg_del": 0.525,
          "peak_del": 0.61,
          "del_chg": -0.17,
          "avg_vol": 0.635,
          "call_oi_growth_pct": 46.18,
          "put_oi_growth_pct": 27.84,
          "opt_oi_growth_pct": 37.63,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 0.73 neutral"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.28,
          "price_sign": 1,
          "pcr_d1": 0.76,
          "pcr_d2": 0.73,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": 0.36,
          "oi_sign": 1,
          "avg_del": 0.38,
          "peak_del": 0.44,
          "del_chg": -0.12,
          "avg_vol": 0.55,
          "call_oi_growth_pct": 11.11,
          "put_oi_growth_pct": 5.47,
          "opt_oi_growth_pct": 8.66,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.47,
          "pcr": 0.87,
          "pcr_chg_1d": -0.07,
          "fut_oi": 83721600,
          "oi_chg_pct": -3.51,
          "delivery": 0.61,
          "volume": 0.61,
          "call_oi": 15498000,
          "put_oi": 13550400
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.72,
          "pcr": 0.76,
          "pcr_chg_1d": 0.0,
          "fut_oi": 91450800,
          "oi_chg_pct": -0.62,
          "delivery": 0.44,
          "volume": 0.66,
          "call_oi": 22654800,
          "put_oi": 17323200
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.28,
          "pcr": 0.73,
          "pcr_chg_1d": -0.03,
          "fut_oi": 91778400,
          "oi_chg_pct": 0.36,
          "delivery": 0.32,
          "volume": 0.44,
          "call_oi": 25171200,
          "put_oi": 18270000
        }
      ]
    },
    {
      "symbol": "PETRONET",
      "rank": 205,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u25cb NONE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          4.5,
          1.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.03,
        "pcr_first": 0.67,
        "pcr_last": 0.61,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 8.41,
        "cumulative_price_chg_pct_window": 0.13,
        "persistence_score": 2.17,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 4.5,
          "signals": [
            "PCR 0.62 neutral",
            "PCR collapsing -0.13",
            "Del 1.56x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "phase_1_long",
          "price_chg_pct": 0.36,
          "price_sign": 1,
          "pcr_d1": 0.67,
          "pcr_d2": 0.62,
          "pcr_chg": -0.13,
          "fut_oi_chg_pct": 9.65,
          "oi_sign": 1,
          "avg_del": 1.565,
          "peak_del": 2.31,
          "del_chg": 1.49,
          "avg_vol": 1.45,
          "call_oi_growth_pct": 37.63,
          "put_oi_growth_pct": 26.06,
          "opt_oi_growth_pct": 32.97,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 0.61 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u25cb NONE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.23,
          "price_sign": 0,
          "pcr_d1": 0.62,
          "pcr_d2": 0.61,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -1.13,
          "oi_sign": -1,
          "avg_del": 1.54,
          "peak_del": 2.31,
          "del_chg": -1.54,
          "avg_vol": 1.375,
          "call_oi_growth_pct": 2.14,
          "put_oi_growth_pct": 1.49,
          "opt_oi_growth_pct": 1.89,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 3.8,
          "pcr": 0.67,
          "pcr_chg_1d": 0.01,
          "fut_oi": 33474200,
          "oi_chg_pct": -0.32,
          "delivery": 0.82,
          "volume": 0.85,
          "call_oi": 10387300,
          "put_oi": 6999600
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.36,
          "pcr": 0.62,
          "pcr_chg_1d": -0.13,
          "fut_oi": 36704200,
          "oi_chg_pct": 2.57,
          "delivery": 2.31,
          "volume": 2.05,
          "call_oi": 14295600,
          "put_oi": 8823600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.23,
          "pcr": 0.61,
          "pcr_chg_1d": -0.01,
          "fut_oi": 36288100,
          "oi_chg_pct": -1.13,
          "delivery": 0.77,
          "volume": 0.7,
          "call_oi": 14601500,
          "put_oi": 8954700
        }
      ]
    },
    {
      "symbol": "RELIANCE",
      "rank": 206,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (long)",
        "direction": "long",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -7.5,
          1.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.135,
        "pcr_first": 0.74,
        "pcr_last": 0.47,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 3.19,
        "cumulative_price_chg_pct_window": 0.18,
        "persistence_score": -1.83,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -7.5,
          "signals": [
            "PCR 0.44 call writers dominant",
            "\u26a0 NEW SHORTS: FutOI +4.4% + Price -1.3%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -1.32,
          "price_sign": -1,
          "pcr_d1": 0.74,
          "pcr_d2": 0.44,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": 4.42,
          "oi_sign": 1,
          "avg_del": 0.68,
          "peak_del": 0.7,
          "del_chg": 0.04,
          "avg_vol": 0.795,
          "call_oi_growth_pct": 157.44,
          "put_oi_growth_pct": 51.16,
          "opt_oi_growth_pct": 112.2,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 0.47 call writers dominant"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 1.52,
          "price_sign": 1,
          "pcr_d1": 0.44,
          "pcr_d2": 0.47,
          "pcr_chg": 0.03,
          "fut_oi_chg_pct": -1.17,
          "oi_sign": -1,
          "avg_del": 0.875,
          "peak_del": 1.05,
          "del_chg": 0.35,
          "avg_vol": 0.85,
          "call_oi_growth_pct": -4.06,
          "put_oi_growth_pct": 3.7,
          "opt_oi_growth_pct": -1.71,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.88,
          "pcr": 0.74,
          "pcr_chg_1d": 0.01,
          "fut_oi": 89582500,
          "oi_chg_pct": -0.74,
          "delivery": 0.66,
          "volume": 0.69,
          "call_oi": 31242500,
          "put_oi": 23158000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.32,
          "pcr": 0.44,
          "pcr_chg_1d": 0.01,
          "fut_oi": 93538500,
          "oi_chg_pct": 1.8,
          "delivery": 0.7,
          "volume": 0.9,
          "call_oi": 80429500,
          "put_oi": 35006500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.52,
          "pcr": 0.47,
          "pcr_chg_1d": 0.03,
          "fut_oi": 92444000,
          "oi_chg_pct": -1.17,
          "delivery": 1.05,
          "volume": 0.8,
          "call_oi": 77162000,
          "put_oi": 36302500
        }
      ]
    },
    {
      "symbol": "UNOMINDA",
      "rank": 207,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -8.5,
          1.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.28,
        "pcr_first": 1.05,
        "pcr_last": 0.49,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 10.14,
        "cumulative_price_chg_pct_window": -1.12,
        "persistence_score": -2.17,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -8.5,
          "signals": [
            "PCR 0.50 call writers dominant",
            "\u26a0 NEW SHORTS: FutOI +11.8% + Price -3.3%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "phase_1_short",
          "price_chg_pct": -3.27,
          "price_sign": -1,
          "pcr_d1": 1.05,
          "pcr_d2": 0.5,
          "pcr_chg": 0.0,
          "fut_oi_chg_pct": 11.84,
          "oi_sign": 1,
          "avg_del": 0.845,
          "peak_del": 1.07,
          "del_chg": -0.45,
          "avg_vol": 0.86,
          "call_oi_growth_pct": 235.47,
          "put_oi_growth_pct": 61.09,
          "opt_oi_growth_pct": 146.29,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 0.49 call writers dominant"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 2.22,
          "price_sign": 1,
          "pcr_d1": 0.5,
          "pcr_d2": 0.49,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": -1.52,
          "oi_sign": -1,
          "avg_del": 0.87,
          "peak_del": 1.12,
          "del_chg": 0.5,
          "avg_vol": 0.855,
          "call_oi_growth_pct": 3.26,
          "put_oi_growth_pct": 1.39,
          "opt_oi_growth_pct": 2.64,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.14,
          "pcr": 1.05,
          "pcr_chg_1d": -0.16,
          "fut_oi": 4455000,
          "oi_chg_pct": 0.11,
          "delivery": 1.07,
          "volume": 1.0,
          "call_oi": 376750,
          "put_oi": 394350
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -3.27,
          "pcr": 0.5,
          "pcr_chg_1d": 0.0,
          "fut_oi": 4982450,
          "oi_chg_pct": -2.42,
          "delivery": 0.62,
          "volume": 0.72,
          "call_oi": 1263900,
          "put_oi": 635250
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 2.22,
          "pcr": 0.49,
          "pcr_chg_1d": -0.01,
          "fut_oi": 4906550,
          "oi_chg_pct": -1.52,
          "delivery": 1.12,
          "volume": 0.99,
          "call_oi": 1305150,
          "put_oi": 644050
        }
      ]
    },
    {
      "symbol": "GODREJCP",
      "rank": 208,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -3.5,
          1.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.04,
        "pcr_first": 0.95,
        "pcr_last": 0.87,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 0,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 13.68,
        "cumulative_price_chg_pct_window": 0.27,
        "persistence_score": -0.5,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -3.5,
          "signals": [
            "PCR 0.92 approaching bullish zone",
            "\u26a0 NEW SHORTS: FutOI +14.1% + Price -1.1%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": -1.1,
          "price_sign": -1,
          "pcr_d1": 0.95,
          "pcr_d2": 0.92,
          "pcr_chg": -0.01,
          "fut_oi_chg_pct": 14.12,
          "oi_sign": 1,
          "avg_del": 0.55,
          "peak_del": 0.6,
          "del_chg": -0.1,
          "avg_vol": 0.595,
          "call_oi_growth_pct": 100.18,
          "put_oi_growth_pct": 95.64,
          "opt_oi_growth_pct": 97.97,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 0.87 approaching bullish zone",
            "PCR easing -0.05"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.39,
          "price_sign": 1,
          "pcr_d1": 0.92,
          "pcr_d2": 0.87,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": -0.39,
          "oi_sign": -1,
          "avg_del": 0.515,
          "peak_del": 0.53,
          "del_chg": 0.03,
          "avg_vol": 0.52,
          "call_oi_growth_pct": 14.23,
          "put_oi_growth_pct": 7.34,
          "opt_oi_growth_pct": 10.92,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.29,
          "pcr": 0.95,
          "pcr_chg_1d": 0.1,
          "fut_oi": 10935500,
          "oi_chg_pct": 1.44,
          "delivery": 0.6,
          "volume": 0.69,
          "call_oi": 570500,
          "put_oi": 539500
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.1,
          "pcr": 0.92,
          "pcr_chg_1d": -0.01,
          "fut_oi": 12480000,
          "oi_chg_pct": 1.71,
          "delivery": 0.5,
          "volume": 0.5,
          "call_oi": 1142000,
          "put_oi": 1055500
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.39,
          "pcr": 0.87,
          "pcr_chg_1d": -0.05,
          "fut_oi": 12431000,
          "oi_chg_pct": -0.39,
          "delivery": 0.53,
          "volume": 0.54,
          "call_oi": 1304500,
          "put_oi": 1133000
        }
      ]
    },
    {
      "symbol": "SBICARD",
      "rank": 209,
      "days_available": 3,
      "latest_score": 1.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -2.5,
          1.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 0,
        "neutral_windows": 2,
        "total_windows": 2,
        "pcr_slope_7d": -0.165,
        "pcr_first": 1.06,
        "pcr_last": 0.73,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 0,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -0.77,
        "cumulative_price_chg_pct_window": 0.94,
        "persistence_score": -0.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -2.5,
          "signals": [
            "PCR 0.76 neutral-to-bullish",
            "PCR easing -0.08"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "pre_phase_1_short",
          "price_chg_pct": -0.35,
          "price_sign": -1,
          "pcr_d1": 1.06,
          "pcr_d2": 0.76,
          "pcr_chg": -0.08,
          "fut_oi_chg_pct": -0.64,
          "oi_sign": -1,
          "avg_del": 0.52,
          "peak_del": 0.66,
          "del_chg": 0.28,
          "avg_vol": 0.58,
          "call_oi_growth_pct": 40.88,
          "put_oi_growth_pct": 0.86,
          "opt_oi_growth_pct": 20.33,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 1.0,
          "signals": [
            "PCR 0.73 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.29,
          "price_sign": 1,
          "pcr_d1": 0.76,
          "pcr_d2": 0.73,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": -0.13,
          "oi_sign": -1,
          "avg_del": 0.54,
          "peak_del": 0.66,
          "del_chg": -0.24,
          "avg_vol": 0.565,
          "call_oi_growth_pct": 4.48,
          "put_oi_growth_pct": 0.84,
          "opt_oi_growth_pct": 2.91,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 0.27,
          "pcr": 1.06,
          "pcr_chg_1d": -0.18,
          "fut_oi": 25096000,
          "oi_chg_pct": 4.31,
          "delivery": 0.38,
          "volume": 0.49,
          "call_oi": 4295200,
          "put_oi": 4535200
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.35,
          "pcr": 0.76,
          "pcr_chg_1d": -0.08,
          "fut_oi": 24935200,
          "oi_chg_pct": 0.78,
          "delivery": 0.66,
          "volume": 0.67,
          "call_oi": 6051200,
          "put_oi": 4574400
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.29,
          "pcr": 0.73,
          "pcr_chg_1d": -0.03,
          "fut_oi": 24901600,
          "oi_chg_pct": -0.13,
          "delivery": 0.42,
          "volume": 0.46,
          "call_oi": 6322400,
          "put_oi": 4612800
        }
      ]
    },
    {
      "symbol": "TIINDIA",
      "rank": 210,
      "days_available": 3,
      "latest_score": -0.5,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "Mild long build",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (short)",
        "direction": "short",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          2.0,
          -0.5
        ],
        "bullish_windows": 0,
        "bearish_windows": 0,
        "neutral_windows": 2,
        "total_windows": 2,
        "pcr_slope_7d": -0.08,
        "pcr_first": 0.69,
        "pcr_last": 0.53,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 3,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 0.44,
        "cumulative_price_chg_pct_window": 0.64,
        "persistence_score": 0.33,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": 2.0,
          "signals": [
            "PCR 0.55 neutral",
            "Del 1.04x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (long)",
            "direction": "long",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.59,
          "price_sign": 1,
          "pcr_d1": 0.69,
          "pcr_d2": 0.55,
          "pcr_chg": 0.01,
          "fut_oi_chg_pct": -0.43,
          "oi_sign": -1,
          "avg_del": 1.045,
          "peak_del": 1.31,
          "del_chg": -0.53,
          "avg_vol": 0.845,
          "call_oi_growth_pct": 105.88,
          "put_oi_growth_pct": 62.93,
          "opt_oi_growth_pct": 88.33,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": -0.5,
          "signals": [
            "PCR 0.53 call writers dominant"
          ],
          "interpretation": "Mild long build",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": 0.05,
          "price_sign": 0,
          "pcr_d1": 0.55,
          "pcr_d2": 0.53,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": 0.88,
          "oi_sign": 1,
          "avg_del": 0.765,
          "peak_del": 0.78,
          "del_chg": -0.03,
          "avg_vol": 0.835,
          "call_oi_growth_pct": 14.95,
          "put_oi_growth_pct": 12.11,
          "opt_oi_growth_pct": 13.95,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 2.2,
          "pcr": 0.69,
          "pcr_chg_1d": 0.03,
          "fut_oi": 2541000,
          "oi_chg_pct": -0.24,
          "delivery": 1.31,
          "volume": 0.82,
          "call_oi": 170200,
          "put_oi": 117600
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 0.59,
          "pcr": 0.55,
          "pcr_chg_1d": 0.01,
          "fut_oi": 2530000,
          "oi_chg_pct": 2.55,
          "delivery": 0.78,
          "volume": 0.87,
          "call_oi": 350400,
          "put_oi": 191600
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.05,
          "pcr": 0.53,
          "pcr_chg_1d": -0.02,
          "fut_oi": 2552200,
          "oi_chg_pct": 0.88,
          "delivery": 0.75,
          "volume": 0.8,
          "call_oi": 402800,
          "put_oi": 214800
        }
      ]
    },
    {
      "symbol": "DMART",
      "rank": 211,
      "days_available": 3,
      "latest_score": 0.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605\u2605 DOUBLE (short)",
        "direction": "short",
        "count": 2
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          5.0,
          0.0
        ],
        "bullish_windows": 1,
        "bearish_windows": 0,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.05,
        "pcr_first": 0.86,
        "pcr_last": 0.76,
        "days_delivery_institutional": 1,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -12.78,
        "cumulative_price_chg_pct_window": 0.73,
        "persistence_score": 1.67,
        "regime": "MIXED BULLISH-LEANING"
      },
      "all_windows": [
        {
          "score": 5.0,
          "signals": [
            "PCR 0.81 neutral-to-bullish",
            "Del 1.24x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2191 SHORT COVERING (lagging)",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.07,
          "price_sign": 1,
          "pcr_d1": 0.86,
          "pcr_d2": 0.81,
          "pcr_chg": -0.03,
          "fut_oi_chg_pct": -12.28,
          "oi_sign": -1,
          "avg_del": 1.245,
          "peak_del": 2.09,
          "del_chg": -1.69,
          "avg_vol": 1.445,
          "call_oi_growth_pct": 53.14,
          "put_oi_growth_pct": 44.7,
          "opt_oi_growth_pct": 49.25,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 0.0,
          "signals": [
            "PCR 0.76 neutral-to-bullish",
            "PCR easing -0.05"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605\u2605 DOUBLE (short)",
            "direction": "short",
            "count": 2
          },
          "phase": "no_signal",
          "price_chg_pct": -0.34,
          "price_sign": -1,
          "pcr_d1": 0.81,
          "pcr_d2": 0.76,
          "pcr_chg": -0.05,
          "fut_oi_chg_pct": -0.57,
          "oi_sign": -1,
          "avg_del": 0.42,
          "peak_del": 0.44,
          "del_chg": 0.04,
          "avg_vol": 0.365,
          "call_oi_growth_pct": 2.53,
          "put_oi_growth_pct": -3.07,
          "opt_oi_growth_pct": 0.03,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 7.94,
          "pcr": 0.86,
          "pcr_chg_1d": 0.03,
          "fut_oi": 4782300,
          "oi_chg_pct": -5.35,
          "delivery": 2.09,
          "volume": 2.54,
          "call_oi": 1140750,
          "put_oi": 975900
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": 1.07,
          "pcr": 0.81,
          "pcr_chg_1d": -0.03,
          "fut_oi": 4195050,
          "oi_chg_pct": -0.96,
          "delivery": 0.4,
          "volume": 0.35,
          "call_oi": 1746900,
          "put_oi": 1412100
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": -0.34,
          "pcr": 0.76,
          "pcr_chg_1d": -0.05,
          "fut_oi": 4171050,
          "oi_chg_pct": -0.57,
          "delivery": 0.44,
          "volume": 0.38,
          "call_oi": 1791150,
          "put_oi": 1368750
        }
      ]
    },
    {
      "symbol": "BIOCON",
      "rank": 212,
      "days_available": 3,
      "latest_score": 0.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -7.0,
          0.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 1,
        "neutral_windows": 1,
        "total_windows": 2,
        "pcr_slope_7d": -0.075,
        "pcr_first": 0.83,
        "pcr_last": 0.68,
        "days_delivery_institutional": 0,
        "days_delivery_above_normal": 1,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": 16.74,
        "cumulative_price_chg_pct_window": -0.34,
        "persistence_score": -2.33,
        "regime": "MIXED BEARISH-LEANING"
      },
      "all_windows": [
        {
          "score": -7.0,
          "signals": [
            "PCR 0.70 neutral",
            "PCR easing -0.04",
            "\u26a0 NEW SHORTS: FutOI +18.0% + Price -1.2%"
          ],
          "interpretation": "\u26a0 NEW SHORTS (Bearish)",
          "triple_convergence": {
            "status": "\u2605\u2605\u2605 TC (SHORT)",
            "direction": "short",
            "count": 3
          },
          "phase": "no_signal",
          "price_chg_pct": -1.17,
          "price_sign": -1,
          "pcr_d1": 0.83,
          "pcr_d2": 0.7,
          "pcr_chg": -0.04,
          "fut_oi_chg_pct": 17.96,
          "oi_sign": 1,
          "avg_del": 0.55,
          "peak_del": 0.73,
          "del_chg": -0.36,
          "avg_vol": 0.6,
          "call_oi_growth_pct": 122.52,
          "put_oi_growth_pct": 87.63,
          "opt_oi_growth_pct": 106.72,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 0.0,
          "signals": [
            "PCR 0.68 neutral"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 0.84,
          "price_sign": 1,
          "pcr_d1": 0.7,
          "pcr_d2": 0.68,
          "pcr_chg": -0.02,
          "fut_oi_chg_pct": -1.03,
          "oi_sign": -1,
          "avg_del": 0.385,
          "peak_del": 0.4,
          "del_chg": 0.03,
          "avg_vol": 0.33,
          "call_oi_growth_pct": 2.99,
          "put_oi_growth_pct": 0.51,
          "opt_oi_growth_pct": 1.97,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 1.19,
          "pcr": 0.83,
          "pcr_chg_1d": 0.04,
          "fut_oi": 31885000,
          "oi_chg_pct": -0.34,
          "delivery": 0.73,
          "volume": 0.85,
          "call_oi": 9182500,
          "put_oi": 7600000
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -1.17,
          "pcr": 0.7,
          "pcr_chg_1d": -0.04,
          "fut_oi": 37610000,
          "oi_chg_pct": 2.82,
          "delivery": 0.37,
          "volume": 0.35,
          "call_oi": 20432500,
          "put_oi": 14260000
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 0.84,
          "pcr": 0.68,
          "pcr_chg_1d": -0.02,
          "fut_oi": 37222500,
          "oi_chg_pct": -1.03,
          "delivery": 0.4,
          "volume": 0.31,
          "call_oi": 21042500,
          "put_oi": 14332500
        }
      ]
    },
    {
      "symbol": "TATATECH",
      "rank": 213,
      "days_available": 3,
      "latest_score": 0.0,
      "latest_tier": "NO SIGNAL",
      "latest_sign": "neutral",
      "latest_phase": "no_signal",
      "latest_interpretation": "\u2192 CONSOLIDATION",
      "latest_triple_convergence": {
        "status": "\u2605 SINGLE",
        "direction": "none",
        "count": 1
      },
      "latest_date_d1": "2026-04-09",
      "latest_date_d2": "2026-04-10",
      "trajectory": {
        "window_scores": [
          -0.5,
          0.0
        ],
        "bullish_windows": 0,
        "bearish_windows": 0,
        "neutral_windows": 2,
        "total_windows": 2,
        "pcr_slope_7d": -0.085,
        "pcr_first": 0.91,
        "pcr_last": 0.74,
        "days_delivery_institutional": 2,
        "days_delivery_above_normal": 2,
        "total_days": 3,
        "cumulative_oi_chg_pct_window": -12.25,
        "cumulative_price_chg_pct_window": 0.87,
        "persistence_score": -0.17,
        "regime": "CHOPPY / INDECISIVE"
      },
      "all_windows": [
        {
          "score": -0.5,
          "signals": [
            "PCR 0.86 approaching bullish zone",
            "PCR surging +0.09"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": -0.44,
          "price_sign": -1,
          "pcr_d1": 0.91,
          "pcr_d2": 0.86,
          "pcr_chg": 0.09,
          "fut_oi_chg_pct": -10.72,
          "oi_sign": -1,
          "avg_del": 0.71,
          "peak_del": 1.05,
          "del_chg": 0.68,
          "avg_vol": 0.73,
          "call_oi_growth_pct": 38.27,
          "put_oi_growth_pct": 30.61,
          "opt_oi_growth_pct": 34.62,
          "date_d1": "2026-04-01",
          "date_d2": "2026-04-09"
        },
        {
          "score": 0.0,
          "signals": [
            "PCR 0.74 neutral",
            "PCR collapsing -0.12",
            "Del 1.07x + Price\u2191 INSTITUTIONAL ACCUMULATION"
          ],
          "interpretation": "\u2192 CONSOLIDATION",
          "triple_convergence": {
            "status": "\u2605 SINGLE",
            "direction": "none",
            "count": 1
          },
          "phase": "no_signal",
          "price_chg_pct": 1.32,
          "price_sign": 1,
          "pcr_d1": 0.86,
          "pcr_d2": 0.74,
          "pcr_chg": -0.12,
          "fut_oi_chg_pct": -1.71,
          "oi_sign": -1,
          "avg_del": 1.07,
          "peak_del": 1.09,
          "del_chg": 0.04,
          "avg_vol": 0.915,
          "call_oi_growth_pct": 16.27,
          "put_oi_growth_pct": -0.36,
          "opt_oi_growth_pct": 8.59,
          "date_d1": "2026-04-09",
          "date_d2": "2026-04-10"
        }
      ],
      "daily_timeline": [
        {
          "date": "2026-04-01",
          "price_chg_pct": 4.29,
          "pcr": 0.91,
          "pcr_chg_1d": 0.0,
          "fut_oi": 8028800,
          "oi_chg_pct": -3.83,
          "delivery": 0.37,
          "volume": 0.57,
          "call_oi": 1323200,
          "put_oi": 1202400
        },
        {
          "date": "2026-04-09",
          "price_chg_pct": -0.44,
          "pcr": 0.86,
          "pcr_chg_1d": 0.09,
          "fut_oi": 7168000,
          "oi_chg_pct": -1.84,
          "delivery": 1.05,
          "volume": 0.89,
          "call_oi": 1829600,
          "put_oi": 1570400
        },
        {
          "date": "2026-04-10",
          "price_chg_pct": 1.32,
          "pcr": 0.74,
          "pcr_chg_1d": -0.12,
          "fut_oi": 7045600,
          "oi_chg_pct": -1.71,
          "delivery": 1.09,
          "volume": 0.94,
          "call_oi": 2127200,
          "put_oi": 1564800
        }
      ]
    }
  ],
  "phase_map": {
    "phase_2_long": [
      "POWERINDIA",
      "NAM-INDIA",
      "ABB",
      "SONACOMS",
      "CUMMINSIND",
      "ADANIENSOL",
      "POLYCAB",
      "UNIONBANK",
      "WAAREEENER",
      "PIDILITIND",
      "COCHINSHIP",
      "MOTILALOFS",
      "VEDL",
      "VOLTAS",
      "SIEMENS",
      "SUZLON",
      "WIPRO",
      "RVNL",
      "ASTRAL",
      "OBEROIRLTY",
      "SUPREMEIND",
      "GODFRYPHLP"
    ],
    "phase_1_long": [
      "GODREJPROP",
      "360ONE",
      "ABCAPITAL",
      "HEROMOTOCO",
      "ASIANPAINT",
      "CAMS",
      "KOTAKBANK",
      "VBL",
      "LICI",
      "DIVISLAB",
      "LAURUSLABS",
      "AMBER",
      "UNITDSPR",
      "RECLTD",
      "TATAPOWER",
      "JINDALSTEL",
      "KALYANKJIL",
      "ADANIENT",
      "NATIONALUM",
      "POLICYBZR",
      "IREDA",
      "UPL",
      "JSWSTEEL",
      "LTF",
      "KAYNES",
      "ETERNAL",
      "HINDUNILVR",
      "MCX",
      "PHOENIXLTD",
      "SOLARINDS",
      "NESTLEIND",
      "MANAPPURAM",
      "HINDALCO",
      "IRFC",
      "NMDC",
      "ICICIPRULI",
      "DIXON",
      "BAJAJHLDNG",
      "PFC",
      "KFINTECH",
      "HUDCO",
      "MAZDOCK",
      "VMM"
    ],
    "pre_phase_1_long": [
      "BAJAJ-AUTO",
      "MOTHERSON",
      "MARICO",
      "FEDERALBNK",
      "BHEL",
      "ASHOKLEY",
      "MFSL",
      "TMPV",
      "LUPIN",
      "ICICIBANK",
      "PREMIERENE",
      "TORNTPHARM",
      "TITAN",
      "HDFCLIFE",
      "SBIN",
      "LT",
      "GRASIM",
      "IEX",
      "AUROPHARMA"
    ],
    "phase_2_short": [
      "COALINDIA",
      "TCS",
      "SUNPHARMA",
      "INFY",
      "COFORGE"
    ],
    "phase_1_short": [
      "NAUKRI",
      "MPHASIS"
    ],
    "pre_phase_1_short": [
      "DELHIVERY",
      "GLENMARK"
    ],
    "no_signal": [
      "BOSCHLTD",
      "AMBUJACEM",
      "SAMMAANCAP",
      "LODHA",
      "INDIANB",
      "MAXHEALTH",
      "TVSMOTOR",
      "EICHERMOT",
      "TRENT",
      "HINDPETRO",
      "ULTRACEMCO",
      "OFSS",
      "BHARATFORG",
      "PNBHOUSING",
      "HAL",
      "JIOFIN",
      "BLUESTARCO",
      "GMRAIRPORT",
      "ONGC",
      "GAIL",
      "YESBANK",
      "BSE",
      "CGPOWER",
      "CHOLAFIN",
      "PAYTM",
      "M&M",
      "BAJFINANCE",
      "HDFCAMC",
      "ADANIPORTS",
      "CROMPTON",
      "CIPLA",
      "ADANIGREEN",
      "BPCL",
      "INDHOTEL",
      "DRREDDY",
      "INOXWIND",
      "DLF",
      "CANBK",
      "CDSL",
      "ANGELONE",
      "PNB",
      "COLPAL",
      "BAJAJFINSV",
      "AXISBANK",
      "ZYDUSLIFE",
      "HINDZINC",
      "IDFCFIRSTB",
      "BANKBARODA",
      "DALBHARAT",
      "AUBANK",
      "IDEA",
      "TATACONSUM",
      "JUBLFOOD",
      "NBCC",
      "EXIDEIND",
      "MUTHOOTFIN",
      "PPLPHARMA",
      "ADANIPOWER",
      "INDIGO",
      "PAGEIND",
      "BHARTIARTL",
      "SHRIRAMFIN",
      "TATASTEEL",
      "APOLLOHOSP",
      "IOC",
      "NYKAA",
      "RBLBANK",
      "MARUTI",
      "DABUR",
      "FORCEMOT",
      "BRITANNIA",
      "MANKIND",
      "NHPC",
      "SRF",
      "PIIND",
      "LTM",
      "SWIGGY",
      "TATAELXSI",
      "NUVAMA",
      "HAVELLS",
      "BANKINDIA",
      "BDL",
      "INDUSTOWER",
      "CONCOR",
      "INDUSINDBK",
      "PERSISTENT",
      "NTPC",
      "HDFCBANK",
      "LICHSGFIN",
      "BEL",
      "SBILIFE",
      "JSWENERGY",
      "PRESTIGE",
      "KEI",
      "TORNTPOWER",
      "APLAPOLLO",
      "FORTIS",
      "KPITTECH",
      "OIL",
      "HYUNDAI",
      "SHREECEM",
      "POWERGRID",
      "TECHM",
      "SAIL",
      "PATANJALI",
      "ITC",
      "ALKEM",
      "HCLTECH",
      "ICICIGI",
      "PGEL",
      "BANDHANBNK",
      "PETRONET",
      "RELIANCE",
      "UNOMINDA",
      "GODREJCP",
      "SBICARD",
      "TIINDIA",
      "DMART",
      "BIOCON",
      "TATATECH"
    ]
  },
  "warnings": [
    {
      "file": "Derivative_Analytics_01-Apr-2026.csv",
      "row": 214,
      "reason": "missing critical field"
    }
  ]
}
```
