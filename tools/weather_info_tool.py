import os
from utils.weather_info import WeatherForecastTool
from langchain_community.tools import tool
from typing import List
from dotenv import load_dotenv

class WeatherInfoTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("WEATHERAPI_KEY")
        self.weather_service = WeatherForecastTool(self.api_key)
        self.weather_tool_list = self._setup_tools()
    
    def _setup_tools(self) -> List:
        """Setup all tools for the weather forecast tool"""

        @tool
        def get_current_weather(city: str) -> str:
            """Get current weather for a city using WeatherAPI"""
            weather_data = self.weather_service.get_current_weather(city)
            if weather_data:
                location = weather_data.get("location", {}).get("name", city)
                country = weather_data.get("location", {}).get("country", "N/A")
                temp = weather_data.get("current", {}).get("temp_c", "N/A")
                desc = weather_data.get("current", {}).get("condition", {}).get("text", "N/A")
                return f"Current weather in {location}, {country}: {temp}°C, {desc}"
            return f"Could not fetch weather for {city}"

        @tool
        def get_weather_forecast(city: str) -> str:
            """Get 3-day weather forecast for a city using WeatherAPI"""
            forecast_data = self.weather_service.get_forecast_weather(city)
            if forecast_data and "forecast" in forecast_data:
                forecast_summary = []
                for day in forecast_data["forecast"]["forecastday"]:
                    date = day["date"]
                    avg_temp = day["day"]["avgtemp_c"]
                    desc = day["day"]["condition"]["text"]
                    forecast_summary.append(f"{date}: {avg_temp}°C, {desc}")
                return f"Weather forecast for {city}:\n" + "\n".join(forecast_summary)
            return f"Could not fetch forecast for {city}"

        return [get_current_weather, get_weather_forecast]
