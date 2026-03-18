import pandas as pd

def load_and_preprocess_data():
   
    data = pd.read_csv("CropData.csv")
    data = data.dropna()
    
    
    X = data[["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]]
    y = data["label"]
    
    return X, y