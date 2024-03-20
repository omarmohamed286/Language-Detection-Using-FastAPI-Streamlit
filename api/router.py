from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import numpy as np

model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'model','joblib_model.sav')
model,vectorizer,encoder = joblib.load(model_path)


def predict(text):
    text = [text]
    text_vector = vectorizer.transform(text).toarray()
    predictions = model.predict(text_vector)
    return encoder.classes_[np.argmax(predictions)]


app = FastAPI()

class TextObject(BaseModel):
    text: str

@app.get('/')
def home():
    return {'msg':'Language Detection Model Is Ready To Use'}

@app.post('/detectLanguage')
def detect_lanuage(data:TextObject):
    text = data.text
    prediction = predict(text)
    return {'language':prediction}

