import csv
import json
from memory import connect

def export_memory_to_csv(filename="memory_export.csv"):
    with connect() as conn:
        rows = conn.execute("SELECT * FROM memory").fetchall()
        with open(filename, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["user_id", "name", "message", "reply"])
            writer.writerows(rows)

def export_memory_to_json(filename="memory_export.json"):
    with connect() as conn:
        rows = conn.execute("SELECT * FROM memory").fetchall()
        data = [{"user_id": r[0], "name": r[1], "message": r[2], "reply": r[3]} for r in rows]
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
