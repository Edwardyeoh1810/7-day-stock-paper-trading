# Research note / 研究记录 — 2026-09-24 16:00 (slot 2026-09-24_check_1600)

- Run: `2026-09-24_check_1600-research`
- Slot scheduled: 2026-09-24T16:00+08:00 — run started 16:03:48+08:00, observation 08:04:07Z, five book sweeps
  08:05:18Z–08:10:59Z, decision ~16:15. **On time (11 minutes), not a late run.** Fourteenth consecutive on-time
  check since the 09:00 stall on 09-22.
- Account: **flat**, 5000 USDT cash and equity, no positions, no open orders, nothing to reconcile. No exit order
  has ever been placed in this experiment.
- Decision: **no_trade**. Best candidate **ETHUSDT short** — and ETH is now the *only* candidate available.

## Headline

**BNBUSDT printed a demo artifact at 02:45Z and is excluded under L-001. ETHUSDT is now the ONLY readable
contract in the experiment — the first check at which four of five contracts are excluded.**

The 09:00 note asked the falsifiable question: **does BNB leave the 765.20 / 769.15 box, and which way?** It
left **upward** — but the answer is contaminated, because the same window contains a print the market never made.

**The single most important finding of this check: the 780.90 print is an artifact, and it "resolved" BOTH of the
declined 23:00 constructions at once — hitting the long's target and the short's stop at the identical price.**
Under the strategy's artifact rule neither resolution counts. **L-002's tally is NOT advanced.**

## THE ARTIFACT — BNBUSDT 02:45Z, 780.90

The 09-24 02:45Z BNBUSDT 5m bar reads **O772.94 H780.90 L772.37 C774.09**:

- **0.881% upper wick on a 0.149% body = 5.9x**
- range **1.104%** against a BNB 5m frame median of roughly 0.15% = **~7x the frame median**
- **fully retraced inside its own bar** (close 774.09, only 0.15% above the open)

**Cross-contract comparison at the same 02:45Z candle — no other contract shows anything:**

| contract | 02:45Z 5m range | upper wick |
|---|---|---|
| **BNBUSDT** | **1.104%** | **0.881%** |
| ETHUSDT | 0.093% | 0.015% |
| BTCUSDT | 0.129% | 0.000% |
| XRPUSDT | 0.233% | 0.000% |
| SOLUSDT | 0.504% | 0.000% |

This is the strategy's artifact definition met exactly — "a single candle with a wick of many percent that none of
the other four contracts shows". It is **unrevised and live in the current window**, and it propagates into:

- the **09-24 02:00Z 1h bar** (H780.90, 1.086% upper wick, range 2.191% against neighbours of 0.285% and 0.985%)
- the **09-24 00:00Z 4h bar** (O767.82 H780.90 L764.10 C767.00 — a **1.704% upper wick on a 0.107% body = 15.9x**)
- the **09-24 daily bar** (H780.90)

**BNBUSDT is therefore caught by L-001 and is excluded.** `high24h` reads 791.04, which comes from the 09-23
08:00Z 1h bar and is *not* contaminated — but the 4h and daily highs are.

**A second consequence, which is the subtler one: the artifact corrupts BNB's noise floor N, not merely its
levels.** N measured over any window containing 02:45Z reads **1.104%**, which would inflate the required span to
**2.90%** — so the artifact can make a contract look untradeable as easily as tradeable. Either way the contract
is unreadable, which is precisely what L-001 says to do about it.

## L-002 TALLY — ONE ARTIFACT RESOLVED TWO OPPOSITE CONSTRUCTIONS AT THE SAME PRICE

Both declined 23:00 constructions were carried forward by the 09:00 note as live. Measuring BNB from 23:00Z to
08:05Z: **raw high 780.90 (02:45Z), raw low 764.10 (02:10Z), artifact-excluded high 777.89 (07:30Z).**

| declined construction | entry | stop | target | raw prints | verdict |
|---|---|---|---|---|---|
| 23:00 **long** | 766.85 | 758.55 | **780.90** | target touched **exactly**; stop never approached | **NOT resolved** |
| 23:00 **short** | 766.74 | **780.90** | 757.90 | stop touched **exactly**; target never reached | **NOT resolved** |

**The long's target and the short's stop are the same number, and one artifact wick touched it.** On raw exchange
prints the long won and the short lost, at the identical instant, on the identical tick.

**Neither counts.** The strategy says to "never anchor a stop or target to" an artifact and to exclude it from
range and high/low figures. Excluding the 02:45Z print, BNB's genuine high since 23:00Z is **777.89**, which is
**0.39% short of 780.90**. Both constructions remain **live and unresolved**.

**Tally NOT advanced. It stands at one of three.**

**Recorded explicitly against interest:** a reading that ignored the artifact rule would advance L-002's re-test
clock to **two of three** on the strength of that long — the closest this experiment has come to re-testing a
lesson. I did not advance it, and per the LESSONS.md preamble **whether it should be advanced is the review's
call, not this check's.**

**And this is the experiment's first live demonstration of the strategy's own warning** — "an artifact can still
trigger a resting stop or target, because the exchange acts on its own prices." Had the 23:00 short been open, a
reduce-only stop resting on the demo exchange would have been filled at a price the market never traded. The
account was flat, so it cost nothing. **It is the clearest argument yet for why L-001 excludes whole contracts
rather than merely excluding levels.**

## L-001 artifact scan — 5m / 1h / 4h / daily

**Readable contracts: ETHUSDT only.** This is the narrowest the tradable set has ever been.

- **BNBUSDT — NEWLY EXCLUDED**, on the 02:45Z print above. First exclusion of BNB in the experiment.
- **BTCUSDT — excluded, twentieth consecutive check, contamination completely unchanged.** The 09-21 daily still
  reads **O81,144.10 H95,804.10 L81,079.00 C86,523.40 — an 11.437% upper wick on a 6.629% body, 18.147% range**
  against neighbouring daily ranges of 1.412%, 1.508%, 1.612%. Nothing has been revised.
- **SOLUSDT — excluded, tenth consecutive check.** The 09-22 daily still reads **L106.67 — a 9.941% lower wick on
  a 0.345% body, 28.8x**, and the 09-22 19:00Z 1h bar still carries the 570x print. 24h quote volume **436.0M USDT
  against 104–133 BILLION** for the other four — a ~250x shortfall, unchanged.
- **XRPUSDT — excluded.** The 09-23 04:00Z 4h bar still reads **O1.6177 H1.6855 on a 0.124% body — a 4.191% wick,
  33.8x** — and the 09-23 daily still reads H1.6855 (7.227% wick). **`high24h` has now stopped reading 1.6855 and
  reads 1.6185**, exactly as the 09:00 note predicted in advance (the print left the 24h window at 09-24 04:00Z =
  12:00 local). **Per L-006 this is the window moving, not XRP becoming readable.** The print is still live in the
  4h and daily frames. **XRP stays excluded.**

## L-006 — three instances, and one of them moved while I watched it

**(1) XRPUSDT's 24h figure, predicted and confirmed — and it dissolves.** XRP's 24h change read **−7.099%** at
08:04Z against a pack of −1.60% to −1.97%, an apparently enormous relative weakness and exactly the kind of
crossing a check waits for. **XRP's price did not move**: 1.5006 at the 09:00 check → **1.5036** now, i.e. *up*
0.20%. The entire −1.34pp deterioration in the relative figure since 09:00 is **the reference point rolling
forward** — 24h-ago moved from ~1.593 to 1.6158, the top of XRP's 09-23 spike day. **Dissolves. Cannot be used.**

**(2) The same figure moved 0.305pp in FOUR MINUTES, in front of me.** Between the 08:04Z and 08:08Z ticker
reads, with price essentially static:

| contract | 24h chg 08:04Z | 24h chg 08:08Z | move |
|---|---|---|---|
| **XRPUSDT** | −7.099% | **−6.794%** | **+0.305pp** |
| ETHUSDT | −1.972% | −1.788% | +0.184pp |
| BTCUSDT | −1.963% | −1.901% | +0.062pp |
| BNBUSDT | −1.601% | −1.733% | −0.132pp |
| SOLUSDT | −1.969% | −1.945% | +0.024pp |

**This is the strongest L-006 instance the experiment has produced, because it is not a reconstruction — it is the
window visibly moving inside one check.** Any `market_context` claim resting on a 24h relative figure at this
moment is resting on a number that changes by more in four minutes than the spread between four of the five
contracts. **Recorded as a reason not to claim the category.**

**(3) SOLUSDT's `low24h` still reads 113.03, not 106.67** — the release recorded at 09:00 persists, and the
artifact remains live in the 1h, 4h and daily frames. **Dissolved, and stays dissolved.**

## Structure — BNB left the box upward, but the answer is unusable

**Recorded for the review even though BNB is excluded, because the 09:00 note asked a falsifiable question.**

BNB left the 765.20 / 769.15 box **upward**, clearing 769.15 at ~04:40Z and never re-entering. It then ground
**766.05 (04:00Z) → 777.89 (07:30Z), +1.54% over 3h30m**, on unbroken 5m higher lows.

**But it did not meet the 09:00 note's own stated criterion.** The note required "a close outside on **expanding
volume**". Breakout-bar volumes were **741k, 454k, 727k, 813k** against a window median of roughly 400–500k and a
window maximum of **1,178k** (06:20Z) — entirely ordinary. **The close outside happened; the volume expansion did
not.** Under the note's own test the picture did not change, and the artifact makes the point moot.

**ETHUSDT — the only readable contract.** Range **2679.09 – 2698.06 = 0.708%** over the last ~75 minutes.

- **Resistance 2696.48 — touched exactly three times (07:30Z, 07:35Z, 07:40Z)**, then broken to **2698.03/2698.06
  (07:50Z, 07:55Z)**, with **2697.41 (05:05Z)** in the same cluster.
- **The breakout failed inside one bar**: 07:55Z opened 2698.03 and closed 2692.23, a 0.215% body reversal, and
  price has printed **lower lows since — 2691.08, 2688.95, 2688.91.**
- **Support 2679.09 — held twice (07:00Z, 07:05Z)**, with 2684.22 (06:50Z/06:55Z) and 2685.74 between.
- Entry region 2688.95–2690.96, i.e. roughly mid-range.

## L-002 / L-006 — N stated four ways, and the honest reading is 2.3x the flattered one

| ETHUSDT N | value | 2.5N + 0.14% required span |
|---|---|---|
| full preceding hour (12 closed bars, 07:10Z–08:05Z) | **0.228%** (07:30Z and 07:55Z tie) | 0.710% |
| excluding those bars | 0.169% | 0.563% |
| wider 26-bar window (~2h10m) | 0.228% (same bars) | 0.710% |
| **window containing the bar that BUILT the resistance being traded** (05:05Z, which printed 2697.41) | **0.515%** | **1.4275%** |

**The 05:05Z bar is the setup-defining bar** — it created the 2697.41 high that forms the upper third of the
2696.48–2698.06 cluster every construction here is priced against. Per L-002's amendment and L-006, **the binding
measurement is the one whose window contains it: N = 0.515%, required span = 1.4275%.**

*The 09:00 note predicted this: "if the US pre-session prints anything real, N and the required span JUMP BACK
toward 0.40–1.15%." BNB's N went **0.159% → 0.313%** and ETH's honest N is **0.515%. The forecast was correct.***

## L-004 span screen — run FIRST, and it refuses both constructions decisively

Entry prices from the 08:05:18Z sweep. Drag 0.14% round trip.

| construction | risk | xN(hour) | **xN(honest)** | nearest-target NET RR | span vs required | verdict |
|---|---|---|---|---|---|---|
| **ETH short** E2690.97 S2698.30 T2684.22 | 0.272% | 1.19x | **0.53x** | **0.407** | 0.522% vs **1.4275%** | **FAIL by 0.906pp** |
| **ETH long** E2691.10 S2678.90 T2696.48 | 0.453% | 1.99x | **0.88x** | **0.132** | 0.652% vs **1.4275%** | **FAIL by 0.776pp** |

**Both stops are sub-noise against the honest window (0.53x and 0.88x N) and L-002 refuses both outright,
independently of the span.**

**These are not near-misses.** At 09:00 the best candidate missed by **0.003pp**; here the misses are **0.906pp
and 0.776pp — roughly 300x and 260x larger.** The structure on the only readable contract does not remotely offer
the span.

**And every construction that passes the 1.5 floor does so only by jumping structure (L-004 target validity):**

- **ETH short → 2666.20** (net 2.643): jumps **2684.22**, **2679.09 (held TWICE at 07:00Z and 07:05Z)**, 2675.76
  and 2674.91 — four intervening supports. The nearer targets **2684.22 (0.407), 2679.09 (0.986) and 2675.76
  (1.415) all fail the 1.5 floor**, the last by 0.085.
- **ETH long → 2717.02** (net 1.851): jumps **2696.48 (three touches), 2697.41 and 2698.06 (two touches)** and
  then reaches **0.70% into a structural vacuum** with nothing in between. The nearer targets 2696.48 (0.132) and
  2698.06 (0.277) both fail badly.

**Additionally, L-002's magnet clause refuses the short's stop on its own terms:** 2698.30 sits **0.009% above
2698.06, touched at 07:50Z and 07:55Z — ten and fifteen minutes before this decision.** That is the lesson's
original formulation verbatim.

## L-003 requote — twelfth consecutive material check, both forms again inside one check

**The legitimate form — ETH short, fixed stop 2698.30 / target 2684.22, five quotes over 341 seconds:**

| quote | bid | risk | reward | NET RR |
|---|---|---|---|---|
| s1 08:05:18Z | 2690.97 | 0.272% | 0.251% | **0.407** |
| s2 08:07:16Z | 2690.53 | 0.289% | 0.235% | 0.327 |
| s3 08:09:07Z | 2690.53 | 0.289% | 0.235% | 0.327 |
| s4 08:09:46Z | 2688.95 | 0.348% | 0.176% | **0.103** |
| s5 08:10:59Z | 2689.52 | 0.326% | 0.197% | 0.175 |

Price drifted **away** from the fixed stop: **risk grew 0.272% → 0.348% while reward shrank 0.251% → 0.176%**, and
the ratio decayed **0.407 → 0.103, a 75% fall**. Chasing it means widening risk to keep the target, which is a
refusal. **The span screen fails at all five quotes.**

**The pathological form — ETH long, fixed stop 2678.90 / target 2696.48:** the ratio **doubled, 0.132 → 0.270**,
entirely because the ask drifted **2691.10 → 2689.78 toward the fixed stop**. Both halves improved from one cause
(risk shrinking 0.453% → 0.405%), and **at that same instant the stop fell from 0.88x to 0.79x N against the
honest window — deeper into sub-noise.** It never came near 1.5, but it is L-003's warning in pure form.

**Clock stays at ZERO.**

## L-005 — five sweeps in 341 seconds, and FOUR healthy samples meant nothing

| contract | worst bid | worst ask | note |
|---|---|---|---|
| **ETHUSDT** | **40.3 USDT (s5)** @ 0.967 bps | 1,103,022 (s5) | **held both sides s1–s4, then collapsed** |
| BNBUSDT | **54.2 USDT (s5)** | **248.4 (s1)**, 2,602.1 (s5) | both sides unquoted again; excluded regardless |
| BTCUSDT | **9,153 (s3)**, 72,332 (s5) | **84.5 USDT (s4)** | smallest ask of the check |
| SOLUSDT | **1,015.7 (s4)** | **232.0 (s2)**, 1,081.4 (s5) | excluded regardless |
| XRPUSDT | 678,283 (s2) | 621,321 (s2) | **only contract to hold both sides across all five** |

**ETHUSDT is the finding, and it is the largest bid collapse in the experiment's record.** Its bid went
**2,841,844 USDT (s4) → 40.3 USDT (s5) in 73 seconds — a 70,517x collapse**, beating the previous record (BNB's
7,497x at 09-23 22:00) by nearly tenfold. **A maximum 2,500 USDT market sell is 62x the entire visible bid.**

**This refuses both ETH constructions independently of every geometric finding above:**

- **ETH short** sells into the bid → **40.3 USDT at s5.** Refused.
- **ETH long** exits into the bid, **and its reduce-only stop rests on that side between checks** → same 40.3 USDT.
  Refused.

**L-005's core claim — "a single healthy sample means nothing on this host" — is now demonstrated at four
samples.** ETH held both sides at s1, s2, s3 and s4 and was the best book of the five throughout; the
fifth sample erased it. The previous strongest form of this was three samples (09:00 and 02:00).

**No contract breached the 25 bps cap. The widest spread of the entire check was 10.391 bps (SOLUSDT, s3/s4), and
the 40.3 USDT ETH bid quoted 0.967 bps. The cap was blind to all of it — an eleventh consecutive check.**

**Recorded against interest:** XRPUSDT held both sides across all five sweeps — the first contract of the
experiment to do so — and it is excluded on the artifact, not on the book. The book filter and the artifact filter
disagreed for the first time, and the artifact filter is the binding one.

## Funding — and a correction to the 09:00 note

**The 09:00 note wrote that "funding settles 08:00Z = 16:00 LOCAL, so the 16:00 check sits ON the settlement."
That is off by one settlement.** The 08:00Z settlement had **already passed** when this run read the data at
08:04Z; `nextFundingTime` reads **2026-09-24 16:00Z = 00:00 local tomorrow.** **It is the 00:00 check, not this
one, that sits on a settlement.**

**Funding remains clamped and carries no information — a twelfth consecutive check:**

| contract | rate | reading |
|---|---|---|
| BTCUSDT | **+0.010000%** | exactly at the cap |
| SOLUSDT | **+0.010000%** | exactly at the cap |
| ETHUSDT | +0.009417% → +0.009183% | just under the cap |
| BNBUSDT | **0.000000%** | exactly zero |
| XRPUSDT | −0.004380% → −0.004585% | the only unclamped rate |

A long opened now would **pay** into the 16:00Z settlement; a short would **receive**. At +0.0092% on ETH this is
~0.23 USDT on a 2,500 USDT notional — immaterial against a 0.14% round-trip drag.

**Open interest is flat to within 0.0025% on all five across four minutes** (BTC +0.0011%, ETH +0.0010%, BNB
+0.0024%, SOL +0.0001%, XRP +0.0025%). **`derivatives` NOT claimed.**

## Evidence gate — NOT passed, and this time it fails on COUNT as well as independence

Taking the **ETHUSDT short**, the only construction with any structural premise:

- `price_action` — **supports, weakly.** A genuine failed breakout: 2696.48 broke after three touches, reached
  2698.06, and reversed inside one bar to 2692.23, with lower lows since (2691.08, 2688.95, 2688.91). **This is
  the one honest category on the board.**
- `volume` — **OPPOSES.** The 07:00Z 1h volume of **2,168,257 is the highest of the last ten hours** and it came
  on the **up**-move. The rejection bar (07:55Z) traded **309,771** against the preceding up-bar's **345,840** —
  **no expansion on the rejection at all.** Volume argues the breakout attempt, not the failure.
- `trend` — **CONTRADICTORY, so not claimable in either direction.** Daily closes fall 2775.61 → 2752.43 →
  2684.16, but the last three **4h highs RISE** (2681.21 → 2690.73 → 2698.06) and the **4h lows rise** (2641.37 →
  2668.06 → 2666.20 → 2669.37). A short-term uptrend inside a multi-day downtrend supports neither side cleanly.
- `market_context` — **NOT claimable, for two independent reasons.** (a) ETH's 24h reads **−1.972%** against BTC
  **−1.963%** and SOL **−1.969%** — **dead mid-pack, a nine-thousandths-of-a-percent spread from BTC**, so the
  category asserts only "crypto is down", which is the identical observation that would make `trend` down. Per the
  strategy's independence requirement they are **one observation, not two** — the same failure as at 09:00. (b)
  **The figure itself moved 0.184pp in four minutes with price static** (L-006 above), and XRP's apparent −7.099%
  outlier is entirely window movement. **The number is not stable enough to carry a category.**
- `derivatives` — **NOT claimed.** Funding clamped, OI flat to 0.0025%.
- `news` — **RECORDED, NOT CLAIMED.** The **Trump–Xi summit and state dinner are today**, and this check sits
  closer to it than 09:00 did. Anything opened here is held **through** the event under the 24-hour limit. A
  single scheduled event is not two categories, and it is recorded as a **reason not to trade**.

**Count: one category (`price_action`), with `volume` actively opposing it. The two-category minimum is not met.**
At 09:00 the gate failed on independence with two nominal categories; **here it fails on the raw count as well.**
That is a stricter failure, and it is the binding one.

## Reasons not to trade, and the decision

Seven independent refusals, any one of which is sufficient:

1. **L-001** — BNBUSDT is newly excluded on the 02:45Z artifact, leaving **ETHUSDT as the only readable
   contract**. Four of five contracts are out.
2. **L-004 span screen** — both ETH constructions fail at their nearest structural target by **0.906pp and
   0.776pp**, ~300x and ~260x larger than the 09:00 near-miss.
3. **L-004 target validity** — every construction that clears 1.5 does so only by jumping four intervening
   supports (short) or three rejected highs into a 0.70% vacuum (long).
4. **L-002** — both stops are sub-noise against the honest window (**0.53x and 0.88x N**), and the short's stop
   sits **0.009% above a level touched twice ten minutes before the decision**.
5. **L-003** — the requote decays the short **0.407 → 0.103 (−75%)** and doubles the long purely by shrinking its
   risk while its stop goes deeper sub-noise.
6. **L-005** — the side both trades must cross collapsed to **40.3 USDT**, the largest collapse on record, **after
   four consecutive healthy samples**.
7. **Evidence gate** — only one honest category, with `volume` opposing it. And **news**: anything opened now is
   carried through the Trump–Xi summit.

**Decision: `no_trade`.** Best candidate ETHUSDT short, refused seven ways.

## For the 20:00 check (12:00Z)

1. **THE ARTIFACT IS THE STORY. Re-scan BNBUSDT at 5m/1h/4h/daily and state whether 780.90 has been revised.**
   It will still sit in the 09-24 daily bar and the 00:00Z 4h bar at 20:00. **BNB stays excluded until a full
   clean day including the higher frames — do not let the 5m window rolling past 02:45Z read as a recovery;
   that is precisely the L-006 flicker.** If BNB is excluded and ETH is refused, **the tradable set may be
   empty, and that is an acceptable finding, not a problem to solve.**
2. **DO NOT ADVANCE L-002's TALLY WITHOUT RE-READING THE ARTIFACT SECTION ABOVE.** Both 23:00 constructions —
   short 766.74/780.90/757.90 and long 766.85/758.55/780.90 — are **still live**, because their only resolution
   was an artifact touch at 780.90. The artifact-excluded high since 23:00Z is **777.89**. Tally stands at
   **one of three**. Whether the artifact touch should count is **the review's call**.
3. **N WILL MOVE AGAIN AND THE HONEST WINDOW IS THE BINDING ONE.** ETH's N is **0.228% on the hour and 0.515%
   on the window containing the 05:05Z bar that built the resistance**. State N four ways again. **BNB's N is
   itself artifact-contaminated (1.104% over any window containing 02:45Z)** — another reason not to price it.
4. **ETHUSDT IS THE ONLY READABLE CONTRACT.** Its levels at this check: resistance **2696.48 (3 touches) /
   2697.41 / 2698.03–2698.06 (2 touches)**; support **2679.09 (2 touches) / 2684.22 / 2685.74**. **Do not reuse
   2698.30 / 2678.90 / 2684.22 / 2696.48 — re-derive from whatever structure exists at 12:00Z.**
5. **FIVE BOOK SAMPLES MINIMUM, READ QUANTITY BEFORE SPREAD, AND TREAT THE ENGINE QUOTE AS A SAMPLE.** ETH held
   **four** healthy samples and then printed a **40.3 USDT bid at 0.967 bps**. Four good samples mean nothing.
6. **XRP's 24h FIGURE IS NOW USELESS AS `market_context`** until the 09-23 spike day fully clears the reference
   window. It moved **0.305pp in four minutes** with price static. Re-state what entered and left the window.
7. **FUNDING NEXT SETTLES 16:00Z = 00:00 LOCAL.** The **00:00 check**, not the 20:00 or 22:00 check, sits on the
   settlement. (This corrects the 09:00 note, which was off by one settlement.)
8. **THE TRUMP–XI SUMMIT AND STATE DINNER ARE TODAY** and the 20:00–02:00 checks sit through and after it.
   **Justify any entry through the event, not around it.**

## Lessons applied

- **L-001** applied with the scan at **5m/1h/4h/daily**, and it is **the primary refusal of this check**.
  **BNBUSDT newly excluded** on a 5.9x wick/body, ~7x frame-median print that no other contract shows and that
  propagates to the 1h, 4h and daily frames. BTCUSDT excluded a **twentieth** consecutive check with the 09-21
  daily 11.437% wick unchanged; SOLUSDT a **tenth**; XRPUSDT excluded with the 4h and daily still carrying 1.6855
  even though `high24h` released it. **ETHUSDT is the only readable contract — a first.**
- **L-002** applied and **decisive for an eleventh consecutive check**. N stated **four ways** on ETH (0.228% /
  0.169% / 0.228% / **0.515%**), with the binding measurement being the window containing the 05:05Z bar that
  built the resistance. Both stops sub-noise (0.53x, 0.88x N); the magnet clause independently bars the short's
  2698.30. **Tally NOT advanced and the reason is recorded at length; stands at one of three.**
- **L-003** applied, **twelfth consecutive material check**, with **both** forms inside it: the legitimate decay
  (short 0.407 → 0.103, −75%) and the pathological inflation (long 0.132 → 0.270 as its stop went 0.88x → 0.79x
  N). Clock stays at **zero**.
- **L-004** applied **FIRST, before any ratio**, refusing **both** constructions on span (by 0.906pp and 0.776pp)
  and every passing construction on target validity.
- **L-005** applied with **five sweeps**, refusing both constructions independently of all geometry for an
  **eleventh consecutive check**, and producing **the largest bid collapse of the experiment (70,517x) after four
  consecutive healthy samples.**
- **L-006** applied to every window-derived figure, producing **three instances, all dissolving**, including the
  first one observed **live inside a single check** (24h figures moving up to 0.305pp in four minutes with price
  static). It is also the reason BNB's exclusion will not lapse when the 5m window rolls past 02:45Z.

**No lesson was loosened, reinterpreted, retired or overridden; no rule or risk limit was relaxed. Nothing under
`reviews/` was read for modification or modified. No script, config, watchlist, schedule or safety switch was
touched. No order API was called except through `paper_engine.py`.**
