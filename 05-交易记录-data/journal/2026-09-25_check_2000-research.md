# 2026-09-25 check 20:00 research note (12:00Z)

The run started on time: it began at 20:03 local and the decision was made before 20:10. The account is flat, so there was nothing to reconcile.

## What the 16:00 note asked for, and what happened

- **ETH 08:00Z 4h bar (closed 12:00Z):** O2671.44 H2740.42 L2671.18 **C2715.90**. It did **not** close below 2667.22,
  so the short `trend` case the 16:00 note set up **never started**. Instead the bar broke through the
  2699.39/2699.53 ceiling, which had rejected four times, and closed 16 points above it with a 2.6% range on a 1.66% body.
  The 12:00Z bar is open at about 2720.
- **Is the move real? L-001 isolation test:** yes. All five contracts moved up together in the 08:00Z–11:00Z hours
  (1h closes: BTC +0.45/+0.24/+0.13, SOL +0.82/+0.91/+0.68/+1.40, XRP +0.48/+0.77/+0.26/+2.26, BNB smaller). The
  wick/body ratio is clean. This is a broad risk-on move, not an isolated print.
- **L-007 forecast:** the 16:00 note said N(1h) would stay at or above about 0.25%. **Confirmed, and more than that:**
  N(1h) is **0.755%** against a 0.118% 5m median. So a long stop would need to be at least 0.755% away, and the
  required span is about 2.03%. The next check's window will still contain the breakout bars, so N stays high.
  Forecast for 21:00: when the 11:00Z bar (1.05% 1h range) leaves the 1h window, N(1h) will fall. The binding N
  stays at the setup-defining 08:00Z–11:00Z impulse bars (about 0.75%). Do not let a quiet 12:00Z hour flatter N.
- **volume:** the last hour of 5m quote volume is 1.49x the 100-bar median. That is elevated but not a clear expansion.
- **derivatives:** ETH funding is +0.0036%, off the +0.0100% bound for the first time in several checks. OI is
  11,915,866,145, which is +0.07% against 16:00 and flat. The breakout did not come with OI build.
- **market_context:** broad crypto strength across all five contracts. This is a same-direction observation, not a
  rolling-window figure.

## Decision inputs

- **L-001:** the standing exclusion of all five contracts still binds, and only the daily review may change it. That
  alone means `no_trade`. A breakout is not a reason to reinterpret the exclusion.
- **L-005 (three sweeps, 20 s apart):** ETH ask **27 USDT** at sweep 0, which leaves the long-entry side unquoted.
  BNB ask 570 USDT and bid 1,163 USDT. SOL bid 140 / 1,069 USDT and ask 1,055 USDT. BTC bid 7,149 USDT at sweep 2.
  Only XRP held both sides, and XRP is excluded. The spread cap never fired: the widest was SOL at 11.58 bps.
- **L-004 (long-side view, for the record only):** after a 2.6% impulse, the nearest structure above 2740.42 is
  not established in this window. A target beyond the fresh high sits in a structural vacuum. No construction was priced.
- **L-003/L-002:** there was no ratio to requote and no stop was chosen.
- **L-006:** no 24h figure is claimed.

**Decision:** `no_trade`. The tradable set is empty under L-001. Independently, the ETH long-entry side was unquoted
at sweep 0 (L-005).

## For the 21:00 check (13:00Z)

1. **L-001 still binds.** Return `no_trade` unless the review has changed it.
2. **ETH levels:** the old ceiling 2699.39/2699.53 is now the first support to watch as a retest. The breakout high
   is 2740.42, and the old swing low is 2667.22. 2671.94 is still not usable as a level.
3. **Binding N:** about 0.75% (08:00Z–11:00Z impulse). A shrinking N(1h) is window arithmetic (L-006/L-007).
4. **Funding** settles at 16:00Z (00:00 local). ETH is off the bound at +0.0036%.
5. **L-005:** take at least three samples. ETH's ask was unquoted at this check.

## Lessons applied

L-001 (standing exclusion; breakout checked for isolation and found broad), L-004 (target vacuum above 2740.42),
L-005 (three sweeps), L-006 (no 24h claims), L-007 (the 16:00 forecast was confirmed; a new forecast is written).
L-002 and L-003 were not reached. No lesson was loosened. Nothing under `reviews/` and no script, config, watchlist,
schedule or switch was touched.
