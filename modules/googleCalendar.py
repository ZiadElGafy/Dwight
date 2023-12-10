import datetime
import os.path
import time
import tzlocal

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from datetime import datetime
from datetime import timedelta
from dateutil import parser

TIMEZONE = tzlocal.get_localzone()
TIMEZONE_OFFSET = (-time.timezone) / (60 * 60)

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_credentials():
    creds = None
    
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    
    return creds

def create_event():
    # title, description, date, start, duration
    title = input("Enter event title: ")
    description = input("Enter event description: ")
    date = input("Enter event date (YYYY-MM-DD): ")
    time = input("Enter event start time (HH:MM:SS in 24 hour format): ")
    duration = float(input("Enter event duration in hours: "))

    date_formatted = datetime.strptime(date, "%Y-%m-%d").date()
    time_formatted = datetime.strptime(time, "%H:%M:%S").time()
    seconds_to_remove = timedelta(seconds = time_formatted.second)
    # time_formatted -= seconds_to_remove

    start = datetime.combine(date_formatted, time_formatted)
    start -= seconds_to_remove
    start -= timedelta(hours = TIMEZONE_OFFSET) # Apply timezone changes
    end = start + timedelta(hours = duration)

    start = start.isoformat() + 'Z'
    end = end.isoformat() + 'Z'
    
    event = {
        'summary': title,
        'description': description,
        'start': {
            'dateTime': start,
        },
        'end': {
            'dateTime': end,
        },
    }

    return event

def add_event_to_calendar(creds, event_object):
    try:
        service = build('calendar', 'v3', credentials = creds)
        event = service.events().insert(calendarId = "primary", body = event_object).execute()
        print('Event created successfully')
        print('%s' % (event.get('htmlLink')))
        return
    except HttpError as error:
        print('An error occurred: %s' % error)

def driver():
    creds = get_credentials()
    event_object = create_event()
    add_event_to_calendar(creds, event_object)
