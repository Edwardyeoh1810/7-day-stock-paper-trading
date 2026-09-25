# Research journal — 2026-09-22_check_0900-research

Companion to the generated journal entry for `2026-09-22_check_0900_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-22T14:05Z (22:05 Asia/Kuala_Lumpur), slot `2026-09-22_check_0900`.
- **What was done:** Read AGENTS.md, TRADING-STRATEGY.md, CONTINUITY.md, AUTOMATION-PROMPT.md, readiness.json,
  current-state.json, the 02:00 slot's research note and reviews/LESSONS.md. Ran the read-only observation for the
  due slot at 01:12Z, researched all five watchlist contracts from the demo host's public endpoints (5m, 1h and 60
  daily bars, book, 24h ticker, funding, open interest), ran the artifact scan at both 5m and 1h resolution as the
  02:00 note instructed, re-implemented the engine's reward/risk formula independently, took a second quote three
  minutes after the first, and checked the news. **The run then stalled for roughly twelve hours and forty minutes
  before a decision could be written**, so the decision submitted through `paper_engine.py` is a `no_trade` with
  reason `late run`.
- **Why it was done:** The 09:00 slot was due (`due_slot: 2026-09-22_check_0900`, 240 planned slots) and no
  position was open, so an entry was permitted if and only if every entry condition was met — until the stall
  removed the question.
- **Timing:** Observation ran at 01:12:02Z (09:12 MYT) and research was pulled at 01:13:20Z (09:13 MYT), **both on
  time**, 12 and 13 minutes after the slot with over half an hour of the entry window to spare. The decision was
  submitted at 14:00:43Z (22:00 MYT) — **778 minutes after the slot**. This run is **LATE**.
- **Order proposed:** No.
- **Order placed:** No. The engine returned `status: no_trade`, `live_order_sent: false`.
- **Order filled:** No.
- **Exchange stop/target reconciliation:** None to reconcile. The account was flat before this check and is flat
  after it; no exit order has ever been placed in this experiment.
- **Current holdings:** None. Flat.
- **Current cash:** 5000 USDT. Demo wallet balance 5000.04174826 USDT.
- **Current risk:** 0 USDT open risk; 0 USDT realized today. The ledger rolled to `2026-09-22`.
- **Evidence captured:** `05-交易记录-data/evidence/2026-09-22_check_0900.json` (read-only run),
  `05-交易记录-data/evidence/2026-09-22_check_0900_paper.json` (engine), and this note.

## The governing fact: this run stalled for twelve hours and forty minutes

The research was on time. The decision was not. The gap between them is the whole story of this check, and it is an
operational finding rather than a market one.

| Event | UTC | MYT | vs slot |
|---|---|---|---|
| Slot scheduled | 01:00Z | 09:00 | — |
| Read-only observation ran | 01:12:02Z | 09:12 | +12 min |
| Research pulled, first quote | 01:13:20Z | 09:13 | +13 min |
| Second quote (drift check) | 01:16:42Z | 09:16 | +16 min |
| **Stall** | | | **~12h 40m** |
| Decision submitted | 14:00:43Z | 22:00 | **+778 min** |

The host clock was cross-checked against the exchange's own `/fapi/v1/time` endpoint, which agreed to within 0.1
second. **This is a real stall, not a clock fault.** Under the late-run rule an entry is forbidden and the engine
would reject it regardless; no position was open, so `manage` and `close` did not apply; `no_trade` with reason
`late run` under the original slot's run id is the required outcome, and that is what was recorded.

**Three slots were lost.** The 16:00, 20:00 and 21:00 checks of 2026-09-22 passed with no check at all. No position
was open at any point during the stall, so **the account never carried unprotected risk** — this cost observations,
not money. They are deliberately **not** backfilled: backfilling a historical trade is forbidden, and this decision
is confined to the 09:00 slot.

## The market settled the question afterwards, and it settled it emphatically

The stale research is preserved below as a faithful record of what the 09:00 slot saw. What makes it worth reading
is what happened next. A final read-only quote sweep at 14:0xZ against the 01:13Z research prices:

| Contract | bid 01:13Z | bid 14:0xZ | drift |
|---|---|---|---|
| BTCUSDT | 85800.10 | 86240.00 | +0.51% |
| ETHUSDT | 2750.54 | 2756.89 | +0.23% |
| BNBUSDT | 793.660 | 791.03 | −0.33% |
| SOLUSDT | 118.0100 | 117.70 | −0.26% |
| **XRPUSDT** | **1.5158** | **1.5843** | **+4.52%** |

**The XRP short this check refused carried a 1.5320 stop. XRP is at 1.5843. It would have been stopped out many
hours ago**, and the 1.4849 target it could only reach for was never approached. Four contracts went essentially
nowhere in thirteen hours while the fifth — the one with the best-looking bearish structure — broke out hard in the
opposite direction.

Two things follow, and they should be kept apart:

1. **The late-run rule was correct and cost nothing here.** It is designed for exactly this: a decision written on
   thirteen-hour-old prices is not a decision, it is a guess. The rule refused it before judgement had to.
2. **The refusal was also right on the merits**, and for a reason that had nothing to do with the stall — see
   below. The check would have recorded `no_trade` on time as well. The two arguments point the same way, which is
   why this outcome is not evidence about the quality of the entry filters either way.

## What the research found at the slot: the inversion reappeared as an inversion of *distance*

Everything in this section describes 01:13Z and **every price in it is stale**. The reasoning carries; the numbers
do not.

Over the seven-hour gap the complex rallied into the 20:00–22:00Z window and then pulled back together for three to
four hours. For the first time in the experiment, **structure and volume agreed on direction**:

- **XRPUSDT** ran 1.4888 → **1.5701** (22:00Z) → 1.5158, giving back about two thirds of the move, with a clean
  descending hourly-high sequence **1.5701 → 1.5654 → 1.5401 → 1.5313**.
- **SOLUSDT** ran to **119.86** (21:00Z) → 118.01, hourly highs stepping down 119.86 → 119.74 → 119.80 → 119.37 →
  118.37.
- The **heaviest 5m bar of the two-hour window was a DOWN bar on three of five**: BTCUSDT 01:00Z; ETHUSDT 01:00Z at
  478,840, nearly twice the next-heaviest, closing −0.745%; SOLUSDT 00:55Z at 148,504, roughly three times the
  next, closing −0.905%. BTCUSDT printed **eight consecutive DOWN 5m bars** into the quote.

The 02:00 note's volume-versus-arithmetic inversion had apparently resolved. It had not — it had changed form.
**On the two contracts with genuine bearish structure, the nearest honest target was too close to pay 1.5, and the
only passing target required jumping two or three intervening supports:**

| Construction | Stop | Nearest support | 2nd support | Reaching target |
|---|---|---|---|---|
| XRPUSDT short | 1.5320 (above the 1.5313 lower high), risk 1.096% | 1.5041 → **0.515** | 1.4973 → **0.884** | 1.4849 → 1.557 |
| SOLUSDT short | 118.42 (above the 118.37 hourly high), risk 0.470% | 117.59 → **0.194** | — | 117.04 → 0.986 (still fails) |

The XRP short cleared the floor **only** by targeting 1.4849, which sits beyond both 1.5041 and 1.4973. That is
precisely the error the 00:00 note refused when it ruled the XRP long cleared *"only by reaching for 1.5441"*.
**Applied symmetrically to the short side, it is refused again.** SOL failed outright in both directions.

### Everything that did clear 1.5 cleared it on a noise-width stop

This is trap (a) from the 02:00 note — *a stop resting just under a level the market has been touching is a size,
not a stop* — and this check produced the most extreme examples of it yet:

| Construction | RR | Stop distance | Max 5m bar range, preceding hour |
|---|---|---|---|
| XRPUSDT long | **4.615** | **0.060%** | 0.883% |
| BNBUSDT long | 2.015 | 0.155% | 0.444% |
| BNBUSDT short | 1.673 | 0.166% | 0.444% |

The XRP long's stop was **one fifteenth of a single 5m bar's range** — it would have been taken out by noise inside
one bar, and it was a long into an active decline besides. **BNBUSDT passed in BOTH directions simultaneously**, on
mirror-image stops 0.155% and 0.166% away. A contract clearing the floor both ways at once on opposing noise stops
is the clearest possible demonstration that the geometry, not the market, is producing the number. All three
refused.

### BTCUSDT: excluded for a sixth consecutive check, now on spread as well

The 01:13Z book was **85800.10 / 86080.60 = 32.59 bps**, against the 25 bps cap — a breach on its own. A re-quote
three minutes later returned **1.06 bps**, so the demo book was *unstable* as well as wide. On top of that, the
hourly pass found **two new artifacts** inside the gap:

| BTC 1h bar | Body | Upper wick | High |
|---|---|---|---|
| 09-21 19:00Z | 0.669% | **5.148%** | 91000.00 |
| 09-21 20:00Z | 0.404% | **3.985%** | 90389.80 |

These sit on top of the standing 95804.10 double contamination (09:00Z and 14:00Z, the latter an 11.747% upper
wick) and 87888.00. Running the scan at 1h as well as 5m — the 02:00 note's instruction — is again what found them.

**One clean result:** the 5m artifact scan over the last 24 bars on all five returned **nothing**, a second
consecutive fully clean two-hour scan.

## Two smaller findings worth carrying

**The news argued against the short rather than for it.** Press coverage of the 21 September rally described it as
a **short squeeze that liquidated more than USD 648 million of bitcoin short positions above 85,000**. Selling an
unconfirmed pullback in a market that has just forced that much bearish positioning out is the wrong side of a
crowded unwind. Recorded as `market_context` rather than as a tradeable `news` catalyst, since no scheduled macro
event was identified for the session. Higher-timeframe trend agreed: 24h changes were **+6.117%** on XRP,
**+5.362%** on BTC, **+4.693%** on SOL — any short was counter-trend on the daily, which raises the bar rather than
lowering it. Given where XRP finished the day, this was the single most useful piece of evidence on the board.

**The open-interest limitation has changed slightly and should be restated accurately.** The standing note in prior
checks is that open interest is unavailable on the demo host. As of this check, `/fapi/v1/openInterest`
**does** return a value (XRPUSDT 15,646,486,925,706.1 at 01:17Z) — but `/futures/data/openInterestHist` still
returns the bare string `ok` with no history. So the **change** in open interest, which is the part that carries
information about positioning, remains unavailable, and the absolute figure is implausible enough to look like a
demo artifact. **The `derivatives` category is still effectively reduced to funding alone**, but the reason is now
"no history" rather than "no endpoint". Funding itself was neutral: the 0.0100% baseline on four contracts and
0.003859% on BNBUSDT, next funding 08:00Z, so negligible carry and no crowding to fade or squeeze.

## Next task focus

Account is flat and the ledger has rolled to 2026-09-22. **The immediate priority is not a setup, it is the stall**
— see the human-confirmation section. Assume nothing in this note is live.

1. **Re-derive everything from fresh bars.** Every level here is thirteen hours old and XRP has moved 4.5% since.
   The thresholds are dead; only the reasoning carries.
2. **XRPUSDT has broken out, not broken down.** It is at 1.5843, above the entire descending sequence this note
   documented (1.5701 / 1.5654 / 1.5401 / 1.5313) — that sequence is gone and the short premise with it. **Do not
   re-use this check's short case.** If a long is considered, the same discipline applies that killed it here: the
   structural stop must sit below real structure, not 0.06% away, and the target must be reachable without jumping
   intervening resistance. Re-derive the post-breakout structure from scratch.
3. **The distance problem is now the central structural finding of the experiment and should go to the review as
   such.** It has appeared three times in three different forms: the 00:00 note's ruling that XRP produces nothing
   valid until a structural stop and target sit more than roughly 2.5% apart; the 02:00 note's finding that a
   target only 1.6% away against ~1.3% hourly ranges makes the confirmation wait unaffordable; and this check's
   finding that on the two contracts with genuine directional structure, the nearest honest target paid 0.19–0.52
   while only a target beyond two or three supports cleared the floor. **These are one problem, not three.** The
   1.5 net floor and the structural-stop requirement are jointly selecting against setups on this watchlist at
   these volatilities, and the review should look at that directly.
4. **Cite, do not re-argue, the two traps.** (a) A stop resting on or just under a repeatedly-touched level is a
   size, not a stop — this check's XRP long at 0.060% and BNB's both-ways pass are the sharpest examples yet.
   (b) A reward/risk ratio that improves because price moved *toward* the stop is not an improving trade.
5. **BTCUSDT stays excluded** — sixth consecutive check, now on spread (32.59 bps) as well as artifacts, with two
   new contaminated hourly bars. Keep running the artifact scan at 1h as well as 5m. **SOLUSDT** rallied through
   the 118.9100 reference the 02:00 note confirmed, so that construction is retired. **BNBUSDT** remains the
   weakest contract (+1.272% over 24h).

## Human confirmations needed

None for demo paper trading; live trading remains disabled. **One item genuinely needs Edward's attention, and it
is not about the market.**

**(a) The scheduled run stalled for roughly twelve hours and forty minutes, and three checks were lost.** The
16:00, 20:00 and 21:00 slots of 2026-09-22 did not run. This is the first such failure of the experiment and it is
an infrastructure problem, not a trading one — worth Edward checking whether the machine slept or the desktop app
was closed, since scheduled tasks only run while the app is open. **The risk consequence this time was nil**
because the account was flat throughout; had a position been open, the 24-hour hold limit and the between-check
reconciliation would both have been missed, though the exchange-side stop and target would still have protected it.
That is the case worth guarding against.

**(b)** The stale-research outcome is worth the review's attention as a validation rather than a warning: the
refused XRP short would have been stopped out hours ago, so the late-run rule and the evidence-based refusal agreed.
**(c)** The open-interest situation has changed in detail (point-in-time now readable, history still not) and the
standing note in earlier checks should be updated to say so. **(d)** BTCUSDT has now been untradeable for six
consecutive checks for structural reasons, and breached the spread cap for the first time.

The 22:00 daily review owns `reviews/` and was due at essentially the moment this decision was submitted;
`LESSONS.md` was read (still empty — no closed trades) and **nothing in that folder was modified**.
