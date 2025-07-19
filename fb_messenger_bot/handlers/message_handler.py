# -*- coding: utf-8 -*-
# /fb_messenger_bot/handlers/message_handler.py

"""
Message Handler Module: The Oracle that deciphers incoming transmissions.
It listens to the whispers of users and crafts replies.
"""

from ..api import send_message

def handle_message(sender_id, message):
    """
    Processes an incoming message and crafts a response.

    Args:
        sender_id (str): The identifier of the message's originator.
        message (dict): The message payload from the digital ether.
    """

    # The user's query, a ripple in the fabric of spacetime.
    message_text = message.get("text")

    if message_text:
        # A simple echo, for now. A reflection of the user's soul.
        response_text = f"Ancient echoes say: '{message_text}'"
        send_message(sender_id, response_text)
    else:
        # When words fail, silence speaks volumes.
        send_message(sender_id, "I received a message I cannot comprehend, like a forgotten cosmic language.")
