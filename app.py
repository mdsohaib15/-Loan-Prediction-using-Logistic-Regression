import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("loan_predict_model.pkl")

st.title("🏡 Housing Affordability Index Predictor")
st.markdown("Enter urban features to estimate housing affordability:")

# Input fields
income = st.number_input("Median Household Income", min_value=0)
rent = st.number_input("Median Rent", min_value=0)
unemployment = st.number_input("Unemployment Rate (%)", min_value=0.0, format="%.2f")
supply = st.number_input("Housing Supply Index", min_value=0.0, format="%.2f")

if st.button("Predict HAI"):
    input_data = np.array([[income, rent, unemployment, supply]])
    prediction = model.predict(input_data)
    st.success(f"Predicted HAI: {prediction[0]:.2f}")
