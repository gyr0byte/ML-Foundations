import joblib
import pandas as pd
import streamlit as st


model = joblib.load("SVM_heart_model.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

st.title("Heart Stroke Prediction by Gaurav")
st.markdown()