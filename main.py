import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select the number of forecasted days")
view = st.selectbox("Select data to view",
                    ("Temperature", "Sky"))

st.subheader(f"{view} for the next {days} days in {place}")


data = get_data(place, days, view)


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C°)"})
st.plotly_chart(figure)