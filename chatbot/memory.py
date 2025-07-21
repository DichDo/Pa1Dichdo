import sqlite3

def connect():
    return sqlite3.connect('chatbot/memory.db')

def init_db():
    with connect() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                user_id TEXT,
                name TEXT,
                message TEXT,
                reply TEXT
            )
        ''')
        conn.commit()

def save_user_memory(user_id, message, reply, name=None):
    with connect() as conn:
        if name:
            conn.execute("INSERT INTO memory (user_id, name, message, reply) VALUES (?, ?, ?, ?)",
                         (user_id, name, message, reply))
        else:
            conn.execute("INSERT INTO memory (user_id, message, reply) VALUES (?, ?, ?)",
                         (user_id, message, reply))
        conn.commit()

def get_user_memory(user_id):
    with connect() as conn:
        rows = conn.execute(
            "SELECT name, message, reply FROM memory WHERE user_id = ? ORDER BY ROWID DESC LIMIT 5",
            (user_id,)
        ).fetchall()
        return rows

def get_latest_name(user_id):
    with connect() as conn:
        result = conn.execute(
            "SELECT name FROM memory WHERE user_id = ? AND name IS NOT NULL ORDER BY ROWID DESC LIMIT 1",
            (user_id,)
        ).fetchone()
        return result[0] if result else "friend"
