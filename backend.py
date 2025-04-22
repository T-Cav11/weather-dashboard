import requests
import os
from dotenv import load_dotenv
import pytz
from datetime import datetime

load_dotenv()
APIkey = os.getenv("APIkey")


def get_data(place, forecast_days=None,):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]

    # How many forecast entries to keep (each is 3-hourly)
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    # Timezone for Ireland
    ireland_tz = pytz.timezone("Europe/Dublin")

    # Convert and add local time to each forecast entry
    for forecast in filtered_data:
        utc_time = datetime.utcfromtimestamp(forecast['dt']).replace(tzinfo=pytz.utc)
        local_time = utc_time.astimezone(ireland_tz)
        forecast['local_time'] = local_time.strftime('%Y-%m-%d %H:%M:%S')  # Format as string

    return filtered_data



