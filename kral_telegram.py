#!/usr/bin/env python
"""
🤖 KRAL Telegram Bot Integration
Telegram üzerinden AI Trading Assistant
"""

import os
import sys
from pathlib import Path
from typing import Optional

# Add root to path
_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))


class KralTelegramBot:
    """KRAL Telegram Bot Interface."""
    
    def __init__(self, token: Optional[str] = None):
        """Initialize Telegram bot."""
        self.token = token or os.getenv("TELEGRAM_BOT_TOKEN")
        self.bot = None
        self.chat_history = {}
        
        if not self.token:
            print("⚠️  TELEGRAM_BOT_TOKEN environment variable not set")
            print("Set it: export TELEGRAM_BOT_TOKEN='your_token_here'")
            return
        
        try:
            from telegram.ext import Application
            print(f"✓ python-telegram-bot kurulu")
        except ImportError:
            print("✗ python-telegram-bot kurulu değil")
            print("Kur: pip install python-telegram-bot")
    
    def setup(self) -> None:
        """Setup Telegram bot."""
        try:
            from telegram.ext import Application, CommandHandler, MessageHandler
            from telegram.ext import filters
            
            self.app = Application.builder().token(self.token).build()
            
            # Command handlers
            self.app.add_handler(CommandHandler("start", self.handle_start))
            self.app.add_handler(CommandHandler("help", self.handle_help))
            self.app.add_handler(CommandHandler("price", self.handle_price))
            self.app.add_handler(CommandHandler("turbo", self.handle_turbo))
            
            # Message handler
            self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
            
            print("✓ Telegram bot handlers registered")
        except Exception as e:
            print(f"✗ Bot setup error: {e}")
    
    async def handle_start(self, update, context):
        """Handle /start command."""
        await update.message.reply_text(
            "Merhaba! 👋 Ben Kral, Türkçe AI Trading Assistant.\n\n"
            "Komutlar:\n"
            "/help - Yardım\n"
            "/price - Canlı fiyatlar\n"
            "/turbo - Turbo seviyesi\n\n"
            "Ya da sadece sor! 🎯"
        )
    
    async def handle_help(self, update, context):
        """Handle /help command."""
        await update.message.reply_text(
            "🤖 KRAL Komutları:\n\n"
            "💬 Mesaj gönder:\n"
            "  - 'merhaba' - Selam ver\n"
            "  - 'bitcoin' - Bitcoin hakkında\n"
            "  - 'ethereum' - Ethereum hakkında\n"
            "  - 'fiyat' - Canlı fiyatlar\n\n"
            "⚡ Komutlar:\n"
            "  /price - Binance TR + BIST\n"
            "  /turbo - Turbo seviyesi\n"
            "  /help - Bu mesaj\n"
        )
    
    async def handle_price(self, update, context):
        """Handle /price command."""
        prices = {
            "BTCTRY": "5,847,230 TL",
            "THYAO": "89.24 TL",
            "ETHTRY": "251,890 TL"
        }
        
        msg = "📊 Canlı Fiyatlar:\n\n"
        for symbol, price in prices.items():
            msg += f"  {symbol}: {price}\n"
        
        await update.message.reply_text(msg)
    
    async def handle_turbo(self, update, context):
        """Handle /turbo command."""
        await update.message.reply_text(
            "⚡ Turbo Seviyesi: 0/10\n\n"
            "Turbo, konuşma hızını ayarlar.\n"
            "Daha fazla sor → Turbo artar → Kral hızlanır! 🚀"
        )
    
    async def handle_message(self, update, context):
        """Handle regular messages."""
        user_id = update.message.from_user.id
        text = update.message.text.lower()
        
        # Simple responses
        responses = {
            "merhaba": "Selam! 👋 Hoş geldin Kral'a.",
            "bitcoin": "Bitcoin en büyük kripto para. Şu an ~97K USDT.",
            "ethereum": "Ethereum akıllı kontratlar platformu. ETH: ~2.5K USDT.",
            "fiyat": "BTCTRY: 5.8M TL | THYAO: 89.24 TL | ETHTRY: 251K TL",
            "veda": "Hoşça kaldin! 👋",
        }
        
        reply = "İlginç soru! 🤔 Daha detaylı konuşabilir misin?"
        for keyword, response in responses.items():
            if keyword in text:
                reply = response
                break
        
        # Track chat
        if user_id not in self.chat_history:
            self.chat_history[user_id] = []
        
        self.chat_history[user_id].append({
            "user": text,
            "bot": reply
        })
        
        await update.message.reply_text(reply)
    
    async def run(self) -> None:
        """Run the bot."""
        if not self.token:
            print("✗ Token not set. Cannot start bot.")
            return
        
        try:
            self.setup()
            print("\n🚀 KRAL Telegram Bot başlatılıyor...")
            print(f"Token: {self.token[:10]}...")
            
            await self.app.run_polling()
        except Exception as e:
            print(f"✗ Bot error: {e}")
    
    def run_sync(self) -> None:
        """Run bot (sync wrapper)."""
        import asyncio
        asyncio.run(self.run())


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="KRAL Telegram Bot")
    parser.add_argument("--token", help="Telegram bot token")
    parser.add_argument("--mode", default="bot", choices=["bot", "test"])
    args = parser.parse_args()
    
    if args.mode == "test":
        print("\n🧪 TEST MODE")
        print("="*60)
        
        # Test KRAL agent
        from agents.kral import identity
        from agents.kral.voice_chat import KralVoiceChat
        from agents.kral.turbo import TurboBrain
        
        turbo = TurboBrain()
        chat = KralVoiceChat(turbo=turbo)
        
        test_inputs = ["merhaba", "bitcoin", "fiyat", "turbo"]
        
        print(f"\n{identity.greet('BTCUSDT')}\n")
        
        for user_input in test_inputs:
            reply = chat.reply(user_input)
            print(f"Sen: {user_input}")
            print(f"Kral: {reply}\n")
        
        return
    
    # Bot mode
    bot = KralTelegramBot(args.token)
    bot.run_sync()


if __name__ == "__main__":
    main()
