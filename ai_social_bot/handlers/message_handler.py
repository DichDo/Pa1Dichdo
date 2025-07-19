# 🚀 AI SOCIAL BOT 🚀
# /handlers/message_handler.py

"""
Message Handler for the AI Social Bot.
Processes incoming messages, generates responses, and performs sentiment analysis.
"""

import openai
from config import Config
from utils.meta_api_client import MetaApiClient

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
            # This is a simplified example. In a real application, you would
            # need to parse the message content and handle different message types.
            sender_id = message["id"]
            message_text = "This is a test message."

            # 1. Analyze sentiment
            sentiment = self._analyze_sentiment(message_text)
            print(f"Sentiment: {sentiment}")

            # 2. Generate response
            response_text = self._generate_response(message_text)

            # 3. Send response
            self.meta_api_client.send_message(sender_id, response_text)

    def _analyze_sentiment(self, text: str) -> str:
        """
        Analyzes the sentiment of a text using the OpenAI API.
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Sentiment of the following text: '{text}'",
                max_tokens=10
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            return "neutral"

    def _generate_response(self, text: str) -> str:
        """
        Generates a response to a text using the OpenAI API.
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"The user said: '{text}'. Respond in a friendly and helpful manner.",
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error generating response: {e}")
            return "I'm sorry, I'm having trouble understanding you."
