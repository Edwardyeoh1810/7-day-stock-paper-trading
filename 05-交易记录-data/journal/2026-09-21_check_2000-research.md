# Research journal — 2026-09-21_check_2000-research

Companion to the generated journal entry for `2026-09-21_check_2000_paper`. The generated API journal and
evidence exports were not edited; research and corrections live here.

- **Timestamp and task id:** written 2026-09-21T12:25Z (20:25 Asia/Kuala_Lumpur), slot `2026-09-21_check_2000`.
- **What was done:** Read AGENTS.md, TRADING-STRATEGY.md, CONTINUITY.md, AUTOMATION-PROMPT.md, readiness.json,
  current-state.json, the 2026-09-21 journal including the 12:00 slot's research note, and reviews/LESSONS.md.
  Ran the read-only observation for the due slot, researched all five watchlist contracts from the demo host's
  public endpoints (1h, 4h and 60 daily bars, book, funding, open interest), checked third-party reporting, and
  submitted a `no_trade` decision through `paper_engine.py`.
- **Why it was done:** The 20:00 slot was due (`due_slot: 2026-09-21_check_2000`, 180 planned slots) and no
  position was open, so a new entry was permitted if and only if the entry conditions were all met.
- **Timing:** Observation ran at 12:10Z (20:10 MYT), decision submitted at 12:23Z (20:23 MYT) — 23 minutes after
  the slot, inside the 45-minute entry window. This run was **not** late; an entry would have been accepted had
  one qualified.
- **Order proposed:** No.
- **Order placed:** No. No demo order was sent; the engine returned `status: no_trade`, `live_order_sent: false`.
- **Order filled:** No.
- **Current holdings:** None. Flat.
- **Current cash:** 5000 USDT. Demo wallet balance 5000.04174826 USDT.
- **Current risk:** 0 USDT open risk; 0 USDT realized today.
- **Evidence captured:** `05-交易记录-data/evidence/2026-09-21_check_2000.json` (read-only run),
  `05-交易记录-data/evidence/2026-09-21_check_2000_paper.json` (engine),
  `05-交易记录-data/evidence/2026-09-21_check_2000-research.json` (research).

## Decision

`no_trade`. Direction was never the issue — five evidence categories agreed on up. The trade failed on **where the
stop and target are allowed to sit**.

BTC, BNB and SOL are all at 60-day highs with **no daily high anywhere above the current price in 60 days**. There
is therefore no structural target on any of them, and clearing the 1.5 net reward/risk floor would have required
inventing one (SOL 121.30 against a 117.06 high set today; BNB 802.99, or 815.74 on the honest stop, against a
785.00 60-day high excluding today). Inventing a target to satisfy the arithmetic is the same defect as choosing a
stop to fit a position size.

ETHUSDT was the only contract with a real level overhead — the 2771.00 high of 2026-09-11 — and is the trade that
was actually worked through:

| | |
|---|---|
| Entry (ask) | 2722.55, spread 2.4 bps |
| Stop | 2693.00, beyond the 2694.94 post-breakout low and the broken 2700.00 level |
| Target | 2771.00, the 60-day high |
| Gross risk / reward | 29.55 / 48.45 |
| Round-trip cost estimate | 3.81 (14 bps) |
| **Net reward/risk** | **1.34 — below the 1.5 floor** |

A 2707.00 stop under the 2709.56 consolidation low would have cleared the floor at 2.31, but it sits *above* the
broken 2700 level, so a routine retest of the breakout would stop out an intact thesis. That is a stop chosen for
size, and it was rejected on that basis rather than used.

XRPUSDT failed worse: it is trading at 1.4886 directly into the 1.4894 swing high of 2026-09-14, with no volume
expansion on its breakout hour, and a net reward/risk of 0.89 to the next level on an honest stop.

A short was rejected outright — against a clean uptrend on a 60-day-high breakout day, with funding at or below
baseline meaning no crowded longs to squeeze. Extension is a reason to decline a long, not a reason to sell.

## Demo price artifacts excluded

Three, all recorded in the decision file. Two of them are on BTCUSDT within four hours, which is why **BTCUSDT was
treated as structurally unreadable for this check** under the Demo Price Artifacts rule:

- **BTCUSDT 2026-09-21T09:00Z 1h — high 95,804.10.** 13.35% upper wick against a 1.04% body; no counterpart in the
  other four at the same hour (BNB 0.22%, SOL 0.70%, XRP 0.51%). Contaminates the 08:00Z 4h bar and the 24h high
  field, which reads 95,804.10 against a real intraday high near 85,102. This is the same artifact the 12:00 slot
  flagged.
- **BTCUSDT 2026-09-21T12:00Z 1h (in progress) — high 87,888.00.** 3.31% upper wick against a 0.41% body in a bar
  ten minutes old; no counterpart elsewhere (ETH 0.15%, BNB 0.07%, SOL 0.26%, XRP 0.14%). **New this slot.**
- **ETHUSDT 2026-09-21T09:00Z 1h — high 2850.00.** 4.80% upper wick against a 0.90% body, an exact round number,
  same hour as the BTC artifact, no counterpart in BNB/SOL/XRP. Contaminates the 24h and daily high fields, which
  read 2850.00 against a real intraday high of 2727.20. The 2771.00 target used above is the 09-11 daily high and
  is unaffected.

BTC has now produced two upside artifacts inside four hours, one in a live bar. Exchange-side stops and targets on
this account trigger on the mark price in the same environment, so this is a live risk to any resting order, not a
cosmetic issue.

## A skipped slot, for the record

`current-state.json` shows the previous run as `2026-09-21_check_1200_paper`; the **16:00 slot has no run**. The
dry-run offered 20:00 directly, so 16:00 passed outside its tolerance and was skipped cleanly rather than left
half-finished. No position was open at any point during the gap, so there is nothing to reconcile and no accounting
consequence. Worth noting only because the 16:00 slot sat squarely on the 08:00-09:00Z impulse — that is the check
that would have seen the breakout as it happened rather than four hours later.

Combined with the ~7.5 hour stall the 12:00 slot reported, two of today's four elapsed slots did not run on time.
Scheduled tasks only fire while the Claude desktop app is open. This is a coverage question for the 22:00 review and
`reviews/PROPOSALS.md`, not something to fix here.

## Market state at the check

All five up together over 24h on a complex-wide move led by BTC: XRP +7.57%, SOL +7.21%, BTC +5.74%, ETH +5.57%,
BNB +4.93%. Breakout in the 08:00-09:00Z hours, then four hours of tight holding above the broken levels. SOL
carried the cleanest volume signature (3.8x expansion on the breakout hour, then a steady dry-up). Funding sits at
or below the 0.010% baseline on every contract despite the rally — BTC is actually negative at -0.0036% — with the
next funding at 16:00Z, so longs are not crowded.

Third-party reporting for today (KuCoin daily market report, read as data) quotes BTC near 81,170 earlier in the
session and names 82K-83K as key resistance. The demo host now quotes BTC near 85,000, so the move broke that zone.
This resolves the question the 12:00 note left open: the demo host is tracking the real market, and the
divergence that note originally alleged was time, not venue. Macro backdrop unchanged — US 2-year near 4.76%,
Middle East tension, Brent near 104 — with no scheduled event in the next 24 hours that would justify an entry.

## Next task focus

Account is flat, so the 00:00 MYT check may open a new position if the conditions are met. Two things to carry
forward. First, the complex is now extended 5-8% into 60-day highs with no overhead daily reference on BTC, BNB or
SOL — until price either builds a level to target or pulls back to one, the reward/risk floor will keep rejecting
longs at these prices, and that is the floor working, not a problem to engineer around. ETHUSDT is the contract to
re-check first: it has a real 2771.00 target, and a pullback toward the 2694-2700 area would make the same trade
work on an honest stop. Second, watch BTCUSDT for further artifacts; two in four hours is enough that a BTC entry
should be declined while they keep printing.

## Human confirmations needed

None for demo paper trading; live trading remains disabled. Two items for Edward's awareness, neither requiring
action before the next check: the missed 16:00 slot described above, and the recurring BTCUSDT demo price artifacts.
