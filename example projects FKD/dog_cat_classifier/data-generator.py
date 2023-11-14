from utils import gptConnector
from pathlib import Path
import time

def generate_cats_dogs(n, animaltype="dog"):
    gpt = gptConnector()
    prompt = f"an image of a {animaltype} for a dataset for creating a CNN model that classifies between dogs and cats, images should be from a lot of different angles and environments and lot of different {animaltype} species, insure a varied and complex dataset, include faces in most images"
    prompt = f"Create a high-resolution image, that will be part of a dataset of 1000 diverse images of different {animaltype} breeds in various settings, poses, and lighting conditions. Ensure each image is distinct and clear for classification purposes"
    prompt = f"Generate a high-resolution image of a {animaltype} in various poses and environments. Include different breeds and sizes, ensuring a diverse representation. Avoid any human elements or other animals in the image."
    for j in range(n//5):
        dog_images = gpt.image_predict(
            prompt,
            "dall-e-2",
            n=5,
            size="256x256")
        animalpath = Path(fr"C:\Users\adamj\PycharmProjects\focousedKD\example projects FKD\dog_cat_classifier\data\generated\{animaltype}s")
        for i, image in enumerate(dog_images):

            image.save(animalpath / f"{animaltype}_image_{790 + i + 5 * j}.png")
        time.sleep(60)

if __name__ == "__main__":
    generate_cats_dogs(10, animaltype="cat")
