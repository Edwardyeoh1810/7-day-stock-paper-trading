# Research journal — 2026-09-23_check_0000-research

Companion to the generated journal entry for `2026-09-23_check_0000_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-22T16:14Z (00:14 Asia/Kuala_Lumpur, 2026-09-23), slot
  `2026-09-23_check_0000`.
- **What was done:** Read `AGENTS.md`, `02-项目文档-docs/TRADING-STRATEGY.md`,
  `03-定时任务-routines/AUTOMATION-PROMPT.md`, `04-运行状态-state/readiness.json`,
  `04-运行状态-state/paper-config.json`, `05-交易记录-data/current-state.json`, the **23:00 slot's research
  note** and `reviews/LESSONS.md`. Ran the read-only observation at 16:03:59Z, then pulled 5m, 1h, 4h and daily
  bars, the book, the 24h ticker, funding, mark/index and open interest for all five watchlist contracts from the
  demo host's public endpoints; ran the artifact scan at both 5m and 1h; re-implemented the engine's reward/risk
  formula independently from `paper_ledger.py`; took a confirming requote 140 seconds after the first sweep as
  **L-003** requires; ran one web search for scheduled news. Submitted a `no_trade` decision through
  `paper_engine.py` at 16:12:50Z.
- **Why it was done:** The 00:00 slot was due (`due_slot: 2026-09-23_check_0000`, 240 planned slots) and no
  position was open, so an entry was permitted if and only if every entry condition and every lesson was satisfied.
- **Timing:** Observation 16:03:59Z, research sweep 16:04:37Z, requote 16:06:57Z, decision written 16:11Z, engine
  submitted 16:12:50Z (00:12 MYT) — **13 minutes after the slot. ON TIME**, third consecutive on-time check since
  the 09:00 stall on 2026-09-22.
- **Order proposed:** No.
- **Order placed:** No. The engine returned `status: no_trade`, `live_order_sent: false`.
- **Order filled:** No.
- **Exchange stop/target reconciliation:** None to reconcile. Flat before and after; no exit order has ever been
  placed in this experiment.
- **Current holdings:** None. Flat.
- **Current cash:** 5000 USDT. Demo wallet balance 5000.04174826 USDT.
- **Current risk:** 0 USDT open risk; 0 USDT realized today. Ledger date `2026-09-22`, trading day index 2.
- **Evidence captured:** `05-交易记录-data/evidence/2026-09-23_check_0000.json` (read-only run),
  `05-交易记录-data/evidence/2026-09-23_check_0000_paper.json` (engine), and this note.

## The 23:00 assignment was answered, and the answer falsified the 23:00 hypothesis

The 23:00 note named outcome (1) — a pullback low forming **above** the 1.5701 pivot — as the one construction
that would *solve* the distance problem, reasoning that a structural stop beneath such a retest low would be
**both noise-safe and close**.

**Outcome (1) largely arrived.**

| Time | XRPUSDT | Event |
|---|---|---|
| 15:05Z | O1.5639 **H1.5731** C1.5701 | **Pivot reclaimed** within 30 min of the 1.5633 low |
| 15:25Z | **H1.5827** L1.5699 | Second push; 0.815% range — the new noise bar |
| 15:35Z | **L1.5671** | **Dipped back BELOW the pivot** |
| 15:40Z | L1.5687 | Still below |
| 15:45Z | **H1.5821** L1.5730 | Re-reclaimed; third rejection, lower high |
| 15:55Z | L1.5712 | Pullback low **above** the pivot |
| 16:00Z | **L1.5710** C1.5738 | The retest low outcome (1) asked for |
| 16:06:57Z (requote) | 1.5707 / 1.5708 | **Back on the pivot, −0.197% in 140 s** |
| 16:12:58Z (engine quote) | **1.5633 / 1.5694** | **Pivot lost; spread 38.9 bps, OVER the cap** |

**It solved nothing.** The retest low sits at 1.5710, **0.06% above** the pivot, so the structural stop beneath it
is 0.135%–0.331% from the entry — **0.17× to 0.41× the 0.815% noise bar, the most sub-noise construction of the
entire experiment.** The retest did not produce a stop that was noise-safe and close. It produced the *tightest*
stop yet seen, because a clean retest is **by construction** close to the level, and "close to the level" and
"wider than the noise bar" are the same measurement pulling in opposite directions.

## The contribution: the distance problem as a geometric requirement

A valid entry needs risk ≥ **N** (L-002's noise bar) and reward ≥ 1.5 × risk. So the **structural stop-to-target
span must be at least 2.5N**, plus ~0.14% of round-trip fee and slippage drag — about **2.2% when N = 0.815%**, or
**≈2.7N** as a rule of thumb.

Pinning the stop at 1.5690 and sweeping the entry proves no price rescues it:

| Entry | Risk | vs N | Net RR → 1.5876 |
|---|---|---|---|
| 1.5760 | 0.464% | 0.57× | 1.020 |
| 1.5790 | 0.653% | 0.80× | 0.523 |
| 1.5820 | 0.842% | **1.03×** | 0.222 |
| 1.5850 | 1.029% | 1.26× | 0.021 |
| 1.5880 | 1.216% | 1.49× | −0.124 |

Risk-safety and the ratio move in **opposite directions and never both pass**, because the 1.5690→1.5876 span is
**1.185%**, barely half the ~2.2% required. This converts the distance problem from an observation repeated across
six checks into a **screen that runs before any ratio is computed**: measure N, require ~2.7N of clean structural
span, stop if the structure does not offer it.

## L-003 fired on the long, in 140 seconds, for the first time

Same stop, same target, 140 seconds apart:

| Quote | Book | Risk (stop 1.5690) | Net RR → 1.5876 |
|---|---|---|---|
| 16:04:37Z | 1.5738 / 1.5739 | 0.331% | **1.618** |
| 16:06:57Z | 1.5707 / 1.5708 | **0.135%** | **3.649** |

The ratio **more than doubled** purely because price fell 0.197% **onto** its fixed stop. That is L-003 verbatim —
the improvement is the risk shrinking — and the premise degraded in step, since the reclaim was being re-tested
from above. **The engine's quote six minutes later settled it: the pivot was lost (bid 1.5633) and the spread blew
out to 38.9 bps, over the 25 bps cap.** An entry would have been rejected on spread regardless. Third reproduction
of the L-003 pattern; first on the long side.

## The new finding for the review: the noise test does not stop target-stretching

At the requote, **four constructions clear the 1.5 floor with noise-safe stops, and L-002 rejects none of them**:

| Contract | Side | Stop | vs N | Target | Net RR | Real nearer target |
|---|---|---|---|---|---|---|
| ETHUSDT | long | 2735.50 | 1.12× | 2804.59 | **4.643** | 2761.62 → **1.133** |
| SOLUSDT | long | 116.70 | 1.38× | 119.86 | **3.303** | 117.87 → **0.593** |
| XRPUSDT | short | 1.5840 | 1.06× | 1.5393 | **1.884** | 1.5633 → **0.336** |
| BNBUSDT | long | 782.00 | 3.37× | 800.90 | **1.657** | 792.26 → **0.442** |

Every one passes **only because its target is the extreme of the multi-day range, beyond an intervening level that
has already rejected** — and **not one has two independent evidence categories for its direction.** The arithmetic
is not scarce; it is abundant, and it becomes abundant exactly when the target is allowed to float. L-002 was
written to stop the *stop* being chosen to fit the number; **the mirror failure is choosing the *target* to fit the
number**, and this is the first clean instance, on three contracts at once. This is the review item.

## The evidence bar was the binding constraint — the first inversion of this experiment

| | Supporting categories | Valid construction? |
|---|---|---|
| **XRPUSDT LONG** | **THREE** — trend, derivatives, market_context | **No** — all sub-noise, or target-stretched |
| **XRPUSDT SHORT** | **ONE** — price_action | **Yes** — stop 1.5840, 1.06×, RR 1.884 |

- **trend (for the long):** 4h ascending lows 1.4939 (04:00Z) → 1.5142 (08:00Z) → 1.5306 (12:00Z); the
  failed-breakout 4h bar itself closed in the upper third of its range; daily **+6.272%**.
- **derivatives (for the long):** funding **−0.016553%**, still the **only** negative rate in the complex
  (ETH/SOL +0.010000%, BTC +0.006600%, BNB +0.004865%) and roughly **double** the −0.008393% of an hour ago. It
  has persisted through breakout, failure *and* reclaim — a squeeze signal. Next funding 00:00Z; a long receives.
- **market_context (for the long over 24h, against it at this instant):** XRPUSDT **+5.158%** against BTC +0.646%,
  ETH −0.227%, SOL −0.424%, BNB −1.771%. But in the requote window XRP fell **hardest** (−0.197% vs −0.055 to
  −0.094%). Recorded both ways rather than resolved.
- **volume: examined and explicitly NOT claimed.** The short's natural claim — reclaim on lighter volume — is
  **false**: the fade traded 869.1M / 956.8M / 818.4M but the 15:15Z reclaim bar traded **897.0M**, heavier than
  two of the three. The 1h series is **again a flat band** (15:00Z 5,538.9M vs 14:00Z 5,707.5M vs 13:00Z
  6,066.6M vs 11:00Z 6,182.4M) — **third consecutive check**; this finding is firm enough to stop re-deriving.
- ETH/BNB/SOL longs declined on **evidence**: all three pay positive funding, none has a positive 4h structure
  (BNB is the weakest of the five at −1.771% with 4h lower highs 807.74 → 800.90 → 790.66 → 789.77 → 792.26), and
  market_context is directionless. Zero to one supporting category each.

## Artifact scan — two corrections to the 23:00 note

**No new artifact printed on any contract at either resolution. Fifth consecutive fully clean 5m scan.**

- **Correction 1:** the 23:00 note recorded BTCUSDT's 95804.10 print as having aged out. The 09-21 **09:00Z**
  print did; a **second print of the same price at 09-21 14:00Z is still inside the 30-bar 1h window**. BTCUSDT
  therefore carries **five** contaminated 1h bars this check, not four: 87888.00 (12:00Z), 86769.40 (13:00Z,
  range-only — the print LESSONS records as a 13:50Z 5m artifact, now rolled up), 95804.10 (14:00Z), 91000.00
  (19:00Z), 90389.80 (20:00Z).
- **Correction 2:** the 23:00 note recorded ETHUSDT as scanning clean at 1h. It scans clean on **wick geometry**
  but **not on range** — 09-21 15:00Z high 2795.00, range 2.381% against a 0.647% median. The print has **not**
  aged out.
- BTCUSDT's 24h high field still reads **91000.00** against a real session top near 86400 — and a web source
  placed bitcoin near **$86,000**, the **first external corroboration** of the L-001 contamination.
- BTCUSDT excluded for a **ninth** consecutive check. Its spread was 0.13 and 3.42 bps, so the exclusion rests on
  artifacts alone. **L-001's re-test clock:** last artifact print 09-21 20:00Z, ~20h05m before this decision, so a
  full artifact-free day is reached near **04:00 MYT** — between the 02:00 and 09:00 checks. **The exclusion
  stands in full; only the daily review may retire a lesson.**
- All five were inside the 25 bps spread cap at both research sweeps. SOLUSDT carried the loosest book (7.67 and
  10.24 bps). **The engine's 16:12:58Z quote then showed XRPUSDT at 38.9 bps, over the cap** — the demo book
  degrades fast when the pivot breaks.

## For the 02:00 check

1. **XRPUSDT lost 1.5701 again at 16:12:58Z (bid 1.5633).** The long's `price_action` leg is gone; `trend`,
   `derivatives` and `market_context` may survive. Re-read all three from scratch — reuse no number from this
   check. If price is back at the 1.5633/1.5548 shelf, the relevant question is whether the **4h ascending low
   sequence (1.4939 → 1.5142 → 1.5306) is still intact**; it is the backbone of the whole long case.
2. **Run the span screen FIRST, before any ratio.** Measure N (largest 5m range of the preceding hour) on the
   candidate contract, multiply by ~2.7, and check whether the structural stop and the nearest structural target
   are that far apart. If not, record `no_trade` and stop computing. This is the cheapest thing this experiment
   has learned.
3. **Do not let the target float.** The nearest structural level is the target. If the ratio only passes at a
   level beyond an intervening high or low that has already rejected, the trade fails — regardless of what L-002
   says about the stop. Three contracts passed that way this check.
4. **Funding:** the 00:00Z settlement falls **after** the 02:00 check (08:00 MYT), so 02:00 still reads
   pre-settlement. Whether XRPUSDT's discount survives a **third** settlement is the 09:00 read. The deepening
   from −0.0084% to −0.0166% in one hour is the single most directional thing on the board.
5. **Spread:** XRPUSDT was over the cap at 16:12:58Z. Check the book **before** building anything.
6. **L-001:** BTCUSDT remains excluded at 02:00 (still inside the window). The artifact-free day lands ~04:00 MYT.
   Keep scanning at **both** 1h and 5m — the 1h pass is what caught both corrections above.

**Lessons applied:** **L-002** applied and extended — it disqualified every XRPUSDT construction clearing the
floor on a structural target (0.41×/0.64×/0.95×, tightening to 0.17×/0.40×/0.71× at the requote), and the entry
sweep turned it into a geometric screen. **L-003** applied and **material** for the second consecutive check — the
140-second requote more than doubled the long's ratio on drift alone and changed how `market_context` reads.
**L-001** applied — BTCUSDT excluded for a ninth check, scan run at both resolutions, which is what surfaced the
two corrections. No lesson was loosened, reinterpreted or overridden. Nothing under `reviews/` was read for
modification or modified; the 22:00 review task owns that folder. Live trading remains disabled.
