import streamlit as st
import plotly_express as px
import pandas as pd

st.title("IN Search for Happiness")

horizontal_axis_option = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"))
vertical_axis_option = st.selectbox("Select the data for the Y-axis", ("GDP", "Happiness", "Generosity"))

df = pd.read_csv("happy.csv")

st.subheader(f"{horizontal_axis_option} and {vertical_axis_option}")


match horizontal_axis_option:
    case 'Happiness':
        x = df['happiness']
    case 'GDP':
        x = df['gdp']
    case 'Generosity':
        x = df['generosity']


match vertical_axis_option:
    case 'Happiness':
        y = df['happiness']
    case 'GDP':
        y = df['gdp']
    case 'Generosity':
        y = df['generosity']


figure = px.scatter(x=x, y=y, labels={"x": horizontal_axis_option, "y": vertical_axis_option})

st.plotly_chart(figure)

