# 🏠 House Price Predictor

A machine learning web application built with **Streamlit** and **scikit-learn** that predicts house prices based on property features.

---

## 📋 Overview

This app uses a **Random Forest Regressor** trained on a housing dataset to predict property prices. Users can input house details through an interactive UI and get an instant price estimate.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed, then install the required libraries:

```bash
pip install streamlit scikit-learn pandas numpy
```

### Running the App

```bash
streamlit run Price_Predictor_app.py
```

---

## 📁 Project Structure

```
Housing Price Model/
│
├── Price_Predictor_app.py   # Main Streamlit application
├── housing.csv              # Dataset used for training
└── README.md                # Project documentation
```

---

## 🧠 Model Details

| Property        | Value                     |
|-----------------|---------------------------|
| Algorithm       | Random Forest Regressor   |
| Estimators      | 100 trees                 |
| Random State    | 42                        |
| R² Score        | ~0.70 (Linear Regression baseline) |

The model is trained at app startup on the full dataset each time the app launches.

---

## 🏡 Input Features

| Feature            | Type        | Description                              |
|--------------------|-------------|------------------------------------------|
| Area               | Number      | Size of the house in square feet         |
| Bedrooms           | Number      | Number of bedrooms                       |
| Bathrooms          | Number      | Number of bathrooms                      |
| Parking Spaces     | Number      | Number of parking spots                  |
| Stories            | Number      | Number of floors                         |
| Air Conditioning   | Yes / No    | Whether AC is available                  |
| Basement           | Yes / No    | Whether a basement is present            |
| Hot Water Heating  | Yes / No    | Whether hot water heating is available   |
| Guest Room         | Yes / No    | Whether a guest room is present          |
| Main Road Access   | Yes / No    | Whether the house is on a main road      |
| Preferred Area     | Yes / No    | Whether the house is in a preferred area |
| Furnishing Status  | 3 options   | Unfurnished / Semi-Furnished / Furnished |

---

## 📊 Dataset

The model is trained on `housing.csv`, which contains real estate data with the features listed above and a `price` column as the target variable.

Binary columns (`yes`/`no`) are encoded to `1`/`0` during preprocessing. `furnishingstatus` is ordinally encoded as `0`, `1`, `2`.

---

## ⚠️ Disclaimer

This application is intended for **educational purposes only**. Predictions are estimates and may not reflect actual market prices. Do not use this tool for real estate financial decisions.

---

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
