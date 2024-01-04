import datetime
import os
import pickle

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def get_credentials():
    creds = None
    token_file = 'googleMeetToken.pickle'

    try:
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
    except:
        return None

def create_meeting_link(creds):
    try:
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
            calendarId = 'primary',
            body = event,
            conferenceDataVersion = 1,
        ).execute()

        meeting_link = event['hangoutLink']

        return meeting_link
    except:
        return None