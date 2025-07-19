# -*- coding: utf-8 -*-
# /fb_messenger_bot/api.py

"""
API Module: The conduit to the digital realm of Meta.
Here, we forge connections and dispatch messages to the Graph API.
"""

import requests
from .config import GRAPH_API_URL, PAGE_ACCESS_TOKEN

def send_message(recipient_id, message_text):
    """
    Sends a message to a user through the celestial ether.

    Args:
        recipient_id (str): The unique identifier of the recipient.
        message_text (str): The message to be sent, woven from pure thought.

    Returns:
        dict: The JSON response from the heavens (or an error message).
    """
    params = {
        "access_token": PAGE_ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    }

    # A prayer to the API gods.
    response = requests.post(GRAPH_API_URL, params=params, headers=headers, json=data)

    # Did the gods listen?
    if response.status_code != 200:
        print(f"Error sending message: {response.status_code} {response.text}")

    return response.json()
