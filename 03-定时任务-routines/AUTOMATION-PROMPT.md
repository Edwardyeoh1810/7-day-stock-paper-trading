# Automation Description and Saved Prompt

This is the checked-in prompt for the local Claude scheduled tasks. See [automation-status.json](automation-status.json) for the current deployment status.

## Active Schedule

Project directory: `/Users/edwardmacmini/Projects/7-day-stock-paper-trading`. Crypto trades around the clock, so there are six Asia/Kuala_Lumpur checks a day, every four hours: 00:00, 04:00, 08:00, 12:00, 16:00 and 20:00, on thirty consecutive calendar days. Dates are in [schedule.json](schedule.json) and its [Chinese companion](schedule.zh-CN.json): 180 occurrences and a 30-minute late-start tolerance. One local Claude scheduled task (`paper-trading-4h-check`) fires at those times in the host's local time, which is the schedule's timezone. GitHub-hosted runners are blocked by Binance HTTP 451, so all runs are local.

## Saved Prompt

Perform all project operations only in the project directory. Read both languages of AGENTS, strategy, schedule and CONTINUITY, plus readiness, current-state, the latest journal and `05-交易记录-data/reviews/LESSONS.md`. Apply the lessons: they may make you more selective, never less, and they never override a rule. State in the decision's thesis which lessons applied. Do not edit anything under `reviews/`; the 22:00 review task owns it (see [REVIEW-PROMPT.md](REVIEW-PROMPT.md)). The strategy documents were written for stocks; apply their evidence, risk and no-trade discipline to the USDT-perpetual futures watchlist, long or short, and where they conflict with `AGENTS.md`, `AGENTS.md` wins.

Run `python3 -B 06-程序脚本-scripts/run_observation.py --dry-run` first. If `due_slot` is null (outside the planned sessions or slot tolerance), finish quietly and change nothing. For a due slot, run `python3 -B 06-程序脚本-scripts/run_observation.py`. Stop on duplicate_skipped or another_run_active. Reconcile interrupted read-only runs using `--recover` before continuing.

Research the slot's topic with official calendars, news and verifiable market data for the watchlist pairs only. Save research in separate journal/evidence files using the same run_id with a `-research` suffix, and update next-task focus. Do not edit generated API journals.

After research, independently decide whether to open, manage, close, or record no trade. The user authorized autonomous paper decisions on the Binance demo futures account (virtual funds) only, at the configured 5x isolated leverage. Never submit a production Binance order, transfer, or account-setting change, never change `BINANCE_ENV`, readiness safety switches, risk limits, the watchlist or any script, and never call the order API except through `paper_engine.py`.

For every decision, create a non-secret JSON file under `05-交易记录-data/decisions/` with `paper_trading_only: true`, an `action` of `open_long`, `open_short`, `manage`, `close`, or `no_trade`, and for an entry the `symbol`, `thesis`, `stop_price`, `target_price` (for a short the stop is above and the target below the entry; the stop may be at most 10% from the entry) and an `evidence` list of at least two categories (each item with `category` and `source`). Then run `python3 -B 06-程序脚本-scripts/paper_engine.py --decision <file> --run-id <date_slot>_paper`; the `_paper` suffix prevents overwriting the read-only runner's evidence file. The engine refreshes the demo readiness check, rejects stale or unsafe state, resets the daily loss counter on a new local day, sizes the order from the risk limits (at most 50% of capital in notional and 0.5% of capital at risk), sets 5x isolated leverage, sends one MARKET order to the demo futures account, records the actual fill in the local ledger and immediately places a reduce-only stop and take-profit trigger order on the demo exchange. Funding paid or received while a position is open is booked when it closes. If the engine rejects a decision, record the reason and do not retry with loosened parameters.

Whenever a position is open, submit a `manage` decision (or `close` with a `reason` of `thesis_invalid` or `manual_exit`) at every check: the engine first books any stop or target the exchange triggered since the last check (status `exchange_exit_reconciled`), and closes a position that has been held for 24 hours. A new entry is allowed at any check when no position is open. At the 20:00 check of the last planned date, submit `close` with reason `end_of_day` for any open position and confirm the account is flat. Never place, cancel or amend exchange orders yourself.

Keep 5000 USDT paper capital, the configured leverage and existing limits; record no trade when fees, liquidity, data quality, or evidence make trading infeasible. Stops and targets rest on the demo exchange between checks; a triggered stop sells at market, so the realised loss can differ slightly from the planned loss. Read credentials locally through the scripts; never display, print or copy them.

Stay quiet for unchanged or non-actionable state. Report on scheduled runs, meaningful changes, completion, failure or required user action. After the last planned date's 20:00 check, do nothing on later runs; the final review is written by the review task.

## Verification Boundary

All 180 times and bilingual schedules are checked offline by the test suite. The demo readiness check, market snapshots for all five pairs, validate-only test orders, a no-trade engine pass, and live demo futures round trips (market entry, exit trigger orders placed, status, a triggered stop, cancel, reduce-only market exit) were verified on 2026-09-21. Scheduled tasks only run while the Claude desktop app is open; every run must compare the actual host time with the intended slot and must never backfill a historical trade.
