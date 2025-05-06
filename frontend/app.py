import streamlit as st
import requests

st.set_page_config("Credit Risk Predictor", layout="centered")
st.title("📊 Credit Risk Prediction")

# Use two columns for layout
col1, col2 = st.columns(2)

with st.form("form"):
    with col1:
        age = st.number_input("Age", 18, 100)
        income = st.number_input("Income")
        emp_length = st.number_input("Employment Length (years)", 0.0, 50.0)
        loan_amount = st.number_input("Loan Amount")
        percent_income = st.number_input("Percent of Income to Loan (%)")
    with col2:
        home_ownership = st.selectbox("Home Ownership", ["RENT", "MORTGAGE", "OWN", "OTHER", "NONE", "ANY"])
        loan_intent = st.selectbox("Loan Intent", ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"])
        loan_grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])
        interest_rate = st.number_input("Interest Rate (%)")
        default_on_file = st.selectbox("Default on File", ["N", "Y"])
        credit_hist_length = st.number_input("Credit History Length (years)")

    # Layout for predict button and result
    btn_col, result_col = st.columns([1, 3])
    submitted = btn_col.form_submit_button("Predict")

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
                prediction = response.json()["prediction"]
                if prediction.lower() == "high risk":
                    result_col.markdown(f"<span style='color:red; font-weight:bold;'>🔴 Prediction: {prediction}</span>", unsafe_allow_html=True)
                elif prediction.lower() == "low risk":
                    result_col.markdown(f"<span style='color:green; font-weight:bold;'>🟢 Prediction: {prediction}</span>", unsafe_allow_html=True)
                else:
                    result_col.markdown(f"<span style='color:orange; font-weight:bold;'>🟠 Prediction: {prediction}</span>", unsafe_allow_html=True)
            else:
                result_col.error("Prediction failed.")
        except Exception as e:
            result_col.error(f"Could not reach backend: {e}")
