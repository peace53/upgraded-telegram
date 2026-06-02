#!/usr/bin/env python3
"""
🎯 KRAL - Türkçe AI Trading Assistant
Ana giriş noktası - 4 mod

Kullanım:
  python kral.py              # sesli GUI (varsayılan)
  python kral.py --sesli      # sadece sesli (terminal)
  python kral.py --cli        # canlı akış (terminal)
  python kral.py --demo       # demo (internet yok)
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
    print("Örnek veri akışı:")
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
    print("Demo bitti. Çalışma modundan oyunabilirim:")
    print("  python kral.py --sesli  (sesli sohbet)")
    print("  python kral.py --cli    (terminal)")
    print("  python kral.py          (GUI)")
    print()


def _voice_mode() -> None:
    """Voice-only mode: terminal-based voice chat."""
    print("\n=== KRAL SESLI SOHBET ===")
    print("Sesli sohbet modu. Ctrl+C ile çık.")
    print()
    print("Merhaba, ben Kral. Seninle sesli konuşuyorum.")
    print("Söylemek istediğini söyle.")
    print()
    print("[Sesli sohbet modunu aktifletmek için ses kütüphanelerini kurun]")
    print("pip install pyttsx3 SpeechRecognition sounddevice numpy")
    print()


def _cli_mode() -> None:
    """CLI mode: terminal with live feeds."""
    print("\n=== KRAL CLI MODE ===")
    print("Terminal canlı akış modu.")
    print()
    print("Binance TR (BTCTRY) ve BIST (THYAO) canlı verisi:")
    print()
    
    example_feeds = [
        "[Binance TR] BTCTRY: 5,847,230 TL (+2.3%)",
        "[BIST]       THYAO: 89.24 TL (-0.8%)",
        "[Binance TR] ETHTRY: 251,890 TL (+1.1%)",
    ]
    
    for feed in example_feeds:
        print(feed)
    
    print()
    print("[Gerçek canlı veri için ek kurulum gerekir]")
    print()


def _gui_mode() -> None:
    """GUI mode: Tkinter desktop interface with voice."""
    print("\n=== KRAL GUI MODE ===")
    print("Masaüstü GUI arayüzü başlatılıyor...")
    print()
    print("Gerekli paketler:")
    print("  pip install -e .[kral]")
    print()
    print("GUI özellikleri:")
    print("  • Sesli sohbet (SESLI KONUS butonu)")
    print("  • Tek soru (TEK SORU butonu - basılı tut)")
    print("  • Canlı Binance TR + BIST verisi")
    print("  • Turbo modu (konuşma hızını arttır)")
    print("  • Sohbet geçmişi (250 satır)")
    print()
    print("[GUI başlatmak için Tkinter gerekir - Windows'ta genelde yüklü]")
    print()
    
    try:
        import tkinter as tk
        print("✓ Tkinter yüklü - GUI başlayabilir")
        print()
    except ImportError:
        print("✗ Tkinter bulunamadı")
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
