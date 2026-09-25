# Research journal — 2026-09-23_check_0900-research

Companion to the generated journal entry for `2026-09-23_check_0900_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-23T01:30Z (09:30 Asia/Kuala_Lumpur), slot `2026-09-23_check_0900`.
- **What was done:** Read `AGENTS.md`, `02-项目文档-docs/TRADING-STRATEGY.md`,
  `03-定时任务-routines/AUTOMATION-PROMPT.md`, `03-定时任务-routines/CONTINUITY.md`,
  `04-运行状态-state/readiness.json`, `05-交易记录-data/current-state.json`, the **02:00 slot's research note**
  and `reviews/LESSONS.md`. Ran the read-only observation at 01:04:00Z, then pulled 1d, 4h, 1h and 5m bars, the
  book, the 24h ticker, funding (live and six settled prints), mark/index and open interest for all five
  watchlist contracts from the demo host's public endpoints; ran the artifact scan at **both** 5m and 1h; ran the
  **span screen before any ratio**; took a confirming requote 132 seconds later as **L-003** requires; ran one web
  search for corroboration and scheduled news. Submitted a `no_trade` decision through `paper_engine.py` at
  01:09:46Z.
- **Why it was done:** The 09:00 slot was due (`due_slot: 2026-09-23_check_0900`, 240 planned slots) and no
  position was open, so an entry was permitted if and only if every entry condition and every lesson was satisfied.
- **Timing:** Observation 01:04:00Z, sweep 01:04:43Z, requote 01:06:55Z, engine 01:09:46Z (09:09 MYT) — **nine
  minutes after the slot. ON TIME**, fifth consecutive on-time check since the 09:00 stall on 2026-09-22.
- **Order proposed:** No. **Order placed:** No (`status: no_trade`, `live_order_sent: false`). **Order filled:** No.
- **Exchange stop/target reconciliation:** None to reconcile. Flat before and after; no exit order has ever been
  placed in this experiment.
- **Current holdings:** None. Flat. **Current cash:** 5000 USDT (demo wallet 5000.04174826).
- **Current risk:** 0 USDT open risk; 0 USDT realized today. Trading day index 3.
- **Evidence captured:** `evidence/2026-09-23_check_0900.json` (read-only run),
  `evidence/2026-09-23_check_0900_paper.json` (engine), and this note.

## The headline: the evidence got stronger and the trade got worse

The 02:00 note left the long hanging on one question. It was answered in the **affirmative** — and the long is
still refused, for a reason that had not appeared in this experiment before.

### (1) The 4h ascending-low sequence extended to a fifth and sixth low

| 4h bar | Low |
|---|---|
| 09-22 04:00Z | 1.4939 |
| 09-22 08:00Z | 1.5142 |
| 09-22 12:00Z | 1.5306 |
| 09-22 16:00Z | 1.5475 |
| **09-22 20:00Z** | **1.5577** |
| 09-23 00:00Z (in progress) | 1.5695 |

Six ascending 4h lows. The 1.5701 pivot, lost three times, is reclaimed and has held seven hours, and XRPUSDT
printed a **new 24h high of 1.6006** at 09-22 19:00Z. `trend` is clean and strengthened.

### (2) The funding question is closed — and it closed *against* the long

The 02:00 note asked for the 00:00Z settlement and said that if the sign alternated again, the fifth and sixth
data points should retire "XRP funding is a squeeze signal" for good.

| Settlement | XRPUSDT rate |
|---|---|
| 09-21 08:00Z | +0.010000% |
| 09-21 16:00Z | +0.010000% |
| 09-22 00:00Z | −0.006889% |
| 09-22 08:00Z | +0.010000% |
| 09-22 16:00Z | −0.017407% |
| **09-23 00:00Z** | **+0.010000%** |

**The sign has alternated three times across six settlements.** It is an oscillation, conclusively. The 00:00
note's "persisting discount" framing is dead, and so is the signal.

More than that: **the leg has flipped from absent to actively against the long.** Predicted funding for 08:00Z
reads **+0.006982%** (01:04:43Z) and **+0.005892%** (01:06:55Z). A long now *pays*, having paid the maximum two
hours ago. `derivatives` is claimed **against** the long, not merely withheld.

### (3) The span screen, run first — and it kills the long for the opposite reason to the last two checks

**N = 0.518%** (00:25Z bar). Required span = 2.5N + 0.14% ≈ **1.435%**.

The problem is no longer a cramped stop. It is a **vanished target.** Price is 1.5904 and the *only* overhead
structure in the entire window is the 1.6006 high — **0.641% away, less than half the required span and barely
more than one N.**

| Stop | Target | Risk | vs N | Net RR |
|---|---|---|---|---|
| 1.5841 | 1.6006 | 0.396% | **0.765×** | **rejected by L-002 before pricing** |
| 1.5811 | 1.6006 | 0.585% | 1.13× | **0.932** |
| 1.5695 | 1.6006 | 1.314% | 2.54× | **0.434** |
| **1.5577** | 1.6006 | 2.056% | 3.97× | **0.281** |

The best construction pays **0.932**. The one the thesis actually requires — stop below 1.5577, the level whose
loss would end the ascending sequence — pays **0.281**.

### (4) The only path to 1.5 is target-stretching in its purest form

Stop 1.5811 with an invented 1.6100 pays **1.863**. But **1.6006 is the highest price in the window**, so a
target above it has *no structure beneath it at all* — not merely intervening rejections.

**At 02:00 target-stretching meant reaching beyond four rejected highs. At 09:00 it means reaching beyond the end
of the data.** Third consecutive check in which this screen has disqualified the check's own best candidate,
second prospectively. It remains the binding constraint of this experiment, and it belongs to the review task.

### (5) L-003 reproduced in its *original* direction for the first time since 09-21

| Quote | Ask | Risk | vs N | Net RR |
|---|---|---|---|---|
| 01:04:43Z | 1.5904 | 0.585% | 1.13× | **0.932** |
| 01:06:55Z | 1.5916 | 0.660% | 1.27× | **0.726** |
| engine 01:09:46Z | 1.5943 | 0.828% | 1.60× | **0.393** |

Net RR fell **22% in 132 seconds and 58% in five minutes** as price advanced **away** from its fixed stop and
**toward** its fixed target. The last three checks reproduced only L-003's mirror form (ratio improving by
drifting onto the stop). **Both directions of L-003 are now demonstrated on this watchlist.** Neither
construction was within reach of 1.5 at any of the three quotes.

## New artifact — the largest of the experiment, and it is not on BTCUSDT

**SOLUSDT, 09-22 19:00Z 1h bar: O 118.09 / H 118.59 / L 106.67 / C 118.07.**

A **9.655% lower wick on a 0.017% body — a ratio of roughly 568×** — and a **10.096% range against a 0.776%
median.** No other contract shows anything at 19:00Z. It is contaminating **SOLUSDT's 24h low field, which reads
106.67** against a real session floor of 115.55. The 02:00 sweep at 18:05Z could not have seen it; the bar had
not formed.

**SOLUSDT is excluded** under L-001's own unreadable-structure criterion, on top of its standing data-quality
flag (24h quote volume 413.7M against 96,316M–137,582M for the other four, a factor of ~250).

**This is a direct and material challenge to L-001's hypothesis** that artifacts are "a BTCUSDT phenomenon rather
than a host-wide one." The biggest print the experiment has recorded landed on SOLUSDT. **I have not touched the
lesson** — only the daily review may amend one. Recorded for the review as the strongest evidence yet on L-001's
scope.

## L-001 re-test clock — and an awkwardness for the review

- BTCUSDT's last artifact print remains **09-21 20:00Z 90389.80, now 29h04m ago**. **The full artifact-free day
  is complete at both resolutions and L-001's stated re-test condition is formally met.**
- **BTCUSDT nevertheless stays excluded for an eleventh consecutive check.** A check may not retire a lesson.
- **The review should note the awkwardness:** the re-test condition was met on BTC in the *same check* in which
  the hypothesis's premise was falsified on SOL.
- **Standing item closed:** BTCUSDT's 24h high field now reads **86556.20 against a real top of 86556.20** — the
  **91000.00 contamination has aged out of the 24h window**, carried since 09-21.
- Only two BTC 1h bars still flag in the 30-bar window: 09-21 20:00Z 90389.80 (wick) and 09-22 08:00Z (range
  only). 86769.40, 95804.10, 86999.00 and ETHUSDT's 2795.00 have all aged out.

## Book size, checked before anything was built

The 02:00 quantity-instability finding is **confirmed on a second check**, over 132 seconds:

| Contract | 01:04:43Z | 01:06:55Z |
|---|---|---|
| **BTCUSDT** | bid 4,883,310 / ask **3,575,031** USDT, 1.49 bps | bid 4,448,230 / ask **995** USDT, **0.30 bps** |
| SOLUSDT | bid 85,905 / ask 30,540 | bid 17,320 / ask 201,079 |
| **XRPUSDT** | bid 20,211,266 / ask 12,297,687 | bid 7,953,392 / ask 19,009,418 |
| ETHUSDT | bid 342,685 / ask 5,478,940 | bid 408,737 / ask 10,453,076 |
| BNBUSDT | bid 8,713,875 / ask 8,996,736 | bid 7,192,713 / ask 19,997,019 |

BTCUSDT's ask collapsed to **0.0115 BTC while quoting the tightest spread of the experiment.** A 0.30 bps spread
on a 995 USDT touch against a 2500 USDT maximum notional is not a measurement, and the 25 bps cap cannot see it.
**XRPUSDT's book, by contrast, was genuinely deep on both sides at both sweeps — the book was not the binding
constraint on the contract that mattered. The geometry was.**

All five spreads inside the 25 bps cap at both sweeps (BTC 1.49/0.30, ETH 1.81/2.97, BNB 3.66/0.13, SOL
6.73/3.36, XRP 4.40/5.66).

## The other contracts

- **BNBUSDT short — the 02:00 runner-up is gone, and this is a clean falsification of a prior check's read.** Its
  trend leg was six descending 4h highs; **the sequence has broken**: 789.77 → 792.26 → 791.56 → 791.57 → 793.14,
  the last four ascending or flat, price 791.41 near the top of the 782.33–796.35 range. `market_context` decayed
  from −1.046% to −0.359%. At most one soft category — it no longer even reaches the bar it failed on geometry at
  02:00.
- **ETHUSDT long dies on the span screen before evidence.** Its 4h lows genuinely ascend (2716.01 → 2722.76 →
  2722.62 → 2729.14 → 2737.75 → 2749.28), but price 2764.78 sits **0.091% below the 2767.30 24h high** — the
  entire available reward is **0.43× N**. It also pays maximum +0.010000% funding and has no `market_context` at
  +0.770%.
- **XRPUSDT short:** one category at most (1.6006 has held six hours), with `trend` and `market_context` firmly
  against. One is not two.
- **`volume` examined and not claimed, fifth consecutive check — and negative this time.** XRPUSDT's 1h band is
  flat (5682.4M, 5893.4M, 5507.8M, 5491.4M, 5805.1M from 20:00Z) and the breakout 5m bars off 1.5780 (398M, 635M,
  885M, 649M) sit *inside* the same band as the quiet ones. **The new 24h high was not made on expanding
  participation** — itself a reason not to chase it.

## External corroboration

One web search places XRP at about **1.58 USD**, 24h range **1.49–1.59**, **+5.48%** over 24h, against the demo's
1.5897/1.5916, 1.4939–1.6006 and +4.694%. **XRPUSDT itself is not contaminated** and the relative-strength read is
independently confirmed. No chaotic news, no scheduled event requiring a stop; `news` not claimed.

**One divergence worth recording:** the externally reported 24h high is ~1.59 against the demo's **1.6006** — so
the single level the entire long construction depends on as its target is the one level the outside world does not
fully confirm. That 1.6006 print also flags *marginally* on the wick screen (1.231% upper wick on a 0.317% body,
3.9×), though its range is normal for a contract that moved 4.7% in a day, so **I do not classify it as an
artifact.** But a target that is simultaneously the edge of the data, unconfirmed externally and marginally
wick-flagged is not a target to build on.

## The net position

**XRPUSDT long has the strongest evidence of the experiment so far — two clean categories, six ascending 4h lows,
a reclaimed pivot and a new high — and no valid construction whatsoever, because it has already travelled to the
top of its own range and now pays the maximum funding to hold.** This is the cheapest kind of trade to refuse and
the easiest to rationalise. Chasing a +4.7% move into the 0.64% that remains beneath its high, on a stop that must
sit 2.06% away to be structurally honest, is exactly what the span screen exists to prevent. Staying flat is
correct and unforced.

## For the 16:00 check

1. **Do not rebuild the XRP long on `trend` + `market_context` alone.** Those two categories have now been
   present and insufficient for three consecutive checks. The binding question is never the evidence; it is
   whether a *nearest*-structural target sits ≥ 2.7N from a noise-safe stop. **Run the span screen first, again.**
2. **The XRP long only becomes tradeable on a pullback, not a continuation.** Concretely: a retrace toward
   1.5695–1.5760 that holds would put a noise-safe stop under 1.5577 back within ~2.7N of 1.6006. **A further
   advance makes the trade worse, not better** — that is this check's whole lesson, and L-003 demonstrated it
   three times in five minutes.
3. **Watch the 1.5577 4h low.** It is the level whose loss ends the six-bar ascending sequence and hands the
   short a real `trend` leg for the first time.
4. **Read the 08:00Z XRP settlement.** Predicted +0.006982% → +0.005892%. If it settles positive, that is a
   seventh point and the funding signal should be considered retired rather than oscillating — for the review.
5. **SOLUSDT: re-scan the 19:00Z bar and check whether 106.67 persists or is revised.** If further artifacts print
   on non-BTC contracts, L-001's scope hypothesis is in real trouble and the review should say so.
6. **BTCUSDT stays excluded until the review says otherwise**, even though its re-test condition is now met.
7. **Check book *size* first, not spread.** BTC quoted 0.30 bps on a 995 USDT touch this check.

**Lessons applied:** **L-001** applied — BTCUSDT excluded for an eleventh consecutive check despite its re-test
condition being formally met; the scan was run at **both** 1h and 5m, and **the 1h pass is what caught the
SOLUSDT 106.67 print that the 5m window could not reach**; SOLUSDT excluded under the same lesson's
unreadable-structure criterion. **L-002** applied and decisive — it rejected the 1.5841 stop at **0.765× N**, the
only stop that would have made the ratio presentable. **L-003** applied and **material for a fourth consecutive
check**, this time in its original direction — the requote cut the best net RR from 0.932 to 0.726, and the
engine's own quote three minutes later cut it to 0.393. No lesson was loosened, reinterpreted or overridden, and
no lesson was used to justify an action a rule forbids. Nothing under `reviews/` was read for modification or
modified; the 22:00 review task owns that folder. Live trading remains disabled.
