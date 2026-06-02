"""Kral agent package."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class Identity:
    """Kral identity and constants."""
    
    NAME = "Kral"
    VERSION = "0.1.0"
    LANGUAGE = "Turkish"
    
    def greet(self, symbol: str = "BTCUSDT") -> str:
        """Greet user with symbol context."""
        return f"Merhaba! Ben {self.NAME}. {symbol} fiyatini takip ediyorum."
    
    def tick(self, symbol: str, price: str, volume: str) -> str:
        """Format price tick."""
        return f"📊 {symbol}: {price} | Hacim: {volume}"


identity = Identity()


@dataclass
class State:
    """Session state."""
    turbo_level: int = 0
    last_price: str | None = None
    last_bist_price: str | None = None
    session_start: str = ""
    
    def __post_init__(self):
        if not self.session_start:
            self.session_start = datetime.now().isoformat()


def load_state(filepath: str = "data/kral_state.json") -> State:
    """Load state from file."""
    fpath = Path(filepath)
    if fpath.exists():
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return State(**data)
        except (json.JSONDecodeError, TypeError):
            pass
    return State()


def save_state(state: State, filepath: str = "data/kral_state.json") -> None:
    """Save state to file."""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump({
            "turbo_level": state.turbo_level,
            "last_price": state.last_price,
            "last_bist_price": state.last_bist_price,
            "session_start": state.session_start,
        }, f, indent=2)


class Evolve:
    """Evolution system for Kral."""
    
    @staticmethod
    def load_state(filepath: str = "data/kral_state.json") -> State:
        """Load existing state."""
        return load_state(filepath)
    
    @staticmethod
    def save_state(state: State, filepath: str = "data/kral_state.json") -> None:
        """Save state."""
        save_state(state, filepath)
    
    @staticmethod
    def evolve(state: State) -> State:
        """Evolve state (e.g., increase turbo)."""
        state.turbo_level = min(state.turbo_level + 1, 10)
        return state


evolve = Evolve()
