# 🚀 AI SOCIAL BOT 🚀
# /utils/database.py

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
        CREATE TABLE IF NOT EXISTS memory (
            user_id TEXT PRIMARY KEY,
            name TEXT,
            last_message TEXT,
            tags TEXT
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
    cursor.execute("SELECT name, last_message, tags FROM memory WHERE user_id = ?", (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    if user_data:
        return {"name": user_data[0], "last_message": user_data[1], "tags": user_data[2]}
    return None

def update_user(user_id, name, last_message, tags):
    """
    Updates a user's data in the database.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO memory (user_id, name, last_message, tags)
        VALUES (?, ?, ?, ?)
    """, (user_id, name, last_message, tags))
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
    if "price" in message.lower() or "commission" in message.lower():
        tags.append("lead")
    if "love your work" in message.lower() or "amazing" in message.lower():
        tags.append("fan")
    return ",".join(tags)

def export_to_json():
    """
    Exports the user memory to a JSON file.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM memory")
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
    cursor.execute("SELECT * FROM memory")
    rows = cursor.fetchall()
    conn.close()
    with open("user_memory.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([c[0] for c in cursor.description])
        writer.writerows(rows)
