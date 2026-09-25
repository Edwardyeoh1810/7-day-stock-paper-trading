# Research journal — 2026-09-22_check_0000-research

Companion to the generated journal entry for `2026-09-22_check_0000_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-21T16:22Z (00:22 Asia/Kuala_Lumpur on 2026-09-22),
  slot `2026-09-22_check_0000`.
- **What was done:** Read AGENTS.md, TRADING-STRATEGY.md, CONTINUITY.md, AUTOMATION-PROMPT.md, readiness.json,
  current-state.json, the 23:00 slot's research note and reviews/LESSONS.md. Ran the read-only observation for the
  due slot, re-researched all five watchlist contracts from the demo host's public endpoints (5m, 1h and 60 daily
  bars, book, 24h ticker, funding), tested the three-part confirmation condition the 23:00 note named in advance for
  XRPUSDT, worked through the short that the same note said would be triggered by a failure, re-verified the 60-day
  overhead scan for all five at current prices, re-ran the artifact scan, and submitted a `no_trade` decision
  through `paper_engine.py`.
- **Why it was done:** The 00:00 slot was due (`due_slot: 2026-09-22_check_0000`, 240 planned slots) and no position
  was open, so a new entry was permitted if and only if every entry condition was met.
- **Timing:** Observation ran at 16:10Z (00:10 MYT), decision submitted at 16:17Z (00:17 MYT) — 17 minutes after the
  slot, inside the 45-minute entry window with 28 minutes to spare. This run was **not** late; an entry would have
  been accepted had one qualified. Worth stating plainly this hour because the XRPUSDT long's reward/risk actually
  **passed** at the decision-time quote and was declined on evidence, not on timing.
- **Order proposed:** No.
- **Order placed:** No. No demo order was sent; the engine returned `status: no_trade`, `live_order_sent: false`.
- **Order filled:** No.
- **Exchange stop/target reconciliation:** None to reconcile. The account was flat before this check and is flat
  after it; no exit order has ever been placed in this experiment.
- **Current holdings:** None. Flat.
- **Current cash:** 5000 USDT. Demo wallet balance 5000.04174826 USDT.
- **Current risk:** 0 USDT open risk; 0 USDT realized today. No daily-limit or consecutive-stop constraint is near.
- **Evidence captured:** `05-交易记录-data/evidence/2026-09-22_check_0000.json` (read-only run),
  `05-交易记录-data/evidence/2026-09-22_check_0000_paper.json` (engine),
  and this note.

## The test set at 23:00 resolved, and it failed on all three parts

The 23:00 note deliberately set this check up so it would not have to re-derive the XRP case: the headline price
trigger had already fired at 15:05Z and had not sufficed, so it was declared spent. What remained was a three-part
condition — **hold**, **hourly volume**, **heaviest 5m bar**. All three failed.

**1. Hold — failed, and became a third rejection.** The requirement was that price still be above 1.4969 a full
45+ minutes after the break rather than eight. It was not, and it never held in between:

| Bar | Open | High | Low | Close |
|---|---|---|---|---|
| 15:05Z | 1.4970 | **1.5077** | 1.4970 | 1.5049 |
| 15:15Z | 1.5016 | 1.5017 | 1.4957 | 1.4958 |
| 15:25Z | 1.4942 | 1.4947 | **1.4849** | 1.4866 |
| 15:50Z | 1.4994 | 1.5011 | 1.4993 | 1.4993 |
| 16:10Z | 1.4952 | 1.4976 | 1.4949 | 1.4954 |

Five consecutive bars (15:15Z–15:40Z) closed beneath 1.4969, with a low of 1.4849 — 1.51% off the high. Counting
the whole session that is **three rejections of the 1.5000–1.5077 zone inside 80 minutes**, on top of the completed
14:05Z failed breakout.

**2. Hourly volume — failed on both comparisons.** The test was the 15Z or 16Z hour exceeding the 13Z hour.

| Hour | Quote volume |
|---|---|
| 13Z | 6,080,932,514 |
| 14Z | 6,047,285,710 |
| 15Z (made the high) | **5,446,947,705** |

The hour that printed the new 24h high traded less than either hour before it.

**3. Heaviest 5m bar — failed.** It is **15:15Z at 905,600,567**, the down bar that erased the breakout
(1.5016 → 1.4958). The heaviest up bar of the stretch is 15:30Z at 634,823,054, 30% smaller.

## The finding of the hour: both directions passed, neither honestly

This is the part worth carrying forward, because it is a cleaner demonstration than anything the day has produced.

At 23:00 the best honest XRP long construction printed **1.499** and was declined. At this check, with the ask down
to 1.4954, the *same* structure prints:

| Stop | Target 1.5270 | Verdict |
|---|---|---|
| 1.4880 | **3.107** | market traded 1.4863 twice at 15:30Z/15:35Z — stop already violated |
| 1.4849 | **2.343** | sits exactly on the 15:25Z low |
| 1.4765 | 1.405 | the only stop the tape has not violated — **fails** |

**Every named condition got worse and the ratio doubled.** Nothing improved; the entry simply fell 0.41% toward
fixed stops. That is the drift trap the 22:00 and 23:00 notes named in advance, now shown at six times the
amplitude of the 0.0010 drift that prompted the original warning. And the only stop the market has *not* traded
through is the one that fails.

The short the 23:00 note predicted was then worked through in full, because its trigger genuinely fired — price
was back below 1.4969, making the 15:05Z break a second failed breakout. From the 1.4953 bid with the stop above
the 1.5077 session high (1.5085, 0.90% risk):

| Target | Net R/R |
|---|---|
| 1.4849 — the low the last rejection produced | **0.543** |
| 1.4765 — the 14Z low, base of the first failed breakout | **1.093** |
| 1.4710 — two levels deep, asks for a 1.6% fall | **1.452** |

Not one honest stop clears the floor. The only construction that does is a **1.5020 stop with a 1.4765 target at
1.900** — and 1.5020 sits *below* the 1.5077 high that is the entire premise of the trade. The defining print
would take the stop out. That is a stop fitted to a size, and it is the identical error the 23:00 note refused on
the long side.

So both directions produced a passing ratio on *some* construction and neither produced one on an honest stop.
That is the strongest evidence yet that XRP's ratios this session are manufactured by geometry, not earned by edge.

### The market settled it three minutes later

The most valuable single data point of the check is accidental. When `paper_engine.py` re-read the book at
**16:17:23Z** — three minutes after the 16:14:23Z decision quote of 1.4953/1.4954 — it returned **1.5019/1.5020**.

XRP rallied **0.44% in three minutes**, back above 1.4969, above 1.5011, and **through the 1.5020 fitted stop**.
Had this check taken the only short construction that passed the reward/risk floor, it would have been stopped out
within three minutes of entry, for a full 0.5% loss, on a move that carried no new information. The prohibition on
fitting a stop to a size is usually justified in the abstract; here it was demonstrated inside one engine call.

It also retrospectively vindicates declining the long on evidence rather than arithmetic: price went *up*, which
would have looked like vindication of the long, but it did so without ever satisfying the volume or hold
conditions — a coin landing heads does not make the call correct.

## SOLUSDT and BNBUSDT changed status, and both fail on the same geometry

The one genuinely new development: both contracts pulled back off today's highs, so for the first time each **has
an overhead reference**. The 23:00 objection — no target exists, so reward/risk is meaningless — is gone. It is
replaced by the upside-down geometry that has disqualified XRP all day.

| | Ask | Target | Distance | Own 15Z hourly range |
|---|---|---|---|---|
| SOLUSDT | 117.61 | 118.9100 | **1.10%** | 117.36–118.91 = **1.32%** |
| BNBUSDT | 801.23 | 806.090 | **0.61%** | 797.670–806.090 = **1.06%** |

Both targets sit inside a single hour of the contract's own range. SOL clears at 2.391 only with a 117.30 stop —
0.28%, smaller than several individual recent 5m bars (15:15Z spanned 0.71%, 16:00Z 0.57%) and four ticks under the
117.36 shelf that printed as the low of three consecutive bars. Honest stops beneath that shelf give 1.465 (117.00)
and 1.066 (116.71). SOL's volume opposes as well: the two heaviest 5m bars of the 15Z–16Z stretch, 7,985,396 at
15:15Z and 7,839,238 at 15:20Z, are both the down bars that rejected 118.9100.

BNB fails harder — 1.310 even on the fitted 799.50 stop, 0.798 on an honest one — though its spread recovered from
35.78 bps to **4.37 bps**, so the engine-level disqualification from 23:00 is gone. All five spreads are inside the
25 bps limit for the first time in several checks.

## ETHUSDT printed the experiment's first non-BTC artifact

The **15:50Z 5m bar**: open 2749.66, close 2750.66, low 2749.50 — a body of 0.04% — with a high of **2795.00**, an
upper wick of **1.61%**. Cross-checked against the same five minutes on every other contract:

| | Move above close |
|---|---|
| BTCUSDT | 0.08% |
| BNBUSDT | 0.09% |
| SOLUSDT | 0.06% |
| XRPUSDT | 0.12% |

Nothing else moved a tenth of what ETH supposedly did. It is an artifact, it contaminates ETH's 15Z hourly high,
and it is the **first artifact on a contract other than BTC** in the experiment — which matters for the review,
because the working assumption so far has been that the defect is BTC-specific. It is not.

BTC itself printed a **seventh** artifact at 15:05Z (86999.00, a 0.92% upper wick, no counterpart). With it, the
95804.10 pair and the 12Z 87888.00 print excluded, the 60-day scan finds no valid daily high above BTC's ask
anywhere, so BTC remains untradeable under the rule covering contracts whose structure artifacts have made
unreadable.

ETHUSDT itself failed for a sixth consecutive check: it needed 2720.39 or lower and sits at 2746.91, printing
**0.350** net — the worst of the sequence 1.34, 0.55, 1.40, 0.45, 0.38, 0.350.

## Next task focus

Account is flat, so the 02:00 check may open if conditions are met. Four things to carry forward.

1. **XRP is back at 1.5020 as of 16:17:23Z, and the important correction is that NO near-term XRP scenario
   produces an honest trade.** Price has now crossed 1.4969 in both directions four times in two hours; treat
   further crossings as noise, since the level has been tested to exhaustion and no longer discriminates. The
   instinct is to say "a break of 1.5077 makes the long work and a break of 1.4849 makes the short work." **Both
   are false, and the arithmetic should be checked rather than assumed** — it was computed this hour precisely so
   the 02:00 run does not have to re-derive it:

   | Scenario | Construction | Net R/R |
   |---|---|---|
   | Long after a 1.5077 break, ask 1.5100 | stop 1.4849, target 1.5270 | **0.547** |
   | " | stop 1.4849, target 1.5441 | **1.175** |
   | " | stop 1.4940, target 1.5441 | 1.766 — but a 1.06% stop inside the range |
   | Short from a 1.4800 bid | stop 1.5085, target 1.4710 | **0.227** |
   | " | stop 1.5085, target 1.4617 | **0.531** |

   A break upward pushes the entry away from 1.5270 faster than it approaches it, so the long only clears by
   reaching for 1.5441 *and* tightening the stop into the range — the same two errors refused this hour. A break
   downward leaves the honest 1.5085 stop 1.9% overhead, which no target can outrun. **The structural conclusion:
   XRP produces no valid trade until a stop and a target that are both structural sit more than roughly 2.5%
   apart**, which requires either a lower high forming well beneath 1.5077 (bringing the short's stop down toward
   1.4900) or a pullback that holds a level far above 1.4849. Neither exists yet. The middle of the range, where
   this check found it, is simply the clearest case of a condition that currently holds everywhere on this
   contract.
2. **The fitted-stop prohibition now has a concrete case, and it should be cited rather than re-argued.** The only
   short construction that passed the floor (1.5020 stop) was violated by the market three minutes after the
   decision quote. Any future construction whose stop sits inside the range that defines the setup should be
   rejected on sight with reference to this hour, without recomputing the ratio.
3. **SOLUSDT is now the second contract to watch, ahead of ETHUSDT.** It has a valid target (118.9100) and a real
   support shelf (117.36, three consecutive bar lows), and it is the strongest contract of the five. The trade
   becomes honest if price falls to the shelf and holds it: at a 117.45 ask with a 117.00 stop the 118.91 target
   gives **2.108** net — the cleanest prospective setup on the watchlist, and the only one where a structural stop
   and a structural target are far enough apart to work. Do not take it from the middle — at 117.61 the only
   passing stop is 0.28%, which is the error described in item 2. Re-verify that 118.9100 has not been invalidated
   by a new high first.
4. **ETHUSDT drops to fourth and should be checked once, mechanically.** The threshold is **2720.39 or lower** for
   1.50 net on the unchanged 2693.00/2771.00 structure — unchanged from the 23:00 note, because the stop and
   target are fixed, so the threshold does not move with the current ask. It is 26.52 below the current ask. Six
   consecutive failures. Do not re-examine it unless it has actually fallen that far. BTCUSDT
   stays excluded on artifacts; re-run the artifact scan on **all five** rather than BTC alone, since ETH has now
   shown the defect is not BTC-specific.

## Human confirmations needed

None for demo paper trading; live trading remains disabled. Four items for Edward's awareness, none requiring
action before the next check. **(a)** The demo artifact defect has spread beyond BTC: ETHUSDT printed a 1.61%
phantom wick to 2795.00 at 15:50Z, the first non-BTC artifact of the experiment, alongside BTC's seventh. **(b)**
BTCUSDT's reported 24h high remains an artifact, leaving the contract with no valid overhead reference in sixty
days — it has now been untradeable for four consecutive checks for structural reasons. **(c)** The standing
open-interest endpoint limitation on the demo host still reduces the `derivatives` category to funding alone.
**(d)** The missed 16:00 slot recorded by the 20:00 note remains an open coverage question for the review. The
22:00 daily review owns `reviews/` and may be running concurrently; `LESSONS.md` was read (still empty — no closed
trades) and nothing in that folder was modified.
