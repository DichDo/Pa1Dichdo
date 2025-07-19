# 🚀 AI SOCIAL BOT 🚀
# /utils/meta_api_client.py

"""
Meta API Client for the AI Social Bot.
Handles all communications with the Meta Graph API.
"""

import time
import requests
from config import Config

class MetaApiClient:
    """
    A client for interacting with the Meta Graph API.
    """
    def __init__(self, config: Config):
        self.config = config
        self.base_url = "https://graph.facebook.com/v20.0"

    def send_message(self, recipient_id: str, message: str):
        """
        Sends a message to a user.
        """
        url = f"{self.base_url}/me/messages"
        params = {"access_token": self.config.meta_page_access_token}
        payload = {
            "recipient": {"id": recipient_id},
            "message": {"text": message}
        }

        self._make_request("POST", url, params=params, json=payload)

    def get_messages(self):
        """
        Fetches new messages.
        """
        url = f"{self.base_url}/me/conversations"
        params = {"access_token": self.config.meta_page_access_token}
        response = self._make_request("GET", url, params=params)
        return response.json().get("data", [])

    def _make_request(self, method: str, url: str, **kwargs):
        """
        Makes a request to the Meta Graph API with retry logic.
        """
        retries = 3
        for i in range(retries):
            try:
                response = requests.request(method, url, **kwargs)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                print(f"Error making request: {e}")
                if i < retries - 1:
                    time.sleep(2 ** i)
                else:
                    raise
