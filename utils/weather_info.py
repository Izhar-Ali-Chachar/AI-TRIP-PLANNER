import requests

class WeatherForecastTool:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url_current = "http://api.weatherapi.com/v1/current.json"
        self.base_url_forecast = "http://api.weatherapi.com/v1/forecast.json"

    def get_current_weather(self, city: str) -> dict:
        params = {
            "key": self.api_key,
            "q": city
        }
        response = requests.get(self.base_url_current, params=params)
        if response.status_code == 200:
            return response.json()
        return {}

    def get_forecast_weather(self, city: str, days: int = 3) -> dict:
        params = {
            "key": self.api_key,
            "q": city,
            "days": days
        }
        response = requests.get(self.base_url_forecast, params=params)
        if response.status_code == 200:
            return response.json()
        return {}
