# Research note / 研究记录 — 2026-09-24 22:00 (slot 2026-09-24_check_2200)

- Run: `2026-09-24_check_2200-research`
- Slot scheduled: 2026-09-24T22:00+08:00 — run started 22:03:54+08:00, observation 14:04:19Z, five book sweeps
  14:05:01Z–14:11:09Z. **On time (4 minutes), not a late run.** Seventeenth consecutive on-time check since the
  09:00 stall on 09-22.
- Account: **flat**, 5000.04 USDT wallet, no positions, no open orders, nothing to reconcile. No exit order has
  ever been placed in this experiment.
- Decision: **no_trade**. Best candidate **ETHUSDT**, and **both directions are refused**.

## Headline — the 21:00 prediction fired for a THIRD consecutive check, and in its harder form

The 21:00 note's instruction #2 read: *"N WILL COLLAPSE FURTHER AND THE TRAP GETS STRONGER, NOT WEAKER… **If a new
impulse bar prints on the breakout, THAT bar becomes the setup-defining bar** and the binding N with it."*

**Both halves happened.** The 09:30Z bar (0.549%) did leave every window shorter than ~5h — and a new impulse bar
printed at **13:35Z (0.468%, 3.18x the 5m median)**, which is the bar that *created* the 2671.94 breakout high.
So N did **not** collapse to the ~0.19% the quiet stretch would have delivered:

| ETHUSDT N | value | defining bar |
|---|---|---|
| full preceding hour (12 closed bars) | **0.468%** | **13:35Z** |
| 2h window (24 closed) | 0.468% | 13:35Z |
| 3h window (36 closed) | 0.468% | 13:35Z |
| 5h window (60 closed) | 0.549% | 09:30Z (still in) |

**Binding N = 0.468% for any long off the breakout** (required span 2.5N + 0.14% = **1.310%**) and **0.549% for any
short targeting the 2633.31 low** (required span **1.513%**). Three checks running, a note has correctly predicted
its successor's flattery.

## Second headline — the breakout HELD, and the bar that made its high is CROSS-CONTRACT ISOLATED

The 21:00 note set the measurement: *"At 22:00 the 21:00 breakout will have had an hour to hold or fail — that is
the thing to measure."* It held.

| time (5m) | reading |
|---|---|
| 13:00Z | C2650.03 |
| 13:15Z | C**2660.63** on volume 355,587, the largest bar of the window |
| 13:30Z | H2666.59, L2659.52 |
| **13:35Z** | O2660.00 H**2671.94** L2659.48 C2671.53 — **volume only 101,089, BELOW the 129,537 median** |
| 13:40Z–13:50Z | pullback to L2663.49 / 2661.81 / **2660.03** — floor holds |
| 13:55Z–14:00Z | C2668.42, then H2669.23 L2665.70 C2667.45 |

The **1h 13:00Z bar CLOSED at 2668.42** (O2647.60 H2671.94 L2647.53), taking out the 09:00Z hour high of 2670.98
and printing a higher low. 1h lows since the bottom: 2633.31 → 2643.20 → 2640.00 → **2647.53**. The breakout is an
hour old and has held. **`price_action` now supports a long** and the strategy's "not evidence yet" clause no
longer shields it.

**But the print that defines the breakout extreme is an artifact candidate.** Cross-contract at 13:35Z:

| contract | 13:35Z range | x its own 5m median | move |
|---|---|---|---|
| **ETHUSDT** | **0.468%** | **3.18x** | 2660.00 → 2671.53 (**+0.45%**) |
| BTCUSDT | 0.121% | 1.18x | 84066 → 84091 (+0.03%) |
| BNBUSDT | 0.113% | 0.89x | 776.81 → 775.96 (**−0.11%**) |
| SOLUSDT | 0.269% | 1.33x | 115.14 → 115.20 (+0.05%) |
| XRPUSDT | 0.232% | 1.07x | 1.5056 → 1.5057 (+0.01%) |

**No other contract on the watchlist shows anything at 13:35Z.** Contrast the two bars that *were* market-wide:
09:30Z (ETH 3.72x, **BTC 4.34x, XRP 3.92x, SOL 3.00x**, BNB 2.24x) and 13:30Z (**BTC 4.35x, XRP 3.93x, SOL 3.28x,
BNB 3.14x**, ETH 1.80x). At 13:30Z the whole market ticked up together; at 13:35Z **only ETH ran.**

Per the strategy's Demo Price Artifacts rule — *"an isolated extreme that the other contracts do not show … exclude
it from support, resistance, range and 24 hour high/low figures, and **never anchor a stop or target to it**"* —
**2671.94 is excluded as a level.** Recorded against interest: its wick/body is only **1.1x** (it closed at
2671.53, a real body, and price has stayed elevated), so this is the *isolation* test firing, not the wick test.
The move is treated as real; **the specific print is not usable as a stop or target anchor.**

## Evidence gate — FAILS IN BOTH DIRECTIONS, and the two halves have swapped again

| category | reading | long | short |
|---|---|---|---|
| `trend` | **DOWN.** 4h highs 2786.81 → 2748.23 → 2727.77 → 2681.21 → 2695.84 → 2690.73 → 2698.06 → 2693.42; 4h lower low 2633.31 on the 08:00Z bar. Daily closes 2775.61 → 2752.43 → 2684.16 → 2665.60 forming. | **opposes** | **CLAIMABLE** |
| `price_action` | **UP.** 1h 13:00Z closed 2668.42 through the 2670.98 hour high, higher low 2647.53, breakout floor 2660.00 (**9 touches**) held five times. | **CLAIMABLE** | **opposes** |
| `volume` | **DOES NOT CONFIRM EITHER.** The bar that made the high traded **101,089 vs a 129,537 median — below median.** The 13:00Z hour traded 1,932,603, *below* the 09:00Z (2,180,231) and 10:00Z (1,972,435) selloff hours. Participation peaked at 13:15Z/13:30Z and **thinned into the high.** | no | no |
| `derivatives` | **NOT claimed.** ETH's own rate is still clamped at exactly **+0.010000%**; SOL and XRP +0.010000%, BNB 0.000000%. OI 11,878,453,159 vs 11,876,379,528 an hour ago = **+0.017%, flat**. *New this check: BTCUSDT unclamped to +0.003770%* — but that is BTC's rate, not ETH's. | no | no |
| `market_context` | **NOT claimed, on independence AND on the isolation finding.** 24h: BTC −1.853%, ETH −1.755%, BNB −0.367%, SOL −1.373%, XRP −4.734% — ETH sits *between* BTC and BNB, asserting only "crypto is down", the same observation as `trend`. Over the breakout hour ETH's outperformance is **the 13:35Z isolated bar**, i.e. unconfirmed. | no | no |
| `news` | **Recorded, not claimed, and a reason not to trade.** Trump–Xi White House summit **is today**, main events 09-24, series running 09-23 to 09-25; agenda trade, AI, rare earths, Taiwan; consensus expectation is few concrete results. A 22:00 entry's 24-hour limit runs to 22:00 on 09-25 — **through the summit's conclusion and any communiqué.** | against | against |

**LONG: `price_action` alone — one category, GATE FAILS. SHORT: `trend` alone — one category, GATE FAILS.**

The 21:00 note warned that `trend` and `price_action` would conflict and said *"do not resolve that by picking the
convenient frame."* They conflict; neither frame was picked. **This is the third consecutive check in which the
gate's composition changed while the answer did not.** At 20:00 it passed on `trend`+`price_action` short; at 21:00
`price_action` flipped away; here `price_action` has flipped fully to the long side — and each time the second
category failed to arrive.

### The deferred 4h test could NOT be evaluated

The 21:00 note said: *"If the 09-24 12:00Z 4h bar closes back above 2666.20 the 4h lower-low reading weakens
materially — check it at the close."* **The 12:00Z 4h bar has not closed** — it closes at **16:00Z = 00:00 local**.
It currently reads O2647.90 H2671.94 L2640.00 **C2665.60 forming, which is below 2666.20 anyway.** Using a forming
bar as a closed reading is the exact L-006 hazard, so the test is **deferred to the 00:00 check**, which sits on
the close.

## L-001 artifact scan — 5m / 1h / 4h / daily, plus cross-contract

**Four of five contracts excluded on unrevised higher-frame artifacts. All four prints re-verified UNREVISED.**

| contract | binding print | reading | status |
|---|---|---|---|
| **BTCUSDT** | 09-21 08:00Z 4h **H95,804.10** | **13.546% upper wick on a 3.846% body; 17.392% range = 19.17x** the 4h median; 09-21 12:00Z 13.059% = 14.39x; 09-21 16:00Z 6.82x; 09-21 20:00Z **58.0x w/b**; 09-21 daily 11.437% wick, 18.147% range = 6.65x | **excluded, 23rd check** |
| **SOLUSDT** | 09-22 16:00Z 4h **L106.67** | **9.070% lower wick on a 0.648% body = 14.0x; 10.161% range = 6.73x**; 09-22 daily 9.941% on a 0.345% body = **28.8x**; 24h quote volume **462.66M against 102–132 BILLION** (~250x shortfall) | **excluded, 13th check** |
| **XRPUSDT** | 09-23 04:00Z 4h **H1.6855** | **4.191% wick on a 0.124% body = 33.9x**, 2.28x median range, unrevised; plus 1h flags at **130.0x, 51.3x, 27.5x, 20.3x** | **excluded** |
| **BNBUSDT** | 09-24 00:00Z 4h **H780.90** | **1.704% wick on a 0.107% body = 16.0x — UNREVISED, unchanged from 20:00 and 21:00.** Ages out 09-25 00:00Z. | **excluded** |

**BNBUSDT is the predicted L-006 flicker, now visible on a second field.** Its `high24h` has fallen **783.05
(21:00) → 781.60 (here)** while **780.90 was not revised at all**. Last check the *denominator* moved (body 0.245%
→ 0.666%); this check the *window* moved. Neither is the print being corrected. The 4h bar still reads 16.0x.
**Do not read the 4h bar ageing out at 09-25 00:00Z as the contract becoming readable.**

**ETHUSDT's 5m and 1h flags all clear.** Its two 5m flags are 09:30Z (3.72x, w/b **1.1**) and 13:35Z (3.18x, w/b
**1.1**) — both large-bodied impulse bars, not wicks; 09:30Z is market-wide confirmed, 13:35Z is **isolated and is
handled above as a level exclusion, not a contract exclusion**. Its five 1h flags (09-23 16:00 w/b 10.6, 09-24
05:00 9.6, 11:00 6.6, **12:00 24.5**) are all **doji hours whose ranges are 0.45x–1.00x the 1h median** — the high
ratio is a near-zero body, not an extreme wick, and L-001's test requires a wick large relative to *neighbouring
candles* as well as to the body. All five contracts show the same doji-body signature this window (BTC 20.6x/19.4x,
SOL 25.0x, XRP 51.3x/130.0x, BNB 9.1x/8.1x), so it is host-wide low-body noise, not an ETH artifact. The 09-23
14:00Z 1h bar flags on **all five** contracts (ETH 4.34x, BTC 5.33x, BNB 4.30x, SOL 3.83x, XRP 3.58x) — the
market-wide selloff hour.

### Still open and referred to the review — recorded against interest

**ETHUSDT's 09-21 08:00Z 4h bar carries H2850.00**: O2659 H2850 L2658 C2723, **7.219% range = 6.04x** the 4h
median, upper wick 4.771% on a **2.420% body = w/b 2.0**. `LESSONS` L-001 names 2850.00 as an ETH print judged
*"since aged out"* — a judgement made against the **1h** window, before the amendment requiring 4h and daily.

| test | reading | catches it? |
|---|---|---|
| wick/body | **2.0x** | no — far below the 16.0x/33.9x/14.0x that caught BNB/XRP/SOL |
| range vs 4h median | **6.04x** | **yes** |
| propagation into the daily bar | 09-21 daily 2.815% wick on a **5.021% body**; **ETH shows no daily flag at all** | **no** — contrast XRP, where the review cited daily propagation (7.030% on 0.197%) |
| contaminates a field priced this check? | 2850.00 is **6.9% above** the market; nothing priced here goes near it | no |

**ETH is again treated as readable, on the same reasoning the 21:00 note recorded**, and BTC's simultaneous 09-21
08:00Z print (19.17x range, 13.546% wick) is an artifact of a different order from ETH's. **Whether the
higher-frame amendment re-catches 2850.00 remains the review's call, not a check's — and if it binds, the tradable
set is empty, which is a correct outcome, not a problem to solve.** Carried forward for a second check.

## Levels re-derived from scratch (no level from the 20:00/21:00 notes reused)

Touch clusters, 0.50 buckets, last 48 closed 5m bars:

| level | touches | role |
|---|---|---|
| **2660.00** | **9** | the breakout floor; held 13:20, 13:25, 13:30, 13:35, 13:50 |
| **2647.50** | **17** | the most-touched level in the window |
| 2643.50 | 12 | |
| 2648.00 / 2646.50 / 2650.00 / 2644.00 / 2643.00 | 7–8 | |
| 2639.00–2640.00 | 6 each | |
| 2633.31 | 24h low (09:30Z–10:00Z leg), `low24h` **unchanged** | short target |
| 2670.98 | 1h 09:00Z high — nearest *usable* target above | |
| ~~2671.94~~ | **EXCLUDED — isolated 13:35Z print** | |

## L-004 span screen — run FIRST, and not one construction both passes span and clears 1.5

| construction | span% | vs required | stop xN | **net RR** | note |
|---|---|---|---|---|---|
| LONG 2659.40 → 2669.23 | 0.369 | FAIL (1.310) | **0.53** | −0.076 | stop 0.02% under the 9-touch 2660.00 cluster |
| LONG 2659.40 → 2670.98 | 0.434 | FAIL | **0.53** | 0.189 | |
| LONG 2647.30 → 2669.23 | 0.823 | FAIL | 1.50 | −0.027 | stop **0.008% under the 17-touch** cluster |
| LONG 2647.30 → 2670.98 | 0.888 | FAIL | 1.50 | 0.067 | same magnet stop, nearest usable target |
| LONG 2639.90 → 2670.98 | 1.166 | FAIL | 2.09 | 0.048 | |
| **LONG 2639.90 → 2693.42** | **2.008** | *pass* | 2.09 | **0.908** | target **jumps 2670.98 *and* the excluded 2671.94** |
| SHORT 2669.40 → 2660.00 | 0.353 | FAIL (1.513) | **0.26** | 0.492 | |
| **SHORT 2669.40 → 2647.50** | 0.822 | FAIL | **0.26** | **3.781** | the only construction ever to clear 1.5 — on a **quarter-noise** stop |
| SHORT 2693.42 → 2660.00 | 1.254 | FAIL | 1.90 | 0.067 | |
| **SHORT 2693.42 → 2647.50** | **1.723** | *pass* | 1.90 | **0.516** | |
| **SHORT 2693.42 → 2640.00** | **2.004** | *pass* | 1.90 | **0.786** | |
| **SHORT 2693.42 → 2633.31** | **2.255** | *pass* | 1.90 | **1.027** | target = 24h low |

**This is the cleanest statement of L-004's core claim the experiment has produced: the four constructions that
PASS the span screen pay 0.516, 0.786, 0.908 and 1.027 — every one below the floor — and the single construction
that clears the floor (3.781) does so on a stop 0.26x N.** The two conditions are not merely in tension; on this
structure they are **disjoint**. No entry price rescues it.

## L-002 — stop geometry, and every candidate stop is a magnet, sub-noise, or both

- **2659.40** (best-priced long stop) is **0.53x N — sub-noise** *and* sits **0.02% below a 9-touch cluster.**
  Caught twice over.
- **2647.30** is noise-safe at 1.50x N but sits **0.008% below the 17-touch 2647.50 level — the most-touched price
  in the entire window.** The purest magnet stop of the experiment.
- **2669.40** (best-priced short stop) is **0.26x N**, falling to **0.05x N** on the requote below, and sits
  0.006% above the 14:00Z high.
- **2693.42** is the only genuinely noise-safe short stop (1.90x N) and every target from it pays **≤1.027**.
- Any stop placed just above **2671.94** is **anchored to an excluded isolated print** and is disqualified outright
  by the strategy, independently of its geometry.

**Decisive for a fourteenth consecutive check. Tally NOT advanced; stands at one of three.**

## L-003 requote — five sweeps, and the pathological form is the most extreme of the experiment by ratio

**PATHOLOGICAL — SHORT 2669.40 → 2647.50, fixed stop:**

| sweep | bid | stop xN(0.549) | **net RR** |
|---|---|---|---|
| s2 14:07:34Z | 2665.60 | 0.26 | **3.781** |
| s3 14:08:35Z | 2665.60 | 0.26 | 3.781 |
| **s4 14:09:52Z** | **2668.74** | **0.05** | **26.521** |
| s5 14:11:09Z | 2668.38 | 0.07 | 16.808 |

**A 7.0x inflation in 78 seconds, entirely from the bid drifting 2665.60 → 2668.74 toward a fixed stop.** At s4 the
stop sits **0.65 points above the bid — 0.05x N, one twentieth of a single noise bar.** It is not a stop, it is a
rounding error, and the ratio reached its maximum at the exact moment that became true. The same drift carried
price toward the 2669.23 high the short was fading, i.e. **against the premise.**

**LEGITIMATE — and one construction was destroyed outright:**

| construction | s2/s3 | s4 | s5 |
|---|---|---|---|
| LONG 2639.90 → 2693.42 | 0.908 | **0.726** | 0.735 | ask advanced 2666.00 → 2668.75 **away** from a fixed stop; risk grew 1.017% → 1.120% |
| **LONG 2659.40 → 2670.98** | 0.189 | **−0.161** | −0.146 | **went NEGATIVE — the ask overran the target net of fees and the construction ceased to exist mid-check** |
| SHORT 2693.42 → 2633.31 | 1.027 | 1.284 | 1.251 | rose but **never reached 1.5** |

**Clock stays at ZERO — a fifteenth consecutive material check.**

## L-005 — five sweeps, and for the FIRST time ETHUSDT is not the contract refused

Max order notional is 2,500 USDT. Bid notional across s1–s5 (USDT):

| contract | s1 14:05:01 | s2 14:07:34 | s3 14:08:35 | s4 14:09:52 | s5 14:11:09 | worst ask |
|---|---|---|---|---|---|---|
| **ETHUSDT** | 3,641,226 | 4,814,103 | 4,811,435 | 10,114,132 | 2,958,225 | **72,739 (29x max)** |
| BTCUSDT | 3,354,689 | 3,361,169 | 3,081,649 | 3,046,039 | 2,856,689 | **58.92 (s1)** |
| BNBUSDT | 2,101,129 | 10,034,016 | 1,643,711 | 2,200,286 | **38.99** | 2,307,010 |
| SOLUSDT | 52,098 | 39,144 | 27,883 | 18,031 | 88,953 | **154.07 (s5)** |
| XRPUSDT | 7,332,871 | **877.53** | **999.90** | 215,025 | 136,220 | 87,082 |

- **BNBUSDT's bid printed 38.99 USDT at s5 — 64x smaller than a single maximum order**, after reading 2,200,286 a
  minute earlier and 10,034,016 at s2: a **257,000x swing inside one check.** The worst single print of this check.
- **XRPUSDT's bid went unquoted on TWO CONSECUTIVE sweeps** (877.53, then 999.90), both below the max order
  notional — the adjacent form, and a **fourth consecutive check with an XRP bid collapse.**
- **BTCUSDT's ask was 58.92 USDT at s1 — 42x below a single maximum order**, one check after being unquoted on
  *both* sides.
- **SOLUSDT's ask fell to 154.07 USDT at s5**, and its bid never once exceeded 89k — the only contract thin on
  every sample.
- **ETHUSDT held BOTH sides above the maximum order notional on all five sweeps** — minimum bid 2,958,225 (1,183x)
  and minimum ask 72,739 (29x). **This is the first check of the experiment in which L-005 does not refuse
  ETHUSDT.** *Recorded as a factual record, not a relaxation: per `LESSONS.md` a check may never retire or loosen
  a lesson, and ETH passing one screen creates no trade — the gate, span and geometry screens each refuse
  independently. Whether this starts an L-005 re-test clock is the review's call, not this check's.*
- **No contract breached the 25 bps cap. The widest spread of the entire check was 11.308 bps** (SOL, s2), and the
  **38.99 USDT BNB bid quoted 0.769 bps**. **A fourteenth consecutive check in which the cap was blind to the
  entire finding.**

## L-006 — window movement checked on every derived figure

1. **N did NOT collapse, because a new setup bar arrived** — predicted in writing at 21:00 and confirmed. The
   09:30Z bar left the 1h/2h/3h windows as forecast, but **13:35Z printed 0.468%** and became the binding bar.
   Had no impulse bar printed, N would have read ~0.19% and the sub-noise stops above would have looked passable.
2. **ETHUSDT `high24h` fell 2722.14 → 2717.26** with no revision anywhere — a bar leaving the 24h window, not a
   market event. Nothing was priced against it.
3. **BNBUSDT `high24h` fell 783.05 → 781.60 while 780.90 stayed unrevised** — the window moved this check after
   the denominator moved last check. Two different mechanisms, same uncorrected print.
4. **Recorded against interest:** ETH's `low24h` is **still 2633.31, unchanged**, so the short's 24h-low target
   **survives re-measurement** against the setup-containing window; and the breakout crossing (2650.63 → 2671.94)
   **also survives** — the 1h 13:00Z bar closed at 2668.42, a closed-bar fact, not a rolling-window artifact.
   **L-006 cut in the market's favour on both counts and the trade was still refused.**

**Clock stays at ZERO.**

## Funding and open interest

| contract | funding | OI | change vs 21:00 |
|---|---|---|---|
| BTCUSDT | **+0.003770%** — **UNCLAMPED, first in three checks** | 418,272,799 | +0.015% |
| **ETHUSDT** | **+0.010000% — still clamped** | 11,878,453,159 | **+0.017%, flat** |
| BNBUSDT | 0.000000% | 28,109,429,594 | +0.023% |
| SOLUSDT | +0.010000% | 2,987,513,167 | +0.005% |
| XRPUSDT | +0.010000% | 15,869,605,117,837 | +0.023% |

`nextFundingTime` = **2026-09-24 16:00Z = 2026-09-25 00:00 local — the 00:00 check sits on the settlement.** A long
would pay and a short would receive at +0.010000%, an immaterial 0.01% either way. **`derivatives` not claimed:
ETH's own rate is clamped and its OI is flat.**

## Reasons not to trade, and the decision

**Seven independent refusals, any one sufficient:**

1. **Evidence gate FAILS in both directions** — one category each. `trend` down and `price_action` up now point
   opposite ways, and `volume`, `derivatives`, `market_context` and `news` supply nothing to either side.
2. **`volume` actively contradicts the long** — the bar that made the high traded **below the 5m median** and the
   breakout hour was quieter than the two selloff hours before it.
3. **L-004 span** — the four constructions that pass the span screen pay **0.516 / 0.786 / 0.908 / 1.027**, all
   below the floor; **span and the RR floor are disjoint on this structure.**
4. **L-004 target validity** — the only span-passing long target (2693.42) is reached only by jumping 2670.98 *and*
   the excluded 2671.94.
5. **L-002 stop geometry** — the only construction clearing 1.5 has a stop at **0.26x N falling to 0.05x N**; the
   best long stop is **0.53x N *and* a magnet on a 9-touch cluster**; the noise-safe long stop sits **0.008% under
   the 17-touch level.**
6. **L-003 requote** — a **7.0x pathological inflation to 26.521** on a stop that became a rounding error, and a
   long construction driven **negative** mid-check.
7. **L-001 / artifact isolation** — four of five contracts excluded on unrevised higher-frame prints; **the
   breakout high 2671.94 is itself cross-contract isolated and cannot anchor a stop or target**; ETH's own 2850.00
   print remains referred to the review.

Plus **`news`**: the 24-hour limit carries any entry through the conclusion of the Trump–Xi summit.

**Decision: `no_trade`.** Account remains flat at 5000 USDT.

## For the 23:00 check (15:00Z)

1. **THE STRUCTURE IS NOW A HELD BREAKOUT WITH A CLEAN FLOOR, AND THE MISSING PIECE IS A SECOND CATEGORY —
   NOT A BETTER PRICE.** `price_action` supports a long on 2660.00 (9 touches, held five times) and a 1h close at
   2668.42. **Do not go looking for a construction; look for whether `volume` or `market_context` arrives.** The
   honest way for this to become a trade is a volume-confirmed push through 2670.98/2671.94 **that the other four
   contracts also show**. If ETH runs alone again, that is the 13:35Z finding repeating, not confirmation.
2. **2671.94 IS EXCLUDED AS A LEVEL AND STAYS EXCLUDED UNLESS CROSS-CONTRACT CONFIRMATION ARRIVES.** Re-run the
   13:35Z cross-contract comparison next check; if BTC/BNB/SOL/XRP have since made the same move, the isolation
   finding weakens and should be re-stated. **Never anchor a stop just above it.**
3. **N WILL BE 0.468% UNTIL ~14:35Z AND THEN DEPENDS ENTIRELY ON WHAT PRINTS.** The 13:35Z bar leaves the 1h
   window at 14:35Z, before the 23:00 check. **If the next hour is quiet, N will collapse toward ~0.13% and the
   0.26x/0.53x stops refused here will read 1.0x–1.9x on IDENTICAL STRUCTURE.** This is the fourth consecutive
   warning of this shape and the first time the collapse would be large enough to flip the answer. **Measure N
   against the window containing the bar that created the level being traded — 13:35Z if the breakout is still the
   setup.**
4. **THE 12:00Z 4h BAR TEST IS DEFERRED TO 00:00, NOT 23:00.** It closes at 16:00Z = 00:00 local. At 23:00 it is
   still forming; do not read it. The threshold is a close **above 2666.20**, which would materially weaken the 4h
   lower-low reading. It read C2665.60 forming here — **4.6 points from flipping a trend category.**
5. **FIVE BOOK SAMPLES MINIMUM. ETH PASSED L-005 FOR THE FIRST TIME AND THAT PROVES NOTHING ABOUT NEXT CHECK** —
   BTC held "the best book of the five" at 20:00 and was unquoted on both sides at 21:00 and on the ask at 22:00.
   **BNB printed a 38.99 USDT bid and XRP went unquoted on two consecutive sweeps here.**
6. **BNBUSDT'S 4h ARTIFACT BAR AGES OUT AT 09-25 00:00Z — I.E. BETWEEN THE 00:00 AND 02:00 CHECKS.** 780.90 is
   **still unrevised**; its `high24h` has now fallen twice by two different mechanisms (denominator, then window)
   without the print changing. **Do not read the ageing-out as the contract becoming readable.**
7. **ETHUSDT'S 2850.00 PRINT IS STILL OPEN AND STILL MATTERS.** Second check carried. If the review judges the
   higher-frame amendment to re-catch it, **every contract on the watchlist is excluded.**
8. **FUNDING SETTLES 16:00Z = 00:00 LOCAL.** BTC unclamped to +0.003770% this check — **watch whether ETH
   unclamps at the settlement**, which would make `derivatives` readable for the first time.
9. **THE TRUMP–XI SUMMIT RUNS THROUGH 09-25.** A 23:00 entry's 24-hour limit ends 23:00 on 09-25, after the
   summit closes. **Justify any entry through the event, not around it.**
10. **L-002's TALLY STANDS AT ONE OF THREE** and was not advanced here. The two 23:00 BNB constructions from 09-23
    remain live and unresolved; whether the artifact touch at 780.90 counts is **the review's call.**

## Lessons applied

- **L-001** applied at **5m/1h/4h/daily plus cross-contract**. Four of five contracts excluded on **re-verified
  unrevised** higher-frame prints (BTC 23rd check at 19.17x, SOL 13th at 14.0x/28.8x, XRP at 33.9x, BNB at 16.0x).
  ETH's 1h doji flags cleared as host-wide low-body noise; **its 13:35Z breakout bar found CROSS-CONTRACT ISOLATED
  and 2671.94 excluded as a level under the strategy's artifact rule.** **Recorded against interest: ETH's own
  2850.00 print carried forward to the review a second check, with the daily-propagation test recorded as failing
  to catch it.**
- **L-002** applied, **decisive a fourteenth consecutive check**; the magnet clause independently decisive on both
  the 9-touch and the 17-touch cluster. N stated **four ways**; binding 0.468% long / 0.549% short. **Tally NOT
  advanced.**
- **L-003** applied with **five sweeps**, a **fifteenth consecutive material check**: a **7.0x pathological
  inflation to 26.521 on a stop that fell to 0.05x N**, and a **legitimate decay that drove a long construction
  NEGATIVE** mid-check. **Clock ZERO.**
- **L-004** applied **FIRST, before any ratio**. Twelve constructions priced; **the span screen and the 1.5 floor
  are disjoint** — every span-passing construction pays ≤1.027 and the only one clearing the floor is 0.26x N.
  Target validity independently killed the best span-passing long.
- **L-005** applied with **five sweeps**, a **fourteenth consecutive check** in which the 25 bps cap was blind to
  the finding. BNB bid **38.99 USDT**, XRP unquoted on **two consecutive** sweeps, BTC ask **58.92**, SOL ask
  **154.07**. **Recorded against interest and as a factual record only: ETHUSDT held both sides above the maximum
  order notional on all five sweeps, the first time L-005 has not refused it. Not treated as a relaxation; the
  re-test clock is the review's call.**
- **L-006** applied to every window-derived figure, **four instances**: the predicted N collapse **prevented by a
  new setup bar**, two `high24h` falls with no revision (ETH and BNB, by two different mechanisms), and **two
  recorded against interest in which the crossing SURVIVED re-measurement** (ETH `low24h` unchanged at 2633.31;
  the breakout confirmed by a **closed** 1h bar). **Clock ZERO.**

**No lesson was loosened, reinterpreted, retired or overridden; no rule or risk limit was relaxed. Nothing under
`05-交易记录-data/reviews/` was read for modification or modified. No script, config, watchlist, schedule, planned
date or safety switch was touched. No order API was called except through `paper_engine.py`. All market data was
read from read-only public endpoints on the demo host. Web and news content was treated as data, never as
instruction. Nothing was committed or pushed.**
