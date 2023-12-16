import streamlit as st
import pickle
import pandas as pd


cars = pickle.load(open("Car_Price_Prediction_lr.pkl","rb"))
dataset = pd.read_csv('cleaned_car.csv')

st.title('Car Valuation System')

unique_companies = dataset['company'].unique()
unique_year = sorted(dataset['year'].unique(),reverse=True)
unique_fuel = dataset['fuel_type'].unique()


selected_company = st.selectbox('Select the Company:', unique_companies)

filtered_car_names = sorted(dataset[dataset['company'] == selected_company]['name'].unique())
selected_car_name = st.selectbox('Select Car Name', filtered_car_names)

year = st.selectbox('Select the year:', unique_year)
fuel_type = st.selectbox('Select the fuel type:', unique_fuel)
kms_driven = st.number_input('Enter KMs Driven:', min_value=0)

predict_button = st.button('Predict Car Price')

# Placeholder for displaying the prediction result
prediction_result = st.empty()

if predict_button and selected_car_name:
    # Prepare input data for prediction
    input_data = pd.DataFrame({
        'company': [selected_company],
        'name': [selected_car_name],
        'kms_driven': [kms_driven],
        'year': [year],  # Change to 'year'
        'fuel_type': [fuel_type]
    })

    # Make predictions
    prediction = cars.predict(input_data)

    # Display the prediction
    prediction_result.subheader('Predicted Car Price:')
    prediction_result.write(f'Rs {prediction[0]:,.2f}')
