# Proposals for Edward

Rule, limit, watchlist, schedule or code changes the reviews suggest. Nothing here takes effect until Edward
approves it and the change is made by him or at his request. Format per proposal: date, what to change, the
evidence (with sample size), the expected effect, the risk of being wrong, status (open / approved / rejected).

---

## P-001 — Bound the age of the evidence behind a decision, not just the quote

- **Date raised:** 2026-09-21 (day 1)
- **Status:** open
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
- **Status:** open
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
- **Status:** open
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

