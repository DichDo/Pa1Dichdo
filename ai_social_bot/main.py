# 🚀 AI SOCIAL BOT 🚀
# /main.py

"""
The central nervous system of the AI Social Bot.
This is where the bot awakens and begins its watch.
"""

from flask import Flask
from webhook import webhook_blueprint

app = Flask(__name__)
app.register_blueprint(webhook_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
