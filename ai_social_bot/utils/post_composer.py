# 💡 AI-Powered Post Generator

import openai
from config import Config

config = Config()
openai.api_key = config.openai_api_key

def compose_post(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role":"user","content": prompt}],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()
