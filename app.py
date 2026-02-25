from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

MODEL_PATH = "model/loan_model.pkl"
SCALER_PATH = "model/scaler.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("loan_model.pkl not found. Train model first.")

model = pickle.load(open(MODEL_PATH, "rb"))

scaler = None
if os.path.exists(SCALER_PATH):
    scaler = pickle.load(open(SCALER_PATH, "rb"))


@app.route("/")
def home():
    return render_template("index.html", form_data={})


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Store form data
        form_data = request.form.to_dict()

        input_data = np.array([[ 
            int(form_data["gender"]),
            int(form_data["married"]),
            int(form_data["dependents"]),
            int(form_data["education"]),
            int(form_data["self_employed"]),
            float(form_data["applicant_income"]),
            float(form_data["coapplicant_income"]),
            float(form_data["loan_amount"]),
            float(form_data["loan_amount_term"]),
            float(form_data["credit_history"]),
            int(form_data["property_area_urban"]),
            int(form_data["property_area_semiurban"])
        ]])

        if scaler:
            input_data = scaler.transform(input_data)

        probability = model.predict_proba(input_data)[0][1]
        confidence = round(probability * 100, 2)

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
            reason_text=reason,
            form_data=form_data
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {e}",
            form_data=request.form.to_dict()
        )


if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="127.0.0.1", port=5000, debug=True)
