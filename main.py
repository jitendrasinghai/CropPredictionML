
from flask import Flask, request, render_template_string
from predict import predict_crop
from pathlib import Path
import math

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "model.pkl"

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crop Prediction Tool</title>

    <style>
        * { box-sizing: border-box; }

        body {
            margin: 0;
            padding: 30px 15px;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #e8f5e9, #f1f8e9);
            color: #263238;
        }

        .container {
            max-width: 480px;
            margin: auto;
            padding: 30px;
            background: white;
            border-radius: 18px;
            box-shadow: 0 10px 35px rgba(0,0,0,0.08);
        }

        h1 {
            text-align: center;
            color: #198754;
            margin-bottom: 8px;
        }

        .subtitle {
            text-align: center;
            color: #777;
            margin-bottom: 25px;
        }

        label {
            display: block;
            margin: 15px 0 7px;
            font-weight: bold;
        }

        input {
            width: 100%;
            padding: 13px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 15px;
        }

        input:focus {
            outline: 2px solid #198754;
            border-color: transparent;
        }

        button {
            width: 100%;
            padding: 15px;
            margin-top: 25px;
            border: none;
            border-radius: 8px;
            background: #198754;
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }

        button:hover { background: #146c43; }

        .result {
            margin-top: 25px;
            padding: 20px;
            text-align: center;
            background: #e8f5e9;
            border-radius: 10px;
            color: #146c43;
        }

        .error {
            margin-top: 20px;
            padding: 15px;
            background: #ffebee;
            color: #c62828;
            border-radius: 8px;
        }

        footer {
            text-align: center;
            margin-top: 25px;
            color: #888;
            font-size: 12px;
        }
    </style>
</head>

<body>
<div class="container">

    <h1>🌱 Crop Prediction</h1>
    <p class="subtitle">Smart Agriculture Recommendation System</p>

    <form method="POST">

        <label>Nitrogen (N)</label>
        <input type="number" step="any" name="n" required>

        <label>Phosphorus (P)</label>
        <input type="number" step="any" name="p" required>

        <label>Potassium (K)</label>
        <input type="number" step="any" name="k" required>

        <label>Temperature (°C)</label>
        <input type="number" step="any" name="temp" required>

        <label>Humidity (%)</label>
        <input type="number" step="any" name="humidity" required>

        <label>Soil pH (0-14)</label>
        <input type="number" step="any" name="ph" min="0" max="14" required>

        <label>Rainfall (mm)</label>
        <input type="number" step="any" name="rainfall" min="0" required>

        <button type="submit">Predict Best Crop</button>

    </form>

    {% if result %}
    <div class="result">
        <h2>🌾 Recommended Crop</h2>
        <h1>{{ result }}</h1>
    </div>
    {% endif %}

    {% if error %}
    <div class="error">{{ error }}</div>
    {% endif %}

    <footer>Crop Prediction ML System</footer>

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
            if not MODEL_PATH.is_file():
                raise FileNotFoundError("Model file model/model.pkl is missing.")

            values = [
                float(request.form["n"]),
                float(request.form["p"]),
                float(request.form["k"]),
                float(request.form["temp"]),
                float(request.form["humidity"]),
                float(request.form["ph"]),
                float(request.form["rainfall"])
            ]

            if not all(math.isfinite(v) for v in values):
                raise ValueError("Please enter valid finite numbers.")

            result = str(predict_crop(*values)).upper()

        except Exception:
            app.logger.exception("Crop prediction failed")
            error = "Prediction failed. Check model file, inputs and server logs."

    return render_template_string(
        HTML,
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
