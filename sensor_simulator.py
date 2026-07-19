import random
import time
import joblib
import pandas as pd

model = joblib.load('water_potability_model.pkl')

def generate_reading():
    reading = {
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
    return reading

def predict_quality(reading):
    df = pd.DataFrame([reading])
    prediction = model.predict(df)[0]
    return "Potable" if prediction == 1 else "Not Potable"

if __name__ == "__main__":
    while True:
        reading = generate_reading()
        result = predict_quality(reading)
        print(reading, "->", result)
        time.sleep(2)