from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from datetime import datetime
from .db import insert_prediction

app = FastAPI()
model = joblib.load("backend/model.pkl")

class InputData(BaseModel):
    age: int
    income: float
    home_ownership: str
    emp_length: float
    loan_intent: str
    loan_grade: str
    loan_amount: float
    interest_rate: float
    percent_income: float
    default_on_file: str
    credit_hist_length: float

@app.post("/predict")
def predict(data: InputData):
    encoded = {
        "home_ownership": {"RENT": 0, "MORTGAGE": 1, "OWN": 2, "OTHER": 3, "NONE": 4, "ANY": 5},
        "loan_intent": {"PERSONAL": 0, "EDUCATION": 1, "MEDICAL": 2, "VENTURE": 3, "HOMEIMPROVEMENT": 4, "DEBTCONSOLIDATION": 5},
        "loan_grade": {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6},
        "default_on_file": {"N": 0, "Y": 1}
    }

    row = [
        data.age,
        data.income,
        encoded["home_ownership"].get(data.home_ownership, 0),
        data.emp_length,
        encoded["loan_intent"].get(data.loan_intent, 0),
        encoded["loan_grade"].get(data.loan_grade, 0),
        data.loan_amount,
        data.interest_rate,
        data.percent_income,
        encoded["default_on_file"].get(data.default_on_file, 0),
        data.credit_hist_length
    ]

    prediction = model.predict([row])[0]
    label = "High Risk" if prediction == 1 else "Low Risk"

    insert_prediction({
        "age": data.age,
        "income": data.income,
        "home_ownership": data.home_ownership,
        "emp_length": data.emp_length,
        "loan_intent": data.loan_intent,
        "loan_grade": data.loan_grade,
        "loan_amount": data.loan_amount,
        "interest_rate": data.interest_rate,
        "percent_income": data.percent_income,
        "default_on_file": data.default_on_file,
        "credit_hist_length": data.credit_hist_length,
        "prediction": label,
        "timestamp": datetime.now()
    })

    return {"prediction": label}
