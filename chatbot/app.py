# 🚀 AI SOCIAL BOT 🚀
# /app.py

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request
from openai_response import generate_openai_reply
from memory import get_user_memory, save_user_memory, get_latest_name, init_db
from utils.name_utils import extract_name_from_message
from utils import send_facebook_reply, simulate_typing_delay
from scheduler import schedule_campaigns
import threading
import csv
from datetime import datetime


app = Flask(__name__)
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

# Initialize the database
init_db()

def log_conversation(user_id, user_msg, bot_reply):
    # Ensure the 'logs' directory exists
    if not os.path.exists("chatbot/logs"):
        os.makedirs("chatbot/logs")
    with open("chatbot/logs/conversations.csv", mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), user_id, user_msg, bot_reply])

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Verification failed", 403

    if request.method == "POST":
        data = request.get_json()
        if not data:
            return "Error: Invalid JSON", 400

        for entry in data.get("entry", []):
            for msg_event in entry.get("messaging", []):
                sender_id = msg_event.get("sender", {}).get("id")
                if not sender_id:
                    continue

                if "message" in msg_event:
                    user_message = msg_event["message"].get("text", "")

                    try:
                        # Detect name if possible
                        name = extract_name_from_message(user_message)
                        memory = get_user_memory(sender_id)
                        known_name = name or get_latest_name(sender_id)

                        # Typing simulation
                        simulate_typing_delay(user_message)

                        # Generate reply
                        reply = generate_openai_reply(user_message, memory, known_name)

                        # Save
                        save_user_memory(sender_id, user_message, reply, name)

                        # Log conversation
                        log_conversation(sender_id, user_message, reply)

                        # Send reply
                        send_facebook_reply(sender_id, reply)
                    except Exception as e:
                        print(f"Error handling message: {e}")
                        send_facebook_reply(sender_id, "I'm sorry, I encountered an error. Please try again later.")


        return "OK", 200

if __name__ == "__main__":
    # Start the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=schedule_campaigns)
    scheduler_thread.start()

    app.run(debug=True, port=5000)
