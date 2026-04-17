from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Spam Email Detection API",
    description="API to classify email text as spam or ham",
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

class EmailText(BaseModel):
    email_text: str = Field(..., example="You've won a free iPhone! Click to claim.")
    return_confidence: bool = False

@app.get("/")
def home():
    return {
        "message": "Welcome to the Spam Email Detection API",
        "docs": "/docs",
        "predict": "/api/v1/predict"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/api/v1/predict")
def predict(email: EmailText):
    X = vectorizer.transform([email.email_text])
    pred = model.predict(X)[0]
    result = "spam" if str(pred) in ["1", "spam"] else "ham"
    if email.return_confidence:
        proba = model.predict_proba(X)[0]
        confidence = float(max(proba))
        return {"prediction": result, "confidence": confidence}
    return {"prediction": result}