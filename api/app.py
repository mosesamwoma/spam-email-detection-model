from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Spam Email Detection API",
    description="API to classify email text as spam or not spam(ham)",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "spam_classifier_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "tfidf_vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

@app.get("/")
def home():
    return {
        "message": "Welcome to the Spam Email Detection API 🚀",
        "docs": "/docs",
        "predict": "/predict"
    }

class EmailText(BaseModel):
    text: str = Field(..., example="You've won a free iPhone! Click to claim.")

@app.post("/predict")
def predict(email: EmailText):
    X = vectorizer.transform([email.text])
    pred = model.predict(X)[0]
    result = "spam" if pred == 1 else "not spam"
    return {"prediction": result}
