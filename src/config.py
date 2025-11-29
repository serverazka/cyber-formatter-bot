import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    ADMIN_ID = int(os.getenv('ADMIN_ID', 0))
    
    if not BOT_TOKEN:
        raise ValueError("❌ BOT_TOKEN tidak ditemukan di file .env")
    
    # Bot settings
    MAX_MESSAGE_LENGTH = 4000