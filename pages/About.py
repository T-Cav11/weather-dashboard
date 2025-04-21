import streamlit as st

about ="""
This weather forecasting web app is designed to provide users with accurate short-term weather 
predictions using the OpenWeather API. Built with Streamlit, a Python-based web framework, 
the app offers an intuitive interface where users can enter a location, 
choose the number of forecast days (up to five), and select whether they want to view temperature 
trends or sky conditions. Temperature data is visualized using interactive Plotly charts, 
while sky conditions are displayed using descriptive weather icons. The app fetches real-time data from 
the OpenWeather 5-day forecast API, ensuring the information is up-to-date and location-specific. 
It features a clean, user-friendly design and is structured to support multiple pages for easy navigation 
and future expansion. The modular codebase separates the data-fetching logic from the user interface, 
making it scalable and easy to maintain.
"""
st.title("About this Web page")
st.write(about)