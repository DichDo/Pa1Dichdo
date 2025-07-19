import re
import time

def extract_name_from_message(message: str) -> str:
    match = re.search(r"\b(?:i am|i'm|my name is)\s+([A-Za-z]+)", message, re.I)
    return match.group(1) if match else None

def simulate_typing_delay(text: str):
    time.sleep(min(2, len(text) / 40))  # Simulate natural delay
