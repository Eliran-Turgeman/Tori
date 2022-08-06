from __future__ import annotations

import os
from typing import Any
from Tweet import Tweet


class ThreadPublisher:
    def __init__(self, oauth, thread: list[Tweet]):
        self.oauth = oauth
        self.thread = thread

    def __call__(self):
        first_tweet_payload = self._create_payload_from_tweet(self.thread[0])
        response = self._wrap_post_request(
            "https://api.twitter.com/2/tweets",
            payload=first_tweet_payload,
        )

        prev_tweet_id = response.get("data").get("id")

        for tweet in self.thread[1:]:
            tweet_payload = self._create_payload_from_tweet(tweet, prev_tweet_id)
            response = self._wrap_post_request(
                "https://api.twitter.com/2/tweets",
                payload=tweet_payload,
            )

            prev_tweet_id = response.get("data").get("id")

    def _create_payload_from_tweet(self, tweet: Tweet, prev_tweet_id: str | None = None) -> dict[str, Any]:
        payload = {
            "text": tweet.text
        }

        if prev_tweet_id:
            payload["reply"] = {"in_reply_to_tweet_id": prev_tweet_id}

        if tweet.image_path:
            response = self._wrap_post_request(
                url=f"https://upload.twitter.com/1.1/media/upload.json?command=INIT&total_bytes={os.stat(tweet.image_path).st_size}&media_type=image/jpeg",
                payload={}
            )
            media_id = response.get('media_id')

            self._wrap_post_request(
                url=f"https://upload.twitter.com/1.1/media/upload.json?command=FINALIZE&media_id={media_id}",
                payload={}
            )

            payload["media"] = {"media_ids": [media_id]}

        return payload

    def _wrap_post_request(self, url: str, payload: dict[str, Any]) -> dict[str, Any]:
        response = self.oauth.post(
            url,
            json=payload,
        )

        if response.status_code != 201:
            raise Exception(
                "Request returned an error: {} {}".format(response.status_code, response.text)
            )

        return response.json()
