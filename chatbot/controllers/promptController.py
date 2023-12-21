from chatbot.respond import driver as get_response
from chatbot.controllers.searchTheWebController import driver as search_the_web_controller
from chatbot.controllers.prayerTimesController import driver as prayer_times_controller
from tools.say import driver as say

def driver(intents, tag, prompt):
    response = get_response(intents, tag)
    if response:
        say(response)

    if tag == "unknown":
        search_the_web_controller(prompt, False)
    elif tag == "search":
        search_the_web_controller(prompt, True)
    elif tag == "prayer times":
        prayer_times_controller()