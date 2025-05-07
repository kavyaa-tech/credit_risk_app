# 💳 Credit Risk Analysis App

A full-stack machine learning web application that predicts whether a loan applicant is **High Risk** or **Low Risk** based on credit data.

Built with:
- 🧠 FastAPI for the backend API
- 📊 Streamlit for the frontend interface
- 🗃️ SQLite + SQLAlchemy for saving predictions
- 🤖 Scikit-learn for training the model

---

## 📁 Project Structure

credit-risk-app/
├── backend/
│ ├── main.py # FastAPI backend
│ ├── db.py # Database logic
│ └── model.pkl # Trained machine learning model
├── frontend/
│ └── app.py # Streamlit UI
├── train_model.py # Script to train and save model
├── credit_risk_dataset.csv
├── requirements.txt
└── README.md


---

## ⚙️ Requirements

- Python 3.10 or higher recommended
- pip

Install all dependencies:

bash
pip install -r requirements.txt

🏋️‍♂️ Training the Model
Run the training script to generate model.pkl:

python train_model.py

This uses credit_risk_dataset.csv, applies preprocessing, trains a model, and saves it as model.pkl.

Running the App
1. Start Backend (FastAPI)
cd backend
uvicorn main:app --reload

2. Start Frontend (Streamlit)
In a new terminal:
cd frontend
streamlit run app.py

 API Endpoint
POST /predict
Request Body:

{
  "age": 30,
  "income": 60000,
  "home_ownership": "RENT",
  "emp_length": 4,
  "loan_intent": "PERSONAL",
  "loan_grade": "B",
  "loan_amount": 15000,
  "interest_rate": 13.5,
  "percent_income": 0.25,
  "default_on_file": "N",
  "credit_hist_length": 5
}

Response:
{
  "prediction": "Low Risk"
}

Database
Predictions are saved into a local SQLite database (credit_risk.db) with timestamp and input values.

You can find DB logic in backend/db.py.


Model Details
Trained with scikit-learn

Features encoded manually to match production input

Trained on structured credit data

License
MIT License © 2025

Author
Built by Kavya. Contributions welcome!
