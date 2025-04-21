import requests
import os
from dotenv import load_dotenv

load_dotenv()
APIkey = os.getenv("APIkey")


def get_data(place, forecast_days=None,):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data



