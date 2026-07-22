from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "SVM_heart_model.pkl")
scaler = joblib.load(BASE_DIR / "scaler.pkl")
expected_columns = joblib.load(BASE_DIR / "columns.pkl")

st.title("Heart Stroke Prediction by Gaurav")
st.markdown(
    "This app uses a trained model and scaler stored alongside the script.")
