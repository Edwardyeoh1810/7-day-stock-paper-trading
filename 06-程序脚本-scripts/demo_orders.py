#!/usr/bin/env python3
"""Send Spot MARKET orders to the Binance demo account only (virtual funds, never production)."""

import hashlib
import hmac
import json
from decimal import Decimal
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, build_opener

from binance_readiness_check import NoRedirect, get_json

# Deliberately not read from configuration: this module can reach no other host.
DEMO_HOST = "https://demo-api.binance.com"


class DemoOrderError(ValueError):
    pass


def post_json(url, headers):
    req = Request(url, headers={"User-Agent": "binance-spot/1.0.1 (Skill)", **headers}, method="POST")
    try:
        with build_opener(NoRedirect()).open(req, timeout=10) as response:
            return json.loads(response.read() or b"{}"), None
    except HTTPError as exc:
        # Only a numeric API error code is safe to export, never raw server text.
        suffix = ""
        try:
            body = json.loads(exc.read())
            code = body.get("code") if isinstance(body, dict) else None
            if type(code) is int:
                suffix = " / Binance %d" % code
        except (OSError, ValueError, UnicodeError):
            pass
        return None, "HTTP %d%s" % (exc.code, suffix)
    except (URLError, TimeoutError, OSError):
        return None, "Network or TLS error"
    except (ValueError, UnicodeError):
        return None, "Invalid JSON response"


def market_order(config, symbol, side, quantity, test=False):
    """Place one demo MARKET order and return the actual fill. test=True only validates it."""
    if config.get("BINANCE_ENV") != "demo":
        raise DemoOrderError("Orders are only allowed when BINANCE_ENV is demo")
    if side not in {"BUY", "SELL"}:
        raise DemoOrderError("Unsupported order side")
    quantity = Decimal(str(quantity))
    if not quantity.is_finite() or quantity <= 0:
        raise DemoOrderError("Order quantity must be positive")
    server, error = get_json(DEMO_HOST + "/api/v3/time")
    stamp = server.get("serverTime") if isinstance(server, dict) else None
    if error or type(stamp) is not int or stamp <= 0:
        raise DemoOrderError("Demo server time unavailable")
    query = urlencode({"symbol": symbol, "side": side, "type": "MARKET", "quantity": format(quantity, "f"),
                       "newOrderRespType": "FULL", "timestamp": stamp, "recvWindow": 5000})
    signature = hmac.new(config["BINANCE_API_SECRET"].encode(), query.encode(), hashlib.sha256).hexdigest()
    path = "/api/v3/order/test" if test else "/api/v3/order"
    data, error = post_json(DEMO_HOST + path + "?" + query + "&signature=" + signature,
                            {"X-MBX-APIKEY": config["BINANCE_API_KEY"]})
    if error or not isinstance(data, dict):
        raise DemoOrderError("Demo order rejected: " + (error or "Unexpected response"))
    if test:
        return {"test_order_accepted": True}
    executed = Decimal(str(data.get("executedQty", "0")))
    gross = Decimal(str(data.get("cummulativeQuoteQty", "0")))
    if executed <= 0 or gross <= 0:
        raise DemoOrderError("Demo order did not fill")
    base = symbol[:-4] if symbol.endswith("USDT") else None
    commissions = {}
    for fill in data.get("fills", []):
        asset = str(fill.get("commissionAsset"))
        commissions[asset] = commissions.get(asset, Decimal("0")) + Decimal(str(fill.get("commission", "0")))
    base_fee = commissions.get(base, Decimal("0"))
    quote_fee = commissions.get("USDT", Decimal("0"))
    average = gross / executed
    return {
        "demo_order_id": str(data.get("orderId")),
        "status": str(data.get("status")),
        "side": side,
        "executed_qty": str(executed),
        # A BUY pays its commission in the base asset, so less than executed_qty can be sold later.
        "net_qty": str(executed - base_fee),
        "avg_price": str(average),
        "gross_usdt": str(gross),
        "net_usdt": str(gross + quote_fee if side == "BUY" else gross - quote_fee),
        "fee_usdt": str(base_fee * average + quote_fee),
        "commissions": {asset: str(amount) for asset, amount in commissions.items()},
    }
