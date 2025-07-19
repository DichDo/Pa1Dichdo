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
        self.page_access_token = os.getenv("PAGE_ACCESS_TOKEN")
        self.verify_token = os.getenv("VERIFY_TOKEN")
        self.graph_api_base = os.getenv("GRAPH_API_BASE", "https://graph.facebook.com/v18.0")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
