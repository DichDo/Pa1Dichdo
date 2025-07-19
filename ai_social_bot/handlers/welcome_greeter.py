# 🤖 Hyper-Personal Welcome Bot

import requests
from utils.meta_api_client import MetaApiClient
from config import Config

def greet_new_follower(user_id: str):
    config = Config()
    # Fetch public profile (name, locale)
    profile = requests.get(
        f"{config.graph_api_base}/{user_id}",
        params={"fields": "name", "access_token": config.page_access_token}
    ).json()
    name = profile.get("name", "Friend")
    reply = f"🎉 Welcome, {name}! Thanks for following Elysian Atelier."
    meta_api_client = MetaApiClient()
    meta_api_client.send_message(user_id, reply)
