import os.path

CHARACTER_LIMIT = 144


class Tweet:
    def __init__(self, text: str, image_path: str):
        if len(text) > CHARACTER_LIMIT:
            raise ValueError(f"Tweet exceeded character limit.\n text={text}")

        if image_path and not os.path.isfile(image_path):
            raise ValueError(f"{image_path} is not a valid image path")

        self.text = text

        if image_path:
            print('Media upload is currently not supported, skipping image path provided')
        self.image_path = ""

