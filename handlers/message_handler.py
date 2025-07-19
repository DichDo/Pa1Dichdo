# -*- coding: utf-8 -*-
# /handlers/message_handler.py

"""
Message Handler: The heart of the AI's logic.
This module processes incoming messages and generates responses.
"""

import os
import httpx
from utils.meta_api_client import send_message

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def handle_facebook_message(event):
    """
    Handles an incoming message from Facebook.

    Args:
        event (dict): The message event from the webhook.
    """
    sender_id = event["sender"]["id"]
    user_text = event["message"].get("text", "")

    prompt = f"""You are a helpful assistant for a portrait artist.
The user said: "{user_text}". Respond politely and warmly."""

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a friendly assistant helping an artist manage their art business."},
            {"role": "user", "content": user_text}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.openai.com/v1/chat/completions",
                                     headers=headers, json=payload)
        reply = response.json()["choices"][0]["message"]["content"]

    await send_message(sender_id, reply)
