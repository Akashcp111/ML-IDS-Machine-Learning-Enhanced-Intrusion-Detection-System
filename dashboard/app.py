# app.py
import streamlit as st
import pandas as pd
import joblib
import numpy as np

@st.cache_resource
def load_model():
    return joblib.load('../models/rf_model.joblib')

model = load_model()
st.title("🔐 ML-Based Intrusion Detection System")
st.subheader("Upload network traffic data (CSV) and detect attacks.")

uploaded_file = st.file_uploader("📁 Upload preprocessed CSV file", type=['csv'])

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.success(f"✅ Loaded {data.shape[0]} rows, {data.shape[1]} columns.")

        data.replace([np.inf, -np.inf], np.nan, inplace=True)
        data.dropna(inplace=True)

        predictions = model.predict(data)
        label_map = {0: 'BENIGN', 1: 'ATTACK'}
        readable_preds = [label_map.get(p, 'Unknown') for p in predictions]

        data['Prediction'] = readable_preds
        st.subheader("📊 Prediction Results:")
        st.write(data.head(10))

        summary = data['Prediction'].value_counts()
        st.subheader("📈 Summary:")
        st.bar_chart(summary)

    except Exception as e:
        st.error(f"❌ Failed to process file: {e}")
else:
    st.info("📌 Please upload a CSV file to get started.")
