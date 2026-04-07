import streamlit as st
import pickle
import pandas as pd

# Page config
st.set_page_config(page_title="Energy Predictor", layout="centered")

# Load model
with open("energy_model.pkl", "rb") as f:
    model = pickle.load(f)

# Title
st.title("🏢 Smart Building Energy Predictor")
st.markdown("Predict energy consumption based on environmental and indoor conditions.")

st.divider()

# Section: Environment
st.subheader("🌤️ Environmental Conditions")
Press = st.number_input("Pressure (mm Hg)", value=755.0)
RH_out = st.slider("Outdoor Humidity (%)", 0, 100)
T_out = st.slider("Outdoor Temperature (°C)", -10, 50)
Windspeed = st.slider("Wind Speed", 0.0, 20.0)

st.divider()

# Section: Indoor Conditions
st.subheader("🏠 Indoor Conditions")
T2 = st.slider("Room Temperature T2", 0.0, 50.0)
T3 = st.slider("Room Temperature T3", 0.0, 50.0)
T6 = st.slider("Outdoor Temp T6", -10.0, 50.0)

RH_1 = st.slider("Room 1 Humidity", 0, 100)
RH_3 = st.slider("Room 3 Humidity", 0, 100)
RH_5 = st.slider("Room 5 Humidity", 0, 100)
RH_8 = st.slider("Room 8 Humidity", 0, 100)

lights = st.slider("Lights Usage", 0, 100)

st.divider()

# Time
st.subheader("⏰ Time")
hour = st.slider("Hour of Day", 0, 23)

# Prediction
if st.button("🔮 Predict Energy Consumption"):
    input_data = pd.DataFrame([{
    'T6': T6,
    'T3': T3,
    'lights': lights,
    'Press_mm_hg': Press,
    'T_out': T_out,
    'RH_1': RH_1,
    'RH_8': RH_8,
    'T2': T2,
    'hour': hour,
    'RH_out': RH_out,
    'Windspeed': Windspeed,
    'RH_3': RH_3,
    'RH_5': RH_5
}])

    prediction = model.predict(input_data)

    st.success(f"⚡ Predicted Energy Consumption: {prediction[0]:.2f} Wh")
st.divider()
st.markdown("### 📊 About this model")
st.write("""
This model uses a Random Forest Regressor trained on environmental and indoor sensor data 
to predict building energy consumption. It captures non-linear relationships between 
temperature, humidity, and energy usage.
""")
