import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("loan_predict_model.pkl")

st.set_page_config(page_title="Loan Eligibility Predictor", layout="centered")
st.title("🏠 Dream Housing Loan Eligibility Predictor")

st.markdown("""
This app predicts whether a customer is **eligible for a home loan** based on the application details.
""")

# Input form
with st.form("loan_form"):
    col1, col2 = st.columns(2)

    # Optional Loan ID input (not used in prediction)
    Loan_ID = st.text_input("Loan ID (Optional)", placeholder="E.g., LP001015")

    Gender = col1.selectbox("Gender", ["Male", "Female"])
    Married = col2.selectbox("Married", ["No", "Yes"])
    Dependents = col1.selectbox("Dependents", ["0", "1", "2", "3+"])
    Education = col2.selectbox("Education", ["Graduate", "Not Graduate"])
    Self_Employed = col1.selectbox("Self Employed", ["No", "Yes"])
    ApplicantIncome = col2.number_input("Applicant Income", min_value=0)
    CoapplicantIncome = col1.number_input("Coapplicant Income", min_value=0)
    LoanAmount = col2.number_input("Loan Amount (in thousands)", min_value=0.0)
    Loan_Amount_Term = col1.number_input("Loan Term (months)", min_value=0.0)
    Credit_History = col2.selectbox("Credit History", ["Good (1)", "Bad (0)"])
    Property_Area = col1.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    submitted = st.form_submit_button("Check Eligibility")

# Prediction logic
if submitted:
    gender = 1 if Gender == "Male" else 0
    married = 1 if Married == "Yes" else 0
    dependents = 3 if Dependents == "3+" else int(Dependents)
    education = 0 if Education == "Graduate" else 1
    self_employed = 1 if Self_Employed == "Yes" else 0
    credit_history = 1.0 if Credit_History == "Good (1)" else 0.0
    area = {"Urban": 2, "Semiurban": 1, "Rural": 0}[Property_Area]

    input_data = np.array([[gender, married, dependents, education, self_employed,
                            ApplicantIncome, CoapplicantIncome, LoanAmount,
                            Loan_Amount_Term, credit_history, area]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success(f"✅ Loan ID `{Loan_ID or 'N/A'}` is eligible for the loan.")
    else:
        st.error(f"❌ Loan ID `{Loan_ID or 'N/A'}` is not eligible for the loan.")
