# Review Process and Saved Prompt

The review is how the experiment improves. It runs once a day at 22:00 Asia/Kuala_Lumpur as its own scheduled task (`paper-trading-daily-review`), between the 20:00 and 00:00 trading checks. It never trades.

## Saved Prompt

Work only in the project directory. Never run `paper_engine.py`, `paper_trade.py` or any order or account call; never edit scripts, tests, `readiness.json`, `paper-config.json`, `current-state.json`, the ledger, the schedule, or the key file. The review only writes inside `05-交易记录-data/reviews/`.

1. Run `python3 -B 06-程序脚本-scripts/review_stats.py`. It rebuilds `reviews/stats.json` from the ledger: closed trades, win rate, average R (result divided by the loss planned at entry), drawdown, fees, funding, and the same figures by symbol, side, exit reason and evidence category. Use these numbers; do not recompute them by hand.
2. Read today's journal, decision and evidence files, `reviews/LESSONS.md`, `reviews/PROPOSALS.md` and the previous daily review.
3. Write `reviews/YYYY-MM-DD.md` (local date) with these sections:
   - **Numbers** — today and experiment-to-date, from `stats.json`.
   - **Decisions reviewed** — for every entry, exit and no-trade today: was the evidence real and independent, was the stop placed on price structure, did the trade follow the thesis, and what happened next. Judge the decision by what was knowable at the time, not by the outcome.
   - **Process errors** — rule violations, engine rejections, missed or failed checks, stale data, sloppy evidence. These matter more than P&L.
   - **What worked / what did not** — each point tied to specific trades.
   - **Hypotheses** — patterns worth watching, each with its sample size.
4. Update `reviews/LESSONS.md`: at most 10 lessons, each with its evidence and sample size, the most useful first. Add a lesson only when at least 3 trades or 5 decisions support it; remove lessons the data no longer supports. A lesson may make future decisions more selective (skip a setup, demand an extra evidence category, avoid a time of day); it may never loosen a rule or a risk limit. With fewer than 30 closed trades, phrase lessons as hypotheses.
5. If the evidence suggests a rule, limit, watchlist, schedule or code change, append it to `reviews/PROPOSALS.md` for Edward. Never apply it.
6. On experiment days 7, 14, 21 and 28 also write `reviews/weekly-N.md`: the week's numbers against earlier weeks, which lessons were followed and whether following them helped, which proposals are still open, and an honest statement of whether any edge is visible yet or the results are indistinguishable from chance. After the last planned date write `reviews/final.md` in the same form for the whole experiment.
7. Finish with a short report to Edward: today's numbers, the one or two most important findings, any new lesson, and any new proposal awaiting his decision.

## Boundaries

The review changes how carefully the AI decides, not what it is allowed to do. Risk limits, leverage, watchlist, schedule and code change only when Edward approves a proposal. A small sample proves nothing: a profitable week is not evidence of a profitable system, and the review must say so.
