# 🚀 AI SOCIAL BOT 🚀
# /main.py

"""
The central nervous system of the AI Social Bot.
This is where the bot awakens and begins its watch.
"""

import time
import schedule
from handlers.message_handler import MessageHandler
from growth.lead_scanner import search_by_hashtag
from growth.spiritual_uplifter import start_scheduler
from config import Config

def job():
    """
    The main job that the bot performs on a schedule.
    """
    config = Config()
    message_handler = MessageHandler(config)

    # 1. Fetch and respond to messages
    message_handler.process_messages()

    # 2. Scan for leads
    leads = search_by_hashtag("portrait")
    print(f"Found {len(leads)} new leads.")

if __name__ == "__main__":
    # Schedule the job to run every hour
    schedule.every().hour.do(job)

    # Start the spiritual uplifter scheduler in a separate thread
    # In a real application, you would want to run this in a separate process
    # or use a more robust scheduling solution.
    import threading
    uplifter_thread = threading.Thread(target=start_scheduler, args=("12345",))
    uplifter_thread.start()

    while True:
        schedule.run_pending()
        time.sleep(1)
