# 🚀 AI SOCIAL BOT 🚀
# /webhook.py

"""
Webhook handler for the AI Social Bot.
This module contains the Flask blueprint for handling webhooks from Meta.
"""

import os
import time
import requests
import csv
from datetime import datetime
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv
import openai
from database import init_db, get_user, update_user

load_dotenv()
webhook_blueprint = Blueprint('webhook', __name__)

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

# Initialize the database
init_db()


@webhook_blueprint.route('/webhook', methods=['GET'])
def verify_webhook():
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    return (challenge, 200) if token == VERIFY_TOKEN else ("Invalid token", 403)


@webhook_blueprint.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    print("📩 Incoming webhook event:", data)

    if data.get("object") == "page":
        for entry in data.get("entry", []):
            for messaging_event in entry.get("messaging", []):
                if "message" in messaging_event:
                    sender_id = messaging_event["sender"]["id"]
                    message_text = messaging_event["message"].get("text")

                    if message_text:
                        print(f"🧠 Message received: {message_text}")
                        user_data = get_user(sender_id)
                        ai_reply = generate_openai_reply(message_text, user_data)
                        send_facebook_reply(sender_id, ai_reply)
                        # In a real application, you would fetch the user's name
                        # from the Graph API.
                        update_user(sender_id, "User", message_text, "")
                        log_conversation(sender_id, message_text, ai_reply)

    return "EVENT_RECEIVED", 200


def generate_openai_reply(message, user_data):
    # This is a simplified example. In a real application, you would want to
    # build a more sophisticated prompt based on the user's data.
    prompt = f"The user said: '{message}'"
    if user_data:
        prompt = f"The user, {user_data['name']}, said: '{message}'"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a warm, imaginative, creative portrait artist. "
                        "You speak like an inspired painter who understands beauty and feeling. "
                        "You are replying to fans and clients with kindness, wisdom, and charm."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"⚠️ OpenAI error: {e}")
        return "Sorry, I'm having trouble right now."


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
    time.sleep(2 + len(message) * 0.01)  # delay based on message length

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


def log_conversation(user_id, user_msg, bot_reply):
    # Ensure the 'logs' directory exists
    if not os.path.exists("logs"):
        os.makedirs("logs")
    with open("logs/conversations.csv", mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), user_id, user_msg, bot_reply])
