# 🚀 AI SOCIAL BOT 🚀
# /scheduler.py

"""
This module handles the logic for scheduling and sending campaign messages.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import schedule
import time
from utils.database import get_user
from utils import send_facebook_reply
from campaigns import ART_DROP_CAMPAIGN, FIRST_INTERACTION_FUNNEL, GENTLE_FOLLOW_UP

def send_campaign_message(user_id, campaign_type):
    """
    Sends a campaign message to a user.
    """
    user_data = get_user(user_id)
    if not user_data:
        return

    message = ""
    if campaign_type == "art_drop":
        message = ART_DROP_CAMPAIGN
    elif campaign_type == "first_interaction":
        message = FIRST_INTERACTION_FUNNEL
    elif campaign_type == "gentle_follow_up":
        message = GENTLE_FOLLOW_UP

    if message:
        # In a real application, you would replace these placeholders
        # with actual data.
        message = message.replace("[FirstName]", user_data.get("name", "there"))
        message = message.replace("[PORTFOLIO_LINK]", "https://your-portfolio.com")
        message = message.replace("[VIDEO_LINK]", "https://your-video.com")
        send_facebook_reply(user_id, message)

def schedule_campaigns():
    """
    Schedules the marketing campaigns.
    """
    # This is a placeholder for where you would define your scheduling logic.
    # For example, you could schedule a follow-up message to be sent 3 days
    # after the first interaction.
    schedule.every(3).days.at("10:30").do(send_campaign_message, user_id="12345", campaign_type="gentle_follow_up")

    while True:
        schedule.run_pending()
        time.sleep(1)
