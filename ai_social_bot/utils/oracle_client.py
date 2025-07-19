# 𓂀 AI SOCIAL BOT 𓂀
# /utils/oracle_client.py

"""
The Oracle Client: A conduit to the divine realms of the Meta Graph API.
This client handles all communications with the celestial ether.
"""

import requests
from config import SacredConfig

class OracleClient:
    """
    The Oracle Client, a bridge to the Meta Graph API.
    """
    def __init__(self, config: SacredConfig):
        self.config = config
        self.base_url = f"https://graph.facebook.com/{self.config.graph_api_version}"

    def send_message(self, recipient_id: str, message: str):
        """
        Sends a message to a user through the celestial ether.

        Args:
            recipient_id (str): The unique identifier of the recipient.
            message (str): The message to be sent, woven from pure thought.
        """
        url = f"{self.base_url}/me/messages"
        params = {"access_token": self.config.page_access_token}
        payload = {
            "recipient": {"id": recipient_id},
            "message": {"text": message}
        }

        try:
            response = requests.post(url, params=params, json=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error sending message: {e}")
