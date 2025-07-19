import sys
import os
from flask import Flask, render_template

# Add the project root to the Python path
print("Adding project root to Python path...")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print("Python path:", sys.path)

print("Importing database functions...")
from database import get_leads, get_chat_logs
print("Database functions imported successfully.")

app = Flask(__name__, template_folder='../templates')

@app.route("/")
def home():
    print("Fetching leads and chat logs...")
    leads = get_leads()
    logs = get_chat_logs(limit=50)
    print("Leads and chat logs fetched successfully.")
    return render_template("dashboard.html", leads=leads, logs=logs)

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
