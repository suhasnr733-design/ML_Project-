import numpy as np
import pandas as pd
import pickle
import time
import json
import streamlit as st

try:
    from streamlit_lottie import st_lottie
except Exception:  # pragma: no cover - graceful fallback for deployment environments
    st_lottie = None


st.set_page_config(page_title="Bengaluru House Price Predictor", page_icon="icons/house_logo.png", layout="wide")

@st.cache_data(show_spinner=False)
def load_data():
    paths = ["cleaned_df.csv", "Bengaluru_House_Data.csv"]
    for path in paths:
        try:
            df = pd.read_csv(path)
            if 'location' in df.columns:
                return df
        except Exception:
            continue
    return None

@st.cache_resource
def load_model():
    with open('RFmodel.pkl', 'rb') as file:
        return pickle.load(file)


df = load_data()
if df is None:
    st.error("No usable dataset with a 'location' column found. Place a valid `cleaned_df.csv` or `Bengaluru_House_Data.csv` in the workspace.")
    st.stop()

# Normalize location values and build the numeric encoding used by the trained model.
df['location'] = df['location'].astype(str).fillna('Unknown')
unique_locations = sorted(df['location'].dropna().unique().tolist())
location_map = {loc: code for code, loc in enumerate(unique_locations)}
model = load_model()

st.sidebar.image("icons/house_logo.png", width=150)
st.sidebar.header("House Price Predictor")
st.sidebar.write("Estimate Bangalore house prices using a trained machine learning model.")
st.sidebar.metric("Data rows", len(df))
st.sidebar.metric("Locations", len(unique_locations))
st.sidebar.caption("Prices are estimates for guidance only.")
selection = st.sidebar.radio("Navigate", ['Home', 'Predict Price'])

st.title("Bengaluru House Price Predictor")
st.markdown("Use the sidebar to switch between pages and estimate property price based on Bangalore market data.")

def load_house_anime():
    with open("home_anime.json", 'rb') as file:
        return json.load(file)

if selection == 'Home':
    left, right = st.columns([1, 1])
    with left:
        anime = load_house_anime()
        if st_lottie is not None:
            try:
                st_lottie(anime, width=340)
            except Exception:
                st.info("Animation preview is unavailable right now.")
        else:
            st.info("Animation preview is unavailable right now.")
    with right:
        st.markdown("""
        ##### 🏠 Welcome to the Bangalore House Price Predictor

        Use this app to estimate property prices with a trained machine learning model. Enter property details on the prediction page and receive a quick estimate.

        **What you can do:**
        - Get a fast property price estimate
        - Compare typical Bangalore locations
        - Explore dataset coverage and usage
        """)

    st.markdown("---")
    stat1, stat2, stat3 = st.columns(3)
    stat1.metric("Average price (lakh)", f"{df['price'].mean():.2f}")
    stat2.metric("Unique locations", len(unique_locations))
    stat3.metric("Total listings", len(df))

    top_locations = df['location'].value_counts().head(5).reset_index()
    top_locations.columns = ['Location', 'Records']
    st.markdown("### Top 5 locations in the dataset")
    st.dataframe(top_locations, use_container_width=True)

elif selection == "Predict Price":
    with st.form(key='predict_form'):
        st.subheader("Enter property details")
        col1, col2 = st.columns(2)
        with col1:
            loc = st.selectbox("📍 Location", options=unique_locations)
            sqft = st.number_input("📐 Total Sqft", min_value=300.0, max_value=35000.0, value=1200.0, step=50.0, format="%.1f")
        with col2:
            bhk = st.selectbox("🏠 BHK", options=[1, 2, 3, 4, 5, 6], index=1)
            bath = st.selectbox("🛁 Bathrooms", options=[1, 2, 3, 4, 5, 6], index=1)

        submit = st.form_submit_button('💰 Predict Price')

    if submit:
        encoded_location = location_map.get(loc)
        if encoded_location is None:
            st.error('Selected location is not available for prediction.')
        else:
            data = pd.DataFrame({
                'location': [encoded_location],
                'total_sqft': [sqft],
                'bath': [bath],
                'bhk': [bhk]
            })
            prediction = model.predict(data)[0] * 100000
            with st.spinner('Predicting...'):
                time.sleep(0.8)

            st.success(f"Estimated Price: ₹ {prediction:,.0f}")
            st.markdown("### Prediction summary")
            st.write(
                f"**Location:** {loc}  \
                **Total Sqft:** {sqft:,.0f}  \
                **BHK:** {bhk}  \
                **Bathrooms:** {bath}"
            )
            st.info("This estimate is based on a trained model and should be used for guidance only.")

            with st.expander('Show raw model input'):
                st.write(data)
