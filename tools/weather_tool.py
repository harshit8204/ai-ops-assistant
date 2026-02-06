import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherTool:

    API_KEY = os.getenv("OPENWEATHER_API_KEY")

    @staticmethod
    def get_weather(city: str):
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": WeatherTool.API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
