import os
import requests
from requests_oauthlib import OAuth1


class TwitterClient:
    """
    Uses OAuth 1.0a user-context (common for legacy examples).
    If credentials are missing, methods will safely no-op so the app still runs.
    """

    def __init__(self):
        self.api_key = os.getenv("X_API_KEY")
        self.api_secret = os.getenv("X_API_SECRET")
        self.access_token = os.getenv("X_ACCESS_TOKEN")
        self.access_secret = os.getenv("X_ACCESS_SECRET")

    def _ready(self) -> bool:
        return all(
            [self.api_key, self.api_secret, self.access_token, self.access_secret]
        )

    def tweet_text(self, text: str) -> dict:
        if not self._ready():
            return {"skipped": True, "reason": "Missing X API credentials"}

        url = "https://api.x.com/2/tweets"
        auth = OAuth1(
            self.api_key, self.api_secret, self.access_token, self.access_secret
        )

        r = requests.post(url, json={"text": text}, auth=auth, timeout=20)
        return {"status_code": r.status_code, "body": r.json() if r.content else {}}
