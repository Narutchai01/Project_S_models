from fastapi import FastAPI
from pydantic import BaseModel
from db import get_db_connection
from countance import acne_count
from count_facial import facial_count
from skinanalysis import classify_skin_type
from skincare_recommand import get_skincare_recommendations


app = FastAPI()


class Data(BaseModel):
    id: int
    image: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
async def predict(data: Data):
    return {
        "image": data.image,
        "user_id": data.id,
        "acne_type": [
            {
                "id": 10,
                "count": 10
            },
            {
                "id": 14,
                "count": 2
            }
        ],
        "facial_type": [
            {
                "id": 6,
                "count": 10
            },
            {
                "id": 8,
                "count": 2
            }
        ],
        "skin_id": 16,
        "skincare_id": [1, 2, 3, 4, 5]
    }
