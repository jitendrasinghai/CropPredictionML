
from flask import Flask, request, render_template_string
from predict import predict_crop
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "model.pkl"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Crop Prediction Tool</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial;
            background: #f0f7f0;
            padding: 30px;
            text-align: center;
        }
        .container {
            background: white;
            padding: 25px;
            max-width: 420px;
            margin: auto;
            border-radius: 12px;
        }
        input, button {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            box-sizing: border-box;
        }
        button {
            background: #198754;
            color: white;
            border: none;
            cursor: pointer;
        }
        h2 { color: #198754; }
    </style>
</head>
<body>
<div class="container">
    <h2>🌱 Crop Prediction Tool</h2>
    <form method="POST">
        <input type="number" step="any" name="n" placeholder="Nitrogen (N)" required>
        <input type="number" step="any" name="p" placeholder="Phosphorus (P)" required>
        <input type="number" step="any" name="k" placeholder="Potassium (K)" required>
        <input type="number" step="any" name="temp" placeholder="Temperature (°C)" required>
        <input type="number" step="any" name="humidity" placeholder="Humidity (%)" required>
        <input type="number" step="any" name="ph" placeholder="Soil pH" required>
        <input type="number" step="any" name="rainfall" placeholder="Rainfall (mm)" required>
        <button type="submit">Predict Crop</button>
    </form>
    {% if result %}
        <h2>Recommended Crop: {{ result }}</h2>
    {% endif %}
    {% if error %}
        <p style="color:red">{{ error }}</p>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            if not MODEL_PATH.exists():
                raise FileNotFoundError("Trained model not found!")

            n = float(request.form["n"])
            p = float(request.form["p"])
            k = float(request.form["k"])
            temp = float(request.form["temp"])
            humidity = float(request.form["humidity"])
            ph = float(request.form["ph"])
            rainfall = float(request.form["rainfall"])

            result = str(
                predict_crop(n, p, k, temp, humidity, ph, rainfall)
            ).upper()

        except Exception as e:
            error = str(e)

    return render_template_string(
        HTML, result=result, error=error
    )
