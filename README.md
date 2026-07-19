# 💧 Smart Water Quality Monitoring System

A machine learning-based system that predicts water potability in real-time using simulated IoT sensor data, displayed on a live dashboard.

## 🎯 Problem Statement
Access to safe drinking water is a critical global concern. Traditional water testing methods are slow and resource-intensive. This project uses machine learning to instantly classify water samples as potable or not, based on key physicochemical parameters.

## 🛠️ Tech Stack
- **Python** – core language
- **Pandas, NumPy** – data processing
- **Scikit-learn** – ML model (Random Forest Classifier)
- **Streamlit** – live dashboard
- **Matplotlib, Seaborn** – data visualization

## 📊 Dataset
[Water Potability Dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability) from Kaggle — 3276 samples with 9 water quality parameters (pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, Turbidity) and a Potability label.

## 🔧 How It Works
1. **Data Preprocessing** – handled missing values using mean imputation
2. **Model Training** – Random Forest Classifier, tuned via GridSearchCV
3. **Sensor Simulation** – Python script generates realistic sensor readings every 2 seconds
4. **Live Dashboard** – Streamlit app displays real-time predictions with color-coded alerts (green = potable, red = not potable) and historical trend graphs
![Dashboard Screenshot](<img width="1920" height="1080" alt="Screenshot 2026-07-19 161624" src="https://github.com/user-attachments/assets/e791204c-42cd-4260-bd07-7172dd66db66" />
)(<img width="1920" height="1080" alt="Screenshot 2026-07-19 161644" src="https://github.com/user-attachments/assets/0f21d553-d059-496e-bbeb-501c0dd5e118" />
)
## 📈 Model Performance
- Accuracy: 67%
- Tuned hyperparameters: `max_depth=20, min_samples_split=5, n_estimators=100`

## 🚀 How to Run
pip install -r requirements.txt
streamlit run dashboard.py
## 🔮 Future Scope
- Integrate real IoT hardware (ESP32 + physical sensors)
- Deploy dashboard to cloud (Streamlit Community Cloud)
- Add SMS/email alerts for unsafe water detection

## 👩‍💻 Author
Tejasri – B.Tech CSE (IoT), Raghu Engineering College
