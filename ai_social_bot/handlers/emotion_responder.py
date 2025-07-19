# 𓆩 emotion_responder.py - Sentiment based responses

from textblob import TextBlob
from utils.meta_api_client import MetaApiClient

def respond_with_emotion(sender_id: str, text: str):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.3:
        tone = "😊 So happy to hear that!"
    elif polarity < -0.3:
        tone = "🙏 I'm sorry to hear that. How can I help?"
    else:
        tone = "🤔 Thanks for sharing. Tell me more."

    reply = f"{tone} You said: “{text}”"
    meta_api_client = MetaApiClient()
    meta_api_client.send_message(sender_id, reply)
