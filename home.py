import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")

happy = pd.read_csv("happy.csv")

x_axis = st.selectbox("Select data for X axis", ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select data for Y axis", ("GDP", "Happiness", "Generosity"))

st.subheader(f"{x_axis} and {y_axis}")

# figure = px.scatter(data_frame=happy, x=x_axis.lower(), y=y_axis.lower())
if x_axis == "Happiness":
    x_array = happy['happiness']
elif x_axis == "GDP":
    x_array = happy['gdp']
else:
    x_array = happy['generosity']

if y_axis == "Happiness":
    y_array = happy['happiness']
elif y_axis == "GDP":
    y_array = happy['gdp']
else:
    y_array = happy['generosity']

figure = px.scatter(x=x_array, y=y_array, labels={"x": x_axis, "y": y_axis})

st.plotly_chart(figure)
