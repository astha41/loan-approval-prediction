# Loan Approval Prediction Web Application

This project is a Loan Approval Prediction System built using Flask.
It predicts whether a loan will be Approved, Under Review, or Rejected
based on realistic applicant financial and personal details.

## Project Objective

- Predict loan approval status using applicant data
- Simulate real banking decision logic
- Build an end-to-end web application
- Understand ML-style deployment workflow

## Technologies Used

- Python
- Flask
- HTML & CSS
- Git & GitHub

## Project Structure

Loan_Approval_Prediction/
│
├── app.py
├── README.md
├── requirements.txt
├── templates/
│   └── index.html

## Input Details Required

- Gender
- Marital Status
- Dependents
- Education
- Employment Type
- Applicant Income
- Co-Applicant Income
- Loan Amount
- Loan Term (Days)
- Credit History
- Property Area

## Loan Decision Logic

- Loan term entered in days
- Converted internally to months
- EMI calculated
- EMI-to-Income ratio evaluated
- Credit history and employment considered

## Loan Status Rules

- Score ≥ 70 → Approved
- Score 45–69 → Under Review
- Score < 45 → Rejected

## How to Run the Project

1. Clone the repository
2. Create virtual environment
3. Install dependencies  
   pip install flask
4. Run application  
   python app.py
5. Open browser  
   http://127.0.0.1:5000

## Disclaimer

This project is created for learning and demonstration purposes only.
It should not be used for real financial decisions.

## Future Enhancements

- Integrate ML model
- Improve UI with Bootstrap
- Add database
- Deploy on cloud
