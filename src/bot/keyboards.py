from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

def create_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    buttons = [
        KeyboardButton("📥 INPUT DATA"),
        KeyboardButton("🎭 THEMES"),
        KeyboardButton("📊 MY STATS"),
        KeyboardButton("❓ HELP")
    ]
    
    for i in range(0, len(buttons), 2):
        if i + 1 < len(buttons):
            keyboard.add(buttons[i], buttons[i+1])
        else:
            keyboard.add(buttons[i])
    
    return keyboard

def create_theme_keyboard(data_type="general"):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    themes = [
        KeyboardButton("🔍 FORENSIC"),
        KeyboardButton("📱 MODERN"),
        KeyboardButton("🕵️ DARK"),
        KeyboardButton("🎪 CYBERPUNK"),
        KeyboardButton("🔒 CLASSIFIED"),
        KeyboardButton("⬅️ BACK")
    ]
    
    for i in range(0, len(themes), 2):
        if i + 1 < len(themes):
            keyboard.add(themes[i], themes[i+1])
        else:
            keyboard.add(themes[i])
    
    return keyboard

def remove_keyboard():
    return ReplyKeyboardRemove()