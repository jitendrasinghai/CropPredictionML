import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from data_processing import load_and_preprocess_data

def train_and_save_model():
    print("Loading data and training model...")
    X, y = load_and_preprocess_data()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/model.pkl")
    
    accuracy = model.score(X_test, y_test)
    print(f"Model saved successfully! Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    train_and_save_model()