from chatbot.controllers.searchTheWebController import driver as search_the_web_controller

from modules.googleMeet import create_meeting_link
from modules.googleMeet import get_credentials

from tools.copyToClipboard import driver as copy_to_clipboard
from tools.say import driver as say

def driver():
    creds = get_credentials()
    
    if not creds:
        say("Couldn't get credentials.")
        return
    
    meeting_link = create_meeting_link(creds)

    if meeting_link:
        copy_to_clipboard(meeting_link)
        say("Meeting link copied to clipboard.")
        search_the_web_controller(meeting_link)
    else:
        say("Couldn't create Google Meet.")