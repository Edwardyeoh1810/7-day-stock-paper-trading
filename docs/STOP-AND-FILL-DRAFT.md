# Stop and Fill Rules v0.1

Status: ACTIVE FOR LOCAL PAPER TRADING ONLY. Scope: a local paper experiment in ordinary US stocks/ETFs through Binance Stocks data. Excludes bStocks, leverage, options and crypto.

## Active Parameters

Regular US sessions only, using America/New_York exchange calendars. One position at a time, with notional capped at 10% of initial experiment capital. Require two independent evidence categories, a structural stop and an exit plan before entry. Consider targets offering at least 1.5 times net risk. Reassess after 30 minutes; exit if follow-through is absent and the thesis weakens. Begin removing risk 45 minutes before the actual close and reconcile exits 15 minutes before close, including early-close adjustments. No overnight positions in v0.1.

Proposed observation interval with a paper position: 5 seconds. Suspend new entries after 15 seconds without a successful sample. These are initial experiment parameters, not proven optimal settings. The continuous monitor is not implemented or enabled.

## Risk and Size

For a long position, entry E > stop S > 0. Use Decimal throughout:

```text
quantity * (E - S) + round-trip fees + slippage reserve <= initial capital * 0.005
quantity * E <= initial capital * 0.10
buy notional + buy fee <= available paper cash
```

Round quantity down to the stock's stepSize, then validate minQty, minNotional, fractionable and tradability. Reject if the rounded quantity fails a limit. Use verified applicable fees, never assume zero fees.

## Paper Fills

Buy at the first valid ask observed after the decision; sell at the bid, including slippage and fees. Do not backfill decisions using earlier prices. Available quoted size must cover the simulated fill; otherwise wait or record only a supportable partial fill. A limit-price touch alone does not establish a fill or queue priority.

Trigger a long stop when bid <= stop; exit at the next observed executable bid with slippage. Gaps can exceed planned loss. Reconstruct missing intervals only with trustworthy trades/bars. If a bar touches both stop and target with unknown sequence, assume stop first and label the assumption. Without interval data, mark the result incomplete; a recovery-price exit must not be presented as a stop filled during the gap.

Record price P&L, platform fees, conversion costs, other fees and net P&L separately, with source and receipt times. The documented Stocks quote example lacks an exchange quote timestamp. Receipt time alone does not prove freshness; verify regular-session data freshness before using it for entries.

## Daily Stop

Stop new entries after two consecutive stopped trades, or when max(0, -daily realized net P&L) plus remaining open exit risk reaches 2% of initial capital. Include unpaid exit costs without double-counting paid fees. Pause entries on unreliable quotes, account state or order state; reconcile existing exposure first. No averaging down or increasing limits to recover losses.

## Capital and Execution Boundary

Keep 10000 USDT initial paper capital, 1000 USDT maximum position and 50 USDT maximum planned single-trade risk. When actual minimum order size or fees make these infeasible, record no trade. Synthetic offline test fixtures may exercise fills but must not count as live-data performance.

The documented Stocks order types are MARKET and LIMIT; Spot STOP_LOSS/OCO support must not be assumed. Polling is not broker-held protection. This implementation sends no live orders and accepts no account agreements. Any future ordinary-equity order implementation must set tokenize=false and distinguish acknowledgement from actual fills and cancellation.

Review items: regular sessions, one position, 30-minute reassessment, 1.5-times net-risk target, 5-second samples and no trade when fee-adjusted risk is infeasible.

Sources, checked 2026-09-14: [Market data](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/market-data), [Orders](https://developers.binance.com/en/docs/catalog/advanced-trading-stocks-trading/api/rest-api/trade), [Fees](https://www.binance.com/en/support/faq/detail/a7469c7703524024b5bc2d492b03639d).
