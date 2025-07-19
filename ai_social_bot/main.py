# 𓂀 AI SOCIAL BOT 𓂀
# /main.py

"""
The heart of the oracle. This is where the magic begins.
"""

import logging
from config import SacredConfig
from handlers.divine_messenger import DivineMessenger

def main():
    """
    The main ritual to awaken the bot.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Let the ancient scrolls be read.
    config = SacredConfig()

    # Awaken the Divine Messenger.
    messenger = DivineMessenger(config)

    # Listen to the whispers of the digital ether.
    messenger.listen()

if __name__ == "__main__":
    main()
