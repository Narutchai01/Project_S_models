# Use a pipeline as a high-level helper
from transformers import AutoImageProcessor, AutoModelForImageClassification
from transformers import pipeline
from PIL import Image
import requests
import torch

pipe = pipeline("image-classification",
                model="dima806/skin_types_image_detection")


# Load model directly

processor = AutoImageProcessor.from_pretrained(
    "dima806/skin_types_image_detection")
model = AutoModelForImageClassification.from_pretrained(
    "dima806/skin_types_image_detection")


def classify_skin_type(image_url: str, cur):
    image = Image.open(requests.get(image_url, stream=True).raw)

    resultName = ""
    resultID = 0

    # Preprocess the image and make prediction
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    # Get predicted class and scores
    logits = outputs.logits
    probs = torch.softmax(logits, dim=-1)[0]
    predicted_class = logits.argmax(-1).item()

    # Get confidence score for the predicted class
    confidence = probs[predicted_class].item() * 100

    # Get class labels
    labels = model.config.id2label

    # Return normal if confidence is below 60%
    if confidence < 60:
        resultName = "normal"
    else:
        resultName = labels[predicted_class]

    # Query the database to get the corresponding ID for the resultName
    cur.execute("SELECT id FROM face_problems WHERE name = %s", (resultName,))
    result = cur.fetchone()
    if result:
        resultID = result[0]
    else:
        resultID = 0  # Default if not found in database

    return resultName, resultID
