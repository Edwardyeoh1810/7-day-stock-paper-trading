# 2026-09-26 check 00:00 research note (16:00Z)

The run started on time at 00:03 local. The engine ran at 16:05:29Z (00:05 local, 5 minutes after the slot, not late). The account was flat, so there was nothing to reconcile. This note builds on the 23:00 note.

## What the 23:00 note asked for, and what happened

- **ETH structure:** the decline extended again. The 15:00Z 1h bar reads O2694.58 H2695.56 **L2669.67** C2685.10: a new low below 2677.40 that stopped 2.45 above the 2667.22 swing low. The 16:00Z bar opens quiet (2685.07-2690.15). 3h range: 2669.67-2717.75. Levels: 2740.42 high; 2699-2701.8 resistance; **2669.67 new low**; 2667.22 swing low; 2671.94 unusable (L-001 isolation clause; the new low sits between the two).
- **L-007 forecast check:** the 23:00 note forecast that N would fall to at most about 0.52% if 15:xxZ stayed quiet, and that a new impulse bar would bind if one printed. **The conditional branch fired again.** 15:00Z made a new low, so the bar that set 2669.67 binds, not the rolled window. Forecast: **confirmed on the conditional branch.**
- **derivatives:** lastFundingRate is +0.0100% on BTC, ETH, SOL and XRP, and about 0.0003% on BNB. It settles at 16:00Z. This is recorded but not claimed.

## L-001 full scan (5m/1h/4h/1d, 30 bars, same coarse screen as 23:00)

- **BTCUSDT:** 4h still flags 95,804.1 (09-21 08:00Z and 12:00Z), 91,000.0 and 90,389.8. The daily field still carries 09-21. Excluded.
- **ETHUSDT:** **the 4h scan reads clean at this check.** 2850.00 was not reproduced. The standing note says this does **not** release ETHUSDT, because the daily field still carries it. The 1h flags (11:00Z 2740.42 and 12:00Z 2688.28) are the real rejection and the real retest, as recorded before. Excluded.
- **BNBUSDT:** 780.90 flags at 4h (w/b 16.0), and 786.18 at 1h. The 14:10Z 5m bar (w/b 117) is still recorded only. Excluded.
- **SOLUSDT:** 106.67 flags at 4h (w/b 14.0) and daily (w/b 28.8). Excluded.
- **XRPUSDT:** 1.6855 flags at 4h (w/b 33.9). Excluded.

**The tradable set is empty.** No re-test clock advanced.

## L-005 (three sweeps, 20 s apart, ~16:04Z)

- BTC: bid about 34M, ask 3.1-3.4M; spread 1.25 bps. Held.
- ETH: bid 0.83-1.09M, ask 1.67-2.35M; spread 0.86-1.34 bps. Held.
- BNB: held on both sides (ask about 1.0-1.76M).
- SOL: ask **6,836 / 1,902 / 12,437** USDT; spread 4.15 / 0.83 / 7.48 bps. The ask is thin.
- XRP: bid 12.2M, 10.6M, then **53k**. The spread widened from 7.59 to 10.76 bps.
The books are much healthier than at 23:00, but SOL and XRP still thinned within 40 seconds.

## Decision

`no_trade` (the engine accepted it). No order was proposed or sent. L-002, L-003 and L-004 were not reached.

## For the 02:00 check (18:00Z)

1. **L-001 still binds.** ETH's 4h window reads clean, but that does not release ETHUSDT (standing note).
2. **L-007 forecast:** the 15:00Z bar that made 2669.67 stays inside the 3h window until about 18:00Z, so at 02:00 it may be about to leave. If 16:xx-17:xxZ are quiet, **N(1h) and N(2h) will read lower than the binding N**. That is window arithmetic. The binding N is still the bar that set the latest low.
3. **ETH levels:** 2740.42; 2699-2701.8 resistance; 2669.67 low; 2667.22 swing low; 2671.94 unusable. A break of 2667.22 would complete the lower-low sequence through the swing low.
4. **L-005:** take at least three samples. SOL's ask and XRP's bid thinned this check.

## Lessons applied

L-001 (full scan; standing exclusion of all five), L-005 (three sweeps), L-006 (a falling N is window arithmetic), and L-007 (the 23:00 forecast was confirmed on the conditional branch; a new forecast is written above). L-002, L-003 and L-004 were not reached. No lesson was loosened. Nothing under `reviews/` was touched, and no script, config, watchlist, schedule or switch was changed.
