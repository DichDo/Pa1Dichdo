# 𓇬 lead_scanner.py - Scans and identifies leads (mock)

import requests
from config import Config

def search_by_hashtag(hashtag: str, limit: int = 5):
    config = Config()
    url = f"{config.graph_api_base}/ig_hashtag_search"
    params = {
        "user_id": "<YOUR_IG_USER_ID>",
        "q": hashtag,
        "access_token": config.page_access_token
    }
    # Step 1: get hashtag ID
    res = requests.get(url, params=params).json()
    tag_id = res["data"][0]["id"]
    # Step 2: fetch recent media
    media_url = f"{config.graph_api_base}/{tag_id}/recent_media"
    media = requests.get(media_url, params={
        "fields": "id,caption,permalink",
        "access_token": config.page_access_token
    }).json()["data"]
    return media[:limit]
