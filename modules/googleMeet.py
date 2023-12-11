import os
import pickle
import datetime
import pyperclip
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from .searchTheWeb import driver as search_the_web_driver

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def get_credentials():
    creds = None
    token_file = 'token.pickle'

    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_meeting_link(creds):
    service = build('calendar', 'v3', credentials=creds)
    event = {
        'summary': 'Google Meet Event',
        'description': 'This is a Google Meet event.',
        'start': {
            'dateTime': '2023-01-01T10:00:00',
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': '2023-01-01T11:00:00',
            'timeZone': 'UTC',
        },
        'conferenceData': {
            'createRequest': {
                'requestId': 'abcd1234',
            },
        },
    }

    event = service.events().insert(
        calendarId='primary',
        body=event,
        conferenceDataVersion=1,
    ).execute()

    meeting_link = event['hangoutLink']
    return meeting_link

def copy_to_clipboard(text_to_copy):
    pyperclip.copy(text_to_copy)

def driver():
    creds = get_credentials()
    meeting_link = create_meeting_link(creds)
    copy_to_clipboard(meeting_link)
    print("Meeting link copied to clipboard.")
    search_the_web_driver(meeting_link)