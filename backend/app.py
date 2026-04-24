from fastapi import FastAPI
from model import train_model

app = FastAPI()

model = train_model()

@app.get("/")
def home():
    return {"message": "E-commerce Analytics API Running"}

@app.get("/predict/{day}")
def predict(day: int):
    prediction = model.predict([[day]])
    return {"predicted_revenue": float(prediction[0])}
