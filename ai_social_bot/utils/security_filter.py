# 𓆶 security_filter.py - Simple spam/scam detection

import re

SPAM_PATTERNS = [
    r"free\s+money",
    r"work\s+from\s+home",
    r"https?://\S+"
]

def is_spam(text: str) -> bool:
    for pat in SPAM_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False
