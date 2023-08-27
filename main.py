from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        event = {
         
           "summary":"Study",
           "location": "Online",
           "descriptiom":"Lorem",
            "colorId":6,
            "start": {
                'dateTime': '2023-08-28T09:00:00.000',
                'timeZone': 'UTC+03:00'

            },
            "end": {
                'dateTime': '2023-08-28T12:00:00.000',
                'timeZone': 'UTC+03:00'

            },
            "recurrance":["RRULE:FREQ=DAILY;COUNT=3"],
            "atendees":[
                {"email":"sasho2004@gmail.com"}
            ]

           

       }
      
        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"{event.get('htmlLink')}")

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()