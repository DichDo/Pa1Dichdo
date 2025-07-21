# 🚀 AI SOCIAL BOT 🚀
# /test_bot.py

"""
Test script for the AI Social Bot.
Simulates user interactions and tests the bot's responses.
"""

import requests
import json
import time

WEBHOOK_URL = "http://localhost:5000/webhook"

def send_test_message(sender_id, message_text):
    """
    Sends a test message to the bot's webhook.
    """
    headers = {"Content-Type": "application/json"}
    payload = {
        "object": "page",
        "entry": [
            {
                "messaging": [
                    {
                        "sender": {"id": sender_id},
                        "message": {"text": message_text}
                    }
                ]
            }
        ]
    }
    try:
        response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        print(f"✅ Test message sent: '{message_text}', Response: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error sending test message: {e}")

if __name__ == "__main__":
    # Give the server some time to start
    time.sleep(10)

    # Test cases
    test_cases = [
        {"sender_id": "test_user_1", "message": "Hi"},
        {"sender_id": "test_user_1", "message": "Can I see your portfolio?"},
        {"sender_id": "test_user_2", "message": "I'm interested in a commission."},
        {"sender_id": "test_user_3", "message": "I'm feeling sad today."},
        {"sender_id": "test_user_4", "message": ""}, # Empty message
        {"sender_id": "test_user_5", "message": "Click this link for free money!"}, # Spam
    ]

    for test in test_cases:
        send_test_message(test["sender_id"], test["message"])
