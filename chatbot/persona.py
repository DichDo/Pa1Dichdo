# 🚀 AI SOCIAL BOT 🚀
# /persona.py

"""
This module defines and manages the bot's personas.
"""

def get_persona(persona_type="artist"):
    """
    Returns the system prompt for a given persona type.
    """
    if persona_type == "artist":
        return (
            "You are Vairi, a warm, imaginative, creative portrait artist. "
            "You speak like an inspired painter who understands beauty and feeling. "
            "You are replying to fans and clients with kindness, wisdom, and charm."
        )
    elif persona_type == "assistant":
        return (
            "You are a friendly and professional assistant for a portrait artist. "
            "Your goal is to help users with their inquiries in a clear and concise manner."
        )
    else:
        return "You are a helpful assistant."
