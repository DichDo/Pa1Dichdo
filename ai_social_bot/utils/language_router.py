# 🌐 Multilingual Auto-Switching

from langdetect import detect
from handlers.message_handler import handle_message

def route_by_language(sender_id: str, text: str):
    lang = detect(text)
    # you could load different templates per language
    if lang != "en":
        text = f"[{lang.upper()} translation mode] {text}"
    handle_message(sender_id, text)
