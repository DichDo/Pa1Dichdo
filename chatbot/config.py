import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
    PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    PORTFOLIO_LINK = os.getenv("PORTFOLIO_LINK")
