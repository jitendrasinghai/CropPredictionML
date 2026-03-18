# 🌱 Crop Recommendation System
Hi, I'm **Jitendra Singh**! 👋
I am a 2nd-year Artificial Intelligence & Machine Learning (AIML) student at DSEU. I am passionate about building data-driven solutions and exploring the practical applications of Machine Learning in real-world scenarios.
🔗 **Connect with me on LinkedIn:** [Jitendra Singh](https://www.linkedin.com/in/jitendrasinghai/)

## 🚀 Project Overview
The **Crop Recommendation System** is a Machine Learning project designed to help farmers and agriculture enthusiasts make informed decisions. By analyzing soil nutrients and weather conditions, this AI model predicts the most suitable crop to plant for maximum yield and profitability.
### ✨ Features
The model takes 7 key environmental and soil parameters as input:
1. **Nitrogen (N)** - Ratio of Nitrogen content in soil
2. **Phosphorus (P)** - Ratio of Phosphorus content in soil
3. **Potassium (K)** - Ratio of Potassium content in soil
4. **Temperature** - Temperature in degrees Celsius
5. **Humidity** - Relative humidity in percentage
6. **pH** - Soil pH value (0-14)
7. **Rainfall** - Rainfall in mm

Based on these inputs, the **Random Forest Classifier** predicts the best crop (e.g., Rice, Maize, Coffee, Apple, Mango, etc.) out of 22 different categories.

## 🛠️ Tech Stack Used
* **Programming Language:** Python 3.x
* **Data Manipulation & Analysis:** `pandas`, `numpy`
* **Machine Learning Algorithm:** `scikit-learn` (Random Forest Classifier)
* **Model Serialization:** `joblib`

-## 📂 Project Structure
```text
📦 Crop-Recommendation-System
 ┣ 📜 data_processing.py   # Cleans data and prepares Features (X) & Target (y)
 ┣ 📜 train_model.py       # Trains the ML model and saves it
 ┣ 📜 predict.py           # Loads the saved model and makes predictions
 ┣ 📜 main.py              # Main interactive script for user input
 ┣ 📜 CropData.csv         # The dataset used for training
 ┣ 📜 requirements.txt     # Python dependencies
 ┗ 📂 model
   ┗ 📜 model.pkl          # Saved Random Forest model (generated after training)
