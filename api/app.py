from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

app = FastAPI(
    title="Spam Email Detection API",
    description="API to classify email text as spam or not spam",
    version="1.0"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
MODEL_PATH = os.path.join(BASE_DIR, "models", "spam_classifier_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "tfidf_vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

class EmailText(BaseModel):
    text: str

@app.post("/predict")
def predict(email: EmailText):
    X = vectorizer.transform([email.text])
    pred = model.predict(X)[0]
    result = "spam" if pred == 1 else "not spam"
    return {"prediction": result}
