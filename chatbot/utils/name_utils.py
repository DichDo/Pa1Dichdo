# 🚀 AI SOCIAL BOT 🚀
# /utils/name_utils.py

"""
Name extraction utility for the AI Social Bot.
"""

import re

def extract_name_from_message(message: str) -> str:
    match = re.search(r"\b(?:i am|i'm|my name is)\s+([A-Za-z]+)", message, re.I)
    return match.group(1) if match else None
