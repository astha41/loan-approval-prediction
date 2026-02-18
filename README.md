##Loan Approval Prediction Web Application

This project is a Loan Approval Prediction System built using Machine Learning and Flask.
It predicts whether a loan will be Approved, Under Review, or Rejected based on user-provided details.

The main goal of this project is to demonstrate how a machine learning model can be integrated into a web application.



##Project Objective

To predict loan approval status using applicant data

To deploy a trained ML model using a Flask web app

To provide a simple and user-friendly web interface

To understand end-to-end ML deployment workflow



##Technologies Used

Python
Flask
Scikit-learn
HTML & CSS
Pickle
Git & GitHub



##Project Structure

Loan_Approval_Prediction/
│
├── app.py                  # Flask application file
├── README.md               # Project documentation
├── requirements.txt        # Required libraries
│
├── model/
│   └── loan_model.pkl      # Trained ML model
│
├── templates/
│   └── index.html          # Web form UI
│
├── notebook/               # Model training notebook
├── data/                   # Dataset
├── venv/                   # Virtual environment



##How the Application Works

User enters loan-related details in the web form
Input data is sent to the Flask backend
The trained ML model predicts approval probability
Based on probability:
    Approved
    Under Review
    Rejected
Result is displayed on the web page




##Loan Decision Logic

Probability	Result
≥ 65%	Loan Approved
50% – 64%	Under Review
< 50%	Loan Rejected

This approach avoids relying only on credit history and gives better decision balance.

##How to Run the Project

Clone the repository
Create and activate virtual environment
Install dependencies
Run Flask app
    python app.py
Open browser and go to:
    http://127.0.0.1:5000



##Input Details Required

Gender
Marital Status
Dependents
Education
Employment Type
Applicant Income
Co-applicant Income
Loan Amount
Loan Term
Credit History
Property Area



##Output

The application displays:
    Loan Status (Approved / Rejected / Under Review)
Approval Probability
Short explanation



##Disclaimer

This project is created for learning and demonstration purposes only.
It should not be used for real financial or banking decisions.



##Future Enhancements

Improve UI with Bootstrap
Add database support
Deploy on cloud platform
Improve model accuracy