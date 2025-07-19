# -*- coding: utf-8 -*-
# /main.py

"""
Main Application: The entry point of the AI social media manager.
This script launches the FastAPI application and handles webhooks.
"""

from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv
import os
import json
from handlers.message_handler import handle_facebook_message

load_dotenv()

app = FastAPI()

VERIFY_TOKEN = os.getenv("META_VERIFY_TOKEN")

@app.get("/webhook")
async def verify(request: Request):
    """
    Verifies the webhook with Meta.
    """
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge
    raise HTTPException(status_code=403, detail="Invalid token")

@app.post("/webhook")
async def webhook(request: Request):
    """
    Handles incoming webhook events from Meta.
    """
    body = await request.body()
    data = json.loads(body)

    if data.get("object") == "page":
        for entry in data["entry"]:
            for msg_event in entry.get("messaging", []):
                await handle_facebook_message(msg_event)

    return {"status": "ok"}
