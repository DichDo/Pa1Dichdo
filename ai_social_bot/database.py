# 🚀 AI SOCIAL BOT 🚀
# /database.py

"""
Database module for the AI Social Bot.
Handles all interactions with the SQLite database.
"""

import sqlite3

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
    cursor.execute("SELECT name, last_message, tags FROM user_memory WHERE user_id = ?", (user_id,))
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
        INSERT OR REPLACE INTO user_memory (user_id, name, last_message, tags)
        VALUES (?, ?, ?, ?)
    """, (user_id, name, last_message, tags))
    conn.commit()
    conn.close()
