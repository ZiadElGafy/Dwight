import openmeteo_requests
import requests_cache
import tzlocal

from chatbot.controllers.searchTheWebController import driver as search_the_web_controller

from retry_requests import retry

from tools.getCoordinates import driver as get_coordinates
from tools.say import driver as say

TIMEZONE = tzlocal.get_localzone()

def get_weather_data():
    location = get_coordinates()

    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "timezone": TIMEZONE,
        "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "wind_speed_10m"]
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]

    return response

def get_forecast(response):
    forecast = {}
    current = response.Current()
    forecast["temperature"] = round(current.Variables(0).Value())
    forecast["apparent_temperature"] = round(current.Variables(2).Value())
    forecast["humidity"] = round(current.Variables(1).Value())
    forecast["wind_speed"] = round(current.Variables(3).Value())
    return forecast


def driver():
    response = get_weather_data()
    forecast = get_forecast(response)
    print(forecast)
    say(f"The temperature's {forecast['temperature']} degrees celsius and feels like {forecast['apparent_temperature']}")
    say(f"Humidity is at {forecast['humidity']}% and wind speed is {forecast['wind_speed']} kilometers per hour")
    choice = input("Would you like to know more weather data? [y/n] ")
    while choice != 'y' and choice != 'n':
        say("Would you like to know more weather data?")
        choice = input()
    
    yes = ["yes", "yeah", "yup", "positive", "affirmative"]
    if choice.to_lower() in yes:
        say("Getting more weather data")
        search_the_web_controller("Weather")
