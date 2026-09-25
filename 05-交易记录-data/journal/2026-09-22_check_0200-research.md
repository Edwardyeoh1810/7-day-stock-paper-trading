# Research journal — 2026-09-22_check_0200-research

Companion to the generated journal entry for `2026-09-22_check_0200_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-21T18:20Z (02:20 Asia/Kuala_Lumpur on 2026-09-22),
  slot `2026-09-22_check_0200`.
- **What was done:** Read AGENTS.md, TRADING-STRATEGY.md, CONTINUITY.md, AUTOMATION-PROMPT.md, readiness.json,
  current-state.json, the 00:00 slot's research note and reviews/LESSONS.md. Ran the read-only observation for the
  due slot, re-researched all five watchlist contracts from the demo host's public endpoints (5m, 1h and 60 daily
  bars, book, 24h ticker, funding), resolved the SOLUSDT condition the 00:00 note named in advance, re-verified the
  118.9100 target at 5m resolution, re-implemented the engine's own reward/risk formula independently and validated
  it against the note's ETHUSDT threshold, ran the artifact scan on all five at both 5m and 1h resolution, took a
  second quote six minutes after the first, and submitted a `no_trade` decision through `paper_engine.py`.
- **Why it was done:** The 02:00 slot was due (`due_slot: 2026-09-22_check_0200`, 240 planned slots) and no position
  was open, so a new entry was permitted if and only if every entry condition was met.
- **Timing:** Observation ran at 18:04Z (02:04 MYT), decision submitted at 18:13Z (02:13 MYT) — 13 minutes after the
  slot, inside the 45-minute entry window with 32 minutes to spare. This run was **not** late; an entry would have
  been accepted. Worth stating plainly, because **three** constructions cleared the reward/risk floor during this
  check and all three were declined on evidence or on their own subsequent arithmetic.
- **Order proposed:** No.
- **Order placed:** No. No demo order was sent; the engine returned `status: no_trade`, `live_order_sent: false`.
- **Order filled:** No.
- **Exchange stop/target reconciliation:** None to reconcile. The account was flat before this check and is flat
  after it; no exit order has ever been placed in this experiment.
- **Current holdings:** None. Flat.
- **Current cash:** 5000 USDT. Demo wallet balance 5000.04174826 USDT.
- **Current risk:** 0 USDT open risk; 0 USDT realized today. No daily-limit or consecutive-stop constraint is near.
- **Evidence captured:** `05-交易记录-data/evidence/2026-09-22_check_0200.json` (read-only run),
  `05-交易记录-data/evidence/2026-09-22_check_0200_paper.json` (engine), and this note.

## The SOLUSDT condition resolved: target valid, shelf broken, floor re-formed one level lower

The 00:00 note made SOL the priority and set the condition precisely, so this check did not have to re-derive it:
*becomes honest only on a fall to the 117.36 shelf **that holds** — a 117.45 ask with a 117.00 stop gives 2.108 to
118.9100. Re-verify 118.9100 has not been taken out first.*

**The target is genuine — this needed settling and it was not obvious.** SOL's 15Z *hourly* bar looks like an
artifact at a glance: a 0.84% upper wick on a 0.08% body. The 5m detail clears it:

| SOL 15:15Z 5m | Open | High | Low | Close | Volume |
|---|---|---|---|---|---|
| | 118.60 | **118.91** | 118.07 | 118.07 | **7,985,396** |

Body 0.447%, upper wick **0.261%** — the wick is *smaller* than the body, on the heaviest bar of the stretch. That
is a real traded high that reversed hard, not a phantom print. The hourly "wick" is simply the intra-hour reversal.
**118.9100 stands as a valid overhead reference**, and it has not been taken out (hourly highs since: 118.41,
117.85, 117.14).

**The shelf did not hold.** SOL traded below 117.36 at least seven times — 116.81 (16:35Z), 116.74 (16:40Z), 117.21
(17:15Z), 117.14 (17:45Z), 116.80 (17:50Z), 116.73 (17:55Z), 116.73 (18:00Z). The literal construction is dead: a
117.00 stop has been traded through repeatedly and the 117.45 ask is gone.

**A new floor formed 0.5% lower, and it is arguably better than the original**: 116.74, 116.73, 116.73 — three
touches spanning 75 minutes with a full rally to 117.85 in between, so a genuine re-test rather than one extended
base. Re-sited there the trade passed at the first quote: a **117.04 ask with a 116.40 stop** (below the entire
floor complex, including the 116.71 low of the 13Z hour) and the 118.91 target gives **2.122 net** on a 0.57% stop
comparable to recent 5m ranges — not a fitted one.

It was declined anyway, on two grounds:

1. **Volume decisively opposes.** Five of the six heaviest 5m bars of the last two hours are DOWN bars.

   | Bar | Direction | Volume |
   |---|---|---|
   | 16:35Z | **DOWN** (117.40→116.81, broke the shelf) | **9,671,921** |
   | 17:50Z | DOWN | 7,564,121 |
   | 17:15Z | DOWN | 6,370,864 |
   | 17:45Z | DOWN | 5,479,747 |
   | 16:40Z | UP (the bounce) | 4,889,778 |

   The heaviest up bar is **half** the heaviest down bar. This is the identical test that rejected the XRP long at
   23:00 and 00:00; applied symmetrically it rejects this long.

2. **No hold.** The 116.73 touch sat *four minutes* deep in a still-forming bar. The 23:00 note set the 45-minute
   standard and the 00:00 note failed the XRP long on exactly that clause. Four minutes does not meet it.

Structurally SOL was also a **descending triangle** — hourly highs stepping down 118.91 → 118.41 → 117.85 → 117.14
into a flat floor — the configuration in which a long is the wrong side.

## The finding of the hour: the drift trap demonstrated in both directions inside one check

Two quotes were taken, six minutes apart. The gap between them is the most informative measurement of the check.

**Both long candidates passed the floor and failed it within six minutes, on entry drift alone, with no new
information:**

| | 18:04:30Z | 18:10:09Z | Verdict |
|---|---|---|---|
| SOL long, stop 116.40, target 118.91 | ask 117.04 → **2.122 PASS** | ask 117.34 → **1.273 FAIL** | threshold was ask ≤ 117.2397 |
| BNB long, stop 792.50, target 806.09 | ask 796.63 → **1.591 PASS** | ask 799.16 → **0.747 FAIL** | threshold was ask ≤ 796.8197 |

**And the mirror image ran on XRPUSDT at the same time.** At the first quote XRP offered the **first honest passing
short of the experiment** — a 1.4989 bid with a **1.5085 stop *above* the 1.5077 session high**, the structural stop
the 00:00 note demanded and could not find a passing target for, with the 1.4765 target printing **1.736**. No
fitted stop was required for the first time.

Six minutes later it printed **2.809**. The ratio improved for exactly one reason: the bid rose to 1.5022, moving
the entry *closer* to the fixed stop and collapsing the risk leg from 0.66% to 0.44% while lengthening the reward
leg. **The ratio improved because price moved against the thesis.** That is the drift trap of the 22:00, 23:00 and
00:00 notes running in reverse, and it is the first time both signs of it have been shown inside a single check.

The same move also **destroyed the short's only structural premise**. The case rested on a lower-high sequence of
1.5077 → 1.5020 → 1.4990; at 1.5022 the bid was above the 1.5020 lower high and the sequence no longer existed. The
short was left with zero `price_action` support, `volume` against it (the single heaviest 5m bar of the two-hour
window is 17:20Z at **871,174,547, an UP bar**; four of the top six are up bars; hourly volume *rising* through
5.45bn → 5.71bn → 5.92bn while price recovered off 1.4814) and `trend` against it (+7.162%, now the strongest of
the five). Below two categories, so the 2.809 is refused.

### The engine's own re-quote settled it for a third time

`paper_engine.py` re-read the book at **18:13:37Z** and returned **1.5067/1.5068**.

| Quote | XRP bid | To the 1.5077 high | To the declined 1.5085 stop |
|---|---|---|---|
| 18:04:30Z | 1.4989 | 0.587% | 0.640% |
| 18:10:09Z | 1.5022 | 0.366% | 0.419% |
| **18:13:37Z** | **1.5067** | **0.066%** | **0.119%** |

**XRP rallied 0.52% in nine minutes**, and the stop on the short that passed at 1.736 is now **0.119% away**. Had
this check taken it, it would be all but stopped out before the note was finished. This is the third consecutive
repetition of the pattern the 00:00 note documented at 16:17Z (0.44% in three minutes) — and the first time the
declined trade's stop has been walked to within a tick or two of being hit while the check was still running.

## The volume/arithmetic inversion is the governing reason to stay flat

On **all three readable contracts** the direction volume supports is the direction whose arithmetic fails, and the
direction whose arithmetic passes is the direction volume opposes:

| | Volume points | Arithmetic passes | Best failing side |
|---|---|---|---|
| SOLUSDT | DOWN (5 of 6 heaviest are down bars) | LONG only | short best 1.382 |
| BNBUSDT | DOWN (heaviest 1,120,696,350 is a down bar) | LONG only (at the first quote) | short honest 1.469 |
| XRPUSDT | UP (heaviest 871,174,547 is an up bar) | SHORT only | long best 1.257 |

Three independent contracts showing the same inversion simultaneously is the signature of a pullback that has not
resolved — and the six minutes between the quotes resolved it *upward* across all five at once (XRP +0.22%, SOL
+0.26%, BNB +0.32%, ETH +0.18%, BTC +0.11%). That is a better reason to stay flat than any single contract's
numbers.

**BNB short** is recorded as settled rather than skipped: the honest 799.90 stop with a 789.00 target prints
**1.469**, beneath the floor. The 0.031 gap was not bridged by loosening anything. **SOL short** fails every
construction (best 1.382 on a deep 115.20 target) despite having the clearest directional volume on the board — the
contract with the best evidence offers no tradeable expression of it.

## ETHUSDT, BTCUSDT, and a clean artifact scan

**ETHUSDT** fails a seventh consecutive time at **0.376** (sequence: 1.34, 0.55, 1.40, 0.45, 0.38, 0.350, 0.376).
Its threshold was re-derived **independently from the engine's own formula in `paper_ledger.py`** and came out at
**2720.3887**, matching the 2720.39 carried in the 23:00 and 00:00 notes — which validates the arithmetic running
through this whole sequence of notes. The ask is 2745.84, **25.45 above** the threshold.

**BTCUSDT** is structurally untradeable for a fifth consecutive check. Re-verifying from *hourly* bars this time
rather than 5m produced a new detail: the 95804.10 print contaminates **two separate hourly bars** —

| BTC 1h bar | Body | Upper wick | High |
|---|---|---|---|
| 09:00Z | 1.042% | **13.209%** | 95804.10 |
| 14:00Z | 0.429% | **11.697%** | 95804.10 |
| 12:00Z | 0.726% | 2.970% | 87888.00 |
| 15:00Z | 0.131% | 1.301% | 86999.00 |

Excluding these, the 60-day daily scan returns exactly **one** daily high above the 85930.90 ask — 2026-09-21
itself at 95804.10, which *is* the artifact. No valid overhead reference exists anywhere in sixty days, so no target
can be constructed at all.

**One clean result:** the artifact scan over the last 24 consecutive 5m bars on **all five** contracts returns
**nothing** — the first fully clean two-hour scan in several checks. The standing BTC and ETH daily/hourly
exclusions (including ETH's 2850.00 and the 2795.00 print from 15:50Z) remain.

## The honest counterpart, recorded because it is a real cost

**The SOL floor held and bounced 0.52%** (116.73 → 117.34 by 18:10Z). The long this check declined would have been
working. The confirmation requirement — the 45-minute hold — is precisely what cost the entry, because the entry
threshold (ask ≤ 117.2397) was crossed before confirmation could arrive.

This is not an argument for loosening. It is evidence that **on a setup whose target is only 1.6% away, waiting for
confirmation consumes the edge** — the same conclusion the 00:00 note reached for XRP when it ruled that a
structural stop and a structural target must sit more than roughly 2.5% apart. That conclusion now generalizes to a
second contract, and it should go to the review as the sharpest structural finding of the session so far.

## Next task focus

Account is flat, so the 09:00 check may open if conditions are met. Note the gap: **the next check is seven hours
away** (09:00 MYT / 01:00Z), the longest of the schedule, spanning the quiet 03:00–08:00 window. Everything below
will be stale by then and must be re-derived from fresh bars — thresholds computed at 02:00 prices are **not**
carryable across seven hours. What *is* carryable is the reasoning.

1. **XRP is at 1.5067 and pressing the 1.5077 session high — the level is live for the first time since 15:05Z.**
   Do **not** re-use this check's short: its premise is gone and its stop is 0.119% away. The 00:00 note's
   projections for a break of 1.5077 were computed at a 1.5100 ask and remain the reference — the long clears only
   by reaching for 1.5441 *and* tightening the stop into the range, which is two refused errors. The structural
   requirement is unchanged and now twice confirmed: **XRP produces nothing valid until a structural stop and a
   structural target sit more than roughly 2.5% apart.** If 1.5077 breaks and *holds* for 45+ minutes on a heaviest
   up bar, a long becomes arguable for the first time — but re-derive it, and note the new lower low at **1.4814**
   (16:35Z/16:40Z) now anchors the downside structure in place of 1.4849.
2. **SOLUSDT stays the contract to watch, and its floor is now 116.73** (three touches: 16:40Z, 17:55Z, 18:00Z),
   with **118.9100 confirmed a valid target**. The setup is unchanged in shape: a stop below 116.73 with the 118.91
   target. Its problem is the 1.6% target distance against ~1.3% hourly ranges, which is what made the
   confirmation wait unaffordable. Prefer it only if price returns *near* the floor with a confirming heavy up bar,
   and accept that the window will be narrow; do not take it from the middle.
3. **Cite, do not re-argue, the two demonstrated traps.** (a) A stop resting on or just under a level the market
   has touched repeatedly is a size, not a stop — this check's SOL 116.65/116.70 constructions and the 00:00 note's
   1.4849 case. (b) **A reward/risk ratio that improves because price moved *toward* the stop is not an improving
   trade** — this check's XRP short went 1.736 → 2.809 while its premise was being destroyed. Trap (b) is new and
   is the sharpest statement of the drift problem the experiment has produced.
4. **BNBUSDT and ETHUSDT to fifth and fourth.** BNB is the weakest contract (+4.283%) with hourly highs stepping
   down 806.09 → 804.21 → 799.76 → 796.63; it failed in both directions this check (long 0.747, honest short
   1.469). ETH needs to actually fall to ~2720 on the fixed 2693.00/2771.00 structure — check it once,
   mechanically. **BTCUSDT stays excluded on artifacts**; re-run the artifact scan on all five, at 1h as well as
   5m, since the hourly pass is what revealed the 95804.10 double contamination.

## Human confirmations needed

None for demo paper trading; live trading remains disabled. Four items for Edward's awareness, none requiring
action before the next check. **(a)** The strongest process result of the session is negative and worth the
review's attention: three constructions cleared the reward/risk floor this check and every one was invalidated
within nine minutes by price drift alone, twice on the long side and once on the short. The floor is being cleared
by geometry at a rate that suggests the 1.5 minimum is doing less work than the evidence tests are. **(b)** The
honest cost is recorded alongside it: the declined SOL long would have been working, and the 45-minute hold
requirement is what cost the entry — worth the review judging explicitly, since it is the first time the
selectivity has had a measurable price. **(c)** BTCUSDT's 24h high is an artifact appearing in two separate hourly
bars, leaving the contract with no valid overhead reference in sixty days; it has now been untradeable for five
consecutive checks for structural reasons. **(d)** The standing open-interest endpoint limitation on the demo host
still reduces the `derivatives` category to funding alone. The 22:00 daily review owns `reviews/` and may be
running concurrently; `LESSONS.md` was read (still empty — no closed trades) and nothing in that folder was
modified.
