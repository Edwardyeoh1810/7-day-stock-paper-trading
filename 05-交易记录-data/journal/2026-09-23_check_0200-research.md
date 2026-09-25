# Research journal — 2026-09-23_check_0200-research

Companion to the generated journal entry for `2026-09-23_check_0200_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-22T18:11Z (02:11 Asia/Kuala_Lumpur, 2026-09-23), slot
  `2026-09-23_check_0200`.
- **What was done:** Read `AGENTS.md`, `02-项目文档-docs/TRADING-STRATEGY.md`,
  `03-定时任务-routines/AUTOMATION-PROMPT.md`, `03-定时任务-routines/CONTINUITY.md`,
  `04-运行状态-state/readiness.json`, `05-交易记录-data/current-state.json`, the **00:00 slot's research note**
  and `reviews/LESSONS.md`. Ran the read-only observation at 18:03:59Z, then pulled 1d, 4h, 1h and 5m bars, the
  book, the 24h ticker, funding (live and settled history), mark/index and open interest for all five watchlist
  contracts from the demo host's public endpoints; ran the artifact scan at both 5m and 1h; ran the **span screen
  before any ratio**, as the 00:00 note instructed; took a confirming requote 186 seconds later as **L-003**
  requires; ran one web search for scheduled news. Submitted a `no_trade` decision through `paper_engine.py` at
  18:10:24Z.
- **Why it was done:** The 02:00 slot was due (`due_slot: 2026-09-23_check_0200`, 240 planned slots) and no
  position was open, so an entry was permitted if and only if every entry condition and every lesson was satisfied.
- **Timing:** Observation 18:03:59Z, research sweep 18:05:08Z, requote 18:08:14Z, decision written 18:09Z, engine
  submitted 18:10:24Z (02:10 MYT) — **ten minutes after the slot. ON TIME**, fourth consecutive on-time check
  since the 09:00 stall on 2026-09-22.
- **Order proposed:** No.
- **Order placed:** No. The engine returned `status: no_trade`, `live_order_sent: false`.
- **Order filled:** No.
- **Exchange stop/target reconciliation:** None to reconcile. Flat before and after; no exit order has ever been
  placed in this experiment.
- **Current holdings:** None. Flat.
- **Current cash:** 5000 USDT. Demo wallet balance 5000.04174826 USDT.
- **Current risk:** 0 USDT open risk; 0 USDT realized today. Trading day index 2.
- **Evidence captured:** `05-交易记录-data/evidence/2026-09-23_check_0200.json` (read-only run),
  `05-交易记录-data/evidence/2026-09-23_check_0200_paper.json` (engine), and this note.

## The 00:00 assignment: three tasks, all answered, and the lead signal died

### (1) The 4h ascending-low sequence is intact — and has extended

The 00:00 note called this "the backbone of the whole long case" and asked for it to be re-read from scratch
after the 1.5633 break. **It survived.**

| 4h bar | Low |
|---|---|
| 09-22 04:00Z | 1.4939 |
| 09-22 08:00Z | 1.5142 |
| 09-22 12:00Z | 1.5306 |
| **09-22 16:00Z** | **1.5475** |

Four ascending 4h lows, and the 16:00Z bar closed at 1.5704 in the upper half of its range. `trend` is a clean
supporting category for the long.

### (2) The derivatives leg is gone — the most important finding of this check

The 00:00 note named XRPUSDT's deepening funding discount (−0.008393% → −0.016553% in an hour) **"the single most
directional thing on the board"** and left the third settlement as the 09:00 read. **It did not survive to 09:00.**

| Time | XRPUSDT predicted funding |
|---|---|
| 00:00 check (16:0xZ) | **−0.016553%** |
| 18:05:08Z | −0.000601% |
| 18:08:14Z | **−0.000078%** |

A **99.5% decay in roughly two hours.** It is still nominally the only negative rate in the complex (ETH
+0.010000%, SOL +0.010000%, BTC +0.003891%, BNB +0.001656%), but −0.0001% is not a squeeze signal and I decline
to claim it as one.

**The settled history also corrects the 00:00 note's framing.** The last four settlements are +0.010000%
(09-21 16:00Z), −0.006889% (09-22 00:00Z), +0.010000% (08:00Z), −0.017407% (16:00Z) — **the sign alternated
twice.** That is not a discount "persisting through breakout, failure and reclaim"; it is an oscillation, and the
00:00 note over-read a two-point trend. **XRPUSDT long therefore carries two supporting categories, not three.**

### (3) The span screen, run first — and it fails on every contract

N (largest 5m range of the preceding hour) = **0.506%** on the 17:00–18:00Z clock hour, 0.447% on the last twelve
closed bars. I used the conservative 0.506%. Required clean structural span = 2.5N + ~0.14% drag ≈ **1.41%**.

From 1.5704 the *entire* structural span available to a long is 1.5617 (17:00Z 1h low) → 1.5876 (24h high) =
**1.659%**; the noise-safe version 1.5475 → 1.5876 = 2.592%. Now run it with the **nearest** structural target,
as the 00:00 note demanded, instead of letting the target float:

| Stop | Target | Risk | Net RR |
|---|---|---|---|
| 1.5617 | 1.5731 | 0.554% | **0.058** |
| 1.5617 | 1.5762 | 0.554% | **0.413** |
| 1.5475 | 1.5762 | 1.459% | **0.157** |
| 1.5475 | 1.5876 | 1.459% | **0.655** |

**Every nearest-target construction fails, most by an order of magnitude.**

## The one construction that passes is the target-stretched one

**Stop 1.5617 (0.554% risk, 1.09× N — L-002 does *not* reject it) with target 1.5876 pays net 1.724.**

It passes **only** because 1.5876 sits beyond **four** intervening 1h highs that have each already rejected within
the last five hours: 1.5827 (15:00Z), 1.5762 (16:00Z), 1.5746 (17:00Z), 1.5731 (18:00Z).

The 00:00 note identified target-stretching **retrospectively**, on four constructions, and sent it to the review.
**This is the first time the screen has been applied prospectively to disqualify the check's own best candidate**
— and it is the only thing standing between this experiment and a 1.724 entry that L-002 would have waved through.

## L-002 and L-003 fired in sequence on that construction inside 186 seconds

Same stop 1.5617, same target 1.5876:

| Quote | Ask | Risk | vs N | Net RR |
|---|---|---|---|---|
| 18:05:08Z | 1.5704 | 0.554% | **1.09×** | **1.724** |
| 18:08:14Z | 1.5680 | 0.402% | **0.79×** | **2.761** |

The ratio rose **60%** purely because price fell 0.153% **onto** its fixed stop — L-003 verbatim, **fourth
reproduction, second consecutive check on the long side.** And the same drift carried the stop from *marginally
noise-safe* to *sub-noise*, **so L-002 now rejects outright what it permitted 186 seconds earlier.** L-003 caught
the drift; the drift then handed the rejection to L-002. This is the cleanest joint demonstration of the two
lessons so far.

**The premise broke in the same 186 seconds.** The requote at 1.5678/1.5680 — and the engine's own quote at
18:10:24Z, also 1.5678/1.5680 — puts price **back below the 1.5701 pivot for the third time** (lost 16:12:58Z,
reclaimed, lost again now). The long's `price_action` is not merely ambiguous; it is negative.

## What was examined and explicitly not claimed

- **`price_action` — compression, claimed for neither side.** Five consecutive lower 1h highs (1.5876 → 1.5827 →
  1.5762 → 1.5746 → 1.5731) against rising lows since 16:00Z (1.5475 → 1.5617 → 1.5677): a coil tightening onto
  the pivot, directionally mute.
- **`volume` — fourth consecutive check, not claimed.** The 1h series is a flat band again (13:00Z 6,066.6M,
  14:00Z 5,707.5M, 15:00Z 5,538.9M, 16:00Z 5,739.9M, 17:00Z 6,009.2M) and the 5m recovery off 1.5617 averaged
  ~500M against a 350.6M selloff bar. No expansion, no drying up. **This finding is firm; stop re-deriving it.**
- **`news` — not claimed.** One web search placed XRP at about **1.51–1.56 USD** against the demo's 1.5704, so
  **XRPUSDT itself is not contaminated**, and reported no chaotic or contradictory news and no scheduled event
  requiring a stop. Spot XRP fund inflows and a ~27% monthly outperformance of BTC and ETH are consistent with the
  `market_context` read but are **not** a separate category, which requires a verifiable dated scheduled event.

## The other contracts

- **XRPUSDT short** is the mirror and fails the evidence bar: **one** category (`price_action`, the five lower
  highs), with `trend` against it, `market_context` against it, and funding now marginally against it too, since a
  short pays a negative rate. One is not two.
- **BNBUSDT short** was the only other two-category candidate — `trend` (4h lower highs 807.74 → 800.90 → 790.66 →
  789.77 → 792.26 → 791.56) and `market_context` (−1.046% over 24h, the **only** negative of the five). N =
  0.263%, required span ~0.80%. Noise-safe stop above the 792.26 4h swing high = 0.512% risk = 1.95× N; nearest
  target 787.23 pays **negative**, 785.73 pays **0.348**, and only the 782.33 24h low pays **1.191** — still short
  of 1.5, and already beyond two intervening lows. Tightening the stop to 790.45 (1.07× N) makes 782.33 pay 2.171:
  **target-stretching on a barely-noise-safe stop, the same failure as XRPUSDT, on a second contract, in the same
  check.**
- **ETHUSDT and SOLUSDT longs** declined on evidence: both pay the maximum **+0.010000%** funding (crowded long, a
  long pays at 00:00Z), ETHUSDT's 4h highs descend from 2850 and its low sequence broke at 2716, SOLUSDT's broke
  at 115.55, and neither has `market_context`. Zero to one category each.
- **SOLUSDT data-quality flag:** 24h quote volume **452.5M** against 104,697M–137,784M for the other four — a
  factor of about **250** — with six consecutive 5m bars printing an identical 118.11 high (17:30Z–17:55Z) and a
  spread that moved 0.85 → 8.48 bps on the requote.

## New finding for the review: the demo book is unstable in *quantity*, across the whole watchlist

L-001 records BTCUSDT requoting from 32.59 bps to 1.06 bps in three minutes. The same instability appears in
**top-of-book size on every contract** over 186 seconds:

| Contract | 18:05:08Z | 18:08:14Z |
|---|---|---|
| **BNBUSDT** | bid **0.16** / ask **0.01** units, spread 0.38 bps | bid 1107.52 / ask 9203.63, spread 5.45 bps |
| BTCUSDT | bid 69.3685 / ask 186.7960 | bid 2.8759 / ask **0.0208** |
| ETHUSDT | bid 2004.945 / ask 2432.587 | bid 451.097 / ask 2710.768 |
| XRPUSDT | bid 3,465,619.9 / ask 19,366,259.0 | bid 12,989,181.4 / ask **30,580.0** |

BNBUSDT's swing is roughly **7000×**. **A quoted spread of 0.38 bps on an 0.01-unit touch — about 7.88 USDT,
against a 2500 USDT maximum notional — is not a measurement of anything, and the 25 bps spread cap cannot see
this.** Recorded for the review task; I have changed no rule and no limit.

## Artifact scan — both resolutions, one correction to the 00:00 note

**No new artifact on any contract at either resolution. Sixth consecutive clean 5m scan.**

- **Correction:** the 00:00 note listed **five** contaminated BTCUSDT 1h bars and **omitted the 09-21 15:00Z print
  of 86999.00**, which LESSONS L-001 records and which shows a **1.301% upper wick on a 0.131% body — a 9.9×
  ratio**. The 00:00 count should have been **six**.
- At 02:00 the count is **five** again, because 87888.00 (09-21 12:00Z) has now aged out of the 30-bar 1h window:
  86769.40 (13:00Z), 95804.10 (14:00Z), **86999.00 (15:00Z)**, 91000.00 (19:00Z), 90389.80 (20:00Z).
- ETHUSDT's 09-21 15:00Z 2795.00 print still flags on **range** (2.381% vs 0.647% median) and has not aged out —
  confirms the 00:00 note's correction 2.
- BTCUSDT's 24h high field still reads **91000.00** against a real session top of 86534.
- **BTCUSDT excluded for a tenth consecutive check.** Its spread was 1.60 and 0.47 bps, so the exclusion rests on
  artifacts alone.
- **L-001 re-test clock:** last artifact print 09-21 20:00Z, **22h05m** before this decision, so the artifact-free
  day lands near **20:00Z / 04:00 MYT — between this check and 09:00.** The exclusion stands in full; **only the
  daily review may retire a lesson.**
- **Spreads all inside the 25 bps cap at both sweeps** (BTC 1.60/0.47, ETH 0.44/1.75, BNB 0.38/5.45, SOL
  0.85/8.48, XRP 0.64/1.28). XRPUSDT's 38.9 bps blowout at 16:12:58Z has fully repaired — item (5) of the 00:00
  assignment is answered: **the book was not the binding constraint this time.**

## For the 09:00 check

1. **The funding question is now closed, not open.** The 00:00 note left "does XRPUSDT's discount survive a third
   settlement?" as the 09:00 read. It decayed to −0.000078% *before* the settlement, so the 00:00Z settled print
   is now a formality. **Do not rebuild a long on a funding leg.** Read the 00:00Z and 08:00Z settled rates, and
   if they alternate again, that fifth and sixth data point should retire "XRP funding is a squeeze signal" for
   good.
2. **Run the span screen first, again.** It has now disqualified the best candidate on two contracts in one check.
   Measure N, multiply by ~2.7, and check the structural stop against the **nearest** structural target before any
   ratio is computed.
3. **The target-stretching screen is the binding constraint of this experiment, not L-002.** Two of the last two
   checks produced constructions that L-002 passed and target-stretching killed (1.724 on XRPUSDT, 2.171 on
   BNBUSDT here; four constructions at 00:00). This is the strongest candidate for a new lesson; it belongs to the
   review task, not to a check.
4. **XRPUSDT structure at 09:00:** the pivot is 1.5701, lost three times now. The 4h ascending-low sequence
   (1.4939 → 1.5142 → 1.5306 → 1.5475) is the surviving long premise — **the 09:00 question is whether the 20:00Z
   4h bar makes a fifth ascending low above 1.5475, or breaks it.** A break ends the long case entirely and would
   give the short a second category.
5. **Check the book *size*, not just the spread,** before building anything. BNBUSDT quoted 0.38 bps on an
   0.01-unit ask. The spread cap is blind to this.
6. **L-001:** the artifact-free day is reached at ~04:00 MYT, *before* the 09:00 check. **BTCUSDT nevertheless
   stays excluded at 09:00** — a check may not retire a lesson, only the daily review may. Keep scanning at both
   1h and 5m and hand the review a clean count.

**Lessons applied:** **L-001** applied — BTCUSDT excluded for a tenth check, scan run at **both** 1h and 5m, which
is what caught the 86999.00 omission. **L-002** applied and **decisive** — it moved from permitting the 1.724
construction at 1.09× N to rejecting it at 0.79× N inside 186 seconds. **L-003** applied and **material for a
third consecutive check** — the requote raised the ratio 60% on drift alone, collapsed the funding leg by a
further 87%, and broke the pivot premise. No lesson was loosened, reinterpreted or overridden, and no lesson was
used to justify an action that a rule forbids. Nothing under `reviews/` was read for modification or modified; the
22:00 review task owns that folder. Live trading remains disabled.
