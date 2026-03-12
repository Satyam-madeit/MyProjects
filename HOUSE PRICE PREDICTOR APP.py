import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("housing.csv")

# Encode binary columns
binary_cols = ['airconditioning', 'hotwaterheating', 'basement', 'guestroom', 'mainroad', 'prefarea']
for col in binary_cols:
    df[col] = df[col].map({'yes': 1, 'no': 0})

if 'furnishingstatus' in df.columns:
    df['furnishingstatus'] = df['furnishingstatus'].map({'unfurnished': 0, 'semi-furnished': 1, 'furnished': 2})

# Train model once at startup
FEATURES = ["area", "bedrooms", "bathrooms", "parking", "stories",
            "airconditioning", "basement", "hotwaterheating",
            "guestroom", "mainroad", "prefarea"]

if 'furnishingstatus' in df.columns:
    FEATURES.append("furnishingstatus")

X = df[FEATURES]
y = df["price"]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# ── UI ──────────────────────────────────────────────────────────────────────
st.title("🏠 House Price Predictor")

with st.expander("📊 Training Data Preview"):
    st.dataframe(df.head())

st.header("Enter House Details")

col1, col2 = st.columns(2)

with col1:
    area_input        = st.number_input("Area (sq ft)",   min_value=1000,  max_value=20000, value=5000)
    bedrooms_input    = st.number_input("Bedrooms",       min_value=1,     max_value=8,     value=3)
    bathrooms_input   = st.number_input("Bathrooms",      min_value=1,     max_value=10,    value=2)
    parking_input     = st.number_input("Parking Spaces", min_value=0,     max_value=5,     value=1)
    stories_input     = st.number_input("Stories",        min_value=1,     max_value=5,     value=2)
    if 'furnishingstatus' in df.columns:
        furnishing_input = st.selectbox("Furnishing Status", ["Unfurnished", "Semi-Furnished", "Furnished"])

with col2:
    aircon_input          = st.selectbox("Air Conditioning",  ["Yes", "No"])
    basement_input        = st.selectbox("Basement",          ["Yes", "No"])
    hotwaterheating_input = st.selectbox("Hot Water Heating", ["Yes", "No"])
    guestroom_input       = st.selectbox("Guest Room",        ["Yes", "No"])
    mainroad_input        = st.selectbox("Main Road Access",  ["Yes", "No"])
    prefarea_input        = st.selectbox("Preferred Area",    ["Yes", "No"])

def yn(val):
    return 1 if val == "Yes" else 0

if st.button("🔍 Predict Price", use_container_width=True):
    input_data = [[
        area_input, bedrooms_input, bathrooms_input, parking_input, stories_input,
        yn(aircon_input), yn(basement_input), yn(hotwaterheating_input),
        yn(guestroom_input), yn(mainroad_input), yn(prefarea_input)
    ]]

    if 'furnishingstatus' in df.columns:
        furnishing_map = {"Unfurnished": 0, "Semi-Furnished": 1, "Furnished": 2}
        input_data[0].append(furnishing_map[furnishing_input])

    predicted_price = model.predict(input_data)[0]
    st.success(f"### 💰 Predicted Price: ${predicted_price:,.0f}")
    st.caption("Note: Model is not completely accurate. Use as an estimate only.")
