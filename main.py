import streamlit as st

st.title("Weather forecast for the next few days")
place = st.text_input("Place: ")
days = st.slider("Forecast days:", min_value=1, max_value=10, help="Select the number of days to forecast for")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
