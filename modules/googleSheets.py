import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1w21g-mn-oYib-13eRGMAv5erRffaraRi4JNAtIRxw9E"
RANGE_NAME = "A:B"

def get_credentials():
    creds = None
    try:
        if os.path.exists("googleSheetsToken.json"):
            creds = Credentials.from_authorized_user_file("googleSheetsToken.json", SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port = 0)
            with open("googleSheetsToken.json", "w") as token:
                token.write(creds.to_json())
        return creds
    except:
        print("couldn't get credntials")
        return None

def append_row(prompt, response, creds):
    service = build("sheets", "v4", credentials=creds)
    body = {'values': [[prompt,response]]}
    result = service.spreadsheets().values().append(
    spreadsheetId = SPREADSHEET_ID, range = RANGE_NAME,
    valueInputOption="RAW", body=body).execute()

def driver(prompt,response):
    creds = get_credentials()
    append_row(prompt, response, creds)
