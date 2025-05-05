import streamlit as st
import requests

st.set_page_config("Credit Risk Predictor", layout="centered")
st.title("📊 Credit Risk Prediction")

with st.form("form"):
    age = st.number_input("Age", 18, 100)
    income = st.number_input("Income")
    home_ownership = st.selectbox("Home Ownership", ["RENT", "MORTGAGE", "OWN", "OTHER", "NONE", "ANY"])
    emp_length = st.number_input("Employment Length (years)", 0.0, 50.0)
    loan_intent = st.selectbox("Loan Intent", ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"])
    loan_grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])
    loan_amount = st.number_input("Loan Amount")
    interest_rate = st.number_input("Interest Rate (%)")
    percent_income = st.number_input("Percent of Income to Loan (%)")
    default_on_file = st.selectbox("Default on File", ["N", "Y"])
    credit_hist_length = st.number_input("Credit History Length (years)")

    submitted = st.form_submit_button("Predict")

if submitted:
    payload = {
        "age": age,
        "income": income,
        "home_ownership": home_ownership,
        "emp_length": emp_length,
        "loan_intent": loan_intent,
        "loan_grade": loan_grade,
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "percent_income": percent_income,
        "default_on_file": default_on_file,
        "credit_hist_length": credit_hist_length
    }

    try:
        response = requests.post("http://localhost:8000/predict", json=payload)
        if response.status_code == 200:
            st.success(f"Prediction: {response.json()['prediction']}")
        else:
            st.error("Prediction failed.")
    except Exception as e:
        st.error(f"Could not reach backend: {e}")
