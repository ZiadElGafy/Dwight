import datetime
import os.path
import time
import tzlocal

from datetime import datetime
from datetime import timedelta
from dateutil import parser

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from tools.say import driver as say

TIMEZONE = tzlocal.get_localzone()
TIMEZONE_OFFSET = (-time.timezone) / (60 * 60)

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_credentials():
    creds = None
    
    if os.path.exists("googleCalendarToken.json"):
        creds = Credentials.from_authorized_user_file("googleCalendarToken.json", SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("googleCalendarToken.json", "w") as token:
            token.write(creds.to_json())
    
    return creds

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def get_year():
    try:
        year = int(input())

        if (abs(datetime.now().year - year) > 10):
            raise Exception()
        
        return year
    except:
        say("Please, only say a valid year number.")
        return get_year()

months = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}

def get_month():
    try:
        month_str = input()

        month = 0
        if month_str in months:
            month = months[month_str]
        else:
            month = int(month_str)
        
        if month < 1 or month > 12:
            raise Exception()
        
        month_str = str(month)
        if len(month_str) == 1:
            month_str = "0" + month_str

        return month_str
    except:
        say("Please, say a valid month")
        return get_month()

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_day(month, year):
    leap_year = is_leap_year(year)
    days = days_in_month[month - 1]
    if month == 2 and leap_year:
        days += 1
    
    try:
        day = int(input())

        if day <= 0 or day > days:
            raise Exception()
        
        day_str = str(day)
        if len(day_str) == 1:
            day_str = "0" + day_str

        return day_str
    except:
        say("Please, say a valid day number.")
        return get_day()

def get_hour():
    try:
        hour = int(input())

        if hour == 0 or (13 <= hour and hour <= 23):
            return hour
        
        if 1 <= hour and hour <= 12:
            say("is that AM or PM?")
            choice = input().lower()

            if (choice[0] != 'p' and choice[0] != 'a'):
                raise Exception()
            
            pm = choice[0] == 'p'

            if choice[0] == 'p': #PM
                if hour != 12:
                    hour += 12
            elif choice[0] == 'a': #AM
                if hour == 12:
                    hour -= 12
            else:
                raise Exception()
        
        hour_str = str(hour)
        if len(hour_str) == 1:
            hour_str = "0" + hour_str

        return hour_str
    except:
        say("Please say a valid hour number.")
        return get_hour()

def get_minute():
    try:
        minute = int(input())

        if minute < 0 or minute >= 60:
            raise Exception()
        
        minute_str = str(minute)
        if len(minute_str) == 1:
            minute_str = "0" + minute_str
        
        return minute
    except:
        say("Please say a valid minute between 0 and 59.")
        return get_minute()

def get_duration():
    try:
        duration = float(input())

        if duration <= 0 or duration > 144:
            raise Exception()
        
        return duration
    except:
        say("Please enter a valid duration in hours.")
        return get_duration()

def get_event_data(prompt):
    say("What would you like the title of the event to be?")
    title = input()
    
    say("And the description?")
    description = input()

    say("Alright, from this point on please only say numbers.")
    
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    if "today" in prompt or "tonight" in prompt:
        pass
    elif "tomorrow" in prompt:
        tomorrow = now + timedelta(days = 1)
        year = tomorrow.year
        month = tomorrow.month
        day = tomorrow.day
    else:
        say("What year is the event?")
        year = get_year()

        say("And month?")
        month = get_month()
        
        say("What about the day?")
        day = get_day(int(month), int(year))
    
    date_str = f"{year}-{month}-{day}"
    date = datetime.strptime(date_str, "%Y-%m-%d").date()

    say("What hour is it going to be at?")
    hour = get_hour()
    
    say("And what minute?")
    minute = get_minute()
    
    time_str = f"{hour}:{minute}:00"
    time = datetime.strptime(time_str, "%H:%M:%S").time()

    say("How long (in hours) is the event?")
    duration = get_duration()

    return title, description, date, time, duration

def create_event(prompt):
    title, description, date, time, duration = get_event_data(prompt)

    start = datetime.combine(date, time)
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
        return event
    except HttpError as error:
        print("Error:", error)
        return None