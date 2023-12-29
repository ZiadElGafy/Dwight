from chatbot.controllers.googleMeetController import driver as google_meet_controller
from chatbot.controllers.googleCalendarController import driver as google_calendar_controller
from chatbot.controllers.prayerTimesController import driver as prayer_times_controller
from chatbot.controllers.searchTheWebController import driver as search_the_web_controller
from chatbot.controllers.weatherForecastController import driver as weather_forecast_controller
from chatbot.identifyTag import driver as get_tag
from chatbot.respond import driver as get_response

from tools.say import driver as say

def execute_prompt(intents, tag, prompt):
    response = get_response(intents, tag)
    if response:
        say(response)

    if tag == "unknown":
        search_the_web_controller(prompt)
    elif tag == "search":
        search_the_web_controller(prompt)
    elif tag == "prayer times":
        prayer_times_controller()
    elif tag == "google meet":
        google_meet_controller()
    elif tag == "weather":
        weather_forecast_controller()
    elif tag == "google calendar":
        google_calendar_controller(prompt)

def driver(intents, all_words, device, model, tags):
    sentence = input("You: ")
    tag = get_tag(intents, all_words, device, model, tags, sentence)
    execute_prompt(intents, tag, sentence)