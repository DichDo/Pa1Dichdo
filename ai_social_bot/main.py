# 🚀 AI SOCIAL BOT 🚀
# /main.py

"""
The central nervous system of the AI Social Bot.
This is where the bot awakens and begins its watch.
"""

import time
import schedule
from handlers.growth_automator import GrowthAutomator
from handlers.behavior_analyzer import BehaviorAnalyzer
from handlers.message_handler import MessageHandler
from config import Config
from app import app

def job():
    """
    The main job that the bot performs on a schedule.
    """
    config = Config()
    message_handler = MessageHandler(config)
    growth_automator = GrowthAutomator(config)
    behavior_analyzer = BehaviorAnalyzer(config)

    # 1. Fetch and respond to messages
    message_handler.process_messages()

    # 2. Analyze client behavior
    behavior_analyzer.analyze()

    # 3. Perform growth automation tasks
    growth_automator.run()

if __name__ == "__main__":
    # Schedule the job to run every hour
    schedule.every().hour.do(job)

    # Run the Flask app
    app.run(debug=True)

    while True:
        schedule.run_pending()
        time.sleep(1)
