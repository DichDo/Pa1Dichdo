# 𓂀 spiritual_uplifter.py - Sends motivational quotes

import schedule
import time
from utils.meta_api_client import MetaApiClient

QUOTES = [
    "🌻 “Art enables us to find ourselves...”",
    "🌙 “In the moon’s glow, we create magic...”",
    "✨ “Creativity is the soul’s language...”"
]

def send_daily_uplift(recipient_id: str):
    quote = QUOTES[int(time.time()) % len(QUOTES)]
    meta_api_client = MetaApiClient()
    meta_api_client.send_message(recipient_id, quote)

def start_scheduler(recipient_id: str):
    schedule.every().day.at("09:00").do(send_daily_uplift, recipient_id)
    while True:
        schedule.run_pending()
        time.sleep(60)
