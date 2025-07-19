# 🚀 AI SOCIAL BOT 🚀
# /config.py

"""
Configuration module for the AI Social Bot.
Loads credentials and other constants from the environment.
"""

import os
from dotenv import load_dotenv

class Config:
    """
    Configuration class for the AI Social Bot.
    """
    def __init__(self):
        load_dotenv()
        self.meta_page_access_token = os.getenv("META_PAGE_ACCESS_TOKEN")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
