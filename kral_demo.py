#!/usr/bin/env python
"""Kral Demo - Bagimsiz calisma testi."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


class KralDemo:
    """Kral assistant demo."""
    
    def __init__(self):
        self.name = "Kral"
        self.version = "0.1.0"
        self.turbo_level = 0
        self.session_start = datetime.now()
    
    def greet(self, symbol: str = "BTCUSDT") -> str:
        """Greet user."""
        return f"Merhaba! Ben {self.name}. {symbol} fiyatini takip ediyorum."
    
    def tick(self, symbol: str, price: str, volume: str) -> str:
        """Process price tick."""
        return f"📊 {symbol}: {price} | Hacim: {volume}"
    
    def reply(self, user_input: str) -> str:
        """Generate reply to user input."""
        user_input_lower = user_input.lower()
        
        responses = {
            "merhaba": "Selam! Hosca kaldin. Bitcoin, Ethereum veya Borsa sorusu mu var?",
            "bitcoin": "Bitcoin (BTC) en buyuk kripto para. Halihazirda 97K USDT civari.",
            "ethereum": "Ethereum (ETH) akilli sozlesmeler icin. Gelistiriciler seviyor.",
            "fiyat": "Fiyati almak icin canli veri gerekiyor. --cli veya --gui ile baglan.",
            "turbo": f"Turbo Level: {self.turbo_level}. Arttirmak icin daha fazla sor!",
            "yardim": "Sorabileceklerin: bitcoin, ethereum, fiyat, turbo, hava, tesekkur, veda",
            "hava": "Hava - bana sorma, dis API gerekir :)",
            "tesekkur": "Biseybilgin yok, yardim etmekten mutlu oldum!",
            "veda": "Hosca kaldin! Tekrar gorusuruz.",
        }
        
        for keyword, response in responses.items():
            if keyword in user_input_lower:
                self.turbo_level += 1
                return response
        
        # Default response
        self.turbo_level += 1
        return f"Ilginc bir soru: '{user_input}'. Daha fazla detay verebilir misin?"
    
    def save_state(self, filepath: str = "data/kral_state.json") -> None:
        """Save session state."""
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        state = {
            "version": self.version,
            "turbo_level": self.turbo_level,
            "session_start": self.session_start.isoformat(),
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
        print(f"✓ Durum kaydedildi: {filepath}")
    
    def load_state(self, filepath: str = "data/kral_state.json") -> dict:
        """Load session state."""
        if Path(filepath).exists():
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}


def main() -> None:
    """Run interactive demo."""
    print("\n" + "="*60)
    print("  ^^ KRAL ^^  - Turk AI Trading Assistant")
    print("="*60)
    
    kral = KralDemo()
    
    # Greet
    print(f"\n{kral.greet('BTCUSDT')}\n")
    
    # Demo ticks
    demo_ticks = [
        ("BTCUSDT", "97234.10", "0.004"),
        ("BTCUSDT", "97235.50", "0.120"),
        ("BTCUSDT", "97230.00", "1.500"),
    ]
    
    print("Canli veri ornegi:")
    for symbol, price, volume in demo_ticks:
        print(f"  {kral.tick(symbol, price, volume)}")
    
    # Interactive chat
    print("\n" + "-"*60)
    print("Interaktif sohbet (cikis icin 'veda' yaz)")
    print("-"*60 + "\n")
    
    while True:
        try:
            user_input = input("Sen: ").strip()
            if not user_input:
                continue
            
            reply = kral.reply(user_input)
            print(f"Kral: {reply}")
            print(f"  [Turbo Level: {kral.turbo_level}]\n")
            
            if "veda" in user_input.lower():
                break
        
        except KeyboardInterrupt:
            print("\n\nCikiliyor...")
            break
        except Exception as e:
            print(f"Hata: {e}")
    
    # Save state
    kral.save_state()
    print("\nTekrar gorusuruz!")


if __name__ == "__main__":
    main()
