import joblib
import numpy as np

def load_model():
    return joblib.load("model/model.pkl")

def predict_crop(n, p, k, temp, humidity, ph, rainfall):
    model = load_model()
    
    
    input_data = np.array([[n, p, k, temp, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    
    return prediction[0]