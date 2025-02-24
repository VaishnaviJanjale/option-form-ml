from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model & encoders
model = pickle.load(open("model.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_df = pd.DataFrame([data])

    # Encode categorical data
    for col in ["region", "category", "course"]:
        input_df[col] = label_encoders[col].transform([data[col]])

    # Predict cutoff rank
    predicted_rank = model.predict(input_df)[0]
    
    return jsonify({"predicted_rank": int(predicted_rank)})

if __name__ == '__main__':
    app.run(debug=True)
