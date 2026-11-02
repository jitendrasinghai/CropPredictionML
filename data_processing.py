
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "CropData.csv"

def load_and_preprocess_data():

    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    data = pd.read_csv(DATA_PATH)
    data = data.dropna()

    features = [
        "N", "P", "K",
        "temperature", "humidity",
        "ph", "rainfall"
    ]

    X = data[features]
    y = data["label"]

    return X, y
