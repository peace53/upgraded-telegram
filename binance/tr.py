"""Binance TR integration."""

from __future__ import annotations

# Default symbols
DEFAULT_TR_SYMBOL = "BTCTRY"


def normalize_tr_symbol(symbol: str) -> str:
    """Normalize Binance TR symbol."""
    symbol = symbol.upper().strip()
    if not symbol.endswith("TRY"):
        symbol += "TRY"
    return symbol


def parse_price_tick(data: dict) -> dict:
    """Parse price tick from Binance."""
    return {
        "symbol": data.get("s"),
        "price": data.get("p"),
        "quantity": data.get("q"),
        "timestamp": data.get("T"),
    }
