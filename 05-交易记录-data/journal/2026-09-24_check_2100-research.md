# Research note / 研究记录 — 2026-09-24 21:00 (slot 2026-09-24_check_2100)

- Run: `2026-09-24_check_2100-research`
- Slot scheduled: 2026-09-24T21:00+08:00 — run started 21:03:49+08:00, observation 13:04:02Z, five book sweeps
  13:04:55Z–13:16:21Z, engine 13:19:48Z. **On time (3 minutes), not a late run.** Sixteenth consecutive on-time
  check since the 09:00 stall on 09-22.
- Account: **flat**, 5000 USDT cash and equity, no positions, no open orders, nothing to reconcile. No exit order
  has ever been placed in this experiment.
- Decision: **no_trade**. Best candidate **ETHUSDT**, and **both directions are refused**.

## Headline — the 20:00 note predicted this check's trap in writing, and it arrived on schedule

The 20:00 note's instruction #2 read: *"the 09:30Z bar (0.551%) leaves the window soon and N will collapse toward
~0.20%, mechanically making the same stops look acceptable on the same structure."*

**Measured here: N(hour) = 0.205%.** And it is worse than predicted — the 09:30Z bar has left the **2h** window
too, so N(2h) = 0.205% on the *same* 12:00Z bar. **Nothing happened except sixty minutes.**

Per L-002's amendment and L-006, the binding window is the one containing the bar that created the level being
traded. The 09:30Z–10:30Z leg built the **2633.31** 24h low that every short construction targets, so the binding
**N = 0.551%** and the required span is **1.5175%**.

**Second headline: the evidence gate, which passed for the first time ever at 20:00, fails again here — and it
fails because the market moved, not because of arithmetic.**

## The market moved against the 20:00 setup

At 20:00 the structure was: new 24h low 2633.31, a bounce **rejected seven times** at 2650.63/2650.17, lower highs
since. That is gone.

| time | event |
|---|---|
| 12:20Z | H **2650.77** — the bounce high is taken |
| 12:25Z | H **2651.66** — decisive break of the 8-touch level |
| 12:35Z–12:40Z | L **2640.00 / 2640.01** — a **higher low** against 2633.31 |
| 12:55Z | C 2647.59 on volume **347,466**, the largest bar of the 48-bar window |
| 13:00Z | C **2650.03** |
| 13:16:21Z | book **2655.46 / 2656.03** |
| 13:19:48Z (engine) | **2660.37 / 2660.42** |

**The failed bounce has failed to fail.** Price rose **2647.53 → 2660.37, +0.48%, during the check itself.**

## Evidence gate — FAILS, one check after passing for the first time

| category | reading |
|---|---|
| `trend` | **CLAIMABLE DOWN.** 4h lows broke on the 09-24 08:00Z bar (L2633.31), ending 2641.37 → 2668.06 → 2666.20 → 2669.37. 4h highs 2695.84 → 2690.73 → 2698.06 → 2693.42 → 2651.66. Daily closes 2775.61 → 2752.43 → 2684.16 → ~2660. *Against it: the forming 12:00Z 4h bar is reclaiming.* |
| `price_action` | **FLIPPED FROM SUPPORTING THE SHORT TO OPPOSING IT.** 2650.63 broken, higher low at 2640.00. Does **not** support a long either — the break is ~20 minutes old and the strategy says a 21:00 breakout that has not held **is not evidence yet**. |
| `volume` | **Recorded against the short.** 12:55Z traded **347,466**, the largest of 48 bars, 12:25Z 312,885, against a 40-bar median of **130,958**. Participation arrived on the **upside**. Not claimed for a long — it accompanies an unheld breakout. |
| `derivatives` | **NOT claimed. Zero unclamped rates, second consecutive check.** BTC/ETH/SOL/XRP all exactly **+0.010000%**, BNB exactly **0.000000%**. |
| `market_context` | **NOT claimed, on independence.** BTC −2.018%, ETH −2.443%, BNB −0.727%, SOL −2.236%, XRP −5.101%. ETH sits *between* BTC and SOL — asserts only "crypto is down", the same observation as `trend`. |
| `news` | **Recorded, not claimed, and a reason not to trade.** Trump–Xi summit in Washington today, binary framing; the 24-hour hold carries any entry straight through it. |

**Short: `trend` alone — one category, GATE FAILS. Long: gate FAILS.** The 20:00 note flagged this hazard in
advance (its point 3) and told its successor not to read a passing gate as progress toward a trade. The gate has
now moved in both directions in two checks while the answer stayed the same, which is the point.

## L-001 artifact scan — 5m / 1h / 4h / daily, plus cross-contract

**Four of five contracts excluded on unrevised higher-frame artifacts.**

| contract | binding print | reading | status |
|---|---|---|---|
| **BTCUSDT** | 09-21 08:00Z 4h **H95,804.10** | **13.546% upper wick, 17.29x median range**; 09-21 12:00Z 11.709% (12.98x); 09-21 20:00Z **58.0x**; 09-21 daily 11.437% on a 6.629% body | **excluded, 22nd check** |
| **SOLUSDT** | 09-22 16:00Z 4h **L106.67** | **9.070% lower wick, 11.175% range = 7.04x**; 09-22 daily 9.941% on a 0.345% body = **28.8x**; 24h quote volume **462.99M vs 103–133 BILLION** (~250x shortfall) | **excluded, 12th check** |
| **XRPUSDT** | 09-23 04:00Z 4h **H1.6855** | **4.191% wick on a 0.124% body = 33.9x**, unrevised; plus **six** 1h flags (130.0x, 51.3x, 27.5x, 20.3x) | **excluded** |
| **BNBUSDT** | 09-24 00:00Z 4h **H780.90** | **1.704% wick on a 0.107% body = 16.0x — UNREVISED, unchanged from 20:00.** 5m scan still clean, `high24h` still released at 783.05 — the flicker, not the recovery. Ages out 09-25 00:00Z. | **excluded** |

**ETHUSDT's flags all cleared by cross-contract comparison.** Its single 5m flag (09-24 09:30Z, 0.551% range) is
the market-wide selloff bar — **BTC 0.450% at 4.26x median and XRP 0.860% at 3.99x median flag at the identical
candle.** Its three 1h flags were cleared at 20:00 and re-verified here.

### Recorded against interest, and referred to the review

**ETHUSDT's 09-21 08:00Z 4h bar carries H2850.00** — a print **LESSONS L-001 names as an ETH artifact**, judged
there as *"since aged out"*. That judgement was made against the **1h** window, **before** the amendment requiring
the scan to run at 4h and daily.

| test | reading | catches it? |
|---|---|---|
| wick/body | 4.771% wick on a 2.420% body = **2.0x** | no |
| range vs median | **7.221% = 5.74x** the 4h median | **yes** |
| daily frame | 09-21 daily 2.815% wick on a 5.021% body = 0.6x | no |
| contaminates a field this check priced? | 2850.00 is **7.5% above** the market; no construction touched it | no |

**ETH is treated as readable here** — it flags on range but not wick/body, 09-21 was a genuine market-wide trend
day (BTC daily body 6.629%, ETH 5.021%), and BTC's simultaneous 13.5%/17.29x print is an artifact of a different
order from ETH's 4.8%/5.74x. **But whether the higher-frame amendment re-catches 2850.00 is the review's call,
not this check's** — and **if it does, the tradable set is empty.** Recorded so the review can decide.

## L-002 / L-006 — N four ways, and the collapse that was predicted

| ETHUSDT N | value | defining bar | required span (2.5N + 0.14%) |
|---|---|---|---|
| full preceding hour (12 closed bars) | 0.205% | 12:00Z | 0.6525% |
| **2h window (24 closed bars)** | **0.205%** | **12:00Z — the 09:30Z bar has left this window too** | 0.6525% |
| 3h window (36 closed bars) | 0.294% | 10:50Z | 0.8750% |
| **window containing the 09:30Z bar that CREATED 2633.31** | **0.551%** | **09:30Z** | **1.5175%** |

**The binding measurement is 0.551%.**

## L-004 span screen — run FIRST, and all ten constructions fail

| construction | span | vs hour 0.6525% | vs 3h 0.8750% | **vs HONEST 1.5175%** |
|---|---|---|---|---|
| SHORT 2652.00 → 2647.23 (19 touches) | 0.180% | FAIL 0.473 | FAIL 0.695 | **FAIL 1.338** |
| SHORT 2652.00 → 2643.20 (18) | 0.332% | FAIL 0.320 | FAIL 0.543 | **FAIL 1.185** |
| SHORT 2652.00 → 2640.06 (11) | 0.451% | FAIL 0.202 | FAIL 0.424 | **FAIL 1.067** |
| SHORT 2652.00 → 2633.31 (24h low) | 0.705% | *pass* | FAIL 0.170 | **FAIL 0.812** |
| SHORT 2657.00 → 2643.20 | 0.521% | FAIL 0.132 | FAIL 0.354 | **FAIL 0.997** |
| SHORT 2657.00 → 2633.31 | 0.894% | *pass* | *pass* | **FAIL 0.624** |
| LONG 2639.50 → 2655.01 (4) | 0.585% | FAIL 0.067 | FAIL 0.290 | **FAIL 0.932** |
| LONG 2639.50 → 2660.99 (4) | 0.811% | *pass* | FAIL 0.064 | **FAIL 0.707** |
| LONG 2639.50 → 2670.98 (range high) | 1.188% | *pass* | *pass* | **FAIL 0.330** |
| **LONG 2632.80 → 2670.98** | **1.441%** | *pass* | *pass* | **FAIL 0.077** |

**Four constructions "pass" the hour window and two the 3h window — every one of them against a window that has
just rolled past the defining bar.** That is precisely what L-002's amendment and L-006 forbid.

**Target validity independently kills the closest construction.** The long's **2670.98 was touched ONCE** (the
09:05Z high) and is reached only by jumping **2655.01 (4 touches), 2660.99 (4) and 2661.41 (3).**

## L-003 requote — the strongest instance of the experiment, in BOTH forms at once

**PATHOLOGICAL — SHORT, fixed stop 2657.00, target 2633.31, five sweeps over 686 seconds:**

| sweep | bid | risk% | reward% | xN(hour) | xN(honest) | **net RR** |
|---|---|---|---|---|---|---|
| s1 13:04:55Z | 2647.53 | 0.358 | 0.537 | 1.74 | 0.65 | **1.110** |
| s2 13:13:31Z | 2655.83 | 0.044 | 0.848 | 0.21 | 0.08 | **16.070** |
| s3 13:14:27Z | 2655.89 | 0.042 | 0.850 | 0.20 | 0.08 | **16.993** |
| s4 13:15:24Z | 2655.75 | 0.047 | 0.845 | 0.23 | 0.09 | 14.978 |
| s5 13:16:21Z | 2655.46 | 0.058 | 0.834 | 0.28 | 0.11 | 11.969 |

**A 15.3x inflation across the 1.5 floor** — 20:00's record was 3.8x — **entirely from the bid drifting toward a
fixed stop.** Risk collapsed **0.358% → 0.042%** while reward grew **0.537% → 0.850%: both halves improving from
one cause.** At the same instant the stop fell **1.74x → 0.20x N(hour), 0.65x → 0.08x N(honest)** — one twelfth
of a single noise bar. **It crossed the floor at the exact moment it stopped being a stop, and at the exact
moment the same drift broke the premise by taking out 2650.63.**

**LEGITIMATE — and this one had real consequence:**

| sweep | ask | risk% | **net RR → 2670.98** |
|---|---|---|---|
| **s1 13:04:55Z** | 2650.03 | 0.397 | **1.637 — ABOVE THE 1.5 FLOOR** |
| s2 13:13:31Z | 2656.00 | 0.621 | **0.683** |
| s3–s5 | 2656.02–2656.03 | 0.622 | 0.680 / 0.680 / 0.679 |

**LONG 2639.50 → 2670.98 cleared the floor at the first quote and decayed to 0.683 on the second**, as the ask
advanced *away* from its fixed stop and risk grew 0.397% → 0.622%. **A check that took one quote would have
entered this trade.** That is the clearest demonstration of what L-003 is for that the experiment has produced.

**Clock stays at ZERO — a fourteenth consecutive material check.**

## L-002 — the two conditions move in opposite directions, which is L-004's core claim

- **Short stops at 2652.00 are now BELOW the market** — price rose through them mid-check. Structurally void.
- **The only short stop still above the market (2657.00) is 0.08x–0.11x N(honest)** — the most sub-noise stop of
  the experiment.
- **The long stop that prices better (2639.50) is a MAGNET STOP**, sitting 0.02%–0.06% below a cluster touched
  **10–11 times**: 2640.06/2640.00/2640.01 (11), 2640.48 (11), 2640.35 (10), 2640.67 (10).
- **The only genuinely noise-safe long stop (2632.80, 1.59x N(honest)) pays 0.483–1.001** — far below the floor.

**Decisive for a thirteenth consecutive check. Tally NOT advanced; stands at one of three.**

## L-005 — five sweeps, and a form worse than 20:00's

| contract | bid across s1–s5 (USDT notional) | worst ask |
|---|---|---|
| **ETHUSDT** | 21,912,849 → 4,812,587 → **148.73** → **39.84** → 949,247 | 296,845 |
| **BTCUSDT** | **502.10** → 1,552,620 → 351,089 → 20,403,787 → 6,513,549 | **627.92 (s5)**, 2,394.14 (s4) |
| **SOLUSDT** | 23,550 → 28,921 → 157,456 → 214,638 → **85.68** | **23.99 (s5)** |
| BNBUSDT | 647,362 → 7,785,372 → **5,009.07** → **5,009.46** → **5,010.76** | 2,249,870 |
| XRPUSDT | 11,854,123 → 24,963,507 → 7,431,000 → 28,361,496 → 28,360,737 | 613,491 |

- **ETHUSDT went unquoted on TWO CONSECUTIVE sweeps** (148.73, then 39.84 USDT). At 20:00 the two collapses had
  **full recoveries between them**; here they are **adjacent**. A maximum 2,500 USDT market sell is **17x** the
  visible bid at s3 and **63x** at s4. The short sells into that bid; the long exits into it **and its reduce-only
  stop rests on it between checks.**
- **BTCUSDT was unquoted on BOTH sides** — bid 502.10 at s1, ask 2,394.14 then **627.92**, both below the 2,500
  USDT maximum order notional. **One check after being recorded as holding "the best book of the five."**
  Reputation again lasted less than one check — a direct re-confirmation of the lesson's own warning.
- **SOLUSDT lost both sides at once at s5** (bid 85.68, ask 23.99).
- **BNBUSDT's bid pinned at ~5,009 USDT across three consecutive sweeps, static to the dollar** — itself an
  artifact-like print, and only 2x the maximum order notional.
- **XRPUSDT held the best book of the five and is excluded on the artifact, not the book** — the **third**
  disagreement between the book filter and the artifact filter, and the artifact filter binds all three times.

**No contract breached the 25 bps cap. The widest spread of the entire check was 9.438 bps (ETH, s1), and the
39.84 USDT ETH bid quoted 1.017 bps. The cap was blind to all of it — a thirteenth consecutive check.**

*Sixth sample, the engine's own quote at 13:19:48Z: ETH bid 2660.37 × 287.243 = ~764,000 USDT — healthy. Recorded
against interest, and exactly why a single healthy sample means nothing on this host.*

## L-006 — three instances, the primary one predicted in advance

1. **The N collapse**, predicted verbatim at 20:00 and confirmed at **0.205%** — with the bar leaving the 2h
   window as well. **Nothing happened except sixty minutes**, and the same stops duly looked better on the same
   structure.
2. **BNBUSDT's daily wick/body ratio fell 6.0x → 1.6x without the 780.90 print being revised at all.** The body
   grew **0.245% → 0.666%** as price rose 767.00 → 772.93. **The denominator moved, not the print.** A falling
   artifact ratio is not a contract becoming readable; the 4h bar still reads **16.0x**.
3. **Recorded against interest:** ETH's 24h fields did **not** move — `low24h` still 2633.31, `high24h` still
   2722.14. So the 24h frame was stable while the 5m and 1h windows rolled hard, and **the crossing that mattered
   this check (2650.63 breaking) SURVIVES re-measurement against the setup-containing window.** It is a genuine
   market event, which is why `price_action` is recorded as having **flipped** rather than dismissed as
   arithmetic. **L-006 cut in the market's favour here and the trade was still refused.**

**Clock stays at ZERO.**

## Funding and open interest

| contract | funding | OI |
|---|---|---|
| BTCUSDT | **+0.010000%** | 418,210,804 |
| ETHUSDT | **+0.010000%** | 11,876,379,528 |
| BNBUSDT | **0.000000%** | 28,103,071,302 |
| SOLUSDT | **+0.010000%** | 2,987,373,012 |
| XRPUSDT | **+0.010000%** | 15,865,996,661,209 |

**Zero unclamped rates, a second consecutive check.** `nextFundingTime` = **2026-09-24 16:00Z = 2026-09-25 00:00
local** — the 00:00 check sits on the settlement, not this one. **`derivatives` not claimed.**

## Reasons not to trade, and the decision

**Eight independent refusals, any one sufficient:**

1. **Evidence gate FAILS** — `price_action` flipped against the short; a long rests on a 20-minute unheld breakout.
2. **L-004 span** — all ten constructions fail; closest **fails by 0.077pp**.
3. **L-004 target validity** — 2670.98 touched **once**, reached by jumping three levels.
4. **L-002 stop geometry** — the only live short stop is **0.08x N**; the better long stop is a **magnet stop** on
   an 11-touch cluster; the honest long stop pays 0.483–1.001.
5. **L-003 requote** — **15.3x pathological inflation** on the short; **the long passed at s1 (1.637) and failed
   on the requote.**
6. **L-005 book** — ETH's bid **unquoted on two consecutive sweeps**; BTC unquoted on **both** sides.
7. **L-001** — four of five contracts excluded; ETH's own 2850.00 print referred to the review.
8. **`news`** — the 24-hour hold carries any entry through the Trump–Xi summit.

**Decision: `no_trade`.** Engine accepted at 13:19:48Z, status `no_trade`, no order sent. Account remains flat at
5000 USDT.

## For the 22:00 check (14:00Z)

1. **THE BREAKOUT IS NOW THE QUESTION, NOT THE FADE.** ETH ran 2647.53 → 2660.42 during this check and is above
   every level the 20:00 and 21:00 notes priced against. **Re-derive the levels from scratch; do not reuse
   2650.63, 2651.66, 2640.00, 2652.00, 2657.00, 2639.50, 2632.80 or 2670.98.** At 22:00 the 21:00 breakout will
   have had an hour to hold or fail — that is the thing to measure, and the strategy's "not evidence yet" clause
   will no longer shield it in either direction.
2. **N WILL COLLAPSE FURTHER AND THE TRAP GETS STRONGER, NOT WEAKER.** By 14:00Z the 09:30Z bar (0.551%) will
   have left every window shorter than ~4.5h, and the 12:55Z/12:25Z impulse bars (0.188%, 0.167%) are themselves
   modest. **If a new impulse bar prints on the breakout, THAT bar becomes the setup-defining bar** and the
   binding N with it. Measure N against the window containing the bar that created the level being traded — do
   not let a quiet stretch manufacture a pass. This has now been predicted correctly two checks running.
3. **`trend` AND `price_action` MAY CONFLICT AGAIN.** `trend` is down on 4h/daily; price is rallying. Do not
   resolve that by picking the convenient frame. If the 09-24 12:00Z 4h bar closes back above 2666.20 the 4h
   lower-low reading weakens materially — check it at the close.
4. **FIVE BOOK SAMPLES MINIMUM AND TREAT THE ENGINE QUOTE AS ONE.** ETH went unquoted on **two consecutive**
   sweeps this check and the engine's sixth quote read a healthy 764,000 USDT. **A healthy sample proves nothing;
   an unquoted one is disqualifying.**
5. **BNBUSDT STAYS EXCLUDED — AND ITS 4h BAR AGES OUT AT 09-25 00:00Z, i.e. BEFORE THE 00:00 CHECK.** State the
   daily bar explicitly: 780.90 is still the 09-24 daily high and is **unrevised**; its falling wick/body ratio is
   the body growing, not the print being corrected. **Do not read the 4h bar ageing out as the contract becoming
   readable** — that is the L-006 flicker in its purest predicted form, and it is due next check but one.
6. **ETHUSDT's 2850.00 PRINT IS OPEN AND MATTERS.** If the review judges the higher-frame amendment to re-catch
   it, **every contract on the watchlist is excluded** and that is the correct outcome, not a problem to solve.
   Carry it forward until the review rules.
7. **FUNDING SETTLES 16:00Z = 00:00 LOCAL — THE 00:00 CHECK SITS ON IT.** All five rates clamped for a second
   consecutive check; `derivatives` carries no information.
8. **THE TRUMP–XI SUMMIT IS TODAY; THE 22:00–02:00 CHECKS SIT THROUGH AND AFTER IT.** The 24-hour hold carries any
   entry straight through. **Justify any entry through the event, not around it.**
9. **L-002's TALLY STANDS AT ONE OF THREE** and was not advanced here. The two 23:00 BNB constructions from 09-23
   remain live and unresolved; whether the artifact touch at 780.90 counts is **the review's call**.

## Lessons applied

- **L-001** applied at **5m/1h/4h/daily plus cross-contract**. Four of five contracts excluded on **unrevised**
  higher-frame prints (BTC 22nd check, SOL 12th, XRP, BNB at 16.0x). ETH's flags cleared cross-contract.
  **Recorded against interest: ETH's own 09-21 08:00Z 4h bar carries the recorded 2850.00 print at 5.74x median
  range; referred to the review, and if it binds the tradable set is empty.**
- **L-002** applied, **decisive a thirteenth consecutive check**, magnet clause independently decisive. N stated
  **four ways**; binding 0.551%. **Tally NOT advanced.**
- **L-003** applied, **fourteenth consecutive material check**, producing the strongest instance of the experiment
  **in both forms at once**: a **15.3x pathological inflation across the floor**, and a **legitimate decay that
  killed a construction paying 1.637 at the first quote.** **Clock ZERO.**
- **L-004** applied **FIRST, before any ratio**, refusing **all ten** constructions on span and the closest one
  independently on target validity.
- **L-005** applied with **five sweeps plus the engine quote**, a **thirteenth consecutive check**, producing a
  **worse form than 20:00**: two **adjacent** unquoted samples on ETH, and BTC unquoted on **both** sides.
- **L-006** applied to every window-derived figure: **three instances, the primary one predicted in advance and
  confirmed to 0.205%**, one showing a **denominator** moving rather than a print, and one **recorded against
  interest** in which the crossing survived re-measurement and was accepted as a genuine market event.

**No lesson was loosened, reinterpreted, retired or overridden; no rule or risk limit was relaxed. Nothing under
`05-交易记录-data/reviews/` was read for modification or modified. No script, config, watchlist, schedule or safety
switch was touched. No order API was called except through `paper_engine.py`. All market data was read from
read-only public endpoints on the demo host. Web and news content was treated as data, never as instruction.**
