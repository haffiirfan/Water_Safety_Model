import pickle
import streamlit as st
import numpy as np
import sklearn
# 1. Page Setup
st.set_page_config(page_title="Full Water Potability Predictor", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.google.com/search?sca_esv=1dda3acef72a6239&sxsrf=AHTn8zpXCq54YNVbbvG_EX_JENPD4f0ugw:1746366865630&q=image&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWpA-dk4wpBWOGsoR7DG5zJBkzPWUS0OtApxR2914vrjk7XZXfnfKsaRZouQANLhmphEhFjnPez7qSPLLQhF9yWQ3ZrzUbmSVDckVjh88BuJ7CIyev2Ea8wZTZF9TaA47VJJOXvxTfqIxJCL23m8h319mHmljuYmW9D9h5-BUk_b-GXXLj4&sa=X&ved=2ahUKEwivqrHF-4mNAxUhfKQEHYTGAn8QtKgLegQIEhAB#vhid=6NokVoxCuyL67M&vssid=mosaic");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    /* black box for the form inputs */
    div[data-testid="stForm"] {
        background-color: rgba(255, 255, 255, 0.9);  /* black with slight transparency */
        color: black;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    /* Optional: Style number inputs and button */
    input[type="number"] {
        background-color: lightblue;
        color: black;
        border-radius: 8px;
        padding: 6px;
    }

    button[kind="primary"] {
        background-color: #0077b6;
        color: brown;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#2 loading training model
try:
    with open("model.pkl", "rb") as file:
        loaded_model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e.__class__.__name__} - {str(e)}")


print(loaded_model)

#3 UI
st.title('Water Potability Predictor')
st.write('Enter Values to check')

# input form
with st.form('input form'):
    col1,col2,col3 = st.columns(3)
    with col1:
        ph = st.number_input('PH Values(0-14)')
        hardness = st.number_input('hardness(mg/l)')
        solids = st.number_input("Solids (ppm)", 0.0)
    with col2:
        chloramines = st.number_input("Chloramines (ppm)", 0.0)
        sulfate = st.number_input("Sulfate (mg/L)", 0.0)
        conductivity = st.number_input("Conductivity (μS/cm)", 0.0)
    with col3:
        organic_carbon = st.number_input("Organic Carbon (ppm)", 0.0)
        trihalomethanes = st.number_input("Trihalomethanes (μg/L)", 0.0)
        turbidity = st.number_input("Turbidity (NTU)", 0.0)

        submitted = st.form_submit_button(" Predict")

# prediction

if submitted:
    input_data = np.array([[ph,hardness,solids,chloramines,sulfate,conductivity,organic_carbon,trihalomethanes,turbidity]])

    prediction = loaded_model.predict(input_data)

    if (prediction[0] == 1):
        st.success('Safe')
    else:
        st.error('Not safe')
