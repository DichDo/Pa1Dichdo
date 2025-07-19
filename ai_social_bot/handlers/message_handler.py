import os
import time
import requests
import csv
import openai
from datetime import datetime
from ai_social_bot.config import Config
from ai_social_bot.utils.meta_api_client import MetaApiClient
from ai_social_bot.database import get_user, update_user, tag_user
from ai_social_bot.utils.name_utils import extract_name
from ai_social_bot.handlers.portfolio_handler import PortfolioHandler

class MessageHandler:
    def __init__(self, config: Config):
        self.config = config
        self.meta_api_client = MetaApiClient(config)
        self.portfolio_handler = PortfolioHandler(self.meta_api_client)
        openai.api_key = self.config.openai_api_key

    def handle_webhook_data(self, data):
        print("📩 Incoming webhook event:", data)
        if data.get("object") == "page":
            for entry in data.get("entry", []):
                for messaging_event in entry.get("messaging", []):
                    if "message" in messaging_event:
                        sender_id = messaging_event["sender"]["id"]
                        message_text = messaging_event["message"].get("text")

                        if message_text:
                            print(f"🧠 Message received: {message_text}")

                            if "portfolio" in message_text.lower() or "work" in message_text.lower():
                                self.portfolio_handler.send_portfolio(sender_id)
                            else:
                                user_data = get_user(sender_id)
                                name = extract_name(message_text) or (user_data["name"] if user_data else "User")
                                tags, is_lead = tag_user(message_text)
                                ai_reply = self.generate_openai_reply(message_text, user_data)
                                self.send_facebook_reply(sender_id, ai_reply)
                                update_user(sender_id, name, message_text, tags, is_lead)
                                self.log_conversation(sender_id, message_text, ai_reply)

    def generate_openai_reply(self, message, user_data):
        prompt = f"The user said: '{message}'"
        if user_data:
            prompt = f"The user, {user_data['name']}, said: '{message}'"
            if user_data.get('tags'):
                prompt += f" (tags: {user_data['tags']})"

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

    def send_facebook_reply(self, recipient_id, message):
        url = f"https://graph.facebook.com/v18.0/me/messages?access_token={self.config.meta_page_access_token}"
        headers = {"Content-Type": "application/json"}

        typing_payload = {
            "recipient": {"id": recipient_id},
            "sender_action": "typing_on"
        }
        requests.post(url, json=typing_payload, headers=headers)

        time.sleep(2 + len(message) * 0.01)

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

from ai_social_bot.database import log_conversation as log_db

    def log_conversation(self, user_id, user_msg, bot_reply):
        log_db(user_id, user_msg, bot_reply)
