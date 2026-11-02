
import joblib
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "model.pkl"

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

    return joblib.load(MODEL_PATH)


def predict_crop(n, p, k, temp, humidity, ph, rainfall):
    model = load_model()

    input_data = np.array([[
        n, p, k, temp, humidity, ph, rainfall
    ]])

    prediction = model.predict(input_data)

    return prediction[0]
