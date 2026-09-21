#!/usr/bin/env python3
"""Send USDT-perpetual MARKET orders and protective exit orders to the Binance demo futures
account only (virtual funds, never production)."""

import hashlib
import hmac
import json
from decimal import Decimal
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, build_opener

from binance_readiness_check import NoRedirect, get_json

# Deliberately not read from configuration: this module can reach no other host.
DEMO_HOST = "https://demo-fapi.binance.com"


class DemoOrderError(ValueError):
    pass


def post_json(url, headers, method="POST"):
    req = Request(url, headers={"User-Agent": "binance-futures/1.0.1 (Skill)", **headers}, method=method)
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


def signed_call(config, method, path, params, tolerate=()):
    """One signed request to the demo futures host; refuses every other environment.
    Binance error codes listed in `tolerate` return None instead of raising."""
    if config.get("BINANCE_ENV") != "demo":
        raise DemoOrderError("Orders are only allowed when BINANCE_ENV is demo")
    server, error = get_json(DEMO_HOST + "/fapi/v1/time")
    stamp = server.get("serverTime") if isinstance(server, dict) else None
    if error or type(stamp) is not int or stamp <= 0:
        raise DemoOrderError("Demo server time unavailable")
    query = urlencode({**params, "timestamp": stamp, "recvWindow": 5000})
    signature = hmac.new(config["BINANCE_API_SECRET"].encode(), query.encode(), hashlib.sha256).hexdigest()
    url = DEMO_HOST + path + "?" + query + "&signature=" + signature
    headers = {"X-MBX-APIKEY": config["BINANCE_API_KEY"]}
    data, error = get_json(url, headers) if method == "GET" else post_json(url, headers, method)
    if error and any(error.endswith("Binance %d" % code) for code in tolerate):
        return None
    if error or not isinstance(data, (dict, list)):
        raise DemoOrderError("Demo request rejected: " + (error or "Unexpected response"))
    return data


def positive(value, name):
    value = Decimal(str(value))
    if not value.is_finite() or value <= 0:
        raise DemoOrderError(name + " must be positive")
    return value


def order_fill(config, symbol, side, order_id):
    """The actual fill of one order. Futures order responses omit price and fees; the trade list has them."""
    trades = signed_call(config, "GET", "/fapi/v1/userTrades", {"symbol": symbol, "orderId": order_id})
    executed = sum((Decimal(str(t.get("qty", "0"))) for t in trades), Decimal("0")) if isinstance(trades, list) else Decimal("0")
    if executed <= 0:
        raise DemoOrderError("Demo order did not fill")
    gross = sum(Decimal(str(t.get("quoteQty", "0"))) for t in trades)
    if any(t.get("commissionAsset") != "USDT" for t in trades):
        raise DemoOrderError("Unexpected commission asset")
    return {
        "demo_order_id": str(order_id),
        "side": side,
        "executed_qty": str(executed),
        "avg_price": str(gross / executed),
        "gross_usdt": str(gross),
        "fee_usdt": str(sum(Decimal(str(t.get("commission", "0"))) for t in trades)),
    }


def prepare_symbol(config, symbol, leverage):
    """Isolated margin at the configured leverage, set before every entry."""
    # -4046: the margin type is already ISOLATED.
    signed_call(config, "POST", "/fapi/v1/marginType", {"symbol": symbol, "marginType": "ISOLATED"}, tolerate=(-4046,))
    data = signed_call(config, "POST", "/fapi/v1/leverage", {"symbol": symbol, "leverage": int(leverage)})
    if not isinstance(data, dict) or data.get("leverage") != int(leverage):
        raise DemoOrderError("Leverage was not applied")


def market_order(config, symbol, side, quantity, reduce_only=False, test=False):
    """Place one demo MARKET order and return the actual fill. test=True only validates it."""
    if side not in {"BUY", "SELL"}:
        raise DemoOrderError("Unsupported order side")
    quantity = positive(quantity, "Order quantity")
    params = {"symbol": symbol, "side": side, "type": "MARKET", "quantity": format(quantity, "f")}
    if reduce_only:
        # A reduce-only order can close a position but never open or flip one.
        params["reduceOnly"] = "true"
    data = signed_call(config, "POST", "/fapi/v1/order/test" if test else "/fapi/v1/order", params)
    if test:
        return {"test_order_accepted": True}
    if not isinstance(data, dict) or "orderId" not in data:
        raise DemoOrderError("Unexpected order response")
    return order_fill(config, symbol, side, data["orderId"])


def place_exit_orders(config, symbol, position_side, quantity, stop_price, target_price):
    """Protect a position with a stop and a target that close it at market when the mark price
    triggers them. Both are reduce-only, so a stale one can never open a position."""
    quantity, stop, target = positive(quantity, "Quantity"), positive(stop_price, "Stop"), positive(target_price, "Target")
    if position_side not in {"long", "short"} or (stop >= target) == (position_side == "long"):
        raise DemoOrderError("Stop and target are on the wrong sides")
    placed = {}
    try:
        for key, kind, trigger in (("stop_algo_id", "STOP_MARKET", stop), ("target_algo_id", "TAKE_PROFIT_MARKET", target)):
            data = signed_call(config, "POST", "/fapi/v1/algoOrder", {
                "algoType": "CONDITIONAL", "symbol": symbol, "side": "SELL" if position_side == "long" else "BUY",
                "type": kind, "triggerPrice": format(trigger, "f"), "quantity": format(quantity, "f"),
                "reduceOnly": "true", "workingType": "MARK_PRICE"})
            if not isinstance(data, dict) or "algoId" not in data:
                raise DemoOrderError("Unexpected exit order response")
            placed[key] = str(data["algoId"])
    except DemoOrderError:
        cancel_exit_orders(config, symbol, placed)
        raise
    return {**placed, "stop_price": format(stop, "f"), "target_price": format(target, "f"),
            "quantity": format(quantity, "f")}


def cancel_exit_orders(config, symbol, protection):
    for key in ("stop_algo_id", "target_algo_id"):
        if protection.get(key):
            # -2011: already triggered, cancelled or expired.
            signed_call(config, "DELETE", "/fapi/v1/algoOrder", {"algoId": protection[key]}, tolerate=(-2011,))


def exit_status(config, symbol, position_side, protection):
    """None while both exit orders are still working; otherwise which one filled (if any) and its fill."""
    working = 0
    for reason, key in (("stop", "stop_algo_id"), ("target", "target_algo_id")):
        order = signed_call(config, "GET", "/fapi/v1/algoOrder", {"algoId": protection[key]})
        status = order.get("algoStatus") if isinstance(order, dict) else None
        if status == "FINISHED" and order.get("actualOrderId"):
            fill = order_fill(config, symbol, "SELL" if position_side == "long" else "BUY", order["actualOrderId"])
            cancel_exit_orders(config, symbol, protection)
            return {"reason": reason, "fill": fill}
        working += status == "NEW"
    if working == 2:
        return None
    # An exit order ended without a fill (for example cancelled by hand): the position is unprotected.
    cancel_exit_orders(config, symbol, protection)
    return {"reason": None, "fill": None}


def funding_since(config, symbol, start_ms):
    """Net funding received (+) or paid (-) on the symbol since the position was opened."""
    rows = signed_call(config, "GET", "/fapi/v1/income",
                       {"symbol": symbol, "incomeType": "FUNDING_FEE", "startTime": int(start_ms), "limit": 100})
    return str(sum((Decimal(str(row.get("income", "0"))) for row in rows), Decimal("0")) if isinstance(rows, list) else Decimal("0"))
