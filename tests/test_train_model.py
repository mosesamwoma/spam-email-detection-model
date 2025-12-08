import pandas as pd
from src.train_model import train_and_save_model
import os

def test_train_and_save_model(tmp_path):
    # Sample data
    X_train = ["hello world", "spam message"]
    y_train = ["ham", "spam"]

    model_path = tmp_path / "model.pkl"
    vectorizer_path = tmp_path / "vectorizer.pkl"

    model, vectorizer = train_and_save_model(X_train, y_train, str(model_path), str(vectorizer_path))

    # Check files exist
    assert os.path.exists(model_path)
    assert os.path.exists(vectorizer_path)

    # Check model predicts correctly
    X_vec = vectorizer.transform(["hello world"])
    pred = model.predict(X_vec)
    assert pred[0] == "ham"
