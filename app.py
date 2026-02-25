from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probability = None
    explanation = None

    if request.method == "POST":
        try:
            gender = request.form["gender"]
            married = request.form["married"]
            dependents = int(request.form["dependents"])
            education = request.form["education"]
            employment = request.form["employment"]

            applicant_income = float(request.form["applicant_income"])
            coapplicant_income = float(request.form["coapplicant_income"])
            loan_amount = float(request.form["loan_amount"]) * 1000
            loan_term_days = int(request.form["loan_term_days"])
            credit_history = int(request.form["credit_history"])
            property_area = request.form["property_area"]

            if applicant_income <= 0 or loan_amount <= 0 or loan_term_days <= 0:
                raise ValueError("Invalid numeric values")

            # Convert days to months
            loan_term_months = loan_term_days / 30

            total_income = applicant_income + coapplicant_income
            emi = loan_amount / loan_term_months
            emi_ratio = emi / total_income

            score = 0

            # Credit History
            if credit_history == 1:
                score += 30
            else:
                score -= 40

            # Income strength
            if total_income >= 40000:
                score += 25
            elif total_income >= 20000:
                score += 15
            else:
                score -= 10

            # Employment
            if employment == "Salaried":
                score += 15
            else:
                score += 5

            # Education
            if education == "Graduate":
                score += 10

            # Dependents
            if dependents > 3:
                score -= 10

            # EMI affordability
            if emi_ratio <= 0.35:
                score += 25
            elif emi_ratio <= 0.50:
                score += 10
            else:
                score -= 30

            # Final Decision
            if score >= 70:
                prediction = "Approved"
                probability = 85
                explanation = "Strong financial profile with affordable EMI."
            elif score >= 45:
                prediction = "Under Review"
                probability = 60
                explanation = "Moderate risk. Requires additional verification."
            else:
                prediction = "Rejected"
                probability = 25
                explanation = "High risk due to income, EMI, or credit history."

        except Exception as e:
            prediction = "Error"
            probability = 0
            explanation = "Invalid input. Please check all fields."

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability,
        explanation=explanation
    )

if __name__ == "__main__":
    app.run(debug=True)
