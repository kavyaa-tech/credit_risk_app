from sqlalchemy import create_engine, Table, Column, Integer, Float, String, DateTime, MetaData
from datetime import datetime

# Setup database engine
engine = create_engine("sqlite:///../credit_risk.db", connect_args={"check_same_thread": False})
metadata = MetaData()

# Define the table for saving predictions
risk_predictions = Table("risk_predictions", metadata,
    Column("id", Integer, primary_key=True),
    Column("age", Integer),
    Column("income", Float),
    Column("home_ownership", String),
    Column("emp_length", Float),
    Column("loan_intent", String),
    Column("loan_grade", String),
    Column("loan_amount", Float),
    Column("interest_rate", Float),
    Column("percent_income", Float),
    Column("default_on_file", String),
    Column("credit_hist_length", Float),
    Column("prediction", String),
    Column("timestamp", DateTime)
)

metadata.create_all(engine)

def insert_prediction(data):
    with engine.connect() as conn:
        conn.execute(risk_predictions.insert().values(**data))
