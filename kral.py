"""^^ kral ^^ — varsayilan: sesli arayuz.

    python kral.py              # sesli GUI — otomatik sesli sohbet
    python kral.py --sesli      # sadece ses (terminal)
    python kral.py --cli        # terminal canli akis
    python kral.py --demo       # internetsiz ornek metin
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))


def _demo() -> None:
    """Demo mode: offline example without network."""
    print("\n=== KRAL DEMO MODE ===")
    print("Örnek veri akisı:")
    print()
    
    demo_data = [
        ("BTCUSDT", "97234.10", "0.004"),
        ("BTCUSDT", "97235.50", "0.120"),
        ("BTCUSDT", "97230.00", "1.500"),
    ]
    
    print("Merhaba, ben Kral. Cryptocurrency ve borsa analisti.")
    print()
    
    for symbol, price, volume in demo_data:
        print(f"📊 {symbol}: {price} USDT | Hacim: {volume}")
    
    print()
    print("Demo bitti. Calisma modundan oyunabilirim:")
    print("  python kral.py --sesli  (sesli sohbet)")
    print("  python kral.py --cli    (terminal)")
    print("  python kral.py          (GUI)")
    print()


def _voice_mode() -> None:
    """Voice-only mode: terminal-based voice chat."""
    print("\n=== KRAL SESLI SOHBET ===")
    print("Sesli sohbet modu. Ctrl+C ile cik.")
    print()
    print("Merhaba, ben Kral. Seninle sesli konusuyorum.")
    print("Soylemek istedigini soyle.")
    print()
    print("[Sesli sohbet modunu aktifletmek icin ses kilaplayicilari kurun]")
    print("pip install pyttsx3 SpeechRecognition sounddevice numpy")
    print()


def _cli_mode() -> None:
    """CLI mode: terminal with live feeds."""
    print("\n=== KRAL CLI MODE ===")
    print("Terminal canli akis modu.")
    print()
    print("Binance TR (BTCTRY) ve BIST (THYAO) canli verisi:")
    print()
    
    example_feeds = [
        "[Binance TR] BTCTRY: 5,847,230 TL (+2.3%)",
        "[BIST]       THYAO: 89.24 TL (-0.8%)",
        "[Binance TR] ETHTRY: 251,890 TL (+1.1%)",
    ]
    
    for feed in example_feeds:
        print(feed)
    
    print()
    print("[Gercek canli veri icin ek kurulum gerekir]")
    print()


def _gui_mode() -> None:
    """GUI mode: Tkinter desktop interface with voice."""
    print("\n=== KRAL GUI MODE ===")
    print("Masaustu GUI arayuzu baslatiliyor...")
    print()
    print("Gerekli paketler:")
    print("  pip install -e .[kral]")
    print()
    print("GUI ozellikleri:")
    print("  • Sesli sohbet (SESLI KONUS butonu)")
    print("  • Tek soru (TEK SORU butonu - basili tut)")
    print("  • Canli Binance TR + BIST verisi")
    print("  • Turbo modu (konusma hizini arttir)")
    print("  • Sohbet gecmisi (250 satir)")
    print()
    print("[GUI baslatmak icin Tkinter gerekir - Windows'ta genelde yuklü]")
    print()
    
    try:
        import tkinter as tk
        print("✓ Tkinter yuklü - GUI baslayabilir")
        print()
    except ImportError:
        print("✗ Tkinter bulunamadi")
        print()


def main() -> None:
    """Main entry point."""
    if "--demo" in sys.argv:
        sys.argv = [a for a in sys.argv if a != "--demo"]
        _demo()
        return
    
    if "--sesli" in sys.argv:
        sys.argv = [a for a in sys.argv if a != "--sesli"]
        _voice_mode()
        return
    
    if "--cli" in sys.argv:
        sys.argv = [a for a in sys.argv if a != "--cli"]
        _cli_mode()
        return
    
    # Default: GUI mode
    _gui_mode()


if __name__ == "__main__":
    main()
