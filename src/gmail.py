from __future__ import print_function

import os.path
import base64
from tracemalloc import start

from pkg_resources import get_provider

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# The scope being requested is the Gmail readonly capability so that messages can be read
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Capture contents from a string between two substrings within that string
def capture_between(str, part1, part2, beg_inclusive=False):
    # Stores index to begin substring capture
    start_idx = str.find(part1)

    # Beginning component is not being included
    if not beg_inclusive:
        start_idx += len(part1) # Calculation for end of part1 substring

    # Stores index to end substring capture
    end_idx = str.find(part2)

    return str[start_idx:end_idx]

# Extract the problem number from the title of the email
def extract_problem_number(title):
    captured = capture_between(title, '#', '[')
    return captured.strip()

# Extract the difficulty of the problem from the title of the email
def extract_problem_difficulty(title):
    captured = capture_between(title, '[', ']')
    return captured

# Extract the problem statement from the message body of the email
def extract_problem_statement(message):
    captured = capture_between(message, message[0], '----', beg_inclusive=True)
    return captured.strip()

def print_problem(problem):
    problem_txt = ('Problem #' + problem['problem_number'] + ' [' 
        + problem['problem_difficulty'] + ']')

    print(problem_txt)

    for i in range(len(problem_txt)):
        print('-', end='')
    print()

    print(f'{problem["problem_statement"]}')

    if problem['problem_solved']:
        for implementation in problem['problem_implementations']:
            print(f"Previously solved in {implementation}".upper())
    else:
        print("--------------------")
        print("new: not yet solved!".upper())

# Process email raw body string
# and get problem number and problem description
def get_problem_info(body):
    obj = {}
    subject_heading = "Subject: "
    message_id_heading = "Message-ID: "
    before_message = "quoted-printable"
    after_message = "Upgrade to premium"

    # Capture email title and extract problem number
    email_title = capture_between(body, subject_heading, message_id_heading)
    obj['problem_number'] = extract_problem_number(email_title)
    obj['problem_difficulty'] = extract_problem_difficulty(email_title)
    
    # Capture problem statement
    email_message = capture_between(body, before_message, after_message)
    obj['problem_statement'] = extract_problem_statement(email_message)

    obj['problem_solved'] = False
    obj['problem_implementations'] = []

    return obj

def main():
    creds = None

    # token.json is the file storing the user's access and refresh token
    # This file is generated the first time this program is run
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Allow the user to log in if the credentials are not available from token.json
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_clients_secret_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials into token.json for next time
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Now that the credentials have been established, use the Gmail API below
        service = build('gmail', 'v1', credentials=creds)
        target_email = 'founders@dailycodingproblem.com'
        query = 'from:' + target_email

        # results stores the unique IDs of all emails under the above query
        results = service.users().messages().list(userId='me', labelIds=None, 
            q=query, includeSpamTrash=None).execute()

        email_struct = {}

        # Extract email payload from every listed result
        for email in results['messages']:
            # Full raw message is being accessed as a base64 string from Google
            message_obj = service.users().messages().get(userId='me', id=email['id'], format="raw").execute()
            message_raw = message_obj['raw'] # Raw message bits

            # Using ASCII table, convert the data to a binary string format
            message_raw_bytes = message_obj['raw'].encode("ascii")

            # Convert chunks of 6 bit segments into 1-byte segments
            # print(len(message_raw_bytes))
            message_string_bytes = base64.urlsafe_b64decode(message_raw_bytes)

            # Convert 1-byte segments into a full ASCII string
            message_string = message_string_bytes.decode("ascii")

            # Extract key problem information from email body string
            problem = get_problem_info(message_string)

            print_problem(problem)

            # Add the information object to the email list under problem number
            email_struct[problem['problem_number']] = problem

            break
            


    except HttpError as error:
        # TODO: Handle errors appropriately as per gmail API specs
        print(f'An error occurred: {error}')

if __name__ == "__main__":
    main()