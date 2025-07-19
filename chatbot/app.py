# 🚀 AI SOCIAL BOT 🚀
# /app.py

from flask import Flask, request
from openai_response import generate_openai_reply
from memory import get_user_memory, save_user_memory, get_latest_name
from utils import extract_name_from_message, simulate_typing_delay
from scheduler import schedule_campaigns
import os
import threading

app = Flask(__name__)
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Verification failed", 403

    if request.method == "POST":
        data = request.get_json()
        for entry in data.get("entry", []):
            for msg_event in entry.get("messaging", []):
                sender_id = msg_event["sender"]["id"]
                if "message" in msg_event:
                    user_message = msg_event["message"].get("text", "")

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

                    # (Optional) Send reply via Messenger API here
                    print(f"Reply to {sender_id}: {reply}")

        return "OK", 200

if __name__ == "__main__":
    # Start the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=schedule_campaigns)
    scheduler_thread.start()

    app.run(debug=True, port=5000)
