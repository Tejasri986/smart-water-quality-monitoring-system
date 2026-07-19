import streamlit as st
import pandas as pd
import joblib
import random
import time

st.set_page_config(page_title="Smart Water Quality Monitor", layout="wide")
st.title("💧 Smart Water Quality Monitoring System")

@st.cache_resource
def load_model():
    return joblib.load('water_potability_model.pkl')

model = load_model()

def generate_reading():
    return {
        'ph': round(random.uniform(0, 14), 2),
        'Hardness': round(random.uniform(50, 300), 2),
        'Solids': round(random.uniform(300, 50000), 2),
        'Chloramines': round(random.uniform(0, 13), 2),
        'Sulfate': round(random.uniform(100, 500), 2),
        'Conductivity': round(random.uniform(180, 800), 2),
        'Organic_carbon': round(random.uniform(2, 30), 2),
        'Trihalomethanes': round(random.uniform(0, 130), 2),
        'Turbidity': round(random.uniform(1, 7), 2),
    }

if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame()

placeholder = st.empty()

for _ in range(1000):
    reading = generate_reading()
    df_reading = pd.DataFrame([reading])
    prediction = model.predict(df_reading)[0]
    label = "✅ Potable" if prediction == 1 else "❌ Not Potable"

    st.session_state.history = pd.concat([st.session_state.history, df_reading], ignore_index=True)

    with placeholder.container():
        if prediction == 1:
            st.success(f"✅ Latest Reading: {label}")
        else:
            st.error(f"❌ Latest Reading: {label}")
        st.write(reading)
        st.line_chart(st.session_state.history[['ph', 'Turbidity', 'Sulfate']])

    time.sleep(2)