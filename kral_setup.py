#!/usr/bin/env python
"""Kral Setup & Installation Helper."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def check_python_version() -> bool:
    """Check Python version >= 3.10."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print(f"✗ Python 3.10+ gerekli (bulundu: {version.major}.{version.minor})")
        return False
    print(f"✓ Python {version.major}.{version.minor} OK")
    return True


def check_package(package_name: str, import_name: str | None = None) -> bool:
    """Check if package is installed."""
    if import_name is None:
        import_name = package_name.replace("-", "_")
    
    try:
        __import__(import_name)
        print(f"✓ {package_name} yuklü")
        return True
    except ImportError:
        print(f"✗ {package_name} eksik")
        return False


def install_base_dependencies() -> bool:
    """Install base dependencies."""
    print("\n--- Base Paketler Kuruluyor ---")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        print("✓ pip guncellendi")
        return True
    except subprocess.CalledProcessError:
        print("✗ pip guncellenirken hata")
        return False


def install_voice_dependencies() -> bool:
    """Install voice dependencies."""
    print("\n--- Sesli Sohbet Paketleri Kuruluyor ---")
    packages = [
        "pyttsx3>=2.90",
        "SpeechRecognition>=3.10",
        "sounddevice>=0.5",
        "numpy>=1.26",
    ]
    
    try:
        for package in packages:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✓ {package} kuruldu")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Kurulum hatasi: {e}")
        return False


def install_trading_dependencies() -> bool:
    """Install trading dependencies."""
    print("\n--- Trading Paketleri Kuruluyor ---")
    packages = [
        "httpx>=0.27",
        "websockets>=12",
    ]
    
    try:
        for package in packages:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✓ {package} kuruldu")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Kurulum hatasi: {e}")
        return False


def create_directories() -> None:
    """Create necessary directories."""
    print("\n--- Dizinler Olusturuluyor ---")
    dirs = ["data", "logs", "core", "agents", "voice", "binance", "bist", "memory", "news"]
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
        print(f"✓ {dir_name}/")
    
    # Create __init__.py files
    for dir_name in dirs:
        init_file = Path(dir_name) / "__init__.py"
        init_file.touch()
    print("✓ __init__.py dosyalari olusturuldu")


def create_env_template() -> None:
    """Create .env.example template."""
    print("\n--- Ortam Dosyasi Olusturuluyor ---")
    env_content = """# KRAL Configuration

# Binance
BINANCE_WS_BASE=wss://stream.binance.com:9443/ws

# BIST
BIST_API_KEY=your_key_here
BIST_API_SECRET=your_secret_here

# Voice
VOICE_ENGINE=pyttsx3
STT_ENGINE=speech_recognition

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/kral.log
"""
    
    env_file = Path(".env.example")
    env_file.write_text(env_content)
    print("✓ .env.example olusturuldu")


def run_tests() -> None:
    """Run basic tests."""
    print("\n--- Testler Calistirilyor ---")
    try:
        # Test imports
        print("Temel paketler test ediliyor...")
        import json
        import asyncio
        from pathlib import Path
        print("✓ Temel paketler OK")
    except ImportError as e:
        print(f"✗ Import hatasi: {e}")


def main() -> None:
    """Main setup flow."""
    print("\n" + "="*60)
    print("  KRAL Setup & Installation")
    print("="*60)
    
    # Step 1: Check Python
    print("\n[1/6] Python Kontrolu")
    if not check_python_version():
        sys.exit(1)
    
    # Step 2: Check existing packages
    print("\n[2/6] Yuklü Paketler Kontrolu")
    check_package("pip")
    check_package("setuptools")
    
    # Step 3: Install base
    print("\n[3/6] Base Dependencies")
    install_base_dependencies()
    
    # Step 4: Create directories
    print("\n[4/6] Dizin Yapisi")
    create_directories()
    
    # Step 5: Create config
    print("\n[5/6] Konfigürasyon")
    create_env_template()
    
    # Step 6: Optional installs
    print("\n[6/6] Opsiyonel Paketler")
    print("\nHangi paketleri kurmak istersin?")
    print("1. Sesli Sohbet (pyttsx3, SpeechRecognition, sounddevice, numpy)")
    print("2. Trading (httpx, websockets)")
    print("3. Hepsini Kur")
    print("0. Atla")
    
    choice = input("\nSecim (0-3): ").strip()
    
    if choice in ("1", "3"):
        install_voice_dependencies()
    
    if choice in ("2", "3"):
        install_trading_dependencies()
    
    # Tests
    print("\n[Bonus] Testler")
    run_tests()
    
    # Summary
    print("\n" + "="*60)
    print("  Setup Tamamlandi!")
    print("="*60)
    print("\nSonraki Adimlar:")
    print("  python kral.py --demo      # Demo calistir")
    print("  python kral.py --sesli     # Sesli sohbet")
    print("  python kral_demo.py        # Interaktif demo")
    print("  python kral.py             # GUI basla")
    print()


if __name__ == "__main__":
    main()
