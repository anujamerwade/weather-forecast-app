import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for the next few days")
place = st.text_input("Place: ", "Mumbai")
days = st.slider("Forecast days:", min_value=1, max_value=5, help="Select the number of days to forecast for")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

try:
    filtered_data = get_data(place, days)

# check if name of city is correct
# if place
# add temp graph

    if option == "Temperature":
        temps = [dict["main"]["temp"]/10 for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temps, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
              "Rain": "images/rain.png", "Snow": "images/snow.png"}
    if option == "Sky":

        skies = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in skies]
        st.image(image_paths, width=115,)
except KeyError:
    st.info("City not found.")
