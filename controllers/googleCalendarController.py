from controllers.searchTheWebController import driver as search_the_web_controller

from modules.googleCalendar import add_event_to_calendar
from modules.googleCalendar import create_event
from modules.googleCalendar import get_credentials

from tools.say import driver as say

def driver(prompt):
    creds = get_credentials()

    if not creds:
        say("Couldn't get credentials.")
        return
    
    event_object = create_event(prompt)
    
    event = add_event_to_calendar(creds, event_object)

    if event:
        say(f"{event.get('summary')} event created successfully")

        link = event.get('htmlLink')
        print("Event link:", link)

        say("Would you like to view it?")
        choice = input()
        yes = ["yes", "yeah", "yup", "yep", "positive", "affirmative", "sure", "why not"]
        if choice.lower() in yes:
            search_the_web_controller(link)
    else:
        say("Couldn't create event.")