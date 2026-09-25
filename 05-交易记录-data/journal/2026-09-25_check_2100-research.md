# 2026-09-25 check 21:00 research note (13:00Z)

The run started on time at 21:03 local. The account is flat, so there was nothing to reconcile.

## What the 20:00 note asked for, and what happened

- **ETH retest of the old ceiling:** the 12:00Z 1h bar reads O2715.91 H2721.75 **L2688.28** C2717.13. It
  undercut the 2699.39/2699.53 support by about 11 points, then closed back at the top of its range. This is a
  retest that was wicked through and reclaimed; it is not a clean hold. The 12:00Z 4h bar is open at about 2712.
  The levels are unchanged: 2740.42 high, 2699.39/2699.53 contested support, 2667.22 swing low, 2671.94 unusable.
- **Was the move isolated? (L-001):** no. All five contracts made the same 12:00Z dip and recovery (BTC L83995.6,
  BNB L775.34, SOL L118.69, XRP L1.5835), so the move is real. It does not change the standing exclusion.
- **L-007 forecast check:** the 20:00 note forecast that N(1h) would **fall** once the 11:00Z bar left the window,
  and that the binding N would stay at about 0.75%. **The first half was wrong, and it was wrong in the direction
  that tightens the constraint.** The 12:00Z retest bar was itself an impulse: ETH N(1h) is now **1.128%** (N(3h)
  1.128%) against a 0.124% 5m median, up from 0.755%. The binding N is now 1.128%, so a valid construction would
  need a span of about 2.96% (2.5N + 0.14%). That is wider than the whole 2688.28–2740.42 range (1.94%). No
  construction is possible on ETH at this check, whatever the exclusion says.
- **volume:** the ETH move came with the 12:00Z retest. No expansion is claimed.
- **derivatives:** ETH funding is +0.0068% (it was +0.0036% at 20:00). OI is 11,918,311,012, which is +0.02% and flat.
  The breakout and retest are not coming with position build.
- **market_context:** 24h change BTC +0.99%, ETH +2.33%, BNB +0.66%, SOL +5.82%, XRP +8.20%. Broad risk-on.
  Per L-006, the 24h figures are recorded but not claimed.

## Decision inputs

- **L-001:** the standing exclusion of all five contracts binds. That alone means `no_trade`.
- **L-004:** the ETH required span (~2.96%) is larger than the available structure (1.94%), so no ratio was priced.
- **L-005 (three sweeps, 22 s apart, 13:04:12Z to 13:04:56Z):** ETH was unquoted on **both** sides at sweep 0 and
  sweep 2: bid 22 / ask 475,269, then bid 301 / ask 271, then **bid 22 / ask 14 USDT**. BTC's ask was 101 USDT
  at sweep 0 and its bid 169 at sweep 1. BNB's ask was 156 USDT at sweep 2. XRP's bid was 32 USDT at sweep 0,
  and **XRP's spread was 54.38 bps at sweep 0, over the 25 bps cap**. SOL never exceeded 131k on any side. No
  contract held a usable book on both sides across all three samples.
- **L-002/L-003:** no stop was chosen and there was no ratio to requote.
- **L-006:** the ETH N rise is a market event and not window arithmetic, because the bar that caused it is
  inside every window. It tightens the constraint.

**Decision:** `no_trade`. The tradable set is empty under L-001. Independently, L-004 fails on ETH, and L-005 fails
on every contract.

## For the 22:00 check (14:00Z)

1. **L-001 still binds.** Return `no_trade` unless the 22:00 review has changed it. The review may run at the
   same time as the check, so read LESSONS.md fresh.
2. **L-007 forecast:** the 12:00Z retest bar (ETH 5m range up to 1.128%) stays inside the 1h window until about
   13:55Z and inside the 3h window until about 15:55Z. At 22:00, N(1h) will **fall** as that bar leaves.
   The binding N should stay at about 1.1% (the 12:00Z retest bar, which defines the 2688.28 low any long stop
   would sit under) unless a new impulse prints, in which case that new bar binds. A quiet 13:00Z hour flattering
   N(1h) is window arithmetic.
3. **ETH levels:** 2740.42 is the high. 2699.39/2699.53 is support that was wicked through to 2688.28 and reclaimed.
   2667.22 is the swing low. 2671.94 is still unusable.
4. **Funding** settles at 16:00Z (00:00 local). ETH is +0.0068%.
5. **L-005:** take at least three samples. ETH was unquoted on both sides at two of three samples, and XRP broke
   the spread cap.

## Lessons applied

L-001 (standing exclusion; the retest was broad, not isolated), L-004 (the required span exceeds the structure),
L-005 (three sweeps; every contract failed at least once, and XRP breached the cap), L-006 (no 24h claims; the N rise
was a market event), L-007 (the 20:00 forecast was checked and half of it was wrong, in the tightening direction; a new forecast is written).
L-002 and L-003 were not reached. No lesson was loosened. Nothing under `reviews/` and no script, config, watchlist,
schedule or switch was touched.
