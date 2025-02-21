
from dotenv import load_dotenv
from db_connector import DatabaseConnector as database
import os.path
import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
import random
from user import User
import os

# Load environment variables from .env file
load_dotenv()

# Use the environment variables
__db = database(os.getenv("DATABASE")) 
CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS")
TOKEN_PATH = os.getenv("TOKEN")

def code_validation(generated_code):
    attempt=3
    while attempt>0:
        user_input = input("Enter the Code (XXXX): ")[:4] 
        if not(len(user_input)==4 and str(generated_code)==user_input):    
            print("Invalid Code.. try again")
            attempt-=1
        else:
            return True
    print('''You have entered the verification code incorrectly three times.
For security reasons, your attempt to verify your account has been locked. Please try registering again later.''')
    return False

def email_verification(email:str)->bool:
    verification_code= random.randrange(1000, 9999)
    subject = "Verify Your Account"
    body = f"Please use this code to verify your account : {verification_code}"
    is_verified=False
    email_sent_successfully=send_email_notification(subject,body, email)
    if email_sent_successfully:
        is_verified=code_validation(verification_code)           
    else:
        print("Unfortunately, we were unable to send a verification email to your address. Please try registering again")        
    return is_verified

def sign_up(first_name, last_name, email,encoded_pass,phone ,role="Client"):
    current_user=None
    if __db.is_user_registered(email):
        print("This email already have an account, Try to login")
    else:
        is_verified=email_verification(email)
        if is_verified:
            __db.insert_user((first_name, last_name, email,encoded_pass,phone ,role,))
            current_user=__db.retrive_user(email,encoded_pass)
    return current_user

def login(email,encoded_pass):   
    current_user=__db.retrive_user(email,encoded_pass)
    return current_user

def send_email_notification(subject, body, to):
    
    """Send an email using the Gmail API."""
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIALS_PATH, SCOPES
        )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_PATH, "w") as token:
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
            send_message= "updates"
        print(send_message)
        return True

    except HttpError as error:
        print(f"An error occurred: {error}")
        send_message = None
    return False

