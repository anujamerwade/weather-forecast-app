import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for the next few days")
place = st.text_input("Place: ")
days = st.slider("Forecast days:", min_value=1, max_value=5, help="Select the number of days to forecast for")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

data = get_data(place, days, option)
# add graph
dates = ["2022-07-05", "2022-07-06", "2022-07-07"]
temps = [10, 19, 20]

figure = px.line(x=dates, y=temps, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
