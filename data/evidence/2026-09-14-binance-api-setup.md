# Binance API Setup Evidence - 2026-09-14

## Timestamp

- Local machine time: 2026-09-14T14:39:44+09:00.
- UTC time: 2026-09-14T05:39:44Z.

## Files Created Or Updated

- `config/binance-api.env`: dedicated local-only Binance API credential file with empty placeholders.
- `config/binance-api.env.example`: safe Binance API template without secrets.
- `.env`: general local safety file.
- `.env.example`: safe general template.
- `.gitignore`: ignores `.env`, `.env.*`, and `config/binance-api.env`, while keeping example env files trackable.
- `scripts/binance_readiness_check.py`: read-only Binance verification script using Python standard library only.
- `docs/BINANCE-API-SETUP.md`: local setup and verification instructions.
- `state/readiness.json`: explicit Binance API readiness fields added.

## Verification Result

- Binance production base URL: `https://api.binance.com`.
- Public REST connectivity:
  - `/api/v3/ping`: OK.
  - `/api/v3/time`: OK.
- Signed account check:
  - Skipped because `BINANCE_API_KEY` and `BINANCE_API_SECRET` are empty in local `config/binance-api.env`.
- Stock/ETF API access:
  - Not verified.
  - Public Spot symbol probes for `SPYUSDT` and `QQQUSDT` did not resolve as valid Binance Spot symbols.

## Official Documentation Context

- Binance Developer Documentation: https://developers.binance.com/en/docs/introduction
- Binance Spot REST API general information: https://developers.binance.com/en/docs/products/spot/rest-api
- Binance Spot Testnet documentation: https://github.com/binance/binance-spot-api-docs/blob/master/testnet/general-info.md
- Binance Demo Mode Spot API documentation: https://github.com/binance/binance-spot-api-docs/blob/master/demo-mode/general-info.md
- Binance announcement ceasing stock token support, published 2021-07-16: https://www.binance.com/en/support/announcement/detail/3a0304f3ee1c43668959c1b01f610d59

## Safety Decision

No order was proposed, placed, or filled. `orders_allowed` remains false.

Reason:

- Public API connectivity is not enough to permit trading.
- Signed account read access is not verified until local credentials are added.
- Binance Spot API does not establish U.S. stock/ETF trading eligibility for this experiment.
- Live trading remains prohibited without explicit confirmation for a specific order.
