# 2026-09-25 check 22:00 research note (14:00Z)

The run started on time at 22:03 local, and the engine ran at 14:04:58Z. The account is flat, so there was nothing to reconcile.

## What the 21:00 note asked for, and what happened

- **ETH structure:** the reclaim did not hold. The 13:00Z 1h bar reads O2717.26 H2717.75 **L2686.77** C2693.95. It
  lost 2699.39/2699.53 and undercut the 2688.28 retest low. In the 5m sequence, 13:45Z closed at 2688.53 and
  13:50Z wicked to 2686.77 before closing at 2699.00. The 14:00Z bar (open) has printed **2685.30**, and ETH was
  quoting 2680.35/2683.25 at the engine. The 2699 area is now resistance, not support. The levels are: 2740.42
  high, 2699–2701.8 (lost), 2685.30 (new low, still forming), 2667.22 swing low, and 2671.94 still unusable (L-001).
- **Was the move isolated? (L-001):** no. All five contracts made lower closes at 13:00Z and are lower again at
  14:00Z (BTC 84410.7→83867.7→83760.0; BNB 778.15→774.35→771.29; SOL 120.67→119.58→118.82;
  XRP 1.6027→1.5881→1.5815). The decline is broad and real, and it does not change the standing exclusion.
- **Data oddity (noted, not relied on):** the ETH 13:00Z and 13:05Z 5m bars share an identical H/L
  (2717.41/2710.62). This is a minor host quirk, and no level is drawn from it.
- **L-007 forecast check:** the 21:00 note forecast that N(1h) would **fall** as the 12:00Z bar left the 1h window,
  and that the binding N would stay at about 1.1%. **Both parts were right.** N(1h) = **0.554%** (the 13:50Z bar),
  while N(2h) = N(3h) = **1.128%**. Measured against the window that contains the setup-defining bar, the binding
  N is 1.128%, and the required span is about 2.96%. The drop in N(1h) is window arithmetic (L-006), not quieting.
- **derivatives:** ETH lastFundingRate reads **+0.0100%**, up from +0.0068% at 21:00. It settles at 16:00Z. This is
  recorded but not claimed.
- **market_context:** broad same-direction weakness over the last two hours. Per L-006, no 24h figure is claimed.

## Decision inputs

- **L-001:** the standing exclusion of all five contracts binds. That alone means `no_trade`.
- **L-004:** the binding N is 1.128%, so the required span is about 2.96%. The only nearby structure is
  2699.5 → 2667.22 (about 1.2%), plus a still-forming low. No construction is possible, so no ratio was priced.
- **L-005 (three sweeps about 20 s apart, ~14:04:05Z–14:04:45Z):** BTC ask **50 USDT** at sweep 0 and **2,496**
  at sweep 2. XRP ask **507 USDT** at sweep 2. XRP spread **41.65 / 42.91 / 27.79 bps**, over the 25 bps cap at
  all three sweeps. SOL bid 190k → 29k → **17.6k**. BTC spread 17.95 / 20.34 / 7.02 bps. ETH held about 1.2–1.5M
  on both sides at all three sweeps, but its spread widened 3.65 → 13.19 bps. BNB's bid ran about 0.87–2.0M.
  No contract other than ETH and BNB held a usable book on both sides throughout, and both of those are excluded.
- **L-002/L-003:** no stop was chosen and there was no ratio to requote.
- **L-006:** the drop in N(1h) is attributed to the 12:00Z bar leaving the window, and it was not treated as a relaxation.

**Decision:** `no_trade` (the engine accepted it). No order was proposed or sent.

## For the 23:00 check (15:00Z)

1. **L-001 still binds.** The 22:00 review may have changed LESSONS.md while this check ran, so read it fresh.
2. **L-007 forecast:** the 12:00Z bar (1.128%) leaves the 2h window at about 13:55Z+2h ≈ **15:55Z**, so it is still
   inside N(2h)/N(3h) at 23:00. N(1h) at 23:00 will be set by the 14:00Z bars. If 14:00Z stays quiet, N(1h) will
   **fall** below 0.55%. That would be window arithmetic. The binding N is the bar that defines whatever low ETH
   has made by then: 13:50Z (0.554%) or a new 14:xxZ impulse bar. If a new low prints on a large bar, that bar binds.
3. **ETH levels:** 2740.42 high; 2699–2701.8 now resistance; 2685.30 a forming low; 2667.22 swing low (a likely
   magnet if the decline continues); 2671.94 unusable.
4. **Funding** settles at 16:00Z (00:00 local). ETH is +0.0100%.
5. **L-005:** take at least three samples. XRP was over the cap at every sample this check.

## Lessons applied

L-001 (standing exclusion; the decline is broad, not isolated), L-004 (the required span exceeds the structure),
L-005 (three sweeps; BTC/XRP/SOL thin, XRP over the cap), L-006 (the N(1h) drop is window arithmetic; no 24h claims),
L-007 (the 21:00 forecast was confirmed on both parts; a new conditional forecast is written above). L-002 and L-003
were not reached. No lesson was loosened. Nothing under `reviews/` and no script, config, watchlist, schedule or
switch was touched.
