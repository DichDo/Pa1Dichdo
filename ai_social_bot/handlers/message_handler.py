# 🚀 AI SOCIAL BOT 🚀
# /handlers/message_handler.py

"""
Message Handler for the AI Social Bot.
Processes incoming messages, generates responses, and performs sentiment analysis.
"""

import openai
from config import Config
from utils.meta_api_client import MetaApiClient
from utils.security_filter import is_spam
from handlers.persona_handler import get_persona
from handlers.emotion_responder import respond_with_emotion
from memory.user_memory import store_message, retrieve_memory
from utils.language_router import route_by_language

class MessageHandler:
    """
    A handler for processing incoming messages.
    """
    def __init__(self, config: Config):
        self.config = config
        self.meta_api_client = MetaApiClient(config)
        openai.api_key = self.config.openai_api_key

    def process_messages(self):
        """
        Fetches and processes new messages.
        """
        messages = self.meta_api_client.get_messages()
        for message in messages:
            sender_id = message["id"]
            # This is a simplified example. In a real application, you would
            # need to parse the message content and handle different message types.
            message_text = "This is a test message."

            # 1. Security check
            if is_spam(message_text):
                print(f"Spam detected from {sender_id}. Ignoring.")
                continue

            # 2. Store message in memory
            store_message(sender_id, message_text)

            # 3. Route by language
            route_by_language(sender_id, message_text)

    def handle_message(self, sender_id: str, message_text: str):
        """
        Handles a message after it has been routed by language.
        """
        # 1. Get persona
        persona = get_persona("oracle")

        # 2. Respond with emotion
        respond_with_emotion(sender_id, message_text)
