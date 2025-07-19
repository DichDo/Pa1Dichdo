import openai
import os
from config import Config
from persona import get_persona
from textblob import TextBlob

config = Config()
openai.api_key = config.OPENAI_API_KEY

def get_emotion(text):
    """
    Analyzes the emotion of a text using TextBlob.
    """
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.3:
        return "positive"
    elif analysis.sentiment.polarity < -0.3:
        return "negative"
    else:
        return "neutral"

def generate_openai_reply(user_msg, memory_rows, name, persona_type="artist"):
    memory_block = "\n".join([
        f"{'User (' + (n or name) + ')' if n else 'User'}: {m}\nBot: {r}"
        for n, m, r in memory_rows
    ])

    # Check if the user is asking for a portfolio
    if "portfolio" in user_msg.lower() or "work" in user_msg.lower() or "gallery" in user_msg.lower():
        return f"Of course! You can view my portfolio here: {config.PORTFOLIO_LINK}"

    system_prompt = get_persona(persona_type)
    emotion = get_emotion(user_msg)

    prompt = f"""
You’re speaking to: {name}
The user's emotion seems to be: {emotion}

Chat Memory:
{memory_block}

User's new message: {user_msg}

Reply as if you're in a direct, thoughtful conversation, keeping the user's emotion in mind:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
