import telebot
from bot.keyboards import create_main_keyboard, create_theme_keyboard, remove_keyboard
from bot.states import set_user_state, get_user_state, set_user_data, get_user_data, UserState
from utils.parser import parse_text_input, detect_template_type
from utils.ai_enhancer import ai_enhance_data
from bot.formatter import generate_formatted_text, split_long_message

def setup_handlers(bot):
    """Setup semua message handlers"""
    
    # === MAIN MENU ===
    @bot.message_handler(commands=['start', 'menu'])
    def send_welcome(message):
        welcome_text = """
🤖 **CYBER FORMATTER PRO**

Format teks biasa menjadi laporan professional dengan AI enhancement!

✨ **FITUR UNGGULAN:**
• AI Auto-Enhancement
• Multiple Themes
• Smart Parsing
• Data Validation
"""
        bot.send_message(
            message.chat.id, 
            welcome_text,
            reply_markup=create_main_keyboard(),
            parse_mode='Markdown'
        )
    
    # === INPUT DATA BUTTON ===
    @bot.message_handler(func=lambda message: message.text == "📥 INPUT DATA")
    def ask_for_data(message):
        set_user_state(message.chat.id, UserState.WAITING_FOR_DATA)
        
        bot.send_message(
            message.chat.id,
            "📝 **SILAKAN MASUKKAN DATA ANDA**\n\n"
            "Paste atau ketik data yang ingin diformat:\n\n"
            "**Contoh:**\n"
            "NIK: 1234567890123456\n"
            "Nama: John Doe\n"
            "Alamat: Jakarta Selatan",
            reply_markup=remove_keyboard(),
            parse_mode='Markdown'
        )
    
    # === PROCESS USER DATA ===
    @bot.message_handler(func=lambda message: get_user_state(message.chat.id) == UserState.WAITING_FOR_DATA)
    def process_user_data(message):
        try:
            # Parse input user
            raw_data = parse_text_input(message.text)
            
            if not raw_data:
                bot.send_message(
                    message.chat.id,
                    "❌ **Gagal memproses data!**\n\n"
                    "Pastikan format:\n"
                    "`field: value`\n\n"
                    "Contoh:\n"
                    "`NIK: 1234567890123456`\n"
                    "`Nama: John Doe`",
                    parse_mode='Markdown'
                )
                return
            
            # AI Enhancement
            enhanced_data = ai_enhance_data(raw_data)
            
            # Simpan data user
            set_user_data(message.chat.id, enhanced_data)
            set_user_state(message.chat.id, UserState.WAITING_FOR_THEME)
            
            # Tampilkan preview dan minta pilih theme
            data_type = detect_template_type(enhanced_data)
            
            preview_text = f"✅ **DATA BERHASIL DIPROSES!**\n\n📊 **Preview Data:**\n{format_preview(enhanced_data)}\n\n🎭 **Pilih tema formatting:**"
            
            bot.send_message(
                message.chat.id,
                preview_text,
                reply_markup=create_theme_keyboard(data_type),
                parse_mode='Markdown'
            )
            
        except Exception as e:
            bot.send_message(
                message.chat.id,
                f"❌ **Error:** {str(e)}\n\nCoba lagi atau gunakan format yang berbeda.",
                reply_markup=create_main_keyboard()
            )
            set_user_state(message.chat.id, None)
    
    # === THEME SELECTION ===
    @bot.message_handler(func=lambda message: get_user_state(message.chat.id) == UserState.WAITING_FOR_THEME)
    def handle_theme_selection(message):
        theme_map = {
            "🔍 FORENSIC": "forensic",
            "📱 MODERN": "modern", 
            "🕵️ DARK": "dark",
            "🎪 CYBERPUNK": "cyberpunk",
            "🔒 CLASSIFIED": "classified"
        }
        
        if message.text == "⬅️ BACK":
            set_user_state(message.chat.id, None)
            bot.send_message(
                message.chat.id,
                "Kembali ke menu utama...",
                reply_markup=create_main_keyboard()
            )
            return
        
        if message.text in theme_map:
            theme = theme_map[message.text]
            user_data = get_user_data(message.chat.id)
            
            if user_data:
                # Generate formatted text
                formatted = generate_formatted_text(user_data, theme)
                
                # Split dan kirim message
                message_parts = split_long_message(formatted)
                for part in message_parts:
                    bot.send_message(message.chat.id, part)
                
                # Tanya mau format lagi?
                bot.send_message(
                    message.chat.id,
                    "🔄 **Mau format data lain?**\n\nKlik '📥 INPUT DATA' untuk memulai lagi!",
                    reply_markup=create_main_keyboard()
                )
            
            set_user_state(message.chat.id, None)
    
    # === HELP COMMAND ===
    @bot.message_handler(func=lambda message: message.text == "❓ HELP")
    def send_help(message):
        help_text = """
📖 **BANTUAN PENGGUNAAN**

🎯 **CARA PENGGUNAAN:**
1. Klik **📥 INPUT DATA**
2. Paste data Anda
3. Pilih tema formatting
4. Dapatkan hasil yang keren!

📋 **FORMAT INPUT:**
NIK: 1234567890123456
Nama: John Doe
Alamat: Jakarta

🤖 **AI ENHANCEMENT:**
• Auto gender detection
• Name capitalization  
• Location enhancement
• Data validation
"""
        bot.send_message(
            message.chat.id,
            help_text,
            reply_markup=create_main_keyboard(),
            parse_mode='Markdown'
        )
    
    # === STATS BUTTON ===
    @bot.message_handler(func=lambda message: message.text == "📊 MY STATS")
    def show_stats(message):
        stats_text = """
📊 **YOUR STATS**

✨ **Cyber Agent Level:** 1
📈 **Data Formatted:** 0
🎯 **Success Rate:** 100%

🚀 **Keep formatting to level up!**
"""
        bot.send_message(
            message.chat.id,
            stats_text,
            reply_markup=create_main_keyboard()
        )
    
    # === THEMES BUTTON ===
    @bot.message_handler(func=lambda message: message.text == "🎭 THEMES")
    def show_themes(message):
        themes_text = """
🎭 **AVAILABLE THEMES**

🔍 **FORENSIC** - Laporan investigasi klasik
📱 **MODERN** - Tampilan clean modern
🕵️ **DARK** - Mode gelap misterius
🎪 **CYBERPUNK** - Style futuristik neon
🔒 **CLASSIFIED** - Tampilan rahasia militer

Klik **📥 INPUT DATA** untuk mencoba!
"""
        bot.send_message(
            message.chat.id,
            themes_text,
            reply_markup=create_main_keyboard()
        )
    
    # === FALLBACK HANDLER ===
    @bot.message_handler(func=lambda message: True)
    def handle_other_messages(message):
        if message.text.startswith('/'):
            bot.send_message(
                message.chat.id,
                "❌ Command tidak dikenali.\n\nGunakan button di keyboard atau ketik /start",
                reply_markup=create_main_keyboard()
            )
        else:
            bot.send_message(
                message.chat.id,
                "🤖 **Cyber Formatter Pro**\n\nKlik **📥 INPUT DATA** untuk memulai formatting!",
                reply_markup=create_main_keyboard()
            )

def format_preview(data):
    """Format preview data untuk ditampilkan"""
    preview = ""
    for key, value in list(data.items())[:3]:
        display_key = key.replace('_', ' ').title()
        preview += f"• {display_key}: {value}\n"
    
    if len(data) > 3:
        preview += f"• ... dan {len(data) - 3} field lainnya\n"
    
    return preview