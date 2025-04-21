import streamlit as st
import plotly.express as px
from backend import get_data
import math

# add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the next few days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

try:
    if place:
        # get the temperature/sky data
        filtered_data = get_data(place,days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"]for dict in filtered_data]
            # create a temperature plot
            figure = px.line(x = dates, y=temperatures, labels=({"x":"Date", "y": "Temperature (C)"}))
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear":"images/clear.png", "Clouds": "images/cloud.png",
                          "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            dates = [dict["dt_txt"] for dict in filtered_data]

            # Chunk items into rows (e.g., 5 per row)
            items_per_row = 5
            num_rows = math.ceil(len(image_paths) / items_per_row)

            for row in range(num_rows):
                cols = st.columns(items_per_row)
                for i in range(items_per_row):
                    idx = row * items_per_row + i
                    if idx < len(image_paths):
                        with cols[i]:
                            st.image(image_paths[idx], width=115)
                            # Format datetime nicely
                            dt = dates[idx]
                            date_part, time_part = dt.split(" ")
                            st.markdown(f"<div style='text-align: center'>{date_part}<br>{time_part}</div>",
                                        unsafe_allow_html=True)
except KeyError:
    st.info("Please enter a valid city.")