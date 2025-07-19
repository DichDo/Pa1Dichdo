# 𓂀 AI SOCIAL BOT 𓂀
# /handlers/divine_messenger.py

"""
The Divine Messenger: The heart of the AI's logic.
This module processes incoming messages and generates responses.
"""

from utils.oracle_client import OracleClient
from config import SacredConfig

class DivineMessenger:
    """
    The Divine Messenger, a handler for incoming messages.
    """
    def __init__(self, config: SacredConfig):
        self.oracle_client = OracleClient(config)

    def listen(self):
        """
        Listens for incoming messages and processes them.
        """
        # This is a placeholder for where you would listen for webhooks.
        # For now, we'll simulate an incoming message.
        sample_message = {
            "sender": {"id": "12345"},
            "message": {"text": "Hello, Oracle!"}
        }
        self.handle_message(sample_message)

    def handle_message(self, message: dict):
        """
        Handles an incoming message from the digital ether.

        Args:
            message (dict): The message payload from the webhook.
        """
        sender_id = message["sender"]["id"]
        message_text = message["message"]["text"]

        # A simple echo, for now. A reflection of the user's soul.
        response_text = f"The Oracle has spoken: '{message_text}'"
        self.oracle_client.send_message(sender_id, response_text)
