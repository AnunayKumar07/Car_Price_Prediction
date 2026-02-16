
import streamlit as st
import joblib
import pandas as pd

model = joblib.load("car_price_pipeline.pkl")

st.title("🚗 Car Price Prediction App")

brand = st.selectbox("Brand", ["Toyota","BMW","Audi","Honda"])
body = st.selectbox("Body Type", ["SUV","Sedan","Hatchback"])
fuel = st.selectbox("Fuel Type", ["Petrol","Diesel","Electric"])
trans = st.selectbox("Transmission", ["Manual","Automatic"])
country = st.selectbox("Country", ["USA","Germany","Japan"])

year = st.number_input("Manufacture Year", 2000, 2025)
engine = st.number_input("Engine CC", 800, 5000)
hp = st.number_input("Horsepower", 50, 1000)
mileage = st.number_input("Mileage", 5.0, 40.0)

car_age = 2025 - year
hp_per_cc = hp / engine
eff = mileage * hp_per_cc

if st.button("Predict Price"):
    data = pd.DataFrame([{
        "Brand": brand,
        "Body_Type": body,
        "Fuel_Type": fuel,
        "Transmission": trans,
        "Manufacturing_Country": country,
        "Manufacture_Year": year,
        "Engine_CC": engine,
        "Horsepower": hp,
        "Mileage_km_per_l": mileage,
        "Car_Age": car_age,
        "HP_per_CC": hp_per_cc,
        "Efficiency_Score": eff
    }])

    pred = model.predict(data)[0]
    st.success(f"💰 Estimated Price: ${pred:,.2f}")
