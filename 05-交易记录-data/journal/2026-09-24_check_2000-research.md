# Research note / 研究记录 — 2026-09-24 20:00 (slot 2026-09-24_check_2000)

- Run: `2026-09-24_check_2000-research`
- Slot scheduled: 2026-09-24T20:00+08:00 — run started 20:03:55+08:00, observation 12:04:17Z, five book sweeps
  12:05:09Z–12:09:53Z, decision ~20:22. **On time (4 minutes), not a late run.** Fifteenth consecutive on-time
  check since the 09:00 stall on 09-22.
- Account: **flat**, 5000 USDT cash and equity, no positions, no open orders, nothing to reconcile. No exit order
  has ever been placed in this experiment.
- Decision: **no_trade**. Best candidate **ETHUSDT short**.

## Headline

**The evidence gate passed for the first time in the experiment — and the trade was refused anyway.**

`trend` and `price_action` are both independently claimable for an ETHUSDT short at this check. That has never
happened before: at 09:00 the gate failed on independence, at 16:00 on raw count. **It passed here, and it
changed nothing, because the gate was never the binding constraint.** Six independent refusals remain, any one
of which is sufficient.

The market moved hard between 16:00 and 20:00 — **ETH 2692 → 2642, BTC to 83.4k, a genuine externally-confirmed
selloff** on a 15bp spike in the 10-year Treasury yield to 5.11%. ETH made a **new 24h low at 2633.31**, bounced
0.66% to 2650.63, and is fading. The structure a check waits for finally arrived. **It still does not offer the
span, the stop, the target or the book to trade it.**

## L-001 artifact scan — 5m / 1h / 4h / daily, plus cross-contract

**Readable contracts: ETHUSDT only, for a second consecutive check.**

**BNBUSDT — STAYS EXCLUDED, and this is the 16:00 note's prediction confirmed.** The 16:00 note wrote in advance:
*"do not let the 5m window rolling past 02:45Z read as a recovery; that is precisely the L-006 flicker."*

| frame | reading now | verdict |
|---|---|---|
| 5m (40 bars) | **zero flags** | window has rolled past 02:45Z |
| `high24h` | **783.05** — *above* 780.90 | the print has left the 24h high field |
| **09-24 00:00Z 4h** | **O767.82 H780.90 L764.10 C767.00 — 1.704% wick on a 0.107% body = 16.0x** | **UNREVISED** |
| **09-24 daily** | **H780.90 — 1.459% wick on a 0.245% body = 6.0x** | **UNREVISED** |

**Both windows that carried the artifact have rolled past it. The contamination that actually matters has not
moved at all.** The window moved; the contract did not become readable. **BNB stays excluded.**

- **BTCUSDT — excluded, twenty-first consecutive check, unchanged.** 09-21 daily **O81,144.10 H95,804.10
  L81,079.00 C86,523.40 — an 11.437% upper wick on a 6.629% body, 18.161% range = 10.4x the daily median.**
- **SOLUSDT — excluded, eleventh consecutive check.** 09-22 16:00Z 4h **L106.67, a 9.070% lower wick, 11.175%
  range = 7.3x median**; 09-22 daily **9.941% on a 0.345% body = 28.8x**. 24h quote volume **453.9M USDT against
  104–132 BILLION** for the other four — a ~250x shortfall, unchanged.
- **XRPUSDT — excluded.** 09-23 04:00Z 4h **O1.6177 H1.6855 on a 0.124% body — 4.191% wick, 33.9x**, unrevised.
  `high24h` has now fallen to **1.58**; per L-006 that is the window moving, not XRP becoming readable.

**ETHUSDT's three 1h flags were each CLEARED by cross-contract comparison — the test the strategy actually
specifies.** This matters: without it ETH would have been excluded too and the tradable set would be empty.

| ETH flagged bar | ETH | BTC | BNB | SOL | XRP | verdict |
|---|---|---|---|---|---|---|
| 09-23 14:00Z | rng 2.781%, lw 1.018% | **rng 1.987%** | **rng 2.798%** | — | — | market-wide selloff, **real** |
| 09-23 16:00Z | rng 0.933%, lw 0.631% | 0.743% | 0.863% | 1.509% | 1.668% | ETH **mid-pack**, real |
| 09-24 05:00Z | uw **0.536%** | uw 0.304% | uw 0.213% | uw **0.537%** | uw **0.807%** | **all five wick**, real |

The 09-24 05:00Z bar is the one that built 2697.41, the resistance the 16:00 check priced against. **SOL and XRP
wick harder than ETH at the identical candle.** It is a real rejection. ETH remains readable.

## The market actually moved — and it is externally confirmed

**This is the first check of the experiment at which the demo host's move is corroborated outside it.** Public
reporting on 09-23/09-24: BTC **~83,200, down >3%**, XRP leading losses, Solana and Ethereum lower, driven by the
**10-year Treasury yield closing +15bp at 5.11%**. The demo host reads BTC **83,388**. **The demo price is not
the artifact here** — which is precisely why ETH's 1h flags were cleared rather than excluded.

## Structure — ETHUSDT, the only readable contract

Range since 09:30Z: **2633.31 – 2670.98**. Current **2646.70 / 2646.84**.

- **09:30Z–10:30Z selloff leg**: 2670.98 → **2633.31 (10:30Z), a new 24h low**, touched **exactly once**.
- **10:35Z–11:25Z bounce**: 2633.31 → **2650.63**, +0.66%.
- **11:30Z–12:10Z fade**: lower highs **2650.63 → 2650.50 → 2647.99 → 2647.99 → 2646.84**.

**Level touch counts (5m, 0.03% tolerance) — and this table is the whole refusal:**

| level | touches | note |
|---|---|---|
| **2650.63 / 2650.17** | **7** | 09:35Z + six consecutive bars 11:00Z–11:25Z — the bounce high |
| 2647.99 / 2647.72 | 11 | |
| **2643.20** | **12** | the heaviest level on the board |
| 2642.56 | 11 | |
| 2640.06 | 8 | |
| 2637.86 | 6 | |
| 2635.87 | 3 | |
| **2633.31** | **1** | **the 24h low — a single print, the thinnest level in the window** |

## L-002 / L-006 — N stated four ways, honest reading is 2.7x the flattered one

| ETHUSDT N | value | defining bar | 2.5N + 0.14% required span |
|---|---|---|---|
| full preceding hour (12 bars) | 0.205% | 12:00Z | 0.6525% |
| preceding hour, closed bars only | 0.205% | 12:00Z (same) | 0.6525% |
| wider 2h window (24 bars) | 0.294% | 10:50Z (bounce impulse) | 0.8750% |
| **window containing the 09:30Z bar that CREATED 2633.31** | **0.551%** | **09:30Z** | **1.5175%** |

**The binding measurement is 0.551%.** The setup is the failed bounce off the 24h low; the bar that created that
low is the bar that defines the trade. Per L-002's amendment and L-006, the window must contain it.

## L-004 span screen — run FIRST, and nothing survives

| construction | span | vs req(hour) 0.6525% | vs req(2h) 0.8750% | **vs req(HONEST) 1.5175%** |
|---|---|---|---|---|
| SHORT 2651.20 → 2643.20 (nearest) | 0.303% | FAIL 0.350pp | FAIL 0.572pp | **FAIL 1.215pp** |
| SHORT 2651.20 → 2640.06 | 0.422% | FAIL 0.231pp | FAIL 0.453pp | **FAIL 1.096pp** |
| SHORT 2651.20 → 2633.31 (24h low) | 0.679% | *pass* | FAIL 0.196pp | **FAIL 0.838pp** |
| LONG 2632.80 → 2647.99 (nearest) | 0.577% | FAIL 0.076pp | FAIL 0.298pp | **FAIL 0.941pp** |
| LONG 2632.80 → 2650.63 | 0.677% | *pass* | FAIL 0.198pp | **FAIL 0.840pp** |

**Only two constructions pass any span test, and only against the flattered hour window** — the exact measurement
L-002's amendment and L-006 both forbid.

**Target validity independently kills the only construction that clears the 1.5 floor.** The short's 2633.31
target **jumps five intervening supports — 2643.20 (12 touches), 2642.56 (11), 2640.06 (8), 2637.86 (6),
2635.87 (3) — to reach a level touched exactly once.**

**That is the cleanest statement of this screen's purpose the experiment has produced: the arithmetic works
only against the single thinnest level in the window, and against every heavy level it fails.**

## L-003 requote — the strongest pathological instance of the experiment

**ETH SHORT, fixed stop 2651.20, five quotes over 284 seconds:**

| quote | bid | risk% | xN(hour) | xN(honest) | net RR → 2643.20 | net RR → 2640.06 | **net RR → 2633.31** |
|---|---|---|---|---|---|---|---|
| s1 12:05:09Z | 2642.12 | 0.344 | 1.68 | 0.62 | −0.288 | −0.181 | **0.563** |
| s2 12:06:56Z | 2643.40 | 0.295 | 1.44 | 0.54 | −0.449 | −0.046 | 0.819 |
| s3 12:07:55Z | 2643.78 | 0.281 | 1.37 | 0.51 | −0.421 | 0.003 | 0.912 |
| s4 12:08:54Z | 2643.50 | 0.291 | 1.42 | 0.53 | −0.442 | −0.034 | 0.843 |
| **s5 12:09:53Z** | **2646.70** | **0.170** | **0.83** | **0.31** | −0.046 | 0.652 | **2.152** |

**A 3.8x inflation that crossed the 1.5 floor, and every bit of it came from the bid drifting 2642.12 → 2646.70
toward a FIXED stop.** Risk shrank 0.344% → 0.170% while reward to 2633.31 grew 0.333% → 0.506% — **both halves
of the ratio improving from one cause.**

**And at that same instant the stop fell from 1.68x to 0.83x N(hour): it crossed the floor at the exact moment it
stopped being a stop.** At s1 the stop was noise-safe and the ratio failed; at s5 the ratio passed and the stop
was sub-noise. **The two conditions moved in opposite directions, exactly as L-004 predicts.**

**Worse: the same drift breaks the premise.** The short's entire thesis is a failed bounce making lower highs.
Price reclaiming **2642.12 → 2646.84 in ten minutes** is the failed bounce failing to fail. *The number crossed
the floor at the moment the trade stopped existing* — L-003's strongest form, verbatim.

**The legitimate form ran simultaneously on the long:** net RR to 2647.99 decayed **0.187 → −0.182** as the ask
advanced *away* from its fixed stop, risk growing 0.366% → 0.530%.

**Clock stays at ZERO.**

## L-005 — five sweeps, and ETHUSDT collapsed TWICE inside one check

| contract | bid across s1–s5 (USDT notional) | worst ask |
|---|---|---|
| **ETHUSDT** | **1,236,964 → 66 → 1,074,488 → 7,218,896 → 108** | 2,603,546 |
| BNBUSDT | 2,094,157 → 2,093,295 → 965,200 → 468,894 → 1,509,996 | **8 USDT (s3)** |
| SOLUSDT | **362 (s1)** → 34,849 → 109,304 → 13,817 → 26,787 | **84 USDT (s3)** |
| XRPUSDT | **19 (s1)** → 9,400,561 → 6,122,512 → 25,819,170 → 25,812,907 | **1,473 (s2)** |
| BTCUSDT | 25,188,423 → 2,265,959 → 1,859,020 → 1,406,915 → 28,179 | 21,757 (s2) |

**ETHUSDT is a new form: the side both trades must cross went to double digits TWICE inside one check** — 66 USDT
at s2 (0.87 bps) and 108 USDT at s5 (0.529 bps), with full recoveries to 1.07M and 7.22M in between. A maximum
2,500 USDT market sell is **38x** the entire visible bid at s2 and **23x** at s5.

- The **short sells into that bid.** Refused.
- The **long exits into it, and its reduce-only stop rests on it between checks.** Refused.

Previous instances were a single collapse per check (BNB 7,497x at 09-23 22:00, ETH 70,517x at 16:00). **Two
collapses and two full recoveries inside 284 seconds is the oscillation stated as plainly as it can be.**

**Recorded against interest:** BTCUSDT held the best book of the five — worst sample **21,757 USDT, ~8.7x the
maximum order notional** — across all five sweeps, and it is excluded on the artifact, not the book. **That is
the second time the book filter and the artifact filter have disagreed** (the first was XRPUSDT at 16:00), and
the artifact filter is binding both times.

**No contract breached the 25 bps cap. The widest spread of the entire check was 10.595 bps (SOLUSDT, s1) and the
66 USDT ETH bid quoted 0.87 bps. The cap was blind to all of it — a twelfth consecutive check.**

## L-006 — the predicted flicker, and one instance recorded against interest

**(1) BNBUSDT's artifact leaving two windows at once — predicted at 16:00, confirmed here.** The 5m scan returns
zero flags and `high24h` has moved to 783.05, *above* the 780.90 print. **Both windows rolled past it. The 4h and
daily bars did not move.** Refused as recovery, exactly as instructed.

**(2) Recorded AGAINST INTEREST: the 24h figures were STABLE this check.** Across five reads in 284 seconds with
price moving 0.04–0.25%:

| contract | chg24h drift over 284s |
|---|---|
| BTCUSDT | +0.088pp |
| ETHUSDT | +0.020pp |
| BNBUSDT | +0.012pp |
| SOLUSDT | −0.018pp |
| XRPUSDT | −0.022pp |

**The 0.305pp four-minute move that was the 16:00 note's strongest instance did NOT recur.** This is a factual
record and it relaxes nothing: `market_context` is still refused, on the independence rule alone.

**(3)** XRP's `high24h` has fallen to 1.58 and SOL's `low24h` reads 112.60 — both artifacts aged out of the 24h
fields while remaining live in the 4h and daily frames. Dissolved, and staying dissolved.

## Funding and open interest — zero unclamped rates, a first

| contract | funding | reading |
|---|---|---|
| BTCUSDT | **+0.010000%** | exactly at the cap |
| ETHUSDT | **+0.010000%** | exactly at the cap |
| SOLUSDT | **+0.010000%** | exactly at the cap |
| **XRPUSDT** | **+0.010000%** | **pinned to the cap — it was −0.004380% at 16:00** |
| BNBUSDT | **0.000000%** | exactly zero |

**For the first time there are ZERO unclamped rates** — XRP was the last one and it has pinned. Thirteenth
consecutive check of clamped funding. **Open interest flat to within 0.0041% on all five** (BTC +0.0038%, ETH
+0.0011%, BNB +0.0016%, SOL +0.0011%, XRP +0.0041%). **`derivatives` NOT claimed.**

**`nextFundingTime` reads 2026-09-24 16:00Z = 00:00 local — the 00:00 check sits on the settlement, not this
one.** This confirms the correction the 16:00 note made to the 09:00 note. A short would **receive** ~0.25 USDT
on a 2,500 USDT notional; immaterial against 0.14% round-trip drag.

## Evidence gate — PASSED, for the first time in the experiment

Taking the **ETHUSDT short**:

- **`trend` — CLAIMABLE DOWN, and this is the genuine change since 16:00.** The rising 4h low sequence the 16:00
  note recorded (2641.37 → 2668.06 → 2666.20 → 2669.37) is **broken**: the 09-24 08:00Z 4h bar printed **2633.31,
  a decisive lower low**. 4h highs have turned down too: 2690.73 → 2698.06 → 2693.42 → 2647.99. Daily closes fall
  2775.61 → 2752.43 → 2684.16 → 2646.84. **Lower highs AND lower lows on 4h inside a falling daily sequence.**
  At 16:00 this category was contradictory and claimable in neither direction.
- **`price_action` — SUPPORTS.** New 24h low 2633.31, bounce rejected **seven times** at 2650.63/2650.17, lower
  highs since. Independent of `trend`: behaviour at one specific level, not higher-timeframe structure.
  **Weakened in real time inside the check** — the 12:05Z bar reclaimed 2642.12 → 2646.61.
- **`volume` — ACTIVELY OPPOSES.** Mean 5m volume falls through every leg: **selloff 186,447 → bounce 130,335 →
  fade 106,687**, against a 40-bar median of 133,740. The leg a short would join has *less* participation than
  the bounce it fades. The 12:00Z 1h bar has traded **247,627 against 1.33M–2.18M** on each of the preceding ten
  hours.
- **`market_context` — NOT claimed, on independence.** ETH −2.858% sits between BTC −2.512% and SOL −2.916%, with
  XRP −6.05% the outlier. The category would assert only "crypto is down" — the identical observation that makes
  `trend` down. One observation, not two. *(Note the 16:00 disqualifier — figure instability — did not recur; the
  refusal rests on independence alone.)*
- **`derivatives` — NOT claimed.** Funding fully clamped, OI flat to 0.0041%.
- **`news` — RECORDED, NOT CLAIMED, AND A REASON NOT TO TRADE.** The Trump–Xi summit is in Washington **today**,
  with trade, technology, AI, tariffs and Iran in focus, and the reported set-up is explicitly **binary**. The
  24-hour holding limit means **anything opened now is carried straight through it.**

**Count: two independent categories (`trend`, `price_action`). The gate PASSES for the first time.** It changes
nothing. **The gate was never the binding constraint, and this check is the proof.**

## Reasons not to trade, and the decision

Six independent refusals, any one sufficient:

1. **L-004 span** — against the honest N nothing comes close: **FAIL by 1.215pp / 1.096pp / 0.838pp (short) and
   0.941pp / 0.840pp (long)**. The only constructions that pass do so against the flattered window.
2. **L-004 target validity** — the short's 2633.31 **jumps five supports (12, 11, 8, 6 and 3 touches) to reach a
   level touched once.**
3. **L-002** — both stops sub-noise against the honest window (**0.31x and 0.96x N**), and the short's 2651.20
   sits **0.09% above a level touched seven times**, six of them consecutively.
4. **L-003** — the short's ratio **inflated 3.8x, 0.563 → 2.152**, purely by drifting toward a fixed stop, crossing
   the floor at the instant the stop went sub-noise **and at the instant the premise broke.**
5. **L-005** — the side both trades must cross went to **double digits twice in one check (66 and 108 USDT)**.
6. **Evidence** — `volume` actively opposes the short, and `news` carries any entry through the Trump–Xi summit.

**Decision: `no_trade`.** Best candidate ETHUSDT short, refused six ways, **with the evidence gate passing.**

## For the 21:00 check (13:00Z)

1. **THE GATE IS NOW THE EASY PART — SAY SO EXPLICITLY.** `trend` turned claimable down at this check and will
   likely still be claimable at 21:00. **Do not let a passing gate read as progress toward a trade.** The binding
   constraints are span, target validity, stop geometry and the book, and all four failed by wide margins.
2. **RE-DERIVE N — THE 09:30Z BAR (0.551%) LEAVES THE WINDOW SOON.** At 21:00 a twelve-bar window will not
   contain it and N will collapse toward ~0.20%, **mechanically making the same stops look acceptable on the same
   structure.** That is the exact trap L-002 and L-006 describe and the 21:00→22:00 BNB sequence on 09-23
   demonstrated to two thousandths of a percent. **The binding window is the one containing the bar that created
   the level being traded.**
3. **THE 21:00 BAR IS THE US OPEN AND THE STRATEGY SAYS A BREAKOUT THAT HAS NOT HELD IS NOT EVIDENCE YET.**
   Combined with the summit, treat the first bars after 13:00Z as unreadable rather than informative.
4. **ETHUSDT LEVELS AT THIS CHECK — re-derive, do not reuse:** resistance **2650.63/2650.17 (7 touches)**,
   2647.99/2647.72 (11); support **2643.20 (12)**, 2642.56 (11), 2640.06 (8), 2637.86 (6), 2635.87 (3),
   **2633.31 (1 — the 24h low, and the thinnest level on the board).** Do not reuse 2651.20 / 2632.80.
5. **BNBUSDT STAYS EXCLUDED AND ITS 5m WINDOW IS NOW CLEAN — STATE THE 4h AND DAILY EXPLICITLY.** The 09-24
   00:00Z 4h bar (16.0x) and the 09-24 daily bar (6.0x) still carry 780.90. **A clean 5m scan and a released
   high24h are the flicker, not the recovery.** The 4h bar ages out at 09-25 00:00Z; the daily bar does not age
   out today at all.
6. **FIVE BOOK SAMPLES MINIMUM AND TREAT THE ENGINE QUOTE AS ONE.** ETH collapsed **twice** in this check with
   full recoveries between. A healthy sample immediately after a collapse means nothing.
7. **FUNDING SETTLES 16:00Z = 00:00 LOCAL.** The 00:00 check sits on it. All five rates are now clamped (four at
   the cap, BNB at zero) — `derivatives` carries no information and should not be claimed.
8. **THE TRUMP–XI SUMMIT IS TODAY AND THE 21:00–02:00 CHECKS SIT THROUGH AND AFTER IT.** Reporting frames the
   outcome as binary. **Justify any entry through the event, not around it.**
9. **L-002's TALLY STANDS AT ONE OF THREE.** The two 23:00 BNB constructions remain live and unresolved; their
   only resolution was an artifact touch at 780.90. **Whether that should count is the review's call.**

## Lessons applied

- **L-001** applied at **5m/1h/4h/daily plus the cross-contract test**. BNBUSDT stays excluded on an **unrevised**
  4h (16.0x) and daily (6.0x) print despite a clean 5m window and a released `high24h`. BTCUSDT excluded a
  **twenty-first** consecutive check; SOLUSDT an **eleventh**; XRPUSDT excluded on a 33.9x 4h bar. **ETHUSDT is
  the only readable contract for a second consecutive check** — and its three 1h flags were each **cleared** by
  cross-contract comparison, which is what kept the tradable set from being empty.
- **L-002** applied and **decisive for a twelfth consecutive check**, with the **magnet clause independently
  decisive** (stop 0.09% above a seven-touch level). N stated **four ways**; binding reading 0.551%. **Tally NOT
  advanced; stands at one of three.**
- **L-003** applied, **thirteenth consecutive material check**, producing **the strongest pathological instance of
  the experiment**: a **3.8x inflation across the 1.5 floor** from drift alone, crossing at the exact instant the
  stop went sub-noise *and* the premise broke. The legitimate form ran simultaneously on the long. **Clock ZERO.**
- **L-004** applied **FIRST, before any ratio**, refusing **all five constructions** on span and the only
  floor-clearing construction on target validity — a target reached by jumping five supports to a one-touch level.
- **L-005** applied with **five sweeps plus the engine quote**, a **twelfth consecutive check**, producing a **new
  form: two collapses to double digits inside one check** on the side both trades must cross.
- **L-006** applied to every window-derived figure. The **primary instance was predicted in advance by the 16:00
  note and confirmed** — BNB's artifact left the 5m and 24h-high windows while the 4h and daily contamination did
  not move. **Recorded against interest**: the 24h figures were stable this check, so the 16:00 instability
  instance did not recur; the category is still refused, on independence alone.

**No lesson was loosened, reinterpreted, retired or overridden; no rule or risk limit was relaxed. Nothing under
`reviews/` was read for modification or modified. No script, config, watchlist, schedule or safety switch was
touched. No order API was called except through `paper_engine.py`. All market data was read from read-only public
endpoints on the demo host.**
