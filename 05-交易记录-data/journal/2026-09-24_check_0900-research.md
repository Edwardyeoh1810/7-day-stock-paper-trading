# Research note / 研究记录 — 2026-09-24 09:00 (slot 2026-09-24_check_0900)

- Run: `2026-09-24_check_0900-research`
- Slot scheduled: 2026-09-24T09:00+08:00 — run started 09:03:48+08:00, observation 01:04:49Z, five book sweeps
  01:07:21Z–01:11:10Z, decision ~09:15. **On time, not a late run.** Thirteenth consecutive on-time check since
  the 09:00 stall on 09-22.
- Account: **flat**, 5000 USDT cash and equity, no positions, no open orders, nothing to reconcile. No exit order
  has ever been placed in this experiment.
- Decision: **no_trade**. Best candidate **BNBUSDT short** — the direction flips back from the 02:00 note's long.

## Headline

The 02:00 note asked whether, by this check, BNB had formed **a genuine shelf or a genuine failure** at 766.72.
**Neither. The range simply tightened.** Over the 8h15m 5m window (16:50Z–01:05Z) BNBUSDT's entire range is
**762.63–769.15 = 0.855%**, and **23 of 100 bars contain 766.72 inside their range**. The 02:00 magnet finding
(eleven touches in 165 minutes) is not merely confirmed, it is the dominant fact about the contract.

**Four constructions were priced — BNB long and short, ETH long and short. All four fail the L-004 span screen
at their nearest structural target, and all four pass it only by jumping structure that rejected within hours.**
That is the trade-off L-004 predicts, observed four times out of four in a single check for the first time.

**And L-005 refuses all four independently: for every one of them, the side the trade must cross went unquoted.**

## L-001 artifact scan — 5m / 1h / 4h / daily

Readable contracts remain **BNBUSDT and ETHUSDT only**, unchanged from 02:00.

- **BTCUSDT — excluded, nineteenth consecutive check. The contamination has not moved at all.** Daily 09-21 still
  reads **O81,144.10 H95,804.10** — an **11.437% upper wick, 18.147% range**. 4h still carries three flagged bars:
  09-21 12:00Z (11.709% wick on 1.350% body = 8.7x, range 15.1x frame median), 16:00Z (5.155% / 0.805% = 6.4x),
  20:00Z (**4.390% on a 0.076% body = 58.0x**). The 36-bar 1h and 40-bar 5m scans are clean — **which is exactly
  the flicker L-006 warns about, and is not evidence BTC became readable.**
- **SOLUSDT — excluded, ninth consecutive check.** The 09-22 19:00Z 1h bar still reads **O118.09 H118.59 L106.67
  C118.07 — a 9.654% lower wick on a 0.017% body, 570.0x, range 13.0x the frame median.** Still carried by the
  09-22 16:00Z 4h bar (9.070% / 0.648% = 14.0x) and the **09-22 daily bar (9.941% lower wick on a 0.345% body =
  28.8x)**. 24h quote volume **458.6M USDT against 103–135 BILLION** for the other four.
- **XRPUSDT — excluded.** The 09-23 04:00Z 4h bar still reads **O1.6177 H1.6855 with a 0.124% body — a 4.191%
  wick, 33.8x** — and the 09-23 daily bar still reads H1.6855. **`high24h` STILL READS 1.6855** against a 1.5006
  last. **The 02:00 note's correction to the 00:00 note is confirmed:** the print does *not* leave the window
  before this check; it leaves at 09-24 04:00Z = **12:00 local**, three hours from now.
- **ETHUSDT and BNBUSDT clean on all four frames.**

## L-006 — three window-movement instances, and the first is the check's central finding

**(1) BNB's noise floor collapsed 2.5x with nothing printing, and the span requirement more than halved with it.**

The 02:00 note wrote that "N will move again — by 01:00Z N is governed by whatever printed overnight." **Nothing
printed overnight.** The 17:15Z reclaim bar (0.403%) and every other bar of consequence aged out of the preceding
hour, and the largest bar of the current hour is the 01:00Z bar at **0.159%** — a 1.22-point range in dead chop.

| BNBUSDT N, measured four ways | value | 2.5N + 0.14% required span |
|---|---|---|
| full preceding hour (12 closed bars, 00:10Z–01:05Z) | **0.159%** (01:00Z) | **0.538%** |
| excluding that bar | 0.147% | 0.508% |
| wider 26-bar window (2h05m) | 0.159% (same bar) | 0.538% |
| **8h15m window containing the box actually being traded** | **0.403%** (17:15Z) | **1.148%** |
| setup-defining bar | **none exists — that is the finding** | — |

**The requirement fell from 1.148% at 02:00 to 0.538% now, purely because the window rolled forward over six
quiet hours.** This is the single cleanest L-006 instance yet: the threshold moved, the market did not.

**And the trade fails even the halved bar.** See below — the BNB short misses 0.538% by **0.003pp**. Re-measured
against the honest window that contains the structure being traded, the requirement is 1.148% and the miss is
**0.614pp, a two-hundred-fold larger miss**. The crossing does not merely dissolve on re-measurement; it never
occurred at all.

**(2) SOLUSDT's `low24h` stopped reading 106.67 and now reads 113.03.** The print was 09-22 19:00Z; it left the
24h comparison window at 09-23 19:00Z, **between the 02:00 and 09:00 checks**. Per L-006 this is the window
moving, not SOLUSDT becoming readable — and the print is **still live in the 1h, 4h and daily frames** (above).
**Recorded as a dissolving re-measurement.**

**(3) XRPUSDT's `high24h` has NOT moved**, confirming the 02:00 arithmetic correction. When it stops reading
1.6855 at 12:00 local, that will be the window moving, not XRP becoming readable. Stated in advance, as L-006
requires.

## Structure — there is no setup on either readable contract

**BNBUSDT is a 765.20 / 769.15 box, 0.516% tall, with price at 767.46 dead centre.**

- Support cluster **765.20–765.70 — eight touches**: 765.20 (21:05Z), 765.33 (17:35Z, 20:35Z, 20:45Z), 765.42
  (21:25Z–21:35Z), 765.60/765.63/765.66/765.69 (18:20Z, 18:00Z, 23:15Z, 23:30Z). Below it a **vacuum to 762.63**
  (17:05Z, the 8h low).
- Resistance **769.01–769.15 — three touches**: 769.01 (22:10Z), **769.15 (00:30Z and 00:35Z, thirty-five minutes
  before this check)**. Above it a **vacuum to 777.18** (the 09-23 12:00Z/13:00Z 1h lows).
- Overnight lows rose 762.63 → 765.20 → 765.66 → 766.35 → 766.94; overnight highs 767.92 → 768.87 → 769.01 →
  769.15. **Both ends drifting in — a tightening range, not a shelf and not a failure.** The current 00:00Z 4h bar
  ranges **0.365%**, the tightest 4h bar in the visible window.

**ETHUSDT is the same picture one notch wider.** It fell 2695.84 (22:05Z) → 2679.08 (00:50Z) and has chopped
**2679.08–2690.36 for three hours = 0.421%**. Neither the highs (2695.84 → 2691.93 → 2690.38 → 2687.98 →
**2690.36** → 2684.71) nor the lows (2675.73 → 2682.10 → 2680.41 → 2682.19 → 2679.08) form a clean sequence:
00:30Z printed *above* 00:05Z. **No directional structure.**

## L-004 span screen — run FIRST, and it refuses all four, in both of its forms

Entry prices from the 01:04:49Z snapshot. Drag 0.14% round trip.

| construction | risk | xN | nearest-target NET RR | span vs required | verdict |
|---|---|---|---|---|---|
| **BNB short** E767.46 S769.30 T765.20 | 0.240% | 1.51x | **0.644** | 0.534% vs 0.538% | **FAIL by 0.003pp** |
| **BNB long** E767.53 S765.10 T769.15 | 0.317% | 1.99x | **0.224** | 0.528% vs 0.538% | **FAIL by 0.010pp** |
| **ETH short** E2681.76 S2690.60 T2679.08 | 0.330% | 1.89x | **−0.122** | 0.430% vs 0.575% | **FAIL by 0.145pp** |
| **ETH long** E2682.16 S2678.90 T2687.98 | 0.122% | **0.70x** | **0.633** | 0.339% vs 0.575% | **FAIL by 0.236pp** |

**The ETH short's nearest-target net reward/risk is NEGATIVE** — the round-trip drag exceeds the entire move to
the nearest support. **The ETH long's stop is 0.70x N — sub-noise — and L-002 refuses it outright** regardless of
any ratio.

**And every construction that passes the span screen does so only by jumping structure (L-004 target validity):**

- **BNB short → 763.62** (the 1.5-paying target, net 1.503) or **762.63** (net 2.041): both jump the entire
  **eight-touch 765.20–765.70 support cluster.**
- **BNB long → 777.18** (net 3.529): jumps **769.15, which rejected at 00:30Z and 00:35Z — thirty-five minutes
  before this decision** — plus 769.01 and 768.87. This is the same refusal as 02:00 on the same target, now with
  a *fresher* rejection: the 02:00 note's sharpest form was a level that rejected "inside the decision's own
  hour", and 769.15 rejected inside the decision's own **half-hour**.
- **ETH short → 2670.48** (net 0.851) or **2668.06** (net 1.125): jump 2679.08 (**held twice, 00:50Z and 00:55Z,
  ten minutes before the check**) and 2675.73. *Note both still fail the 1.5 floor even after jumping.*
- **ETH long → 2695.84** (net 3.044): jumps **2687.98 (rejected 00:05Z) and 2690.36 (rejected 00:30Z)**, both
  inside the last hour, on a stop that is already sub-noise.

**Four for four, in both directions, on both readable contracts. This is the most complete demonstration of
L-004's predicted trade-off the experiment has produced.**

## L-002 — the magnet clause bars both stops independently

- **766.72 is in the range of 23 of the last 100 5m bars.** Nearly a quarter of eight hours. No stop may be
  anchored there in either direction; the honest read is chop, exactly as the 02:00 note instructed.
- **The BNB short's stop 769.30 sits 0.02% above 769.15, touched twice in the preceding forty minutes.** That is
  L-002's original formulation verbatim — "a stop that sits just above or below a level the market keeps
  touching, however many multiples of N of room it appears to have." **Refused independently of the span screen.**
- **The ETH long's stop 2678.90 sits 0.007% below 2679.08, touched twice ten minutes before the check**, and is
  **0.70x N**. Refused twice over.
- Nothing here advances L-002's re-test tally, which counts declined setups that would have **won**. **It stands
  at one of three.**

## L-002 tally — both 23:00 constructions remain live

Over 16:50Z–01:05Z BNBUSDT's extremes were **H 769.15 / L 762.63**.

- Declined 23:00 **short** (766.74 / stop 780.90 / target 757.90): **neither level touched. Still live.**
- Declined 23:00 **long** (766.85 / stop 758.55 / target 780.90): **neither level touched. Still live.**
- 02:00's best candidate (BNB long) was refused at the span screen with **no construction priced**, so there is
  nothing to resolve.

**Tally unchanged at one of three. Not advanced.**

## L-003 requote — eleventh consecutive material check, and BOTH directions appear within it

**The legitimate form — BNB short, fixed stop 769.30 / target 765.20, six quotes over 382 seconds:**

| quote | bid | risk | reward | NET RR |
|---|---|---|---|---|
| 01:04:49Z | 767.46 | 0.240% | 0.294% | **0.644** |
| s1 01:07:21Z | 767.10 | 0.287% | 0.248% | 0.375 |
| s3 01:09:15Z | 767.10 | 0.287% | 0.248% | 0.375 |
| s4 01:10:12Z | 766.85 | 0.319% | 0.215% | **0.235** |
| s5 01:11:10Z | 766.92 | 0.310% | 0.224% | 0.272 |

Price drifted **away** from the fixed stop, so **risk grew 0.240% → 0.319% while reward shrank 0.294% → 0.215%**
and the ratio decayed **0.644 → 0.235, a 63% fall, monotonically**. Chasing it means widening risk to hold the
target, which is a refusal. **The span screen fails at every one of the six quotes, never by more than 0.004pp** —
a remarkably stable near-miss.

**The pathological form — ETH long, fixed stop 2678.90 / target 2687.98:** the ratio **nearly doubled, 0.633 →
1.130 at s1**, entirely because the ask drifted 2682.16 → 2681.40 **toward** the fixed stop. Both halves improved
from one cause — risk shrinking 0.122% → 0.093% — and **at that exact instant the stop fell to 0.54x N, the most
sub-noise construction of this check.** It never reached 1.5, but the mechanism is L-003's warning in its purest
form: the number improved because the risk was disappearing, not because the trade was.

**Clock stays at ZERO.**

## L-005 — five sweeps in 229 seconds; not one contract held both sides, tenth consecutive check

| contract | worst bid | worst ask | note |
|---|---|---|---|
| **BNBUSDT** | **445 USDT (s5)** @ 0.261 bps | **176 USDT (s1)** @ 2.085 bps | **BOTH sides caught unquoted inside five minutes** |
| **ETHUSDT** | 762,577 (s2) | **249 USDT (s4)** @ 6.337 bps | bid held; **ask failed** |
| BTCUSDT | 24,116,590 (s5) | **253 (s1), 253 (s4), 2,106 (s5)** | **ask below the 2,500 max order notional at three of five**; s5 quoted **0.059 bps — the tightest spread of the check — on a 2,106 USDT ask** |
| SOLUSDT | **129 USDT (s3)** | 59,359 (s5) | excluded on artifact regardless |
| XRPUSDT | 1,292,121 (s2) | **7 USDT (s1)** | smallest print of the check; excluded regardless |

**This refuses all four constructions independently of every geometric finding above:**

- **BNB short** sells into the bid → **445 USDT at s5. A maximum 2,500 USDT market sell is 5.6x the entire visible
  bid.** Refused.
- **BNB long** buys the ask → **176 USDT (0.23 BNB) at s1. 14x short of a maximum order.** Refused.
- **ETH long** buys the ask → **249 USDT at s4. 10x short.** Refused.
- **ETH short** sells into a bid that held, but **exits by buying the ask, which printed 249 USDT at s4** — and
  the exit side is precisely where the reduce-only stop rests between checks. Refused.

**BNBUSDT is the finding of this sweep: it is the only contract of the experiment to be caught unquoted on both
sides within a single check**, at 0.261 and 2.085 bps respectively. **No contract breached the 25 bps cap; the
widest spread of the entire check was 9.250 bps. The cap was blind to all of it — again.**

## Evidence gate — NOT passed, on independence rather than on count

Taking the **BNBUSDT short**, the only direction the higher-timeframe structure supports:

- `trend` — **supports.** Daily closes 799.71 → 788.70 → 767.76; 4h lower highs since 09-21 (807.74 → 800.90 →
  798.30); 24h −3.128%.
- `market_context` — **supports on its face.** All five contracts down **2.63% to 5.76%** on 24h.
- `price_action` — **opposes.** 760.09 held; overnight lows rose 762.63 → 765.20 → 765.66 → 766.35 → 766.94.
  **Eight hours of higher lows**, with price in the upper half of the box, not breaking down.
- `volume` — **absent.** Overnight volumes are ordinary; no expansion on any move, in either direction.
- `derivatives` — **NOT claimed.** Funding is clamped and carries no information: **BNB exactly 0.000000%**, ETH
  and SOL exactly **+0.010000%** (the cap), BTC +0.009555%, XRP −0.001784%. Open interest is **flat to within
  0.0017% on all five across five minutes.** Next funding 08:00Z = 16:00 local; the 00:00Z settlement passed an
  hour before this check and no check sits on it.
- `news` — **RECORDED, NOT CLAIMED.** The **Trump–Xi summit and state dinner are today (09-24)**. Anything opened
  here is held **through** the event under the 24-hour limit. A single scheduled event is not two categories.

**On a bare count the short has two supporting categories and would pass. It does not pass, and here is why.**
The strategy requires evidence to be **independent** — "a moving average and a trend line drawn over the same
candles are one observation, not two" — and states that the five contracts "are five ways to express one view on
the crypto market, not five independent opportunities." **BNB's 24h is −3.128% against a basket spanning −2.63%
to −5.76%: it is mid-pack, showing no relative strength or weakness whatever.** So `market_context` here asserts
only "crypto is down", which is the identical observation that makes `trend` down. **They are one observation,
not two.** With `price_action` actively opposing and `volume` absent, **the gate is not passed.**

This is the stricter reading and it is the binding one. Recorded explicitly so the review can judge it.

## Reasons not to trade, and the decision

Every screen refuses, and each refusal is independent of the others:

1. **L-004 span screen** — all four constructions fail at their nearest structural target (by 0.003pp, 0.010pp,
   0.145pp and 0.236pp), and this is against a requirement that L-006 shows has **mechanically halved** overnight.
2. **L-004 target validity** — every passing construction jumps structure that rejected within the hour, twice
   within the half-hour.
3. **L-002** — the BNB short's stop rests on a twice-touched level; the ETH long's stop is 0.70x N and sub-noise.
4. **L-003** — the requote decays the best construction 0.644 → 0.235 and inflates another by shrinking its risk.
5. **L-005** — the side each trade must cross went unquoted; BNB failed on both sides at once.
6. **Evidence gate** — the two supporting categories are not independent.
7. **News** — anything opened now is held **through** the Trump–Xi summit under the 24-hour limit, and nothing
   above justifies carrying risk through a scheduled event of that size.

**Decision: `no_trade`.** Best candidate BNBUSDT short, refused seven ways.

## For the 16:00 check (08:00Z)

1. **The box is 765.20 / 769.15 and price is dead centre. The falsifiable question: does BNB leave it, and which
   way?** A close outside on expanding volume changes the picture; a further tightening does not. **Do not reuse
   769.30 / 765.20 / 763.62 / 777.18** — re-derive from whatever structure exists at 08:00Z.
2. **N WILL MOVE AGAIN, AND THIS CHECK'S READING IS THE FLATTERED ONE.** BNB's N is **0.159%**, the lowest of the
   experiment, because six silent hours rolled through the window. If the US pre-session prints anything real, N
   and the required span will jump back toward 0.40–1.15%. **State N four ways again and price against the window
   containing the bar that defines the setup, not the quiet one.**
3. **L-002 tally is ONE OF THREE — do not advance it carelessly.** Both 23:00 constructions are still live:
   short 766.74/780.90/757.90 and long 766.85/758.55/780.90. Record any resolution with the same precision.
4. **BNB AND ETH REMAIN THE ONLY READABLE CONTRACTS.** Carry forward: **XRP's 1.6855 leaves the 24h window at
   12:00 local, before the 16:00 check. When `high24h` stops reading it, that is the window moving, not XRP
   becoming readable** — exactly as SOLUSDT's `low24h` did between 02:00 and this check. XRP stays excluded.
5. **FIVE BOOK SAMPLES MINIMUM, READ QUANTITY BEFORE SPREAD.** BNB was caught unquoted on **both** sides this
   check (176 and 445 USDT) and BTC quoted **0.059 bps on a 2,106 USDT ask**. Treat the engine quote as a sample.
6. **THE TRUMP–XI SUMMIT AND STATE DINNER ARE TODAY.** The 16:00, 20:00 and later checks sit closer to it.
   Justify any entry **through** the event, not around it.
7. **Funding next settles 08:00Z = 16:00 LOCAL — the 16:00 check sits ON the settlement.** Note which side pays.

## Lessons applied

- **L-001** applied with the scan at **5m/1h/4h/daily**. BTCUSDT excluded a **nineteenth** consecutive check with
  4h and daily contamination **unchanged**; SOLUSDT a **ninth** (1h 570.0x, 4h 14.0x, daily 28.8x); XRPUSDT
  excluded with `high24h` still reading 1.6855. BTC's clean 1h and 5m scans recorded as a **flicker**, not a
  relaxation.
- **L-002** applied and **decisive for a tenth consecutive check**. N stated **four ways**; the magnet clause bars
  766.72 in both directions (23 of 100 bars) and independently bars the BNB short's 769.30 stop and the ETH long's
  sub-noise 0.70x N stop. Tally **NOT advanced; stands at one of three**.
- **L-003** applied, **eleventh consecutive material check**, with **both** the legitimate form (BNB short decaying
  0.644 → 0.235) and the pathological form (ETH long inflating 0.633 → 1.130 as its stop fell to 0.54x N) **inside
  the same check**. Clock stays at **zero**.
- **L-004** applied **FIRST, before any ratio**, and is the **primary refusal in both of its forms**, refusing
  **four of four** constructions on span and every passing construction on target validity — including a level
  that rejected **thirty-five minutes** before the decision.
- **L-005** applied with **five sweeps**, refusing every candidate independently of all geometry for a **tenth
  consecutive check**, and producing the experiment's first contract caught **unquoted on both sides at once**.
- **L-006** applied to every window-derived figure and produced **three instances, two of which dissolved**: BNB's
  span requirement halving on a rolled-forward quiet window (the check's central finding), SOLUSDT's `low24h`
  releasing the 106.67 artifact, and XRPUSDT's `high24h` confirming the 02:00 correction. **Whether any of this
  moves L-006's clock is the review's call, not this check's.**

**No lesson was loosened, reinterpreted, retired or overridden; no rule or risk limit was relaxed. Nothing under
`reviews/` was read for modification or modified. No script, config, watchlist, schedule or safety switch was
touched. No order API was called except through `paper_engine.py`.**
