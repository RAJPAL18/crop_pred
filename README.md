Crop Recommendation Project
This project provides a crop recommendation system based on environmental conditions.

Project Overview
The goal of this project is to build a machine learning model that can recommend the most suitable crop to plant based on various environmental factors such as Nitrogen (N), Phosphorus (P), and Potassium (K) content in the soil, temperature, humidity, pH, and rainfall, and Season.

Dataset
The dataset used in this project is Crop_recommendation_renamed.csv. It contains the following columns:

N: Nitrogen content in the soil
P: Phosphorus content in the soil
K: Potassium content in the soil
temperature: Temperature in Celsius
humidity: Humidity in percentage
ph: pH value of the soil
rainfall: Rainfall in mm
Season: Season (Kharif, Rabi, Perennial)
Crop: Recommended crop
Project Steps
Data Loading and Exploration: Load the dataset and perform initial data exploration to understand the data distribution and relationships between features.
Data Preprocessing: Prepare the data for model training, including handling categorical features (like 'Season') using techniques like one-hot encoding.
Model Training: Train a classification model (Random Forest Classifier in this case) to predict the recommended crop based on the input features.
Model Evaluation: Evaluate the performance of the trained model using appropriate metrics such as accuracy, precision, recall, and F1-score.
Model Saving: Save the trained model to a file for later use.
Deployment (Streamlit App): Create a simple web application using Streamlit to allow users to input environmental conditions and get a crop recommendation.
