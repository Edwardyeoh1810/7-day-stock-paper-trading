# AI Trading Experiment Operating Rules

This project is a 7 trading day crypto Spot research and paper trading experiment on the Binance demo account (virtual funds).
It was forked from a stock/ETF experiment; the schedule, risk rules and record keeping are unchanged.
It is not a live trading system and must not be described as a profitable system.

## Safety Defaults

- Default mode is paper trading only. "Paper" means the Binance demo account at `demo-api.binance.com`; no script may send an order to any other host.
- Live trading is disabled unless the user explicitly authorizes a specific live order in chat.
- Never place a real-money order without human confirmation.
- If any readiness check is missing, false, stale, or ambiguous, do not place orders.
- If market conditions are unclear, choose observation over trading.
- Risk control has priority over returns.

## Platform Scope

- Target platform: Binance demo Spot account, USDT pairs on the approved watchlist in `05-交易记录-data/current-state.json` only.
- The demo account holds virtual funds. `BINANCE_ENV` in the local key file must be `demo`; a production key must never be used with this project.
- The local paper ledger remains the record of fills, cash and risk; with `demo_order_execution_enabled: true` its fills are the actual demo-account fills.
- Binance API keys must stay local in the root `09-API密钥-仅本地/binance-api.env`; never ask the user to paste keys in chat. The read-only checker reads only this file. Share `09-API密钥-仅本地/binance-api.env.example`, never the completed credential file.

## Permitted Work

- Read strategy, schedules, state, journal, and evidence.
- Perform read-only account, position, order, and market-data checks when credentials are locally available.
- Produce watchlists, risk notes, and paper trade records.
- In paper trading only, autonomously decide whether to buy, sell, reduce, stop out, flatten, hold, or stay in cash according to the strategy and risk limits.
- Autonomous paper execution requires `autonomous_paper_execution_enabled: true` in readiness and runs only through `06-程序脚本-scripts/paper_engine.py`, which sends MARKET orders to the demo account only and records them in the local ledger.
- Record no-trade decisions with evidence and reasons.

## Prohibited Work

- No live orders without explicit user confirmation.
- No options, futures, margin, leveraged products or tokens, crypto perpetuals, low-liquidity pairs, or any pair outside the approved watchlist.
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

- With `BINANCE_ENV=demo` the checker reads Spot `/api/v3/` endpoints on the demo host. `02-项目文档-docs/BINANCE-API.md` and the strategy documents still describe the original Stocks setup; where they conflict with this file, this file wins.
- `06-程序脚本-scripts/run_observation.py` is read-only. The only POST path is `06-程序脚本-scripts/demo_orders.py`, which is hard-wired to the demo host and refuses to run unless `BINANCE_ENV=demo`.
- The approved paper rules enforce one position, 10% maximum notional, 0.5% maximum planned loss, two evidence categories, 1.5 net reward/risk, no new entry after 11:30 Central, and no overnight position.
- Preserve both languages. Dates in the schedule are provisional until authentication and review pass; do not count setup days as experiment sessions.
