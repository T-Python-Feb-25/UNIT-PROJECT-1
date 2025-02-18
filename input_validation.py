
from email_validator import validate_email, EmailNotValidError
import maskpass
import base64
import re

def text_validation(text:str):
    while True:
        try:
            user_input=input(text)
            if not (user_input.isalpha()):
                raise Exception("Invalid input , please enter charechters only")
        except Exception as message:
            print(message)
        else:
            return user_input
        
def email_validation(text:str):
    while True:
        try:
            user_input=input(text)
            emailinfo = validate_email(user_input, check_deliverability=True)           

        except EmailNotValidError as message:
            print(str(message))
        else:
            return emailinfo.normalized

def phone_validation(text:str):
    
    while True:
        try:
            user_input=input(text)
            if not(len(user_input)==10 and user_input.isdigit() and user_input.startswith("05")):    
                raise Exception("This is invalid number.. try again")
        except Exception as message:
            print(message)
        else:
            return user_input
        
def password_Validation(text:str):
    while True:
        try:
            
            # Password masking
            pwd = maskpass.advpass(text)  
            
            if (len(pwd) < 8 or 
                re.search(r'\s', pwd) or 
                not re.search(r'[A-Z]', pwd) or 
                not re.search(r'[a-z]', pwd) or 
                not re.search(r'[0-9]', pwd) or 
                not re.search(r'[\W_]', pwd)):
                raise Exception("Invalid password. Please adhere to the requirements and try again.")
            # pwd = maskpass.askpass("Password : ")

            # encoding the entered password
            encpwd = base64.b64encode(pwd.encode("utf-8"))
        except Exception as message:
            print(message)
        else:
            return encpwd
   


            
            
