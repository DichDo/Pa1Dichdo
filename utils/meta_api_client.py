# -*- coding: utf-8 -*-
# /utils/meta_api_client.py

"""
Meta API Client: A bridge to the digital realm of Meta.
This module handles all communications with the Meta Graph API.
"""

import os
import httpx
from config import META_PAGE_ACCESS_TOKEN

BASE_URL = "https://graph.facebook.com/v19.0/me/messages"

async def send_message(recipient_id: str, message: str):
    """
    Sends a message to a user via the Meta Graph API.

    Args:
        recipient_id (str): The unique identifier of the recipient.
        message (str): The message to be sent.
    """
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message}
    }
    params = {"access_token": META_PAGE_ACCESS_TOKEN}

    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, params=params, json=payload)
        response.raise_for_status()
