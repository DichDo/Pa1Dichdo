# 🚀 AI SOCIAL BOT 🚀
# /utils/name_utils.py

"""
Name extraction utility for the AI Social Bot.
"""

import re

def extract_name(message):
    """
    Extracts a name from a message using regex.
    """
    match = re.search(r"my name is (\w+)", message, re.IGNORECASE)
    if match:
        return match.group(1)
    return None
