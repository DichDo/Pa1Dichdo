# 🚀 AI SOCIAL BOT 🚀
# /handlers/portfolio_handler.py

"""
Portfolio Handler for the AI Social Bot.
Sends a portfolio of artworks to the user.
"""

from ai_social_bot.utils.meta_api_client import MetaApiClient
from ai_social_bot.portfolio_config import PORTFOLIO_DATA

class PortfolioHandler:
    """
    A handler for sending a portfolio of artworks.
    """
    def __init__(self, meta_api_client: MetaApiClient):
        self.meta_api_client = meta_api_client

    def send_portfolio(self, recipient_id: str):
        """
        Sends a portfolio of artworks to the user.
        """
        attachment_payload = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": PORTFOLIO_DATA
            }
        }

        self.meta_api_client.send_attachment(recipient_id, attachment_payload)
