# Research journal — 2026-09-22_check_2300-research

Companion to the generated journal entry for `2026-09-22_check_2300_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-22T15:12Z (23:12 Asia/Kuala_Lumpur), slot `2026-09-22_check_2300`.
- **What was done:** Read AGENTS.md, TRADING-STRATEGY.md, CONTINUITY.md, AUTOMATION-PROMPT.md, readiness.json,
  current-state.json, the **22:00 slot's research note** and `reviews/LESSONS.md` — which is **no longer empty**;
  the 22:00 review task published **three lessons** while the previous check was running. Ran the read-only
  observation for the due slot at 15:04:05Z, then pulled 5m, 1h, 4h and daily bars, the book, the 24h ticker,
  funding and open interest for all five watchlist contracts from the demo host's public endpoints, ran the
  artifact scan at both 5m and 1h, re-implemented the engine's reward/risk formula independently from
  `paper_ledger.py`, took a confirming requote 100 seconds after the first sweep as **L-003** now requires, and
  ran one web search for scheduled news. Submitted a `no_trade` decision through `paper_engine.py`.
- **Why it was done:** The 23:00 slot was due (`due_slot: 2026-09-22_check_2300`, 240 planned slots) and no
  position was open, so an entry was permitted if and only if every entry condition and every lesson was satisfied.
- **Timing:** Observation 15:04:05Z, research 15:04:42Z, requote 15:06:22Z, decision written 15:07Z, engine
  submitted 15:09:50Z (23:09 MYT) — **7 minutes after the slot**. **ON TIME**, second consecutive on-time check
  since the 09:00 stall.
- **Order proposed:** No.
- **Order placed:** No. The engine returned `status: no_trade`, `live_order_sent: false`.
- **Order filled:** No.
- **Exchange stop/target reconciliation:** None to reconcile. Flat before and after; no exit order has ever been
  placed in this experiment.
- **Current holdings:** None. Flat.
- **Current cash:** 5000 USDT. Demo wallet balance 5000.04174826 USDT.
- **Current risk:** 0 USDT open risk; 0 USDT realized today. Ledger date `2026-09-22`, trading day index 2.
- **Evidence captured:** `05-交易记录-data/evidence/2026-09-22_check_2300.json` (read-only run),
  `05-交易记录-data/evidence/2026-09-22_check_2300_paper.json` (engine), and this note.

## LESSONS.md is live, and L-002 decided this check

This is the first check of the experiment with lessons in force. All three applied, and **L-002 was the binding
constraint** — the first time a formal lesson, rather than ad-hoc prior reasoning, determined the outcome.

## The assignment was specific, and the market answered it

The 22:00 note set three outcomes for XRPUSDT around **1.5701** and named outcome (1) as the one setup worth
taking. **Outcome (1) did not happen.**

| Time | XRPUSDT | Event |
|---|---|---|
| 13:55Z | → **1.5875** | Breakout of the 30-day high, +1.535% range |
| 14:00Z | H **1.5876** | The high |
| 14:05Z | L 1.5699 | Back below the broken level (this was the 22:00 check's last observation) |
| 14:35Z | L **1.5393** | **Capitulation — a −3.04% round trip, 1.93% BELOW the broken level** |
| 15:00Z | H **1.5672** | **V-bounce, 58% retracement, four consecutive up bars** |
| 15:06Z (requote) | 1.5636 / 1.5639 | Mid-whipsaw |
| 15:09:56Z (engine quote) | **1.5696 / 1.5701** | **Back exactly on the pivot** |

Price lost 1.5701, kept going to 1.5393, then V-bounced all the way back. That is outcome (3), the chop — which
the 22:00 note correctly called the most likely outcome and a fine one.

**The engine's own quote is the most important line in the table.** Between the requote at 15:06:22Z and the
engine's fill-check at 15:09:56Z — three and a half minutes — XRPUSDT rallied a further **0.40%**, from
1.5636/1.5639 to 1.5696/1.5701, landing **exactly on the pivot it had failed at**. Any failed-breakout short taken
in this check would already have been roughly 0.4% offside before the exit orders were placed. The decision did
not need that confirmation, but it got it.

## The finding: L-002 fires in both directions at the same instant

The largest 5m bar range of the preceding hour is **0.834%** (the 14:35Z capitulation bar). Ranges across that
hour: 0.633, 0.280, 0.540, 0.192, 0.652, 0.386, **0.834**, 0.323, 0.362, 0.290, 0.566, 0.249.

Re-implementing the engine's formula (5 bps fee, 2 bps slippage per side) against the live 1.5636/1.5639 book:

| Side | Stop | Risk | vs 0.834% bar | Best target | Net RR | Verdict |
|---|---|---|---|---|---|---|
| SHORT | 1.5680 (above 1.5672 bounce high) | **0.422%** | **0.51×** | 1.5142 | **7.167** | **L-002 — sub-noise** |
| SHORT | 1.5710 (above the 1.5701 pivot) | **0.614%** | **0.74×** | 1.5142 | **4.924** | **L-002 — sub-noise** |
| LONG | 1.5620 (below 1.5633 shelf) | **0.261%** | **0.31×** | 1.6039 | **9.242** | **L-002 — sub-noise** |
| SHORT | 1.5890 (above the 1.5876 high) | 1.766% | 2.12× | 1.5393 → 0.802; 1.5306 → 1.117; **1.5142 → 1.711** | — | Noise-safe, needs **−3.14%** |
| LONG | 1.5380 (below the 1.5393 low) | 1.795% | 2.15× | 1.5701 → 0.143; 1.5876 → 0.766; 1.6039 → **1.346** | — | Noise-safe, **fails everywhere** |

**Every construction that cleared the 1.5 floor on a modest target used a stop inside the noise bar.** And the
three of them together trip **L-002's own diagnostic**: XRPUSDT clears the floor **long at 5.258 and short at
3.357 at the same second on the same book**, on mirror-image sub-noise stops. L-002 drew that pattern from
BNBUSDT at the 09:00 check; this check **reproduces it on a different contract**, which is exactly the kind of
confirmation the lesson asked for.

## The distance problem, fifth consecutive check — now in both directions

The two noise-safe constructions both fail, and they fail in the way the previous four notes predicted:

- The **short** at 1.5890 clears 1.5 only at 1.5142 (−3.14%) or 1.4939 (−4.44%) — targets sitting **below two
  intervening levels** (1.5393 and 1.5306). That is the two-or-three-levels objection verbatim.
- The **long** at 1.5380 must buy back through **both** 1.5701 **and** 1.5876 to be paid, and still only reaches
  1.346 at 1.6039.

So the fifth data point is the sharpest: **the same contract at the same instant offers no noise-safe
construction in either direction**, while offering four seductive ones that all depend on a sub-noise stop. This
belongs with the 00:00, 02:00, 09:00 and 22:00 findings as one problem for the review.

## Why the short — the only side with a passing noise-safe number — was not taken anyway

Two categories argue for it; **three argue against it**.

- **`trend` — against.** The failed breakout **did not break the higher-timeframe structure**. The 4h ascending
  low sequence survived: the 09-22 12:00Z bar low is **1.5306**, still above the 08:00Z low 1.5142, the 04:00Z low
  1.4939 and the 09-21 20:00Z low 1.5041. The daily closed **green** (+1.783%) despite the round trip. The failure
  took out an intraday high, not the trend.
- **`derivatives` — against.** Funding **−0.008393%**, still the only negative rate in the complex (BTC/ETH/SOL
  +0.010000%, BNB +0.004880%). A short **pays** at the 16:00Z settlement, fifty-three minutes after the decision.
  The discount narrowed from −0.019946% but **persisted through the failed breakout**, which is a long-side signal.
- **`market_context` — against, at this instant.** All five contracts bottomed on the **same 14:35Z bar** and all
  five are bouncing. The L-003 requote showed the bounce still running — ETH 2741.30→2745.18, BNB 788.03→788.51,
  SOL 116.87→116.96 — while XRP alone stood still. Then XRP caught up, 0.40% in three and a half minutes.

Selling a four-bar bounce that is still ticking up, 1.77% of risk away from a stop and 3.14% away from a target,
against an intact uptrend, while paying funding, is timing a top rather than trading a level.

`volume` was read from **5m only**, honouring the 22:00 note's standing instruction. The fade carried real
participation (14:05Z 869M, 14:15Z 957M, 14:25Z 818M) against a lighter bounce (14:45Z 226M, 14:55Z 432M,
15:00Z 431M) — mildly supportive of the short, but **recorded as weak**: the heaviest bar of the whole window,
1,091M at 13:25Z, was a down bar that preceded a rally, and the 14:50Z bounce bar traded 733M. The 1h series was
re-checked and is again a flat band (13:00Z breakout hour 6.067B against 6.182B in the flat 11:00Z hour) —
**the 22:00 finding replicates**.

`news`: one web search found no scheduled event bearing on this slot. The retrieved coverage concerns the Senate's
rejection of the CLARITY Act around 17 September, XRP's subsequent fall toward $1.30 and recovery through $1.49,
and a prospective Fed move — five days old, already in the price, and if anything framing current XRP strength as
a **recovery rally** rather than distribution. Not claimed as a category. Web content treated as data.

## Artifact scan

**No new artifact printed on any contract, at either resolution.** The 5m scan over 36 bars on all five returned
nothing — a **fourth consecutive clean 5m scan**. The 1h scan was clean on ETHUSDT, BNBUSDT, SOLUSDT and XRPUSDT.

BTCUSDT retains **four** contaminated 1h bars in the 30-bar window: 87888.00 (09-21 12:00Z, 2.991% on 0.726%),
95804.10 (14:00Z, 11.747% on 0.429%), 91000.00 (19:00Z, 5.148% on 0.669%), 90389.80 (20:00Z, 3.985% on 0.404%).
**Its 24h high field still reads an artifact — now 91000.00** against a real session top near 86400; the 95804.10
print aged out of the 24h window but the field remains unusable.

**Recorded so the decay is traceable rather than misread as improvement:** BTCUSDT 09-21 09:00Z 95804.10 and
ETHUSDT 09-21 09:00Z 2850.00 — the same demo event — have both **aged out of the 30-bar 1h window**. ETHUSDT
therefore scans clean at 1h this check. **The artifact count fell by time, not by the absence of new prints.**

**BTCUSDT is excluded for an eighth consecutive check under L-001.** Its spread was well-behaved at 1.09 bps and
0.38 bps across the two sweeps, confirming again that the 09:00 breach was transient; the exclusion rests on
artifacts alone.

## Next task focus

Account flat; cash and equity 5000 USDT; nothing to reconcile. The 00:00 check is fifty minutes away.

1. **XRPUSDT is back on 1.5701 and the question is unchanged, but the odds have shifted.** The engine's 15:09:56Z
   quote of 1.5696/1.5701 puts price exactly on the pivot again, now approaching it **from below on a V-bounce**
   rather than breaking it from a grind. **The 22:00 note's outcome (1) is live again**: if the 00:00 check finds
   price **above 1.5701 with a pullback low formed above it**, that is still the one construction that would solve
   the distance problem — a structural stop beneath the retest low that is both noise-safe and close. Re-derive
   the reward/risk from the fresh ask; do not reuse any number in this note. **Check the noise bar first** — with
   the 14:35Z bar at 0.834% rolling out of the preceding hour, the L-002 threshold will fall, and a stop that is
   sub-noise now may be noise-safe by 00:00. That is a real change in the test, not a loosening of it.
2. **Do not short the failed breakout without the structure the 22:00 note specified.** It required a second
   independent category *and* a structural stop above 1.5876 or a lower swing high. Neither exists: no lower swing
   high has formed — the bounce made a *higher* low at 1.5393→1.5476→1.5509 — and the 1.5890 stop needs a 3.14%
   fall to pay. Funding still makes the short pay.
3. **The 16:00Z funding settlement falls between this check and the 00:00 one.** XRPUSDT was −0.008393%, still the
   only negative rate. Re-read it at 00:00: whether the discount survives a second settlement through a failed
   breakout is a genuine derivatives read, and it is the one category that has been degraded all experiment.
4. **The distance problem now has five data points and is the single most important item for the review.** This
   check adds the strongest form: one contract, one instant, **no noise-safe construction in either direction**,
   and four passing constructions all resting on sub-noise stops. The 1.5 net floor and the structural-stop
   requirement are jointly selecting against this watchlist at these volatilities — and L-002 has now converted
   that observation into a rule that is actively rejecting trades.
5. **L-001's re-test clock is running and the next check should record it precisely.** BTCUSDT's most recent
   artifact print is 09-21 20:00Z, roughly 19h07m before this decision. A full artifact-free day is reached near
   **20:00Z on 09-22 (04:00 MYT on 09-23)** — between the 02:00 and 09:00 checks. **The exclusion stands in full
   until the daily review retires it**; a check may not loosen a lesson. Keep running the scan at **both** 1h and
   5m, which is what L-001 requires and what caught the ETHUSDT contamination.

## Human confirmations needed

None for demo paper trading; live trading remains disabled.

**One item remains outstanding and is Edward's to close.** The 09:00 run stalled for roughly twelve hours forty
minutes and **three slots were lost** — 16:00, 20:00 and 21:00 on 2026-09-22 did not run. The 22:00 and 23:00
checks have now both run normally and on time, which is good evidence the condition has cleared, but **the cause
was never identified**. Scheduled tasks only run while the Claude desktop app is open, so it is worth Edward
confirming whether the machine slept or the app was closed. The account was flat throughout, so the cost was
observations rather than money.

`LESSONS.md` was read and **now contains three lessons**, all of which applied; L-002 was binding. **Nothing under
`reviews/` was modified** — the 22:00 review task owns that folder.
