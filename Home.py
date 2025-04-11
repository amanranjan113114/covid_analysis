import streamlit as st
import pandas as pd

def load_data():
    return pd.read_csv("store.csv", sep="|")

st.set_page_config(page_title="COVID Patient Record System", page_icon="🦠", layout="wide")
st.title("🦠 COVID Patient Record System")

st.write("Welcome! Navigate using the sidebar to manage patients and view data.")

# Overview
try:
    df = load_data()
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Patients", len(df))
    col2.metric("Recovered", (df['Recovered'] == 'Y').sum())
    col3.metric("Not Recovered", (df['Recovered'] == 'N').sum())
except:
    st.warning("No patient data available yet!")