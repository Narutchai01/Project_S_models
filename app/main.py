from fastapi import FastAPI
from pydantic import BaseModel
from ultralytics import YOLO
import numpy as np
import os


app = FastAPI()


def get_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


class Data(BaseModel):
    id: int
    image: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
async def predict(data: Data):

    image_url = data.image
    user_id = data.id
    nameAcne = []
    nameFacial = []

    # Load the model
    acneModel = os.path.join("app", "Model", "acne.pt")
    facialModel = os.path.join("app", "Model", "facial.pt")

    img = get_image(image_url)

    acne_result = acneModel.predict(img, stream=False)
    facial_result = facialModel.predict(img, stream=False)

    # return {
    #     "image": data.image,
    #     "user_id": data.id,
    #     "acne_type": [
    #         {
    #             "id": 1,
    #             "count": 10
    #         },
    #         {
    #             "id": 2,
    #             "count": 2
    #         }
    #     ],
    #     "facial_type": [
    #         {
    #             "id": 1,
    #             "count": 10
    #         },
    #         {
    #             "id": 2,
    #             "count": 2
    #         }
    #     ],
    #     "skin_id": 1,
    #     "skincare_id": [1, 2, 3, 4, 5]
    # }
