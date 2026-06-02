# MEGA_AI / KRAL

**Turkish AI Trading Assistant with Voice Interface**

Modular layout for a trading-aware assistant: shared **core**, market integrations (**binance**, **bist**), **news**, **agents**, **voice**, **memory**, and **logs**.

## 🎯 Quick Start

### Setup
```bash
# 1. Clone and setup
git clone https://github.com/peace53/upgraded-telegram.git
cd upgraded-telegram
git checkout kral-setup

# 2. Run setup
python kral_setup.py

# 3. Test installation
python kral.py --demo
```

### Run Modes

**GUI (Default) - Desktop with Voice**
```bash
python kral.py
```
Features:
- 🎙️ Voice chat ("SESLI KONUS" button)
- 🔘 Single question mode ("TEK SORU" button - hold)
- 📊 Live Binance TR + BIST feeds
- ⚡ Turbo mode (adaptive speed)
- 💬 Chat history (250 lines)

**Voice Only - Terminal Mode**
```bash
python kral.py --sesli
```
Standalone voice conversation without GUI.

**CLI - Live Streaming**
```bash
python kral.py --cli
```
Terminal mode with live market data feeds.

**Demo - Offline Test**
```bash
python kral.py --demo
```
Sample data without network requirements.

**Interactive Demo**
```bash
python kral_demo.py
```
Built-in Q&A with state management.

## 📦 Stack

| Component | Purpose |
|-----------|----------|
| **Language** | Python 3.10+ |
| **Voice** | pyttsx3 (TTS), SpeechRecognition (STT), sounddevice |
| **Markets** | httpx, websockets (Binance), BIST stub |
| **GUI** | Tkinter |
| **Build** | setuptools, ruff |
| **State** | JSON (data/kral_state.json) |

## 🏗️ Project Layout

```
upgraded-telegram/
├── core/              # Shared config, utilities
├── data/              # Models, persistence
├── agents/            # Kral orchestration
├── voice/             # STT/TTS pipeline
├── binance/           # Binance facade
├── bist/              # BIST facade
├── memory/            # SQLite store
├── news/              # News normalization
├── logs/              # Application logs
├── kral.py            # Main entry point
├── kral_demo.py       # Interactive demo
├── kral_setup.py      # Installation helper
└── pyproject.toml     # Package config
```

## 🔧 Installation

### Automatic (Recommended)
```bash
python kral_setup.py
```
Interactive setup with optional voice/trading packages.

### Manual
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\\Scripts\\activate    # Windows

# Install base
pip install -e .

# Optional: Voice
pip install pyttsx3 SpeechRecognition sounddevice numpy

# Optional: Trading
pip install httpx websockets
```

## 🎤 Voice Setup

### Windows
```powershell
# Check Tkinter/GUI support
.\\kontrol_gui.ps1

# Setup microphone
.\\mic_kur.ps1
```

### Linux/Mac
```bash
pip install pyttsx3 SpeechRecognition sounddevice numpy
python -c "import sounddevice; print(sounddevice.query_devices())"
```

## 💬 Interactive Commands

In any mode, try:
- `merhaba` - Greet Kral
- `bitcoin` - Ask about BTC
- `ethereum` - Ask about ETH
- `fiyat` - Request price
- `turbo` - Check turbo level
- `yardim` - Get help
- `veda` - Say goodbye

## 🚀 Features

✅ **Voice Interface** - Speak to Kral, hear responses  
✅ **Live Markets** - Binance TR + BIST streaming  
✅ **Turbo Mode** - Adaptive listening/response speed  
✅ **State Persistence** - Save/load session state  
✅ **Modular Architecture** - Core, agents, integrations separated  
✅ **Turkish Language** - Native Turkish UI and responses  
✅ **Demo Mode** - Test without network/microphone  
✅ **Cross-Platform** - Windows, Linux, macOS support  

## 📝 Configuration

Create `.env` from `.env.example`:

```bash
cp .env.example .env
```

Edit with your settings:
```ini
BINANCE_WS_BASE=wss://stream.binance.com:9443/ws
VOICE_ENGINE=pyttsx3
LOG_LEVEL=INFO
```

## 🔗 Dependencies

**Core:**
- `setuptools>=61`
- `wheel`

**Optional (voice):**
- `pyttsx3>=2.90` - Text-to-speech
- `SpeechRecognition>=3.10` - Speech-to-text
- `sounddevice>=0.5` - Audio I/O
- `numpy>=1.26` - Numeric computing
- `pyaudio>=0.2.14` (Windows)

**Optional (trading):**
- `httpx>=0.27` - Async HTTP client
- `websockets>=12` - WebSocket client

## 🐛 Troubleshooting

**Microphone not working:**
```bash
python -c "import sounddevice; print(sounddevice.query_devices())"
```

**Voice not speaking (Windows):**
```powershell
.\\kontrol_gui.ps1
```

**Import errors:**
```bash
python -m pip install --upgrade --force-reinstall setuptools
python kral_setup.py
```

**Network timeouts:**
Set in `.env`:
```ini
BINANCE_WS_BASE=wss://stream.binance.com:9443/ws
```

## 📖 Documentation

- `README.md` - This file
- `kral.py` - Entry point
- `kral_demo.py` - Demo implementation
- `kral_setup.py` - Setup helper
- `pyproject.toml` - Package metadata

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/xyz`
3. Commit changes: `git commit -am 'Add feature'`
4. Push: `git push origin feature/xyz`
5. Open pull request

## 📄 License

MIT License - see LICENSE file

## 👤 Author

**peace53** - Turkish AI Trading Assistant Project

---

**Ready to start?**

```bash
python kral_setup.py
python kral.py --demo
```

Hosca kaldin! 🚀
