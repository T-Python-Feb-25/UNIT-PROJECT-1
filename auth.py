# Standard library imports
import os.path
import base64
import random
from email.mime.text import MIMEText

# Third-party imports
from colorama import Fore
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError

# Local application imports
from config import  user_db, GOOGLE_CREDENTIALS, TOKEN

def code_validation(generated_code):
    """Validate the user input code against a generated code.

    This function prompts the user to enter a verification code was sent to the email to validate his email.
    The user has three attempts to input the correct code. If the user fails to enter the correct code after three attempts, 
    an error message is displayed, and the function returns False. If the correct code is entered, 
    the function returns True.

    Args:
        generated_code (str): The correct verification code that the user needs to enter.

    Returns:
        bool: True if the user successfully enters the correct code, 
              False if the user fails after three attempts.

    """
    attempt = 3
    while attempt > 0:
        user_input = input("Enter the Code (XXXX): ")[:4] 
        if not (len(user_input) == 4 and str(generated_code) == user_input):    
            print(Fore.RED+"Invalid Code.. try again")
            attempt -= 1
        else:
            return True
    print(Fore.RED+'''You have entered the verification code incorrectly three times.
For security reasons, your attempt to verify your account has been locked. Please try registering again later.''')
    return False

import random

def email_verification(email: str) -> bool:
    """Send a verification email with a code and validate the code.

    This function generates a random verification code and sends an email 
    to the provided address. The user must enter the received code to verify 
    their account. If the email is sent successfully, the function prompts 
    the user to enter the code. If the code is verified correctly, the 
    function returns True; otherwise, it returns False.

    Args:
        email (str): The email address to which the verification code will be sent.

    Returns:
        bool: True if the code is verified correctly, 
              False if the email could not be sent or the code is incorrect.
    """
    verification_code = random.randrange(1000, 9999)
    subject = "Verify Your Account"
    body = f"Please use this code to verify your account: {verification_code}"
    is_verified = False
    email_sent_successfully = send_email_notification(subject, body, email)
    
    if email_sent_successfully:
        is_verified = code_validation(verification_code)           
    else:
        print(Fore.YELLOW+"Unfortunately, we were unable to send a verification email to your address. Please try registering again.")        
    
    return is_verified

def sign_up(first_name, last_name, email,encoded_pass,phone ,role="Client"):
    current_user=None

    if user_db.is_user_registered(email):
        print("This email already have an account, Try to login")
    elif role =="Client":
        is_verified=email_verification(email)
        if is_verified:
            current_user=user_db.insert_user((first_name, last_name, email.lower(),encoded_pass,phone ,role,))
    else:
        current_user=user_db.insert_user((first_name, last_name, email.lower(),encoded_pass,phone ,role,))
    return current_user

def login(email,encoded_pass):   
    current_user=user_db.retrive_user(email.lower(),encoded_pass)
    return current_user

def send_email_notification(subject, body, to):
    
    """Send an email using the Gmail API."""
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

    creds = None
    if os.path.exists(TOKEN):
        creds = Credentials.from_authorized_user_file(TOKEN, SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
            GOOGLE_CREDENTIALS, SCOPES
        )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN, "w") as token:
            token.write(creds.to_json())
    try:
        service = build('gmail', 'v1', credentials=creds)

        # Create the email content
        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}
        # pylint: disable=E1101
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        if subject=='Verify Your Account':
            send_message= "Please enter the code sent to your email to verify your account."
        else:
            send_message= "the order update has been send to the user email"
        print(send_message)
        return True

    except HttpError as error:
        print(Fore.YELLOW+"An error occurred while trying to send the email")
    return False




