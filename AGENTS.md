# AI Trading Experiment Operating Rules

This project is a 30 day crypto futures research and paper trading experiment on the Binance demo futures account (virtual funds).
It was forked from a stock/ETF experiment and keeps its risk limits and record keeping; the schedule is 24-hour: six checks a day, every four hours in Asia/Kuala_Lumpur time, on thirty consecutive calendar days, with a daily review that feeds lessons back into later decisions.
It is not a live trading system and must not be described as a profitable system.

## Safety Defaults

- Default mode is paper trading only. "Paper" means the Binance demo futures account at `demo-fapi.binance.com`; no script may send an order to any other host.
- Live trading is disabled unless the user explicitly authorizes a specific live order in chat.
- Never place a real-money order without human confirmation.
- If any readiness check is missing, false, stale, or ambiguous, do not place orders.
- If market conditions are unclear, choose observation over trading.
- Risk control has priority over returns.

## Platform Scope

- Target platform: Binance demo USDT-perpetual futures account, contracts on the approved watchlist in `05-交易记录-data/current-state.json` only, long or short, one position at a time.
- Leverage is fixed at 5x isolated by `04-运行状态-state/paper-config.json`; the engine sets it before every entry. Leverage only changes the margin a position ties up: the loss per trade stays capped by the stop and the sizing rule.
- The demo account holds virtual funds. `BINANCE_ENV` in the local key file must be `demo`; a production key must never be used with this project.
- The local paper ledger remains the record of fills, cash and risk; with `demo_order_execution_enabled: true` its fills are the actual demo-account fills.
- Binance API keys must stay local in the root `09-API密钥-仅本地/binance-api.env`; never ask the user to paste keys in chat. The read-only checker reads only this file. Share `09-API密钥-仅本地/binance-api.env.example`, never the completed credential file.

## Permitted Work

- Read strategy, schedules, state, journal, and evidence.
- Perform read-only account, position, order, and market-data checks when credentials are locally available.
- Produce watchlists, risk notes, and paper trade records.
- In paper trading only, autonomously decide whether to buy, sell, reduce, stop out, flatten, hold, or stay in cash according to the strategy and risk limits.
- Autonomous paper execution requires `autonomous_paper_execution_enabled: true` in readiness and runs only through `06-程序脚本-scripts/paper_engine.py`, which sends MARKET orders to the demo futures account only and records them in the local ledger.
- Record no-trade decisions with evidence and reasons.

## Prohibited Work

- No live orders without explicit user confirmation.
- No Spot, options, coin-margined or delivery futures, cross margin, leverage other than the configured 5x isolated, low-liquidity contracts, or any contract outside the approved watchlist. No real-money futures under any circumstances.
- No orders based on a single news item or a single indicator.
- No full-account or heavy-position trades.
- No credential leakage into journal, evidence files, logs, or chat.
- Paper trading autonomy does not authorize live trading, live order submission, transfers, account setting changes, or enabling trading permissions.

## Required Startup Reads

Every scheduled run must read these files before taking action:

- `AGENTS.md`
- `AGENTS.zh-CN.md`
- `02-项目文档-docs/TRADING-STRATEGY.md`
- `02-项目文档-docs/TRADING-STRATEGY.zh-CN.md`
- `03-定时任务-routines/schedule.json`
- `03-定时任务-routines/schedule.zh-CN.json`
- `03-定时任务-routines/CONTINUITY.md`
- `03-定时任务-routines/CONTINUITY.zh-CN.md`
- `04-运行状态-state/readiness.json`
- `05-交易记录-data/current-state.json`
- Latest file in `05-交易记录-data/journal/`, if present
- `05-交易记录-data/reviews/LESSONS.md`

## Required End-of-Run Writes

Every scheduled run must update:

- `05-交易记录-data/current-state.json`
- The current trading day's journal file in `05-交易记录-data/journal/`
- Evidence notes in `05-交易记录-data/evidence/`

Each journal entry must state:

- What was done
- Why it was done
- Whether an order was proposed
- Whether an order was placed
- Whether an order filled
- Current holdings
- Current cash
- Current risk
- Next task focus
- Human confirmations needed

## Binance Runtime

- With `BINANCE_ENV=demo` the checker reads USDT-perpetual `/fapi/` endpoints on the demo futures host. `02-项目文档-docs/BINANCE-API.md` still describes the original Stocks setup; where it conflicts with this file or the trading strategy, they win.
- `06-程序脚本-scripts/run_observation.py` is read-only. The only POST path is `06-程序脚本-scripts/demo_orders.py`, which is hard-wired to the demo host and refuses to run unless `BINANCE_ENV=demo`.
- The approved paper rules enforce one position, 50% maximum notional, 0.5% maximum planned loss, 2% maximum daily loss, a stop no further than 10% from the entry, an entry decision no older than 45 minutes after its scheduled check, two evidence categories, 1.5 net reward/risk, and a 24-hour maximum hold. Right after an entry fills, the engine places a reduce-only stop and take-profit trigger order on the demo exchange (mark-price triggered), so the stop works between checks; an entry whose exit orders are rejected is closed immediately. Never place, cancel or amend these orders by hand.
- Every open position must be closed at the final check of the last planned date.

## Review And Improvement

- The daily review follows `03-定时任务-routines/REVIEW-PROMPT.md`: statistics from `06-程序脚本-scripts/review_stats.py`, a written review, and an updated `05-交易记录-data/reviews/LESSONS.md`.
- Every trading check reads `LESSONS.md` and applies it. A lesson may make a decision more selective; it can never loosen or override a rule or risk limit.
- Changes to rules, limits, leverage, watchlist, schedule or code are only proposed in `05-交易记录-data/reviews/PROPOSALS.md`. Only the user approves and applies them.
- Preserve both languages. Dates in the schedule are provisional until authentication and review pass; do not count setup days as experiment sessions.
