# -*- coding: utf-8 -*-
# /main.py

"""
Main Application: The heart of our creation, where all streams converge.
This script is the nexus, the central pillar of our temple.
To run, one must simply invoke `python main.py`.
"""

from flask import Flask, request, abort
from fb_messenger_bot.config import VERIFY_TOKEN
from fb_messenger_bot.handlers.message_handler import handle_message

# The Flask app, a vessel for our digital spirit.
app = Flask(__name__)

@app.route("/webhook", methods=["GET"])
def webhook_verification():
    """
    Verifies the webhook with the ancient rites of Meta.
    """
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello, world of light and shadow.", 200

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    """
    The grand hall where all messages are received and processed.
    """
    data = request.get_json()

    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    sender_id = messaging_event["sender"]["id"]
                    message = messaging_event["message"]
                    handle_message(sender_id, message)

    return "ok", 200

if __name__ == "__main__":
    # The eternal flame is lit. The server listens.
    app.run(port=5000, debug=True)
