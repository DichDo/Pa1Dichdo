# 🚀 AI SOCIAL BOT 🚀
# /webhook.py

"""
Webhook handler for the AI Social Bot.
This module contains the Flask blueprint for handling webhooks from Meta.
"""

import os
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv
from ai_social_bot.config import Config
from ai_social_bot.handlers.message_handler import MessageHandler
from ai_social_bot.database import init_db

load_dotenv()
webhook_blueprint = Blueprint('webhook', __name__)

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

# Initialize the database
init_db()

# Create a config object
config = Config()

# Create a message handler
message_handler = MessageHandler(config)

@webhook_blueprint.route('/webhook', methods=['GET'])
def verify_webhook():
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if token == VERIFY_TOKEN:
        return challenge, 200
    else:
        return "Invalid token", 403

@webhook_blueprint.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    message_handler.handle_webhook_data(data)
    return "EVENT_RECEIVED", 200
