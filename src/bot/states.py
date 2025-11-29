# User states management
user_states = {}
user_data = {}

class UserState:
    WAITING_FOR_DATA = "waiting_for_data"
    WAITING_FOR_THEME = "waiting_for_theme"
    WAITING_FOR_CONFIRMATION = "waiting_for_confirmation"

def set_user_state(chat_id, state):
    user_states[chat_id] = state

def get_user_state(chat_id):
    return user_states.get(chat_id)

def set_user_data(chat_id, data):
    user_data[chat_id] = data

def get_user_data(chat_id):
    return user_data.get(chat_id)