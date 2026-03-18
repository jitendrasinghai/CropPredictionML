import os
from predict import predict_crop

def get_farmer_input():
    print("--- Enter Soil and Weather Data ---")
    n = float(input("Nitrogen (N): "))
    p = float(input("Phosphorus (P): "))
    k = float(input("Potassium (K): "))
    temp = float(input("Temperature (°C): "))
    humidity = float(input("Humidity (%): "))
    ph = float(input("Soil pH (0-14): "))
    rainfall = float(input("Rainfall (mm): "))
    
    return n, p, k, temp, humidity, ph, rainfall

def main():
   
    if not os.path.exists("model/model.pkl"):
        print("Error: Model not found!")
        print("Please run 'train_model.py' first to generate the model.")
        return
        
    n, p, k, temp, humidity, ph, rainfall = get_farmer_input()
    
    
    result = predict_crop(n, p, k, temp, humidity, ph, rainfall)
    
    print(f"\n🌱 Recommended Crop: {result.upper()} 🌱")

if __name__ == "__main__":
    main()