import joblib
import pandas as pd
import streamlit as st


model = joblib.load("SVM_heart_model.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

st.title("Heart Stroke Prediction by Gaurav")
st.markdown("Prove the following details")

age = st.slider("Age",18,100,40)
sex = st.selectbox("SEX"['M','F'])
chest_pain = st.selectbox("Chest Pain Type", ['ATA', 'NAP', 'TA', 'ASY'])
resting_bp = st.number_input('Resting Blood Pressure (mm hg)', 80, 200, 120) 
cholestrol = st.number_input("Cholestrol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0,1])
resting_ecg = st.selectbox("Resting ECG",['Normal', 'ST', 'LVH'])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise-Induced Angina", ['Y','N'])


