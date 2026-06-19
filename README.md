# 🚗 Car Price Prediction using Machine Learning

## Overview

This project predicts the selling price of a car based on its specifications and technical attributes using Machine Learning. The application is deployed using Streamlit and provides real-time price predictions through an interactive web interface.

## Features

* Machine Learning based car price prediction
* Interactive Streamlit web application
* Data preprocessing and feature engineering
* Model comparison and evaluation
* End-to-end Scikit-Learn pipeline
* Real-time price estimation

## Dataset

The dataset contains information about vehicles including:

* Brand
* Manufacturing Year
* Body Type
* Fuel Type
* Transmission
* Engine Capacity (CC)
* Horsepower
* Mileage
* Manufacturing Country

Additional engineered features:

* Car Age
* HP-per-CC Ratio
* Efficiency Score

Dataset file:

```text
dataset/global_cars_enhanced.csv
```

## Machine Learning Workflow

1. Data Cleaning and Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Model Deployment

## Models Evaluated

* Linear Regression
* Random Forest Regressor
* Decision Tree Regressor

Random Forest Regressor was selected as the final model due to its superior predictive performance.

## Project Structure

```text
Car_Price_Prediction/
│
├── app.py
├── requirements.txt
├── car_price_pipeline.pkl
├── README.md
│
├── dataset/
│   └── global_cars_enhanced.csv
│
└── notebook/
    └── Project_AB+.ipynb
```

## Installation

```bash
pip install -r requirements.txt
```

## Run Locally

```bash
streamlit run app.py
```

## Live Demo

https://carpriceprediction-5gu5tyet7bhifkkbjyqscp.streamlit.app/

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib

## Author

Anunay Kumar
B.Tech Information Technology
Haldia Institute of Technology
