#!/usr/bin/env python3
"""Send Spot MARKET orders and protective exit orders to the Binance demo account only
(virtual funds, never production)."""

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


def post_json(url, headers, method="POST"):
    req = Request(url, headers={"User-Agent": "binance-spot/1.0.1 (Skill)", **headers}, method=method)
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


def signed_call(config, method, path, params):
    """One signed request to the demo host; refuses every other environment."""
    if config.get("BINANCE_ENV") != "demo":
        raise DemoOrderError("Orders are only allowed when BINANCE_ENV is demo")
    server, error = get_json(DEMO_HOST + "/api/v3/time")
    stamp = server.get("serverTime") if isinstance(server, dict) else None
    if error or type(stamp) is not int or stamp <= 0:
        raise DemoOrderError("Demo server time unavailable")
    query = urlencode({**params, "timestamp": stamp, "recvWindow": 5000})
    signature = hmac.new(config["BINANCE_API_SECRET"].encode(), query.encode(), hashlib.sha256).hexdigest()
    url = DEMO_HOST + path + "?" + query + "&signature=" + signature
    headers = {"X-MBX-APIKEY": config["BINANCE_API_KEY"]}
    data, error = get_json(url, headers) if method == "GET" else post_json(url, headers, method)
    if error or not isinstance(data, (dict, list)):
        raise DemoOrderError("Demo request rejected: " + (error or "Unexpected response"))
    return data


def build_fill(symbol, side, order_id, status, executed, gross, commissions):
    base = symbol[:-4] if symbol.endswith("USDT") else None
    base_fee = commissions.get(base, Decimal("0"))
    quote_fee = commissions.get("USDT", Decimal("0"))
    average = gross / executed
    return {
        "demo_order_id": str(order_id),
        "status": str(status),
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


def positive(value, name):
    value = Decimal(str(value))
    if not value.is_finite() or value <= 0:
        raise DemoOrderError(name + " must be positive")
    return value


def market_order(config, symbol, side, quantity, test=False):
    """Place one demo MARKET order and return the actual fill. test=True only validates it."""
    if side not in {"BUY", "SELL"}:
        raise DemoOrderError("Unsupported order side")
    quantity = positive(quantity, "Order quantity")
    data = signed_call(config, "POST", "/api/v3/order/test" if test else "/api/v3/order",
                       {"symbol": symbol, "side": side, "type": "MARKET", "quantity": format(quantity, "f"),
                        "newOrderRespType": "FULL"})
    if test:
        return {"test_order_accepted": True}
    executed = Decimal(str(data.get("executedQty", "0")))
    gross = Decimal(str(data.get("cummulativeQuoteQty", "0")))
    if executed <= 0 or gross <= 0:
        raise DemoOrderError("Demo order did not fill")
    commissions = {}
    for fill in data.get("fills", []):
        asset = str(fill.get("commissionAsset"))
        commissions[asset] = commissions.get(asset, Decimal("0")) + Decimal(str(fill.get("commission", "0")))
    return build_fill(symbol, side, data.get("orderId"), data.get("status"), executed, gross, commissions)


def place_exit_oco(config, symbol, quantity, stop_price, target_price):
    """Protect a long position: a stop-loss and a take-profit that both sell at market when
    triggered; the exchange cancels the other leg."""
    quantity, stop, target = positive(quantity, "Quantity"), positive(stop_price, "Stop"), positive(target_price, "Target")
    if stop >= target:
        raise DemoOrderError("Stop must be below target")
    data = signed_call(config, "POST", "/api/v3/orderList/oco", {
        "symbol": symbol, "side": "SELL", "quantity": format(quantity, "f"),
        "aboveType": "TAKE_PROFIT", "aboveStopPrice": format(target, "f"),
        "belowType": "STOP_LOSS", "belowStopPrice": format(stop, "f"), "newOrderRespType": "RESULT"})
    legs = {str(report.get("type")): report.get("orderId") for report in data.get("orderReports", [])
            if isinstance(report, dict)} if isinstance(data, dict) else {}
    if not isinstance(data, dict) or "orderListId" not in data or not {"STOP_LOSS", "TAKE_PROFIT"} <= set(legs):
        raise DemoOrderError("Unexpected exit order response")
    return {"order_list_id": str(data["orderListId"]), "stop_order_id": str(legs["STOP_LOSS"]),
            "target_order_id": str(legs["TAKE_PROFIT"]), "stop_price": format(stop, "f"),
            "target_price": format(target, "f"), "quantity": format(quantity, "f")}


def cancel_exit_oco(config, symbol, protection):
    signed_call(config, "DELETE", "/api/v3/orderList",
                {"symbol": symbol, "orderListId": protection["order_list_id"]})


def exit_status(config, symbol, protection):
    """None while the exit orders are still working; otherwise which leg filled (if any) and its fill."""
    listing = signed_call(config, "GET", "/api/v3/orderList", {"orderListId": protection["order_list_id"]})
    if not isinstance(listing, dict) or listing.get("listOrderStatus") != "ALL_DONE":
        return None
    for reason, key in (("stop", "stop_order_id"), ("target", "target_order_id")):
        order = signed_call(config, "GET", "/api/v3/order", {"symbol": symbol, "orderId": protection[key]})
        executed = Decimal(str(order.get("executedQty", "0"))) if isinstance(order, dict) else Decimal("0")
        if executed <= 0:
            continue
        trades = signed_call(config, "GET", "/api/v3/myTrades", {"symbol": symbol, "orderId": protection[key]})
        commissions = {}
        for trade in trades if isinstance(trades, list) else []:
            asset = str(trade.get("commissionAsset"))
            commissions[asset] = commissions.get(asset, Decimal("0")) + Decimal(str(trade.get("commission", "0")))
        gross = Decimal(str(order.get("cummulativeQuoteQty", "0")))
        return {"reason": reason,
                "fill": build_fill(symbol, "SELL", order.get("orderId"), order.get("status"), executed, gross, commissions)}
    # Both legs ended without a fill (for example cancelled by hand): the position is unprotected.
    return {"reason": None, "fill": None}
