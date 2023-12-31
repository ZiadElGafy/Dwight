from controllers.searchTheWebController import driver as search_the_web_controller

from modules.weatherForecast import get_forecast
from modules.weatherForecast import get_weather_data

from tools.say import driver as say

def driver():
    response = get_weather_data(1)

    if not response:
        say("Couldn't get weather forecast.")
        return
    
    forecast = get_forecast(response)
    print(forecast)
    say(f"The temperature's {forecast['temperature']} degrees celsius and feels like {forecast['apparent_temperature']}")
    say(f"Humidity is at {forecast['humidity']}% and wind speed is {forecast['wind_speed']} kilometers per hour")

    say("Would you like to know more weather data?")
    choice = input()

    yes = ["yes", "yeah", "yup", "yep", "positive", "affirmative", "sure", "why not"]
    if choice.lower() in yes:
        say("Getting more weather data")
        search_the_web_controller("Weather")