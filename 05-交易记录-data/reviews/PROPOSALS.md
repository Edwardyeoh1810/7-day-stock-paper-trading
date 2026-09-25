# Proposals for Edward

Rule, limit, watchlist, schedule or code changes the reviews suggest. Nothing here takes effect until Edward
approves it and the change is made by him or at his request. Format per proposal: date, what to change, the
evidence (with sample size), the expected effect, the risk of being wrong, status (open / approved / rejected).

---

## P-001 — Bound the age of the evidence behind a decision, not just the quote

- **Date raised:** 2026-09-21 (day 1)
- **Status:** approved by Edward on 2026-09-21 and implemented the same day: entries are rejected when their check was scheduled more than 45 minutes ago (`decision_max_age_minutes`); `manage`, `close` and `no_trade` are never blocked.
- **What to change:** Add an evidence-freshness gate. Two parts, either or both: (a) a new
  `paper-config.json` key such as `decision_max_age_minutes` (a starting value of 30, matching the existing
  slot grace, is the obvious candidate); and (b) a check in `paper_ledger.py` / `paper_engine.py` that
  compares the decision file's `checked_at_local` against execution time and **rejects any entry decision**
  whose evidence is older than that bound. A rejected decision would have to be re-observed, not resubmitted.
  Suggested scope: entries only (`open_long` / `open_short`). `no_trade`, `manage` and `close` should not be
  blocked by staleness — refusing to record a no-trade or, worse, blocking an exit because data went stale
  would be strictly worse than allowing it.
- **Evidence (sample size: 1 slot, 1 day — raised on severity, not on statistics):** On 2026-09-21 the
  `check_1200` observation ran at 04:10:09Z and the decision reached the engine at 11:37:20Z, 7h27m later.
  `paper-config.json` bounds `readiness_max_age_hours` (24) and `quote_max_age_seconds` (10), and
  `paper_ledger.py:95` and `:151` enforce both — but no code path anywhere compares the decision's own
  evidence timestamp to execution time. The stale decision therefore passed every existing gate.
- **Expected effect:** Closes a gap that is currently invisible. Had today's decision been the BNBUSDT long
  instead of a no-trade, it would have filled at the live 84,655 market price against a thesis, stop and
  target reasoned at 81,427 — 3.96% away, against a planned risk of 1.45%. The position would have been
  sized from the wrong stop distance and opened with its stop already far out of the money. No existing rule
  would have stopped it. This makes future decisions strictly more selective and cannot loosen anything.
- **Risk of being wrong:** Low, but real: a bound set too tight would reject legitimate decisions on slow
  runs and silently reduce slot coverage, which is the very thing P-002 is trying to measure. Mitigated by
  requiring every rejection to be recorded with its reason (the existing "record the reason and do not retry
  with loosened parameters" rule already covers this) so rejections are counted rather than lost.

---

## P-002 — Decide the stalled-run policy, and measure slot coverage

- **Date raised:** 2026-09-21 (day 1)
- **Status:** approved by Edward on 2026-09-21 and implemented the same day: policy — a late run never enters, still manages or closes an open position, otherwise records `no_trade` with reason `late run`; measurement — `review_stats.py` now reports `slot_coverage`.
- **What to change:** Two related decisions, both Edward's:
  1. **Policy:** when a run resumes after its slot's 30-minute grace has expired, should it (a) submit the
     decision anyway, as happened today, (b) abort and leave the slot unrecorded, or (c) re-observe and
     record the decision against the *current* slot? Today's behaviour is (a) by default, not by choice.
     The reviewer's read: (b) or (c) is safer than (a), and (c) preserves coverage — but this is a rule
     change and is explicitly not the review's to make. Note that adopting P-001 makes (a) impossible for
     entries anyway, which is an argument for settling both together.
  2. **Measurement:** record slot coverage as a first-class number — slots due vs slots with a recorded
     decision — so the final result can state what fraction of the intended cadence actually ran. This is
     probably a small addition to `review_stats.py`, which today counts decisions but has nothing to compare
     them against.
- **Evidence (sample size: 1 day, 3 executions):** Day 1 ran 1 recorded decision against 4 reviewable due
  slots. `check_1600` is missing entirely, inside the 12:10–19:37 stall window. The `check_1200` decision
  arrived ~7h after its grace expired. The 22:00 review started at 19:41. `automation-status.json` carries
  `scheduler_execution_verified: false` and notes tasks run only while the Claude desktop app is open — a
  plausible common cause for the stall and the miss, though not for an early start, so the mechanism is not
  established.
- **Expected effect:** Makes the experiment's central claim measurable. A 30-day result from an unknown
  fraction of 180 intended checks cannot be honestly reported as a 30-day result; with coverage recorded it
  can at least be reported with its true denominator.
- **Risk of being wrong:** Very low for the measurement half — it only adds information. The policy half has
  a genuine trade-off: aborting stale slots produces a cleaner record but fewer decisions, and the sample is
  already small.

---

## P-003 — Treat demo-host price extremes as unusable for stop placement

- **Date raised:** 2026-09-21 (day 1)
- **Status:** approved by Edward on 2026-09-21 and implemented the same day: `TRADING-STRATEGY.md` has a "Demo Price Artifacts" section, and the daily review must flag artifact-triggered exits and report results with and without them. No script check was added. Known limit: an artifact can still trigger a resting stop.

**Update 2026-09-26 (Edward's decision):** amended. The artifact rule now excludes only the price as a level, requires both the wick and the cross-contract isolation test on the 1h/4h frames, and skips a contract only for 24 hours after a print. It never excludes a contract for longer.
- **What to change:** A note in `TRADING-STRATEGY.md` (and, if wanted, a sanity check in the observation
  script) that single-bar high/low extremes on the demo host are not acceptable structure for a stop or
  target, and that a bar whose wick exceeds some threshold of its own body — or which has no counterpart on
  any other watchlist contract — should be excluded from structural levels and from the 24h high/low fields.
- **Evidence (sample size: 1 print, 1 day):** The demo host's BTCUSDT 1h bar opening 2026-09-21T09:00Z
  reports a high of 95,804.10 against an open of 83,753.50 and a close of 84,625.90 — an ~14% wick with no
  counterpart in the other four contracts, which also propagates into the 24h high field.
- **Expected effect:** Prevents a stop or target being anchored to a simulated-book artifact. This is not
  cosmetic: stops and targets on this account rest on the demo exchange between checks, so an artifact print
  near a resting stop can trigger it and book a real loss into the ledger, corrupting the experiment's P&L
  with an event that has no market meaning.
- **Risk of being wrong:** Low. The cost of excluding a genuine extreme is one skipped setup; the cost of
  including an artifact is a fabricated loss in the result set. Note this is a demo-environment defect with
  no live-trading counterpart, so any rule written for it should be marked as such and not carried forward
  if the experiment ever informs live trading.


**Evidence amendment, 2026-09-24 (day 4) — one false print resolved two opposite declined constructions at the
identical price.** The 09-24 02:45Z BNBUSDT 5m bar printed H**780.90** — a 0.881% upper wick on a 0.149% body
(5.9x), ~7x the 5m frame median, **fully retraced inside its own bar**, shown by no other contract at that candle
(ETH ranged 0.093%, BTC 0.129%, XRP 0.233%, SOL 0.504% with no upper wick at all), and propagating unrevised into
the 02:00Z 1h bar, the 00:00Z 4h bar (**16.0x**) and the 09-24 daily bar. **That single price was simultaneously
the declined 09-23 23:00 long's target and the declined 09-23 23:00 short's stop.** On raw exchange prints the
long won and the short lost at the same tick, in a contract neither construction could legally have been opened
on. This is the cleanest demonstration available that demo extremes cannot be used to place, trigger or score
stops and targets: **the symmetry is the proof** — a rule that let this print resolve anything could be made to
prove a case and its opposite at the same instant. `LESSONS.md` L-002 is amended so that a declined setup is
resolved only by a price the market actually made; the re-test tally was **not** advanced and both 23:00
constructions remain live. The proposal is unchanged and still Edward's: the AI can refuse to *score* such prints,
but only a rule change can stop the engine *filling* on them.

---

## P-004 — Record `derivatives` as a degraded evidence category on the demo host

- **Date raised:** 2026-09-21 (day 1)
- **Status:** open — awaiting Edward's decision. Not applied.
- **What to change:** A note in `TRADING-STRATEGY.md` stating that on `demo-fapi.binance.com` the
  `derivatives` category is observable only as funding rate and next funding time, and that funding sitting
  at or below its baseline is a *permissive* condition (longs are not crowded) rather than *supporting*
  evidence for a direction. The selective reading: `derivatives` should not be counted as one of the two
  independent categories required for an entry unless funding is genuinely stretched — i.e. it may veto a
  direction but may not, on this host, be one of the two that authorise one.
- **Evidence (sample size: 1 host limitation, confirmed across all 5 contracts, 3 checks):**
  `/futures/data/openInterestHist` returns an empty response for every watchlist symbol on the demo host.
  Only the absolute snapshot at `/fapi/v1/openInterest` is available, and its magnitudes are unusable as a
  series (XRPUSDT reads 15,600,795,069,537.4). The open-interest *change* that the strategy lists as part
  of the `derivatives` category therefore cannot be observed here at all, leaving funding as the only
  input. This is a standing property of the environment, not a condition of one day.
- **Expected effect:** Closes a gap where a two-category entry could be assembled from `trend` plus a
  `derivatives` reading that is really just "nothing is obviously wrong". The 21:00 check on 2026-09-21
  reached the right answer by judgement — it declined to count funding at the 0.0100% baseline as support
  for the XRPUSDT long — but nothing in the rules required that, and a later check under more pressure
  could count it. Strictly more selective; cannot loosen anything.
- **Evidence amended 2026-09-22 (day 2):** the original wording ("returns an empty response") was wrong in detail
  and is corrected here rather than rewritten. As of the 2026-09-22 09:00 check, `/fapi/v1/openInterest` **does**
  return a point-in-time value (XRPUSDT 15,646,486,925,706.1 at 01:17Z), while `/futures/data/openInterestHist`
  returns the bare string `ok` with no history. The accurate statement is therefore **"no history", not "no
  endpoint"**: the absolute figure is readable but implausible enough to look like an artifact itself, and the
  *change* in open interest — the part that carries positioning information — remains unavailable. The conclusion
  is unchanged: on this host the `derivatives` category reduces to funding rate and next funding time alone.
- **Risk of being wrong:** Low, and the direction of the risk is fewer trades rather than worse ones. The
  cost is that a genuinely informative funding reading can no longer carry an entry on its own — but with
  half the category unobservable, that reading is not available in the form the strategy assumes anyway.
  Note this is a demo-environment limitation; a live venue publishes open-interest history, so the rule
  should be marked as host-specific and not carried forward if the experiment ever informs live trading.

**Amendment, 2026-09-23 (day 3) — the remaining half of the category is also unreliable, so `derivatives` reduces
to nothing usable rather than to "funding alone".** Two findings across nine XRPUSDT settlements. **(1) The rate
oscillates.** The settled history is +0.010000%, +0.010000%, −0.006889%, +0.010000%, −0.017407%, +0.010000%,
−0.009057% — **four sign alternations in seven settlements**. The 09-23 00:00 note had called the deepening
discount "the single most directional thing on the board"; the 02:00 and 09:00 checks retired that read against
their own prior preference, correctly. **(2) The demo's forward rate is wrong by a full sign.** At 09:00 the
predicted rate for the 08:00Z settlement read +0.006982% then +0.005892%, and the 16:00 check found it had
settled **−0.009057%** — a sign flip within two hours of settlement. A forward rate that cannot predict its own
settlement two hours out is not a forward read. The 16:00 and 20:00 checks both declined to claim `derivatives`
*even though it had turned to favour the trade under consideration*, on the stated grounds that a number read as
evidence whichever way it points is not evidence. That is the right handling and needs no rule, but it means the
category has now been unclaimable in every check of the experiment.

---

## P-005 — Distinguish a pending slot from a missed slot in `review_stats.py`

- **Date raised:** 2026-09-21 (day 1)
- **Status:** open — awaiting Edward's decision. Not applied.
- **What to change:** In `slot_coverage()` in `06-程序脚本-scripts/review_stats.py`, treat a slot whose
  scheduled time has passed but whose grace window (`late_start_grace_minutes`, currently 30) has not yet
  expired as **pending** rather than missed: report it in a separate `pending_slots` list and exclude it
  from both the numerator and the denominator of `coverage_percent`, so coverage is computed only over
  slots that have had their full chance to run.
- **Evidence (sample size: 1 review, structural and recurring):** `stats.json` generated at
  2026-09-21T22:01:31+08:00 reports `slots_due: 4`, `slots_decided: 2`, `coverage_percent: 50.0` and
  `missed_slots: ["2026-09-21_check_1600", "2026-09-21_check_2200"]`. The 22:00 slot came due sixty seconds
  earlier and was still inside its grace — and the 22:00 trading check may have been running concurrently
  with the review that read the file. Only `check_1600` is a genuine miss, so the true day-1 figure is 2 of
  3 (66.7%), not 50.0%. This is not a one-off: the daily review and a trading check share the 22:00 slot by
  design, so every daily review will count that day's 22:00 check as missed.
- **Expected effect:** Makes the coverage number P-002 introduced actually correct. Without this, the
  experiment's headline reliability figure carries a systematic downward bias of roughly one slot per day —
  about 30 of 240 planned checks over the experiment, or 12.5 percentage points of coverage — reported as
  scheduler failures that never happened. A measurement that is wrong in a known direction is worse than no
  measurement, because it looks like data.
- **Risk of being wrong:** Very low; it only changes how an already-recorded fact is classified, and it
  cannot affect any trading decision. The one thing to get right is that a slot must move from pending to
  missed once its grace expires, so a genuinely failed 22:00 check still shows up — in the next day's
  review rather than the same night's.

**Evidence amendment, 2026-09-23 — the bias was observed correcting itself inside a single review session, which
is as clean a demonstration as this proposal will ever get.** The first pass of the day-3 review regenerated
`stats.json` at 22:01:43 and read **15 of 20 slots (75.0%)** with `2026-09-23_check_2200` listed among the
missed. It judged by hand that the slot was pending rather than missed and published a corrected **78.9%**. The
22:00 decision then landed at 22:14, and the regeneration at 22:14:45 read **16 of 20 (80.0%)** with that slot
in the decided column and the four genuine misses — all on days 1 and 2 — unchanged. **The counter was wrong for
roughly fourteen minutes, in the direction this proposal predicts, and would have been read as a lost slot by
anyone seeing only the 22:01 figure.** Third consecutive review to apply the correction by hand; first to have it
confirmed within the session. Note also that the fix has a second beneficiary: the 23:00 slot is pending at every
review's runtime too, so the bias is structurally about one slot per day exactly as estimated.



**Evidence amendment, 2026-09-24 (day 4) — fourth consecutive review to make the same correction by hand.**
`stats.json` generated at 22:11:36 reports `slots_due: 28`, `slots_decided: 23`, `coverage_percent: 82.1` and
five missed slots. The fifth, `2026-09-24_check_2200`, **is not a miss**: its read-only observation ran at
14:04:22Z = 22:04 local and it is inside its 30-minute grace while the review is being written. The honest figure
is **23 of 27 expired slots (85.2%) with four genuine misses, all on days 1 and 2**. **The 22:00 decision then
landed at 22:18, inside the review's own session, and the regenerated `stats.json` reported 24 of 28 (85.7%) with
exactly those four misses — the correction confirmed, mid-review, for the second consecutive day.** Every review so far has had
to state a corrected coverage figure in prose next to the generated one, and on 09-23 and 09-24 the pending slot
resolved *inside the review's own session*. The headline consequence is that the generated number understates
coverage by roughly 3 percentage points every single day, in a metric P-002 exists to measure.

---

## P-006 — The 1.5 reward/risk floor and the structural-stop rule may be jointly unsatisfiable on this watchlist

- **Date raised:** 2026-09-22 (day 2)
- **Status:** open — awaiting Edward's decision. Not applied. **The review does not recommend lowering the
  floor and has no authority to do so; this is a measurement handed to Edward, not a request to relax a rule.**

**Update 2026-09-26 (Edward's decision):** resolved — option (b) adopted, plus measured targets. Stops and targets are now drawn from 4h structure; when no structural level is within reach, a measured target of 1.5–2x the stop distance is allowed provided the stop is on structure and outside noise. The 1.5 floor and all risk limits are unchanged.
- **What to change:** Nothing yet — this proposal asks Edward to look at a structural result and decide whether
  anything should change at all. The observation is that the 1.5 net reward/risk floor and the requirement that
  the stop sit on real structure are, at the volatilities these five contracts are currently showing, selecting
  *nothing* rather than selecting good setups from bad. If Edward wants the experiment to produce trades, the
  levers that would not weaken any rule are: (a) **narrow or change the watchlist** toward contracts whose
  typical structural distances are large relative to their bar noise; (b) **lengthen the decision timeframe**, so
  that stops and targets are derived from 4h/daily structure where levels sit further apart than hourly noise;
  or (c) **accept a very low trade count** and report the experiment as a study of a filter that rarely fires.
  Lowering the floor, widening what counts as a valid stop, or permitting targets past intervening structure are
  explicitly *not* on this list.
- **Evidence (sample size: 8 decisions over 2 days, 5 distinct constructions; 0 trades):** the same problem has
  appeared in three forms which are one problem.
  1. *The honest target is too close to pay.* At the 2026-09-22 09:00 check, on the two contracts with genuine
     directional structure, the nearest honest target paid **0.194** (SOLUSDT short to 117.59) and **0.515**
     (XRPUSDT short to 1.5041) net. The second support paid 0.884. Only a target at 1.4849 — beyond *both*
     1.5041 and 1.4973 — cleared the floor at 1.557, and was refused for jumping intervening support.
  2. *The paying target is unreachable without jumping structure.* The same refusal was made symmetrically on
     the long side at the 00:00 check, where the XRPUSDT long cleared the floor "only by reaching for 1.5441".
  3. *Confirmation costs more than the trade is worth.* The 02:00 check found a target 1.6% away against ~1.3%
     hourly ranges: by the time a setup is confirmed, the target has already been reached or lost. The 23:00
     check of 09-21 recorded the same shape — the 1.5270 target sat closer than one hourly range, so every
     structurally honest stop printed 0.70–1.50 net, with 1.50 reached only by a 0.0010 price drift.
  Supporting: across 8 decisions, every construction that cleared the floor did so either on a noise-width stop
  (XRPUSDT long 4.615 on a 0.060% stop; BNBUSDT passing long *and* short simultaneously), on a target past
  intervening structure, or on price drifting toward a fixed stop (XRPUSDT short 1.736 → 2.809). **Not one
  setup in two days cleared the floor on an honest stop and a reachable target at a stable quote.**
- **Expected effect:** Makes explicit something the daily records show but no single check can see: the filter
  may not be discriminating, it may simply be closed. If that is what is happening, the experiment's eventual
  result is a statement about the filter's design and not about the AI's judgement, and it should be reported
  that way. Edward may equally decide that a filter which rarely fires is exactly what he wants, in which case
  nothing changes and the finding stands as the result.
- **Risk of being wrong:** This is the proposal most at risk of being motivated reasoning, and it should be read
  with that in mind. Two days and eight decisions is a very small sample, taken almost entirely from one
  unusual market episode — a complex-wide 5–8% impulse on 09-21 followed by a squeeze — in which every contract
  was either at a 60-day high with nothing overhead or chopping inside a range narrower than its own noise. A
  normal week may produce qualifying setups without any change at all, and acting now would be tuning the rules
  to two days of an outlier. **The safe course is to leave everything as it is and re-examine this at the day-7
  weekly review**, when there will be roughly 50 decisions to judge it on. Raised now only because the pattern
  is consistent and specific enough to be worth watching deliberately rather than rediscovering later.

**Amendment, 2026-09-23 (day 3) — the sample doubled to 16 decisions, and the diagnosis sharpened in a way that
partly argues *against* this proposal.** Three additions.

**(1) The mechanism is now stated precisely enough to test.** The 09-23 00:00 check derived it as a geometric
requirement rather than a case-by-case rejection: a valid entry needs risk of at least N and reward of at least
1.5x risk, so the clean structural span from stop to *nearest* target must be at least ~2.5N + ~0.14% drag. It
then showed, by sweeping the entry price with the stop pinned, that **risk and ratio move in opposite directions
and never both pass** when the span is short — as the entry rises the stop becomes noise-safe and the ratio
collapses; as it falls the ratio passes and the stop goes sub-noise. That is now **L-004**, and it means the
"filter selects nothing" claim is falsifiable: count the checks where the available span exceeded 2.5N + drag.

**(2) The first real test of this proposal happened at 21:00 on 09-23, and it came back ambiguous in an
informative way.** For the first time two contracts (BNBUSDT and ETHUSDT) cleared the two-category evidence bar
cleanly, so the binding constraint moved off the evidence count for the first time in sixteen decisions. **They
still did not trade** — but they failed on stop placement, on a target sitting in a 2.65% structural vacuum, and
on the book going unquoted, which are three different constraints rather than one closed filter. This is the
distinction that matters for P-006: "the filter is closed" and "this watchlist at these volatilities rarely
offers 2.5N of clean span" predict different things over the next four days, and day 3 gave the first data point
that can separate them.

**(3) One of the three options listed above now has direct supporting evidence, and one has less.** Option (b),
lengthening the decision timeframe, is supported: every span failure in the window came from hourly and 5m
structure sitting closer together than the noise bar, while the 4h and daily frames that produced the clean trend
claims at 21:00 have levels much further apart. Option (a), narrowing the watchlist, is now partly moot for a
different reason — **BTCUSDT and SOLUSDT are both excluded on artifacts, so the watchlist is already five on
paper and three in practice**, and it narrowed itself without improving the span problem. The recommendation is
unchanged and is restated deliberately: **leave everything as it is and re-examine at the day-7 weekly review.**

**Update, 2026-09-23 22:00 check — the first test repeated, and the watchlist narrowed again.** The 21:00 result
above was not a one-off: at 22:00 BNBUSDT again held a claimable `trend` *and* `market_context`, XRPUSDT's second
category came within one contested field of firing, and **both were refused on geometry and execution** — a
sub-noise stop, a 2.53% structural vacuum on ETHUSDT, and an entry-side book that went unquoted on four of five
contracts. **Two consecutive checks have now failed for reasons other than the evidence count**, which is the
data point that separates "the filter is closed" from "this watchlist rarely offers 2.5N of clean span". The
sample is 17 decisions. Separately, the watchlist narrowed again and for the same reason: **XRPUSDT now carries
its own artifact**, so on the 22:00 evidence only ETHUSDT and BNBUSDT are cleanly readable — five on paper, two
in practice. That strengthens option (a)'s premise while further undermining its usefulness, since the watchlist
keeps narrowing by itself without the span problem improving. Recommendation still unchanged: re-examine at day 7.


**Evidence amendment, 2026-09-24 (day 4) — three of the narrowest misses in the experiment in one day, and the
review reads none of them as progress.** The span screen failed by **0.020pp** (00:00, BNBUSDT short: 1.158%
available against 1.178% required — the thinnest margin on record), **0.003pp** (09:00, BNBUSDT) and **0.077pp**
(21:00, ETHUSDT long). Taken at face value that looks like a floor on the edge of being satisfiable. **It is not,
and the qualification is the point of this amendment.** The 09:00 miss was measured against a requirement that had
**mechanically halved overnight** — BNB's N fell 0.403% → 0.159% over six silent hours as the setup-defining bars
aged out — and against the honest 8h15m window containing the box actually being traded the miss is **0.614pp, two
hundred times larger**. The 21:00 construction was independently dead on target validity (2670.98 touched once,
reached only by jumping three levels). The 00:00 construction had every 1.5-net target sitting in the vacuum below
the 09-19 daily low. **A near-miss against a rolled-forward window is not a near-miss**, and the honest reading of
day 4 is that the structure is no closer to paying than it was on day 2.

**And at 22:00 the same day the point stopped being an inference.** The 22:00 check priced **twelve**
constructions on ETHUSDT and laid the whole set out: **the four that pass the span screen pay 0.516
(SHORT 2693.42 → 2647.50), 0.786 (→ 2640.00), 0.908 (LONG 2639.90 → 2693.42) and 1.027 (→ 2633.31) — every
one below the 1.5 floor — while the single construction that clears the floor (SHORT 2669.40 → 2647.50 at
3.781) rests on a stop 0.26x N.** The two conditions do not overlap anywhere in the set. **This is the
strongest evidence this proposal has ever had**, because it is no longer "the screen keeps refusing
narrowly" but "the screen and the floor are disjoint on this structure, so no entry price can satisfy both."
It also closes off the reading that the day's near-misses were progress: passing a screen whose other side
you would then fail is not being close. Additional evidence of the same shape:
at **09:00 all four constructions priced — both directions on both then-readable contracts — failed at their
nearest structural target and passed only by jumping structure that had rejected within hours**, the first
four-for-four instance; at **21:00 all ten constructions failed**. Sample now 25 decisions over 4 days, 0 trades.

---

## P-007 — Host reliability: two stalls in two days, four slots lost, cause unidentified

- **Date raised:** 2026-09-22 (day 2)
- **Status:** open — awaiting Edward's decision. Not applied. Part of this one only Edward can do.
- **What to change:** Two parts.
  1. **Diagnosis, which needs Edward:** check whether the machine slept, or the Claude desktop app was closed,
     during 2026-09-22 roughly 01:16Z–14:00Z (09:16–22:00 MYT) and 2026-09-21 04:10Z–11:37Z. Scheduled tasks
     only run while the app is open, and `automation-status.json` still carries
     `scheduler_execution_verified: false`. Until the mechanism is known, nothing can be fixed — only observed.
  2. **Detection, which is a small code change:** have each run write a heartbeat (a timestamp file, or a line
     appended to a run log) when its observation completes, separate from the decision it eventually submits.
     A stall would then be visible as an observation with no decision behind it, at the time it happens,
     instead of being discovered hours later in review. This is measurement only and touches no trading path.
- **Evidence (sample size: 2 days, 2 stalls, 4 lost slots — and the trend is the wrong way):**
  - Day 1: `check_1200` observed at 04:10:09Z, decision submitted 11:37:20Z — a **7h27m** stall; the 16:00
    slot was lost.
  - Day 2: `check_0900` observed at 01:12:02Z and researched at 01:13:20Z, both on time; decision submitted at
    14:00:43Z — a **12h40m** stall, **778 minutes after the slot**; the 16:00, 20:00 and 21:00 slots were lost.
    The host clock was cross-checked against the exchange's `/fapi/v1/time` and agreed to within 0.1 second, so
    the stall is real and not a clock fault.
  - Cumulative slot coverage is **7 of 11 expired slots (63.6%)**, and day 2 was worse than day 1.
- **Expected effect:** The experiment's premise is a fixed cadence of checks. At 63.6% coverage, and with the
  losses clustered rather than random — three consecutive afternoon slots in one event — the 30-day result will
  describe an irregularly sampled strategy, not the one that was designed. Detection would at least make the
  gaps visible as they happen.
- **Risk of being wrong:** Very low; neither part can affect a trading decision. The thing worth being explicit
  about is what has *not* yet happened: **both stalls occurred while the account was flat, so the experiment has
  never yet carried unprotected risk.** That is luck, not design. With a position open, a 12h40m stall would
  have missed the 24-hour hold limit and every between-check reconciliation, leaving only the exchange-side stop
  and target standing — in an environment that produced six BTCUSDT artifact prints in the same two days. The
  cost so far has been observations; the cost of the next one may not be.

**Amendment, 2026-09-23 (day 3) — a third stall, and this time it hit the review task itself.**
The daily review session's first reads ran at 22:08 on 2026-09-22; its next tool call returned at **22:01 on
2026-09-23**, a gap of **23h53m**. Separately, `reviews/2026-09-22.md` and `PROPOSALS.md` carry mtimes of 22:04
and 22:05 on 09-22 — the day-2 review completed while this session was starting, so 09-22 also saw two review
invocations overlapping. No review was written for 09-23 before this one.

Three things follow. **(1) The trading checks recovered and the review did not.** Day 3 lost **zero** check slots
and ran eight consecutive on-time checks; cumulative coverage improved from 63.6% to 78.9%. The day-2 conclusion
that "coverage is getting worse, not better" is falsified — two days was too short a base to call a trend from.
**(2) A stalled review is silent, which makes it worse than a stalled check.** A stalled check leaves a missing
decision that `review_stats.py` counts and reports; a stalled review leaves no trace at all and would simply have
meant day 3 was never reviewed. **The heartbeat proposed in part 2 above should therefore cover the review task
as well as the trading checks** — it is the only one of the two whose failure is otherwise invisible.
**(3) The mechanism is still unidentified** after three occurrences, and part 1 still needs Edward.


**Evidence amendment, 2026-09-24 (day 4) — two clean days, and the cause is still unidentified.** Day 3 lost no
check slot; day 4 decided all seven of its expired slots on time; **seventeen consecutive on-time checks** since the
09:00 stall of 09-22; and the review task, which stalled **23h53m** on 09-23, ran on schedule today. That is the
best two-day run of the experiment and it is recorded as a fact, not a fix — **nothing was diagnosed or changed
between the stalls and the clean days**, so the honest reading is that the failure mode is intermittent and still
present. The proposal stays open on the cause, not on the count. The cheap thing worth confirming remains whether
the machine slept or the Claude desktop app was closed during the 09-22 09:00 stall and the 09-23 review stall,
since scheduled tasks only run while the app is open.

---

## P-008 — Re-derive running totals from the underlying files instead of inheriting them from the previous check

- **Date raised:** 2026-09-23 (day 3)
- **Status:** open — awaiting Edward's decision. Not applied.
- **What to change:** Where a decision file asserts a cumulative count across checks ("the Nth cap breach", "the
  Nth consecutive exclusion", "the Nth artifact print"), require the figure to be re-derived from the underlying
  decision and evidence files rather than carried forward from the previous check's prose. Cheapest version: have
  `review_stats.py` emit the handful of running counts the checks actually use, so there is one authoritative
  source. This is a process and tooling change only; it touches no trading path.
- **Evidence (sample size: 1 confirmed instance, caught on day 3):** the 2026-09-23 20:00 decision states
  "42.10 bps is the FOURTH cap breach of the experiment (after BTC 32.59 on 09-22, SOL 25.51 and XRP 35.90 at
  16:00)". The 16:00 decision file's own `spreads_bps` block records XRPUSDT at **11.18 bps** at the sweep and
  **6.21 bps** at the requote, and contains no 35.90 reading anywhere; its `cap_breach` field names SOLUSDT alone
  and calls it "only the second cap breach of the experiment". The 21:00 check then inherited the inflated total
  and called SOLUSDT 30.06 bps "the FIFTH". **The true count is four.** No decision turned on it — every one of
  these checks was a `no_trade` refused on other grounds — which is exactly why it survived two checks unnoticed.
- **Expected effect:** Prevents a small transcription error from compounding into a "finding". The escalating
  counts in these files (consecutive exclusions, consecutive checks a lesson was decisive, cap breaches) are
  doing real evidential work in the reviews and in `LESSONS.md`, and a count that drifts upward through
  inheritance is indistinguishable from a real trend until someone opens the source file.
- **Risk of being wrong:** Very low. The only cost is a little duplicated arithmetic per check. The thing to get
  right is that the fix must be *re-derivation*, not a second prose summary to inherit from.

**Evidence amendment, 2026-09-23 22:00 check — the behaviour this proposal asks for, performed voluntarily
twice in one check.** The 22:00 check recorded **two findings against its own predecessor's**, in both cases by
going back to the underlying numbers rather than inheriting the prose: (1) the SOLUSDT 30.06 bps cap breach
reported at 21:00 was **transient, not a monotonic deterioration** — spread came back to 10.301 → 0.859 → 0.860
bps, so SOLUSDT is excluded on its artifact and not on its spread; and (2) the 21:00 observation that BTCUSDT
held the only stable book of the five was **directly reversed**, BTC having the worst book of the five an hour
later with both sides gone on the third sample. Neither correction was forced by anything; both came from
re-deriving. This is what the proposal wants to make routine rather than admirable.


**Evidence amendment, 2026-09-24 (day 4) — a second, independent instance, so this is no longer one confirmed
case.** The 09-24 20:00 decision's headline claim is that this was the "FIRST CHECK OF THE
EXPERIMENT AT WHICH THE EVIDENCE GATE IS MET". **It is false.** The gate had already been met twice on 09-23: at 22:00, where the day-3 review
records BNBUSDT holding "a claimable `trend` *and* `market_context`", and at 23:00, where the decision file lists
**three** arguable independent categories and states in terms that "THE EVIDENCE GATE IS NOT WHAT REFUSED THIS
CHECK". The 21:00 check then **inherited** the claim ("the evidence gate, which passed for the first time ever at
20:00"), exactly as the 21:00 check of 09-23 inherited the inflated cap-breach count. No decision turned on it —
both checks were correctly refused on other grounds — which is precisely why it survived two checks unnoticed, for
the second day running. A related figure in the same window could not be re-derived at all: the XRPUSDT 37.281 bps
breach at 09-24 00:00 is the **fifth** genuine cap breach only if this proposal's own re-derived count of four
through day 3 is taken on trust, which is the position the proposal exists to end. **Two independent instances in
two days, in a file set where escalating counts are doing real evidential work in `LESSONS.md`.**

---

## P-009 — Add a top-of-book notional floor to the pre-trade checks, sampled at least three times

- **Date raised:** 2026-09-23 (day 3)
- **Status:** open — awaiting Edward's decision. Not applied. **This is a rule and code change and is Edward's
  alone.** `LESSONS.md` L-005 makes the AI refuse such books in the meantime, but only the rule can make the
  engine refuse them.
- **What to change:** Add a liquidity check alongside the existing 25 bps spread cap in `paper-config.json` and
  the pre-trade path: sample top-of-book notional on **both sides at least three times** during a check, and
  reject the entry if either side falls below some multiple of the maximum order notional (2,500 USDT) at **any**
  sample — not on average. The binding side is the one the position must cross: a short sells into the bid, and a
  long must *exit* into the bid, so the bid is binding for both in this strategy. The multiple is Edward's to set;
  the evidence below suggests that even 1x would have refused several of these books outright.
- **Evidence (sample size: 16 decisions, 5 consecutive checks, 4 of 5 contracts affected each time):**
  - **The spread cap is blind to this.** ETHUSDT quoted **0.15 bps — the tightest spread of the entire experiment
    — on a 16 USDT ask**, with its bid at 82 USDT. BTCUSDT quoted **0.30 bps on a 995 USDT ask** (0.0115 BTC),
    against a 2,500 USDT maximum order. BNBUSDT quoted **0.38 bps on an 0.01 BNB touch worth about 7.88 USDT**.
    A tight spread on an unquoted book is not a measurement of anything, and every one of these readings passed
    the cap comfortably.
  - **The collapses are large, fast and two-way.** XRPUSDT's bid notional went 22,146,602 → **5 USDT** over 317
    seconds while its ask held at 29.2M. BNBUSDT's bid went 36,721,037 → **9,669** → 20,187,299 USDT inside 217
    seconds — a 3,798x collapse and full recovery, at which print a maximum-size market order would have consumed
    roughly a quarter of the entire visible bid. ETHUSDT's bid went 245,634 → **111** → **217** USDT, unquoted on
    two consecutive samples.
  - **It is not contract-specific and cannot be screened by reputation.** BNBUSDT was the *only* contract to
    improve across the 20:00 requote and produced the worst collapse of the experiment one check later.
  - **It has already been decisive.** At 16:00 the book became a reason to refuse for the first time; at 20:00 the
    collapse landed on the **entry** side of the intended short rather than the exit side; at 21:00 both
    two-category candidates had their entry side go effectively unquoted mid-check.
- **Expected effect:** Two things the current rules cannot do. It would refuse entries the spread cap waves
  through — and, more importantly, it bears directly on **whether a resting reduce-only stop can be trusted at
  all on this host.** The experiment's risk model assumes an exchange-side stop stands between an open position
  and the market between checks. On a book that oscillates to 5 USDT at the touch within minutes, that stop
  cannot be assumed to fill near its trigger, and the engine's own quote at fill time would be one more sample
  landing on either state at random. **This is the first proposal that bears on risk rather than on selectivity**,
  and it becomes material the moment the experiment opens its first position.
- **Risk of being wrong:** Moderate, in one direction worth naming. A notional floor set too high would close a
  filter that is already selecting nothing (see P-006), and this review has no way to tell how much of the
  instability is a demo-host artifact that a live book would not show. Two mitigations: the threshold is a number
  Edward picks rather than one this review asserts, and the *measurement* is worth adding regardless of where the
  threshold sits — recording three book samples per check costs nothing and would let the day-7 review say
  whether the oscillation is constant, clustered, or tied to particular hours. If Edward wants only one half of
  this, take the measurement and leave the rejection rule out.

**Evidence amendment, 2026-09-23 22:00 check — the strongest instance yet, and it completes the set.** Across
three samples taken inside 170 seconds, **not one of the five contracts held a quoted entry-side book**, except
ETHUSDT, which was refused on geometry. BNBUSDT's bid went 8,606,494 → **1,148** → 2,782,512 USDT, a **7,497x
collapse and full recovery in 124 seconds**, at which print a maximum 2,500 USDT market sell is more than twice
the entire visible bid. XRPUSDT's bid went to **55 USDT**. BTCUSDT went unquoted on **both sides at once** — bid
129 → 11,592,501 → 94 and ask 2,463,791 → 600 → 94 USDT — having been recorded one hour earlier as the only
contract with a stable book. All five contracts are now affected, so there is no clean subset of the watchlist to
which a weaker rule could be confined.


**Evidence amendment, 2026-09-24 (day 4) — the cap fired once in eight checks, and the one time it fired the
quantity problem was present too.** Across 09-23 23:00 → 09-24 22:00 the 25 bps cap breached **once**: XRPUSDT at
**37.281 bps** (09-24 00:00, sample 1) — on a contract already excluded on artifact grounds, and **on the same
print where its bid was worth ~6 USDT**. At every other check in the window the widest spread of the entire check
was 9–11.3 bps, while the book did this: BNBUSDT's ask, the side a long entry must cross, printed **7.67 USDT**,
326x smaller than a single maximum order (02:00); BNBUSDT failed on **both sides at once** (09:00); ETHUSDT's
crossed side fell to **40.3 USDT — a 70,517x collapse in 73 seconds, the largest on record — after four
consecutive healthy samples** (16:00); and at 21:00 ETHUSDT went unquoted on **two consecutive** sweeps (148.73
then 39.84 USDT), **the first adjacent pair recorded**, where every earlier instance had a full recovery between
them, while BTCUSDT was unquoted on both sides and SOLUSDT lost both sides at one sweep. Recorded against
interest: the engine's own sixth quote at 21:00 read a healthy ~764,000 USDT ETH bid — which is exactly why a
single healthy sample cannot be the test. **At 22:00 the worst print of all: BNBUSDT's bid at 38.99 USDT — 64x
smaller than a single maximum order — after 10,034,016 USDT three sweeps earlier, a 257,000x swing inside one
check, quoting 0.769 bps**, alongside XRPUSDT unquoted on two consecutive sweeps (a fourth consecutive check with
an XRP bid collapse) and BTCUSDT's ask at 58.92 USDT one check after being unquoted on both sides. Widest spread
that check: 11.308 bps. **Sample now 25 decisions, 16 consecutive checks in which the book was material and the
cap was not.**

---

## P-010 — Flag measurement-window transitions, so a check can see when a number moved because a bar left the window

- **Date raised:** 2026-09-23 (day 3, after the 22:00 check)
- **Status:** open — awaiting Edward's decision. Not applied. This is a tooling change and therefore Edward's.
  `LESSONS.md` L-006 makes the AI perform this check by hand in the meantime.
- **What to change:** Where a check reports a rolling-window figure — the noise floor N, 24h relative
  performance, 24h high/low, or the artifact scan over the last 30 bars — have the tooling record **what entered
  and left the window since the previous check**, and flag the case where a reported threshold crossing coincides
  with the departure of the extreme bar that was driving the figure. Cheapest version: `review_stats.py` (or a
  small helper the checks call) emits, per contract per check, the timestamp and range of the largest bar in the
  current window and whether it differs from the previous check's. This is measurement and reporting only; it
  touches no trading path and imposes no new rejection rule.
- **Evidence (sample size: 3 instances across 2 consecutive checks, 17 decisions):**
  - **Both headline "developments" of the 22:00 check were window artifacts, and one of them fired a condition
    the experiment had spent two checks waiting for.** BNBUSDT's noise floor fell from 0.800% to **0.224%**
    purely because the 12:00Z bar that created the setup aged out of the twelve-bar window, making an unchanged
    stop on unchanged structure read 1.76x N instead of 0.49x N. XRPUSDT's 24h relative figure crossed from
    +0.886% to **−0.139%** partly because the excluded 1.6855 artifact decayed out of the 24h comparison — and
    that crossing was precisely the falsifiable condition the 20:00 note had set as the gate for claiming
    `market_context` on an XRP short.
  - **BTCUSDT's artifact scan read clean at 09:00 and 16:00, dirty at 20:00 and cleanest-ever at 22:00**, as
    prints aged in and out of the 30-bar window, while the contamination that actually matters — the 09-21 prints
    in the 4h and daily frames — never moved.
  - **The 21:00 check predicted its successor's trap to two thousandths of a percent** (0.222% forecast, 0.224%
    measured) and told it not to let the passage of time manufacture a pass. That prediction worked, and it is
    the reason this proposal is about automation rather than about discipline: the discipline is already there,
    and it currently depends on one check having the foresight to warn the next one in prose.
- **Expected effect:** Makes a specific and recurring false signal visible at the moment it occurs rather than
  reconstructible afterwards. The three instances above were all caught by hand, but each required the check to
  reconstruct the previous window from raw klines, and two were caught only because the preceding note happened
  to flag the risk explicitly. **A check with no such warning would have had nothing to compare against.** This
  is also the class of error most likely to produce a trade rather than prevent one, because a window rolling
  forward tends to *loosen* a measured constraint: N shrinks when the big bar leaves, a 24h extreme softens when
  the spike leaves, an exclusion looks stale when the prints leave.
- **Risk of being wrong:** Low. It adds reporting, not a rule, and cannot itself refuse a trade. The one thing to
  get right is that the flag must stay **descriptive** — "the largest bar in this window changed since the last
  check" — and must not become an automatic veto, since a window legitimately rolls forward all the time and most
  transitions are harmless. The judgement stays with the check, and with L-006.

**Evidence amendment, 2026-09-24 (day 4) — the transition is now demonstrably forecastable, which strengthens the
case for automating it rather than weakening it.** Two more instances. **(1)** At 09:00 BNBUSDT's noise floor fell
**0.403% → 0.159%, a 2.5x collapse with nothing printing**, as the 17:15Z reclaim bar and every other bar of
consequence aged out of the preceding hour over six silent overnight hours; the required span **mechanically
halved**, 1.148% → 0.538%, and the best candidate failed even the halved bar by 0.003pp — by **0.614pp** against
the honest window. This one was **not forecast**, and the check had to reconstruct the previous window from raw
klines by hand. **(2)** At 21:00 ETHUSDT's N collapsed to **0.205%** exactly as the 20:00 note had forecast in
writing ("toward ~0.20%"), the 0.551% 09:30Z bar having left both the 1h and 2h windows — the **second** forecast
in two days confirmed to within 0.005pp, after 0.222% forecast / 0.224% measured on 09-23. The reviews have now
promoted that practice to `LESSONS.md` **L-007** (name in advance which window will roll and which number it will
flatter). **That makes the proposal more worth doing, not less**: the discipline works, and it currently depends
entirely on one check having the foresight to warn the next one in prose — the unforecast instance was the largest
of the three. **(3)** At 22:00 the forecast was **conditional** and both halves fired: the 21:00 note wrote that N
would keep collapsing **unless a new impulse bar printed on the breakout, in which case that bar would become the
setup-defining bar**, and a 0.468% bar duly printed at 13:35Z, so N held at **0.468%** instead of falling to the
~0.19% a quiet stretch would have delivered. A conditional forecast is the stronger artefact, because it tells the
successor which of two quite different measurements to make before it looks at either — and it is exactly the kind
of branch that is cheap for tooling to evaluate and expensive for prose to carry. Recorded against interest: at
21:00 one crossing **survived** re-measurement (ETH's 24h fields did not move, so the 2650.63 break was a genuine
market event) — so the flag would not be a veto, which is the design constraint this proposal already states.
Sample now 25 decisions, 6 instances across 4 checks, 3 forecasts made and 3 confirmed.

---

## P-011 — The watchlist is now entirely excluded under L-001, and only Edward can decide what happens next

- **Date raised:** 2026-09-24 (day 4)
- **Status:** open — awaiting Edward's decision. Not applied. **The review has no authority to widen a watchlist,
  relax an exclusion or change a frame, and explicitly does not recommend doing any of those in order to
  manufacture activity.**

**Update 2026-09-26 (Edward's decision):** resolved — option (d) adopted (see P-003 amendment). L-001 is retired; all five contracts are tradable again from 2026-09-26. LESSONS.md was reset and capped, and the review may now retire its own lessons.
- **What to change:** Nothing yet — this proposal hands Edward a structural result and asks him to choose. As of
  the 2026-09-24 review **all five watchlist contracts carry unrevised demo artifacts on the 4h or daily frames**
  and are therefore excluded under `LESSONS.md` L-001. The experiment cannot produce a trade under its own rules
  until a print ages out of the higher frames or something changes. The options, none of which the review may
  take:
  (a) **Accept it** and let days 5–30 measure the host rather than the strategy — which is a genuine empirical
  result and arguably the most honest one;
  (b) **widen or change the watchlist** toward contracts whose demo series are cleaner (this overlaps P-006's
  option (a), which was raised for a different reason and points the same way);
  (c) **draw price structure from a non-demo data source** while keeping the demo host for execution only, so
  that levels, artifact scans and noise floors are measured on real prints;
  (d) **change the artifact rule itself** — e.g. bound how long a print contaminates a higher frame, or require
  a wick/body threshold rather than a range multiple on 4h and daily bars.
- **Evidence (sample size: 25 decisions over 4 days, 0 trades; 5 of 5 contracts excluded):** the tradable set
  went **5 → 2 → 1 → 0** over four days, entirely on data-quality grounds, and **not one contract has been
  excluded for anything the market did**.
  - **BTCUSDT** — 22 consecutive checks. 95,804.10 in the 09-21 08:00Z and 12:00Z 4h bars (13.546% upper wick =
    17.29x the median 4h range) and the 09-21 daily bar (11.437% on a 6.629% body), plus five more prints.
  - **SOLUSDT** — 12 checks. 106.67 at 09-22 19:00Z: a 9.654% lower wick on a 0.017% body, **~570x**, no other
    contract showing anything at that candle; 28.8x on the daily; 24h quote volume ~250x below the other four.
  - **XRPUSDT** — 1.6855 at 09-23 04:00Z: clean at 1h (2.2x), **33.9x at 4h**, 7.030% on a 0.197% daily body.
  - **BNBUSDT** — new on day 4. 780.90 at 09-24 02:45Z: 5.9x wick/body at 5m, ~7x frame median, fully retraced
    inside its own bar, **16.0x on the 00:00Z 4h bar**, unrevised.
  - **ETHUSDT** — caught by this review. 2850.00 in the 09-21 08:00Z 4h bar (7.221% range = **5.74x** the 4h
    median) and the 09-21 daily bar, previously ruled "aged out" against the **1h** window before the amendment
    requiring the 4h and daily frames existed. **The counter-argument is recorded in full and is real**: ETH's
    wick/body ratio is only 2.0x, an order of magnitude below every other caught print; it flags on range alone;
    it sits 7.5% above the market; it contaminates no field any current level is drawn from; and ETH's only
    recent 5m flag cleared cross-contract. It is excluded anyway, because ruling the other way would be a
    loosening made on four days of data and zero trades in order to keep a contract tradable. **If Edward
    disagrees with that one ruling, ETHUSDT alone reopens** — the 2850.00 print leaves a 30-bar 4h window at
    2026-09-26 08:00Z in any case, and the 09-21 daily bar persists far longer.
  - **A second artifact signature appeared at 22:00 and it has no wick at all.** ETHUSDT's 13:35Z bar made the
    2671.94 breakout high while no other contract moved (BTC 1.18x its median, BNB 0.89x, SOL 1.33x, XRP 1.07x),
    against neighbouring candles where all five moved together. Its wick/body ratio is **1.1x** — clean on the
    signature that caught the other four. The **isolation** test fired and the wick test did not, so 2671.94 is
    barred from anchoring any stop or target while the move itself is treated as real. If Edward revisits the
    artifact rule under option (d), this is the case that shows the rule needs both tests, not one.
- **Expected effect:** Makes explicit a state the daily checks would otherwise keep reporting one contract at a
  time. It also separates two conclusions that four days of `no_trade` decisions currently confound: *the
  strategy finds nothing worth trading* and *the data will not support a decision either way*. The second is now
  the operative one, and it is a result about the host.
- **Risk of being wrong:** The ETHUSDT ruling is the load-bearing judgement and it is the weakest of the five —
  it rests on a range multiple rather than the wick/body signature that caught the other four, and on a print
  three days old and 7.5% away from the market. If that ruling is wrong, the correct state is "one readable
  contract", not "none", and roughly 26 days of the experiment turn on it. That is precisely why it is here
  rather than being decided by a check. The opposite risk is larger and less recoverable: a review that relaxed
  an exclusion because the alternative was an empty set would have destroyed the only thing this experiment has
  actually measured.
- **Day-5 update (2026-09-25): the empty set is not temporary. It outlasts the experiment.** Every exclusion
  sits in a **daily** bar: BTC and ETH on 09-21, SOL on 09-22, XRP on 09-23, BNB on 09-24. L-001's re-test
  condition names the daily field and its scan uses a 30-bar window, so the earliest of those bars leaves on
  **2026-10-21**, the day after the last planned trading date. The day-4 text above said "until a print ages out
  of the higher frames". **That will not happen inside the experiment.** ETH's 4h print leaving its window at
  2026-09-26 08:00Z does not change this, and `LESSONS.md` now says so explicitly so that no check misreads it
  as a release. The ETH daily-half citation, questioned by three checks, was reproduced by two more (2.40x and
  2.53x the daily median) and stands. Sample: 33 decisions over 5 days, 0 trades. **Unless Edward picks (b),
  (c) or (d), days 6–30 can only measure the host.** Option (a) is still a legitimate choice, but it should be
  a choice rather than a default. The review still recommends none of the loosening options for the sake of
  activity.

---

## P-012 — Don't make a fresh demo symbol read a precondition for recording a `no_trade`

- **Date raised:** 2026-09-25 (day 5)
- **Status:** open — awaiting Edward's decision. Not applied. This is a code change and is Edward's.
- **What to change:** In the engine's decision path, either accept `symbol: null` on a `no_trade` decision, or
  skip the fresh demo rules/quote/orders read for `no_trade`. That read is only needed when an order might be
  sent. `no_trade` places nothing and should not be able to fail on market-data plumbing.
- **Evidence (sample size: 1 rejection in 33 decisions):** at 2026-09-25 02:00 the first submission carried
  `symbol: null`. The engine rejected it with "Fresh demo read verification failed": rules, quote and orders
  all returned HTTP 400, Binance −1121 (invalid symbol). The check resubmitted with only the symbol field set to
  `ETHUSDT`, the contract it had analysed. Every later check has supplied a symbol "because the engine rejects
  symbol: null". No decision was changed or loosened.
- **Expected effect:** Removes one way a check can lose its slot. A late-running check (P-002, P-007) that hits
  this rejection may not have time to resubmit inside its grace. It also stops `symbol` on a `no_trade` record
  from implying a contract was being traded.
- **Risk of being wrong:** Low. If the engine uses the fresh read on `no_trade` for something else, such as
  confirming the account is flat, that check should stay and only the symbol-specific part should be skipped.
  One instance is thin evidence; the argument is mainly that `no_trade` should be the hardest decision to fail.
