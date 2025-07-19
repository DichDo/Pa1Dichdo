# 𓂀 AI SOCIAL BOT 𓂀
# /config.py

"""
The Sacred Config: A tome of ancient secrets and configurations.
"""

import os
from dotenv import load_dotenv

class SacredConfig:
    """
    The Sacred Config, a class to hold all configuration variables.
    """
    def __init__(self):
        load_dotenv()
        self.page_access_token = os.getenv("PAGE_ACCESS_TOKEN")
        self.verify_token = os.getenv("VERIFY_TOKEN")
        self.graph_api_version = os.getenv("GRAPH_API_VERSION", "v20.0")
