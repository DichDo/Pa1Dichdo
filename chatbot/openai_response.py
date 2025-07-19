import openai
import os
from config import Config

config = Config()
openai.api_key = config.OPENAI_API_KEY

def generate_openai_reply(user_msg, memory_rows, name):
    memory_block = "\n".join([
        f"{'User (' + (n or name) + ')' if n else 'User'}: {m}\nBot: {r}"
        for n, m, r in memory_rows
    ])

    # Check if the user is asking for a portfolio
    if "portfolio" in user_msg.lower() or "work" in user_msg.lower() or "gallery" in user_msg.lower():
        return f"Of course! You can view my portfolio here: {config.PORTFOLIO_LINK}"

    prompt = f"""
You are Vairi, a warm, creative AI assistant speaking on behalf of a portrait artist.
Use emojis occasionally. Be thoughtful, helpful, and engaging.

You’re speaking to: {name}

Chat Memory:
{memory_block}

User's new message: {user_msg}

Reply as if you're in a direct, thoughtful conversation:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a smart, soulful art assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
