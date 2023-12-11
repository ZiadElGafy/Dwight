from modules.googleMeet import driver as google_meet_driver
from modules.searchTheWeb import driver as search_the_web_driver
from modules.googleCalendar import driver as google_calendar_driver
from modules.prayerTimes import driver as prayer_times_driver
from modules.weatherForecast import driver as weather_forecast_driver

from tools.say import driver as say

def get_input_option(number_of_options):
    try:
        option = int(input())
        if option < 0 or option > number_of_options:
            raise Exception()
        
        return option - 1
    
    except:
        print("Invalid Input")
        return get_input_option(number_of_options)

def main():
    options = ["Search the web", "Prayer times", "Weather forecast", "Schedule a google calendar event", "Schedule a google meet"]
    say("Welcome, I'm Dwight! Please select one of the following options")
    for i in range(len(options)):
        print(f"{i + 1}: {options[i]}")

    op = get_input_option((len(options)))

    if options[op] == "Search the web":
        search_the_web_driver("", True)
    elif options[op] == "Schedule a google meet":
        google_meet_driver()
    elif options[op] == "Schedule a google calendar event":
        google_calendar_driver()
    elif options[op] == "Prayer times":
        prayer_times_driver()
    elif options[op] == "Weather forecast":
        weather_forecast_driver()

if __name__ == "__main__":
    main()