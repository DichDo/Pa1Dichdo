# 🚀 AI SOCIAL BOT 🚀
# /database.py

"""
Database module for the AI Social Bot.
Handles all interactions with the SQLite database.
"""

import sqlite3
import json
import csv
import re

DB_FILE = "memory.db"

def init_db():
    """
    Initializes the database and creates the user_memory table if it doesn't exist.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_memory (
            user_id TEXT PRIMARY KEY,
            name TEXT,
            last_message TEXT,
            tags TEXT,
            is_lead INTEGER DEFAULT 0
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            user_msg TEXT,
            bot_reply TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def get_user(user_id):
    """
    Retrieves a user's data from the database.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT name, last_message, tags FROM user_memory WHERE user_id = ?", (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    if user_data:
        return {"name": user_data[0], "last_message": user_data[1], "tags": user_data[2]}
    return None

def update_user(user_id, name, last_message, tags, is_lead):
    """
    Updates a user's data in the database.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO user_memory (user_id, name, last_message, tags, is_lead)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, name, last_message, tags, is_lead))
    conn.commit()
    conn.close()

def extract_name(message):
    """
    Extracts a name from a message using regex.
    """
    match = re.search(r"my name is (\w+)", message, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def tag_user(message):
    """
    Tags a user based on keywords in their message.
    """
    tags = []
    is_lead = 0
    if "price" in message.lower() or "commission" in message.lower():
        tags.append("lead")
        is_lead = 1
    if "love your work" in message.lower() or "amazing" in message.lower():
        tags.append("fan")
    return ",".join(tags), is_lead

def export_to_json():
    """
    Exports the user memory to a JSON file.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_memory")
    rows = cursor.fetchall()
    conn.close()
    with open("user_memory.json", "w") as f:
        json.dump([dict(zip([c[0] for c in cursor.description], row)) for row in rows], f, indent=4)

def export_to_csv():
    """
    Exports the user memory to a CSV file.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_memory")
    rows = cursor.fetchall()
    conn.close()
    with open("user_memory.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([c[0] for c in cursor.description])
        writer.writerows(rows)

def get_leads():
    """
    Retrieves all leads from the database.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, name FROM user_memory WHERE is_lead = 1")
    rows = cursor.fetchall()
    conn.close()
    return [{"user_id": row[0], "name": row[1]} for row in rows]

def get_chat_logs(limit=50):
    """
    Retrieves the last N chat logs from the database.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, user_msg, bot_reply, timestamp FROM chat_log ORDER BY timestamp DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [{"user_id": row[0], "user_msg": row[1], "bot_reply": row[2], "timestamp": row[3]} for row in rows]

def log_conversation(user_id, user_msg, bot_reply):
    """
    Logs a conversation to the database.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO chat_log (user_id, user_msg, bot_reply)
        VALUES (?, ?, ?)
    """, (user_id, user_msg, bot_reply))
    conn.commit()
    conn.close()
