from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load model
MODEL_PATH = "model/loan_model.pkl"
SCALER_PATH = "model/scaler.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("loan_model.pkl not found. Train model first.")

model = pickle.load(open(MODEL_PATH, "rb"))

# Load scaler if exists
scaler = None
if os.path.exists(SCALER_PATH):
    scaler = pickle.load(open(SCALER_PATH, "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect inputs
        input_data = np.array([[
            int(request.form["gender"]),
            int(request.form["married"]),
            int(request.form["dependents"]),
            int(request.form["education"]),
            int(request.form["self_employed"]),
            float(request.form["applicant_income"]),
            float(request.form["coapplicant_income"]),
            float(request.form["loan_amount"]),
            float(request.form["loan_amount_term"]),
            float(request.form["credit_history"]),
            int(request.form["property_area_urban"]),
            int(request.form["property_area_semiurban"])
        ]])

        # Scale data if scaler exists
        if scaler:
            input_data = scaler.transform(input_data)

        # Predict probability
        probability = model.predict_proba(input_data)[0][1]
        confidence = round(probability * 100, 2)

        # Decision logic
        if probability >= 0.65:
            result = "✅ Loan Approved"
            reason = "Strong applicant profile with good repayment capability."
        elif probability >= 0.50:
            result = "⚠️ Loan Under Review"
            reason = "Moderate risk. Further verification required."
        else:
            result = "❌ Loan Rejected"
            reason = "High risk based on income, loan amount, or credit history."

        return render_template(
            "index.html",
            prediction_text=result,
            confidence_text=f"Approval Probability: {confidence}%",
            reason_text=reason
        )

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="127.0.0.1", port=5000, debug=True)
''