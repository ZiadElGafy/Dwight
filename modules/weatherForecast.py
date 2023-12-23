import openmeteo_requests
import requests_cache
import tzlocal

from chatbot.controllers.searchTheWebController import driver as search_the_web_controller

from retry_requests import retry

from tools.getCoordinates import driver as get_coordinates

API_CALL_LIMIT = 100

def get_weather_data(trial_number):
    try:
        TIMEZONE = tzlocal.get_localzone()
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
    except:
        if trial_number < API_CALL_LIMIT:
            get_weather_data(trial_number + 1)
        else:
            return None

def get_forecast(response):
    forecast = {}
    current = response.Current()
    forecast["temperature"] = round(current.Variables(0).Value())
    forecast["apparent_temperature"] = round(current.Variables(2).Value())
    forecast["humidity"] = round(current.Variables(1).Value())
    forecast["wind_speed"] = round(current.Variables(3).Value())
    return forecast