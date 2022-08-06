from __future__ import annotations
import os.path

from Tweet import Tweet


class ThreadParser:
    def __init__(self, thread_file_path: str):
        if not os.path.isfile(thread_file_path):
            raise ValueError(f"{thread_file_path} is not a file, can't parse")

        self.thread_file_path = thread_file_path
        self.thread: list[Tweet] = []

    def __call__(self):
        with open(self.thread_file_path) as thread_file:
            tweet_content = ""
            image_path = ""
            for line in thread_file:
                if "upload_image:" in line:
                    image_path = line.split(':')[1].rstrip('\n')

                elif line != "\n":
                    tweet_content += line

                else:
                    self._create_tweet(tweet_content, image_path)
                    tweet_content = ""

            self._create_tweet(tweet_content, image_path)

    def _create_tweet(self, text: str, image_path: str) -> None:
        tweet = Tweet(text, image_path)
        self.thread.append(tweet)
