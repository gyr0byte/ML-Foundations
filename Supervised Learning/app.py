import streamlit as st
import pandas as pd 
import joblib

model = joblib.load("SVM_heart_model.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

