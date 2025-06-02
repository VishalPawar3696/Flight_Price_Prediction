import streamlit as st
import pandas as pd
import joblib
from preprocessing import preprocess_input

model = joblib.load("flight_price_model.pkl")

st.title("Flight Price Predictor")

# User Input
airline = st.selectbox("Airline", ["IndiGo", "Air India", "SpiceJet"])
source = st.selectbox("Source", ["Delhi", "Mumbai", "Bangalore"])
destination = st.selectbox("Destination", ["Delhi", "Cochin", "Kolkata"])
date = st.date_input("Flight Date")
duration = st.text_input("Duration (e.g., 2h 30m)")

if st.button("Predict Price"):
    input_data = pd.DataFrame([{
        "flight date": date,
        "Airline": airline,
        "Source": source,
        "Destination": destination,
        "duration": duration,
    }])

    processed = preprocess_input(input_data)

    # You might need to align columns to the model here
    prediction = model.predict(processed)
    st.success(f"Predicted Price: ₹{int(prediction[0])}")
