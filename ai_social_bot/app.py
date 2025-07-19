# 🚀 AI SOCIAL BOT 🚀
# /app.py

"""
The web UI dashboard for the AI Social Bot.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    """
    Renders the main dashboard.
    """
    # This is a placeholder for where you would fetch real data.
    logs = ["Log entry 1", "Log entry 2", "Log entry 3"]
    stats = {"messages_sent": 100, "leads_followed": 10}
    message_queue = ["Message 1", "Message 2"]

    return render_template("dashboard.html", logs=logs, stats=stats, message_queue=message_queue)
