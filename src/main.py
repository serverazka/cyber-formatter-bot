import logging
import telebot
from config import Config

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    """Main function untuk menjalankan bot"""
    try:
        print("🚀 Starting Cyber Formatter Pro...")
        
        # Initialize bot
        bot = telebot.TeleBot(Config.BOT_TOKEN)
        
        # Import dan setup handlers
        from bot.handlers import setup_handlers
        setup_handlers(bot)
        
        print("✅ Bot started successfully!")
        print("🤖 Waiting for messages...")
        print("📍 Press Ctrl+C to stop")
        
        # Start bot
        bot.polling()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        logging.error(f"Bot error: {e}")

if __name__ == "__main__":
    main()