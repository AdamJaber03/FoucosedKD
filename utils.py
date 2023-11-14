import time
from pathlib import Path

import openai
import requests
import io
import PIL.Image as Image


class gptConnector:
    def __init__(self):
        self.key = r"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"
        openai.api_key = self.key

    def chat_predict(self, msgs, model, temp=0.5):
        result = openai.chat.completions.create(
            model=model,
            messages=msgs,
            temperature=temp
        )
        return result.choices[0].message.content

    def image_predict(self, prompt, model, n=1, size="512x512"):
        response = openai.images.generate(
            model=model,
            prompt=prompt,
            size=size,
            quality="standard",
            n=n,
        )
        images = []
        for gen in response.data:
            print(gen.url)
            images.append(Image.open(io.BytesIO(requests.get(gen.url).content)))
        return images[0] if len(images) == 1 else images




if __name__ == "__main__":
    gpt = gptConnector()
    # prompt = "hello, please respond with a list of 3 simple food items"
    # prompt = "please create a list of 50 examples of spam and non spam (ham) emails, generate only the body for these emails, no need for subject, recipient, ect. . This data will be used to train a spam email detector so make sure it is as rich and varied as possible, as well as resembles real world spam and non spam (ham) emails."
    # msgs = [{"role": "user", "content": prompt}]
    #model = "gpt-3.5-turbo"
    #model = "gpt-4-1106-preview"
    #answer = gpt.chat_predict(msgs=msgs, model=model)
    # for j in range(87):
    #     dog_images = gpt.image_predict("an image of a dog for a dataset for creating a CNN model that classifies between dogs and cats, images should be from a lot of different angles and environments and lot of different dog species, insure a varied and complex dataset, include faces in most images", "dall-e-2", n=5, size="256x256")
    #     dog_path = Path(r"C:\Users\adamj\PycharmProjects\focousedKD\example projects FKD\dog_cat_classifier\data\generated\dogs")
    #     for i, image in enumerate(dog_images):
    #         image.save(dog_path / f"dog_image_{65+i+5*j}.png")
    #     time.sleep(70)
