import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

# Load trained model and label encoders
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        year = int(data["year"])
        round_no = int(data["round_no"])
        region = data["region"]
        category = data["category"]
        course = data["course"]
        reservation = int(data["reservation"])

        # Encode categorical values
        region_enc = label_encoders["region"].transform([region])[0]
        category_enc = label_encoders["category"].transform([category])[0]
        course_enc = label_encoders["course"].transform([course])[0]

        # Prepare input for model
        features = np.array([[year, round_no, region_enc, category_enc, course_enc, reservation]])

        # Predict cutoff rank
        predicted_rank = model.predict(features)[0]

        return jsonify({"predicted_rank": int(predicted_rank)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
