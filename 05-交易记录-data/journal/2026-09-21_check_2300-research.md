# Research journal — 2026-09-21_check_2300-research

Companion to the generated journal entry for `2026-09-21_check_2300_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-21T15:18Z (23:18 Asia/Kuala_Lumpur), slot `2026-09-21_check_2300`.
- **What was done:** Read AGENTS.md, TRADING-STRATEGY.md, CONTINUITY.md, AUTOMATION-PROMPT.md, readiness.json,
  current-state.json, the 22:00 slot's research note and reviews/LESSONS.md. Ran the read-only observation for the
  due slot, re-researched all five watchlist contracts from the demo host's public endpoints (5m, 1h and 60 daily
  bars, book, 24h ticker, funding), tested the two conditions the 22:00 note named in advance for XRPUSDT and
  ETHUSDT, re-verified the 60-day overhead scan for all five at current prices, re-ran the artifact scan, and
  submitted a `no_trade` decision through `paper_engine.py`.
- **Why it was done:** The 23:00 slot was due (`due_slot: 2026-09-21_check_2300`, 240 planned slots) and no position
  was open, so a new entry was permitted if and only if every entry condition was met.
- **Timing:** Observation ran at 15:10Z (23:10 MYT), decision submitted at 15:15Z (23:15 MYT) — 15 minutes after the
  slot, well inside the 45-minute entry window. This run was **not** late; an entry would have been accepted had one
  qualified. The `no_trade` is a judgement on the setups, not a timing artefact. Worth stating plainly this hour
  because XRPUSDT came closer to qualifying than anything has all day.
- **Order proposed:** No.
- **Order placed:** No. No demo order was sent; the engine returned `status: no_trade`, `live_order_sent: false`.
- **Order filled:** No.
- **Current holdings:** None. Flat.
- **Current cash:** 5000 USDT. Demo wallet balance 5000.04174826 USDT.
- **Current risk:** 0 USDT open risk; 0 USDT realized today. No daily-limit or consecutive-stop constraint is near.
- **Evidence captured:** `05-交易记录-data/evidence/2026-09-21_check_2300.json` (read-only run),
  `05-交易记录-data/evidence/2026-09-21_check_2300_paper.json` (engine),
  `05-交易记录-data/evidence/2026-09-21_check_2300-research.json` (research).

## The complex turned back up, and the 22:00 warning did not play out

The 22:00 note's closing line named one thing to watch: the complex had given back ground for the first time today,
and if that continued the question would shift to whether the 08:00Z impulse was being surrendered. It did not
continue. Every contract but ETH gained, and four of five made new session highs:

| | 21:00 | 22:00 | 23:00 |
|---|---|---|---|
| SOLUSDT | +8.25% | +8.82% | **+9.742%** |
| XRPUSDT | +8.16% | +7.18% | **+8.516%** |
| BTCUSDT | +5.87% | +5.67% | **+6.755%** |
| BNBUSDT | +5.15% | +5.04% | **+6.036%** |
| ETHUSDT | +6.08% | +5.67% | +5.631% |

XRP went from weakest of the five back to second strongest in one hour, reversing the relative-strength reading that
counted against it at 22:00. So the hour's headline is that the setup the 22:00 note declined got better, not worse —
which is why this check needed working through carefully rather than dismissed.

## XRPUSDT: the trigger fired, and the trade still fails

The 21:00 note named `1.4969` — a break **and hold** above today's high, on expanding volume. The 22:00 note
restated the bar for re-opening XRP as a long: **back above 1.4894 and holding, with volume on the up bars rather
than the down ones.** The price half fired. The other two halves did not.

**What happened.** After the 14:05Z failed breakout bottomed at 1.4765, XRP rebuilt through 14:15Z–15:05Z and the
15:05Z 5m bar opened 1.4970, printed a new 24h high of **1.5077** and closed 1.5049 — above 1.4969 and well above
the 1.4894 level of 09-14 it had lost an hour earlier. A genuine reclaim of a failed breakout.

**Why it was still declined — three independent reasons, any one sufficient.**

**1. The volume condition failed, and it was the precondition named in advance.** In the whole recovery window the
largest 5m bar is **671,693,897 at 14:55Z — a down bar**: open 1.5022, high 1.5039, low 1.4945, close 1.4963. The
bar that actually made the new high, 15:05Z, traded only 435,222,016, *less than the rejection that preceded it*.
On the hourly frame the reclaiming 14Z hour printed 4,055,848,100 against 4,089,988,720 in the 13Z hour —
contraction, not expansion. The heaviest trade in the window is on the wrong side.

**2. It is not holding.** At decision time the breakout was eight minutes old and had already retraced more than
half of the bar that made it: 1.5077 high and 1.5049 close at 15:05Z, ask **1.5015 at 15:13:50Z** — below that
close. The strategy is explicit that a fresh breakout in the erratic hours after the US open is not evidence yet,
and this tape had already reversed once inside the same hour.

**3. The geometry is upside-down — the structural point, and the most transferable finding of the day.** The
nearest valid overhead level is 1.5270 (08-24 daily high), **+1.70%** from the entry. XRP's own 14Z hourly bar
spanned 1.4765–1.5039, a range of **1.83%**. *The target sits closer than one hour of this contract's current
range.* It is not a 24-hour objective with an edge in front of it; it is inside the noise. Against a target that
close, every structurally honest stop fails:

| Stop | Rationale | Net R/R at ask 1.5015 |
|---|---|---|
| 1.4700 | prior structural low, used all day | **0.70** |
| 1.4765 | low of the 14:05Z failed breakout this leg reversed from | **0.86** |
| 1.4880 | below the 1.4894 level reclaimed | **1.499** |
| 1.4930 / 1.4940 | — | 1.93 / 2.44 |

The only comfortable passes are the 1.4930/1.4940 stops, and those are stops fitted to a size, which the strategy
prohibits: **1.4945 was the low of both the 14:55Z and 15:00Z bars**, so such a stop rests five to fifteen ticks
under a price the market traded within the previous fifteen minutes, in a tape whose last twelve 5m bars average
0.0058 of range and include bars of 0.0094 and 0.0107 — individually larger than the entire stop distance. Even the
defensible 1.4880 stop is inside one hourly bar: price traded 1.4792, below it, 65 minutes earlier.

### Correction: the best construction never actually passed

The decision file's thesis describes the 1.4880-stop construction as printing "exactly 1.50" and sitting "on the
floor". That is a rounding. Computed to three places with the engine's own cost model (5 bps fee and 2 bps slippage
per side), the ask of 1.5015 at 15:13:50Z gives **1.499 — below the 1.50 minimum, not on it.** The conclusion is
unchanged and the trade was declined on the evidence and the geometry regardless, but the arithmetic never passed
either, and the review should read it that way.

The engine's own quote confirmed the point independently. When `paper_engine.py` re-read the book at **15:15:55Z**
it got an ask of **1.5017**, at which the same construction prints **1.468**. Had this check tried to enter on the
1.50 reading, the engine would have rejected it on the reward/risk floor.

### The drift trap, named in advance and sprung on schedule

The 22:00 note left two cautions, and both bit within three minutes of each other:

> quote it at decision time rather than claiming a pass on a drifted price … a fall that clears the floor by
> pushing the entry down is worth less than one where evidence also arrives

At the 15:10:39Z research snapshot the ask was **1.5025** and the 1.4880-stop construction printed **1.349** —
nowhere near. Three minutes later, at 15:13:50Z, the ask had drifted to 1.5015 and the identical construction
printed 1.499. **Nothing about the trade improved; price simply fell 0.0010 toward a fixed stop.** Two minutes
after that it was 1.5017 and the number was 1.468 again. The ratio moved from 1.35 to 1.50 to 1.47 in five minutes
without a single new piece of evidence, which is the clearest demonstration this experiment has produced of why the
ratio must be quoted at decision time and why a number that arrives by drift is not a signal.

## ETHUSDT: the threshold was named, and it moved the wrong way

The 22:00 note made ETH the contract to re-check first and gave the exact figure: **an ask of 2722.68 or lower**
for 1.50 net on the unchanged 2693.00 stop and 2771.00 target, roughly 2710 for real margin, 1.19 away at the time.

It went the other way, to an ask of **2745.69** — 23.01 above the threshold, no longer a near miss. Risk 53.74
against reward 24.21 gives **0.38 net**. Fifth consecutive failure on the same arithmetic:

| 20:00 | 21:00 | 22:00 | 23:00 (research) | 23:00 (decision) |
|---|---|---|---|---|
| 1.34 | 0.55 | 1.40 | 0.45 | **0.38** |

The structure is still valid — 2771.00 is real overhead, 2693.00 a real floor — but ETH has now rallied into the
middle of that pocket and there is no version of this trade that works from here. Its spread, 0.04 bps, was the
tightest on the watchlist; that was never the problem.

## BTCUSDT: two more artifacts, printed this hour

The **14:35Z and 14:40Z 5m bars both print an identical 95804.10 high** — upper wicks of 11.6% and 11.1% against
bodies of 0.24% and 0.55%, on a contract whose spot is 86,243. No counterpart anywhere: in the same ten minutes ETH
ranged 2731.83–2742.56, XRP 1.4931–1.4996, and BNB and SOL moved a few tenths of a percent. Fifth and sixth
confirmed artifacts of the day, all six on BTC.

This one matters more than the earlier four, because **95804.10 is the figure the 24h ticker reports as BTCUSDT's
high** — the contract's entire 24h high is now an artifact. Excluding it leaves BTC with no overhead reference at
all in sixty days, which puts it in the same untradeable position as BNB and SOL for a different reason than
before. Its spread did recover, from 15.37 bps at 22:00 to 2.78 bps, so the book complaint from last hour has
eased; the structural one has not.

A scan of the last six 1h bars on the other four contracts found **no artifact** — no wick above 1.5%, and XRPUSDT
has still produced none at any point today.

## The 60-day overhead scan, re-verified at current prices

Re-run from daily bars rather than carried forward, because prices rose about 1% this hour and it is the fact that
eliminates three of five contracts:

| | Ask | Daily highs above ask in 60 days |
|---|---|---|
| BTCUSDT | 86273.00 | only 95804.10 — **the artifact itself** |
| BNBUSDT | 803.53 | **none** |
| SOLUSDT | 118.63 | **none** |
| ETHUSDT | 2745.69 | 2771.00 (08-21), then today's 2850.00 artifact |
| XRPUSDT | 1.5015 | 1.5270 (08-24), 1.5441 (08-25), 1.5444 (08-23), 1.7000 (08-22) |

BNB and SOL are at 60-day highs with nothing above them. A target has to exist before reward/risk means anything.
BNB additionally blew its spread out to **35.78 bps** at 15:13Z, past the 25 bps limit, so the engine would have
rejected it before any thesis was read.

## No short, and this time it was not close

At 22:00 a short was worked through in detail and rejected at 0.80 net. This hour there is nothing to work through:
the single bearish item that existed — XRP's failed breakout — has been reversed by the reclaim of 1.4894 and
1.4969 and a new 24h high. Four of five extended, the complex is up 5.6–9.7% on the day, and funding at or below
the 0.0100% baseline on all five means there is no crowded long positioning to squeeze. No category points down on
any contract, against a requirement of two.

Funding settles at 16:00Z, about 46 minutes after this check — close enough that a long opened now would pay
0.0100% almost immediately, a real cost against a 1.70% target. BTC funding has drifted marginally negative again
(-0.0000035%) from +0.0021% at 22:00.

## Next task focus

Account is flat, so the 00:00 check may open if conditions are met. Four things to carry forward.

1. **XRPUSDT stays the first contract to re-check, but the bar is now specific and higher.** The headline price
   trigger has already fired and did not suffice, so do not re-run that test. What is missing is *volume* and
   *hold*. Concretely: the reclaim is confirmed only if price is still above **1.4969** at 00:00 — a full 45+
   minutes after the 15:05Z break rather than eight — **and** the 15Z or 16Z hourly bar closes with volume above
   the 13Z hour's 4,089,988,720, **and** the heaviest 5m bar of that stretch is an up bar rather than another
   1.5039-style rejection. If price is back below 1.4969, the 15:05Z break joins the 14:05Z one as a second failed
   breakout inside two hours, which would be a materially bearish development and the first real short candidate —
   though it would still need a second category.
2. **The geometry problem is the thing to solve, and it is not solved by waiting for a better ratio.** XRP's
   nearest valid target, 1.5270, is 1.70% away while the contract's hourly range is 1.83%. Until price either
   clears 1.5270 (putting 1.5441 in play, +2.8%, which is a real 24-hour objective) or falls far enough that
   1.5270 is a genuine distance from a structural stop, **any 1.5 net reading on XRP will be manufactured by a
   tight stop or by drift rather than by an edge.** Specific thresholds if the reclaim does confirm: with a
   1.4880 stop the ask must be **1.5015 or lower** for 1.50 net on the 1.5270 target — which is *below the current
   price*, so a confirming hold that also rallies makes the trade worse, not better. With the deeper and more
   honest 1.4765 stop the ask must be **1.4946 or lower**. These two facts together mean the attractive version of
   this trade is a pullback that holds above 1.4969, not a continuation.
3. **ETHUSDT drops back to second.** It needs **2720.39 or lower** for 1.50 net on the unchanged 2693.00/2771.00
   structure — recomputed this hour and 25.30 below the current ask. That is a 0.9% fall with no change in
   structure, and it has failed five times running. Do not re-examine it unless it has actually fallen that far.
4. **BTCUSDT, BNBUSDT and SOLUSDT remain untradeable, all three for want of an overhead reference.** BTC's
   exclusion is now structural rather than a book complaint: its 24h high is a confirmed artifact printed twice
   this hour. Re-verify the daily scan rather than carrying it forward, since one more hour of gains could put BNB
   or SOL through levels that create a reference — though a new all-time-in-window high does not create one.

The single thing to watch at 00:00 is whether XRP is still above 1.4969. That one fact separates a confirmed
reclaim worth re-examining on a pullback from a second failed breakout in two hours.

## Human confirmations needed

None for demo paper trading; live trading remains disabled. Four items for Edward's awareness, none requiring
action before the next check: the BTCUSDT demo price artifacts, now six for the day and all on BTC, with the
important escalation that the contract's reported 24h high is itself an artifact; BNBUSDT's spread reaching 35.78
bps, past the 25 bps limit, which would block it at the engine regardless of thesis; the standing open-interest
endpoint limitation, which keeps `derivatives` reduced to funding alone; and the missed 16:00 slot recorded by the
20:00 note, still a coverage question for the review rather than something to fix here. The 22:00 daily review owns
`reviews/` and may be running concurrently; `LESSONS.md` was read and nothing in that folder was modified.
