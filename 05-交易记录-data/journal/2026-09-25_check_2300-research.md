# 2026-09-25 check 23:00 research note (15:00Z)

The run started on time at 23:03 local, and the engine ran at 15:05:44Z (23:05 local, 5 minutes after the slot, not late). The account was flat, so there was nothing to reconcile. LESSONS.md was read fresh after the 22:00 review (7 lessons, updated 2026-09-25 22:3x).

## What the 22:00 note asked for, and what happened

- **ETH structure:** the decline extended. The 14:00Z 1h bar reads O2693.81 H2696.07 **L2677.40** C2694.47: a new low below 2685.30, set on the 14:00Z 5m bar (0.520% range), then fully recovered into the close. The 15:00Z bar is quiet so far (2692.10-2695.31). Levels: 2740.42 high, 2699-2701.8 resistance, **2677.40 new low**, 2667.22 swing low, and 2671.94 still unusable (L-001 isolation clause).
- **L-007 forecast check:** the 22:00 note forecast that N(1h) would fall below 0.55% if 14:00Z stayed quiet, and that a new low printed on a large bar would make that bar the binding one. **The conditional branch fired.** A new low printed on the 14:00Z 5m bar, so N(1h) = **0.520%** (14:00Z), N(2h) = 0.554% (13:50Z), and N(3h) = **1.128%** (12:20Z, still inside the window as forecast). The bar that defines the current low is 14:00Z (0.520%). The 1.128% bar still binds for any construction referencing the 12:00Z 2688.28 retest. Forecast: **confirmed** (the tightening branch, as with most of the day-5 record).
- **derivatives:** lastFundingRate is +0.0100% on BTC, ETH, SOL and XRP, and 0 on BNB. It settles 16:00Z (00:00 local). This is recorded but not claimed.

## L-001 full scan (5m/1h/4h/1d, 30 bars each)

A coarse automatic screen was used (rm >= 3x and w/b >= 2, or w/b >= 4 and rm >= 1.5x and wick > 0.3%). Per amendment 5, **a print it fails to reproduce is still a contaminated field.**
- **BTCUSDT:** 4h still flags 95,804.1 (09-21 08:00Z and 12:00Z), 91,000.0 and 90,389.8. The daily screen flagged nothing, but the 09-21 daily bar still carries H95,804.1. Excluded.
- **ETHUSDT:** 2850.00 was **not reproduced** by this screen at 4h or daily. It remains a contaminated field (the re-test condition names the daily field, which does not clear before 2026-10-21). 1h flags on 11:00Z (w/b 8.1) and 12:00Z (w/b 22.6) are the real 2740.42 rejection and the 2688.28 retest, and they move with the other contracts. Excluded.
- **BNBUSDT:** 780.90 still flags at 4h (09-24 00:00Z, w/b 16.0), and 786.18 at 1h. New: a 5m bar at 14:10Z reads w/b 117 on a tiny body (rm 2.01x, 0.31% wick). It is near the threshold and broad selling was in progress, so it is recorded only. Excluded.
- **SOLUSDT:** 106.67 flags at 4h (w/b 14.0) and daily (09-22, w/b 28.8). Excluded.
- **XRPUSDT:** 1.6855 flags at 4h (09-23 04:00Z, w/b 33.9). The daily screen flagged nothing, but the 09-23 daily bar still carries it. Excluded.

**The tradable set is empty.** No contract advanced a re-test clock at this check.

## L-005 (three sweeps, 20 s apart, ~15:04:34Z-15:05:14Z)

- BTC bid 7.94M -> **50** -> **554** USDT. Ask 67.8k -> 2,435 -> 1,654.
- ETH bid 333.6k -> 2.21M -> **19,972**. Ask 3.31M / 339k / 547k. The engine's own quote at 15:05:44Z showed an ask of 0.614 ETH (about 1,653 USDT).
- BNB held on both sides (bid 2.0-7.1M, ask 147k-4.06M).
- SOL bid **385 / 86k / 257**, ask **368 / 501** / 581k. Spread 19.10 / 14.96 / **32.37 bps**, over the cap at sweep 3.
- XRP bid **68 / 18** / 567k. Spread 17.65 / 21.43 / 22.70 bps.
Only BNB held a usable book on both sides throughout, and it is excluded.

## Decision

`no_trade` (the engine accepted it). No order was proposed or sent. L-002 and L-003 were not reached: no stop was chosen and no ratio was priced.

## For the 00:00 check (16:00Z)

1. **L-001 still binds.** ETH 2850.00 leaves the 4h window around 2026-09-26 08:00Z, but that does **not** release ETHUSDT (standing note).
2. **L-007 forecast:** the 12:20Z 1.128% bar leaves the 3h window at about 15:20Z, and the 13:50Z 0.554% bar leaves the 2h window at about 15:50Z. By 16:00Z, **if 15:xxZ stays quiet, N(1h), N(2h) and N(3h) will all fall to at most about 0.52%, with N(1h) possibly near 0.2%.** That is window arithmetic. The binding N is the bar that set the latest low: 14:00Z (0.520%), or a newer impulse bar if one prints. Funding settles at 16:00Z, so a funding-time bar may print and become binding.
3. **ETH levels:** 2740.42; 2699-2701.8 resistance; 2677.40 low; 2667.22 swing low; 2671.94 unusable.
4. **L-005:** take at least three samples. BTC, SOL and XRP each lost a side to under 600 USDT this check.

## Lessons applied

L-001 (full scan run; standing exclusion of all five), L-004 (not reached, because L-001 decides; binding N stated first), L-005 (three sweeps; BTC/SOL/XRP thin, SOL over the cap), L-006 (the N(1h) change is a new bar plus window arithmetic, not a relaxation), and L-007 (the 22:00 conditional forecast confirmed; a new forecast is written above). L-002 and L-003 were not reached. No lesson was loosened. Nothing under `reviews/` and no script, config, watchlist, schedule or switch was touched.
