import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
df = pd.read_csv('credit_risk_dataset.csv')

# Encoding maps
encoded = {
    "person_home_ownership": {"RENT": 0, "MORTGAGE": 1, "OWN": 2, "OTHER": 3, "NONE": 4, "ANY": 5},
    "loan_intent": {"PERSONAL": 0, "EDUCATION": 1, "MEDICAL": 2, "VENTURE": 3, "HOMEIMPROVEMENT": 4, "DEBTCONSOLIDATION": 5},
    "loan_grade": {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6},
    "cb_person_default_on_file": {"N": 0, "Y": 1}
}

# Apply encodings
for col, mapping in encoded.items():
    df[col] = df[col].map(mapping)

# Features and target
X = df[[
    "person_age", "person_income", "person_home_ownership", "person_emp_length",
    "loan_intent", "loan_grade", "loan_amnt", "loan_int_rate",
    "loan_percent_income", "cb_person_default_on_file", "cb_person_cred_hist_length"
]]
y = df["loan_status"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "backend/model.pkl")

print("✅ Model trained and saved to backend/model.pkl")
