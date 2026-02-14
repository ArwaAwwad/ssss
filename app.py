import streamlit as st
import pickle
import numpy as np

# تحديد مسار الملف الحالي
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# تحميل النموذج من نفس مجلد app.py
model_path = os.path.join(BASE_DIR, "diabetes_model.pkl")
model = pickle.load(open(model_path, "rb"))

st.title("Diabetes Prediction App")

st.write("Enter patient data to predict diabetes")

# إدخال البيانات
pregnancies = st.number_input("Pregnancies")
glucose = st.number_input("Glucose Level")
blood_pressure = st.number_input("Blood Pressure")
skin_thickness = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("The patient is likely diabetic")
    else:
        st.success("The patient is not diabetic")
