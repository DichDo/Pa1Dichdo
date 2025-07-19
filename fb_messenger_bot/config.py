# -*- coding: utf-8 -*-
# /fb_messenger_bot/config.py

"""
Configuration Module: A bridge between the ethereal and the tangible.
Here, we summon secrets from the `.env` scrolls.
"""

import os
from dotenv import load_dotenv

# Let the ancient scrolls of `.env` be read.
load_dotenv()

# The sacred tokens and keys, whispered from the environment.
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
GRAPH_API_VERSION = "v20.0"  # The celestial version of the Graph API.
GRAPH_API_URL = f"https://graph.facebook.com/{GRAPH_API_VERSION}/me/messages"
