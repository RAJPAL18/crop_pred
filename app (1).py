import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('random_forest_crop_recommendation_model.joblib')

st.title('Crop Recommendation App')

# Create input fields for the features
st.header('Enter the environmental conditions:')

N = st.number_input('Nitrogen (N) content in soil', min_value=0.0, max_value=200.0, value=90.0)
P = st.number_input('Phosphorus (P) content in soil', min_value=0.0, max_value=200.0, value=42.0)
K = st.number_input('Potassium (K) content in soil', min_value=0.0, max_value=200.0, value=43.0)
temperature = st.number_input('Temperature (°C)', min_value=0.0, max_value=50.0, value=25.0)
humidity = st.number_input('Humidity (%)', min_value=0.0, max_value=100.0, value=50.0)
ph = st.number_input('pH value of the soil', min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input('Rainfall (mm)', min_value=0.0, max_value=500.0, value=100.0)
season = st.selectbox('Season', ['Kharif', 'Rabi', 'Perennial'])

# Create a DataFrame from user inputs
user_input = pd.DataFrame({
    'N': [N],
    'P': [P],
    'K': [K],
    'temperature': [temperature],
    'humidity': [humidity],
    'ph': [ph],
    'rainfall': [rainfall],
    'Season': [season]
})

# Make a prediction using the loaded model
predicted_crop = model.predict(user_input)

# Display the prediction
st.header('Recommended Crop:')
st.write(predicted_crop[0])
