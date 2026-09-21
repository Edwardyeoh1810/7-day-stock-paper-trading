# 30 Day Conservative Crypto Futures Paper Trading Strategy

## Purpose

Run a controlled 30 day experiment to test whether AI-assisted research can manage a small, explainable futures paper portfolio, long or short, using market structure, price action, volume, derivatives data and news. The goal is process quality, traceability, risk discipline and learning through review, not proof of profitability. A profitable month on this sample size is not evidence of a profitable system.

## Capital And Mode

- Starting capital: 5000 USDT of virtual funds on the Binance demo futures account.
- Execution: paper trading only. Orders go to the demo futures account through `06-程序脚本-scripts/paper_engine.py` and nowhere else.
- Live trading: disabled. Nothing in this strategy authorizes a real-money order, a transfer or an account-setting change.
- Accounting: futures style. Cash is the wallet balance; only fees leave it at entry, and profit or loss, fees and funding settle when the position closes.

## Paper Trading Autonomy

Within the demo account only, the AI may independently decide to open a long, open a short, hold, close, or stay flat. The user does not need to approve each paper trade. Every decision must still satisfy this strategy, `AGENTS.md`, readiness, evidence, sizing, stop and daily loss rules, and the current `05-交易记录-data/reviews/LESSONS.md`.

## Tradable Instruments

Only USDT-margined perpetual contracts on the watchlist in `05-交易记录-data/current-state.json`:

- BTCUSDT, ETHUSDT, BNBUSDT, SOLUSDT, XRPUSDT

One position at a time, long or short. These five contracts move together most of the time: they are five ways to express one view on the crypto market, not five independent opportunities. Prefer the contract where the evidence is clearest and the spread tightest.

## Prohibited

- Spot, options, coin-margined or delivery futures
- Cross margin, or any leverage other than the configured 5x isolated
- Contracts outside the watchlist, low-liquidity contracts
- Adding to a position, averaging down, hedging with a second position
- Placing, cancelling or amending exchange orders by hand; changing leverage or margin mode by hand
- Any real-money order under any circumstances

## Leverage And Margin

Leverage is fixed at 5x isolated by `04-运行状态-state/paper-config.json`; the engine sets it before every entry. Leverage does not change the risk of a trade: the loss is set by the stop distance and the position size, and the engine sizes the position so that the planned loss stays inside the risk budget. Leverage only changes how much margin the position ties up and where liquidation would sit. With 5x isolated, liquidation is roughly 18-19% from the entry, and stops further than 10% from the entry are rejected, so the stop always comes first.

## Evidence Categories

Use these category names in every decision file, exactly as written, so the review statistics stay comparable:

- `trend` — direction and structure on a higher timeframe (4h, daily): higher highs and lows, or lower; position relative to major moving averages.
- `price_action` — behaviour at a specific level: break and retest of a range, rejection at support or resistance, failed breakout.
- `volume` — participation compared with recent average: expansion on the move, drying up on the pullback.
- `derivatives` — funding rate, open interest and its change, long/short positioning, liquidation clusters.
- `market_context` — what BTC and the wider market are doing, relative strength of the contract against BTC, correlation with risk assets.
- `news` — a verifiable scheduled event, macro release, regulatory or exchange announcement, with a source link. Never a single social post or rumour.

Two items of the same category count as one category. Evidence must be independent: a moving average and a trend line drawn over the same candles are one observation, not two.

## Demo Price Artifacts

The demo exchange is a simulation and sometimes prints prices the real market never traded, for example a single candle with a wick of many percent that none of the other four contracts shows. This is a defect of the demo environment, not market structure, and this rule should not be carried into any live use.

- Before using a high or low as a level, compare the same candle across the watchlist. An isolated extreme that the other contracts do not show, or a wick several times the size of the candle's body and of neighbouring candles, is an artifact: exclude it from support, resistance, range and 24 hour high/low figures, and never anchor a stop or target to it.
- Record every artifact you exclude in the evidence file, with the contract, candle time and price.
- If recent artifacts make a contract's structure unreadable, record `no_trade` for that contract.
- An artifact can still trigger a resting stop or target, because the exchange acts on its own prices. Nothing in the rules can prevent that; the daily review identifies such exits and reports results with and without them.

## Entry Conditions

An entry may be considered only when all of these hold:

- `04-运行状态-state/readiness.json` allows paper trading and does not allow live trading, and the demo account was verified in this run.
- No position is open, and the contract is on the watchlist.
- At least two independent evidence categories support the same direction. For a short the bar is the same as for a long: shorting is not a reaction to a red candle.
- The stop is placed where the thesis is wrong, on price structure (beyond the level that defines the setup), and is within 10% of the entry. Do not choose a stop to fit a desired position size.
- The target is a level the market can plausibly reach within the 24 hour holding limit, and the net reward/risk after fees is at least 1.5.
- The spread is normal and the move is not so fast that a controlled stop cannot be defined.
- Funding has been checked: note the current rate and the next funding time, and whether the position would pay or receive.
- The reasons not to take the trade have been considered and recorded.
- Every applicable lesson in `LESSONS.md` has been applied and named in the thesis.

Do not enter on a single headline, a single indicator, an unverified quote, or because the last trade lost. When in doubt, record `no_trade`: staying flat is a valid and common outcome.

## Exits

A position ends in one of these ways:

- **Stop or target on the exchange.** Right after the entry fills, the engine places a reduce-only stop and a reduce-only take-profit on the demo exchange, triggered by the mark price. They work between checks; the next check books the result from the real fill.
- **Thesis invalid.** At any check, close with reason `thesis_invalid` when the evidence that justified the entry is gone, even if the stop has not been reached.
- **Time.** The engine closes a position at the first check after it has been held for 24 hours.
- **End of experiment.** At the final check of the last planned date, close with reason `end_of_day`.
- **Protection failure.** If the exit orders cannot be placed, the engine closes the position at market immediately.

Stops and targets are not moved after entry. If the thesis changes, close the position.

## Position Sizing And Loss Limits

All limits are percentages of the 5000 USDT starting capital and are enforced by the engine, which chooses the size; the AI never sets the quantity.

- Maximum planned loss per trade: 0.5% = 25 USDT, including estimated fees and slippage.
- Maximum position notional: 50% = 2500 USDT.
- Maximum daily loss: 2% = 100 USDT of realized loss per local day; once reached, no new entries that day.
- Two consecutive stop-outs on the same local day block new entries for the rest of that day.
- Net reward/risk at least 1.5; spread at most 25 basis points; stop at most 10% from the entry.
- An entry must be submitted within 45 minutes of its scheduled check. A run that stalled or overran never enters; it may still manage or close an open position.

A stop that triggers sells or buys at market, so in a fast move the realized loss can exceed the planned loss. If the risk budget makes a position impractically small, do not trade.

## Holding Period And Funding

Positions may be held across midnight, up to 24 hours. Perpetual contracts pay or receive funding every eight hours; the engine books the funding of each trade when it closes. A high funding rate against the position is a cost and a crowding signal worth recording; it is not by itself a reason to trade the other way.

## Must Stop Trading

Record `no_trade` and open nothing when:

- `readiness.json` is missing, malformed or unsafe, or live trading appears enabled.
- The demo account, orders, position or market data cannot be verified or reconciled, or the ledger and the exchange disagree.
- The daily loss limit is reached, or two consecutive stops occurred today.
- News or market conditions are chaotic, contradictory or impossible to verify.
- A scheduled check was missed while a position was open and the state has not been reconciled yet.
- The engine rejected a decision. Record the reason; do not retry with loosened parameters.

## Evidence Requirements

For every entry, exit and no-trade decision, save:

- Timestamp and check id
- Contract and direction
- Current price, spread and source
- The evidence items with their category, source and what they showed
- Funding rate and next funding time
- Entry, stop and target levels and why the stop sits where it does
- The engine's result: size, fill, fees, planned loss, or the rejection reason
- Which lessons applied
- Final decision and reason

## Review

The daily review (`03-定时任务-routines/REVIEW-PROMPT.md`) measures results with `06-程序脚本-scripts/review_stats.py`, judges decisions by what was knowable at the time, and maintains `LESSONS.md`. Lessons can only make decisions more selective. Changes to this strategy, the limits, the leverage, the watchlist, the schedule or the code are proposed in `05-交易记录-data/reviews/PROPOSALS.md` and take effect only when the user approves them.
