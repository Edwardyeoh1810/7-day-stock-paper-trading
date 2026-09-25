# Research note / 研究记录 — 2026-09-25 16:00 (slot 2026-09-25_check_1600)

- Run: `2026-09-25_check_1600-research`
- Slot scheduled: 2026-09-25T16:00+08:00. Run started **16:03:29+08:00**, observation 08:03:46Z, market read
  08:04:10Z, three book sweeps 08:04:23Z–08:06:27Z, engine **08:07:16Z**. **On time (7 minutes), not a late run.**
- Account: **flat**, cash/equity 5000 USDT, no positions, no open orders, nothing to reconcile.
- Decision: **`no_trade`**, accepted by the engine on the first submission.

## Headline: the only category the 09:00 check had is gone

The 09:00 note told this check to read two 4h bars after they closed. It named the thresholds: a close above
2699.39 makes `price_action` claimable long, and a close below 2676.02 removes `trend`.

| ETHUSDT 4h bar | O | H | L | C | result |
|---|---|---|---|---|---|
| 09-25 00:00Z | 2686.35 | **2699.53** | 2673.88 | 2677.28 | Poked 0.14 above 2699.39 and closed 22 points below it: a **failed breakout** |
| 09-25 04:00Z | 2677.28 | 2683.74 | **2667.22** | **2671.19** | **Closed below 2676.02**, so `trend` is removed |

The four-bar higher-low sequence 2633.31 → 2640.00 → 2660.49 → 2676.02 is **broken**. The evidence gate on ETHUSDT
has now read 3 → 0 → 1 → 1 → **0** across five checks.

## Evidence categories (none claimed)

- `trend`: **not claimed either way**. There is one lower low, but the 09-24 daily close (2686.59) was higher, and
  today's forming daily bar may not be read as closed.
- `price_action`: **not claimed**. The poke and rejection at 2699.53 is a single observation. Price sits in the
  middle of the 2667–2700 range, not at a level.
- `volume`: **not claimed**. Over the last hour, 5m quote volume was 1.11x the 100-bar median, so there is no
  expansion.
- `derivatives`: **not claimed**. Funding settled at 08:00Z; ETH is back on the **+0.0100%** bound after three
  unclamped readings. BTC, SOL and XRP are also at +0.0100%, and BNB is at +0.004879%. The next funding is at 16:00Z.
  ETH OI is 11,908,218,690, against 11,897,688,432 at 09:00: **+0.09%, flat**.
- `market_context`: **not claimed** (these are rolling 24h figures, see L-006). BTC −0.54%, ETH −0.63%, BNB −0.20%,
  SOL +0.86%, XRP +2.02%. ETH is the weakest of the five.

**Gate: 0 of 2.**

## L-001: the tradable set is still empty

This check used a coarser screen: range at least 3x the frame median **and** wick/body at least 4x, over
100×5m, 30×1h, 30×4h and 30×1d bars. It reproduced:
- **BTCUSDT**: 4h bars at 09-21 12:00Z (H95,804.10, rm 15.1x), 16:00Z (H91,000.00) and 20:00Z (H90,389.80, w/b 58x).
- **SOLUSDT**: 4h bar at 09-22 16:00Z (L106.67, rm 6.5x, w/b 14x).

It did **not** reproduce ETH 2850.00 (which flags on range alone, as L-001 records), XRP 1.6855 or BNB
780.90/786.18. That is because this screen requires both conditions at once and the recorded method does not. **This
is not a reason to readmit any contract.** The standing exclusion binds in full, and only the review may change
it (P-011). The screen difference is referred to the 22:00 review.

## L-005 book sweeps (three, plus the engine's own quote)

| sweep | ETH bid / ask (USDT) | other contracts |
|---|---|---|
| 08:04:23Z | 528,850 / 9,548,871 | SOL bid 28,829 |
| 08:05:25Z | **37.45 / 5.35**, both sides unquoted | SOL bid 52,017 |
| 08:06:27Z | 5,037,959 / 5,068,056 | XRP ask 564,396 |
| 08:07:16Z (engine) | **~40.1 / ~21.4**, both sides thin again | — |

ETH went unquoted on **both sides** in two of four samples. SOL's bid was never a usable multiple of the maximum
order. The 25 bps cap never fired: the widest spread was 7.73 bps (SOL, sweep 3).

## L-002 / L-004 / L-003

With zero categories there is no setup, so no stop, span or ratio was priced. For the record, N(1h) = N(5h) =
**0.305%** on ETH (5m). The L-002 tally is unchanged at **one of three**, and the L-003 clock is **zero**.

## L-007: the first failed forecast

The 09:00 note forecast that N would collapse toward ~0.10–0.15% across the 11:00–15:00 dead zone unless a new
impulse printed. **Wrong:** N(1h) is **0.305%**, close to the 0.327% binding value. The move down from 06:00Z to
08:00Z printed new 0.2–0.3% bars. This is recorded as the first forecast where the figure did not move as
predicted. The failure ran in the tightening direction, so it permits nothing.

## For the 20:00 check (12:00Z)

1. **The tradable set is empty (L-001).** Record the state and return `no_trade` unless the review has changed it.
2. **Levels on ETH:** the ceiling is **2699.39/2699.53** (rejected four times, most recently as a failed breakout).
   The new swing low is **2667.22**. Below that, 2660.49 and 2640.00 are the earlier 4h lows, and the 24h low
   2633.31 is unchanged. 2671.94 is still not usable as a level.
3. **Two 4h bars close before or at your check:** 08:00Z at 12:00Z, which is the slot itself, so read it only once
   it has closed. A close **below 2667.22** makes a lower-low sequence and would start a short `trend` case. That
   case would still need a second, independent category.
4. **L-007 forecast:** the 0.305% bar was printed in the last hour. The 12:00Z window is 16:00–20:00 local, the
   pre-US ramp, so N will probably **stay at or above ~0.25%** rather than collapse. If it falls below ~0.20%, state
   the binding value first.
5. **Funding:** 16:00Z. ETH is back on the +0.0100% bound. OI is flat.
6. **L-005:** take at least three samples. ETH was unquoted on both sides twice in this check.
7. **The review task** should reconcile this check's coarser artifact screen with L-001's recorded method (XRP, BNB
   and ETH flags not reproduced by an AND-screen).

## Lessons applied

L-001 (standing exclusion binds), L-002/L-003/L-004 (nothing to price; N stated), L-005 (three sweeps plus the
engine quote), L-006 (24h figures not claimed), L-007 (the forecast failed and was recorded honestly). No lesson was
loosened, retired or overridden. Nothing under `reviews/` was modified. No script, config, watchlist, schedule,
leverage or safety switch was touched, and BINANCE_ENV is unchanged. No order API was called except through
`paper_engine.py`, and it sent no order.
