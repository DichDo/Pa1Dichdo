# 🚀 AI SOCIAL BOT 🚀
# /utils/__init__.py

from .database import *
from .name_utils import *
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")

def simulate_typing_delay(text: str):
    time.sleep(min(2, len(text) / 40))  # Simulate natural delay

def send_facebook_reply(recipient_id, message):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    headers = {"Content-Type": "application/json"}

    # 1. Send typing_on action
    typing_payload = {
        "recipient": {"id": recipient_id},
        "sender_action": "typing_on"
    }
    requests.post(url, json=typing_payload, headers=headers)

    # 2. Wait like a human
    simulate_typing_delay(message)

    # 3. Send actual message
    message_payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message}
    }
    try:
        response = requests.post(url, json=message_payload, headers=headers)
        response.raise_for_status()
        print(f"✅ Message sent: {message}")
    except Exception as e:
        print(f"⚠️ Facebook reply error: {e}")
