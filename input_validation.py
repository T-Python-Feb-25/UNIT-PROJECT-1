
from email_validator import validate_email, EmailNotValidError
import maskpass
import base64
import re

pass_requirments='''Please create a strong password that meets the following requirements:
        1. At least 8 characters long.
        2. Contains at least one uppercase letter
        3. Contains at least one lowercase letter
        4. Contains at least one digit (0-9)
        5. Contains at least one special character (e.g., !@#$%^&*).
        6. Cannot contain spaces or tabs.'''

def number_input_validation(prompt:str, limit):
    while True:
        try:
            user_input=input(prompt)
            if not (user_input.isnumeric()):
                raise Exception("Invalid input , please enter numbers only")
            elif int(user_input)>int(limit) or int(user_input)<=0:
                raise Exception("Invalid Choice.")

        except Exception as error:
            print(error)
        else:
            return int(user_input)
        
def text_input_validation(prompt:str):
    while True:
        try:
            user_input=input(prompt)
            if not (user_input.isalpha()):
                raise Exception("Invalid input , please enter charechters only")
        except Exception as error:
            print(error)
        else:
            return user_input
        
def email_input_validation(prompt:str):
    while True:
        try:
            user_input=input(prompt)
            emailinfo = validate_email(user_input, check_deliverability=True)           
        except EmailNotValidError as error:
            print(str(error))
        else:
            return emailinfo.normalized

def phone_input_validation(prompt:str):
    while True:
        try:
            user_input=input(prompt)
            if not(len(user_input)==10 and user_input.isdigit() and user_input.startswith("05")):    
                raise Exception("This is invalid number.. try again")
        except Exception as error:
            print(error)
        else:
            return user_input
        
def password_input_Validation(prompt:str):
    while True:
        try:
            # Password masking
            pwd = maskpass.advpass(prompt)  
            if (len(pwd) < 8 or 
                re.search(r'\s', pwd) or 
                not re.search(r'[A-Z]', pwd) or 
                not re.search(r'[a-z]', pwd) or 
                not re.search(r'[0-9]', pwd) or 
                not re.search(r'[\W_]', pwd)):
                raise Exception("Invalid password. Please adhere to the requirements and try again.")

            # encoding the entered password
            encpwd = base64.b64encode(pwd.encode("utf-8"))
        except Exception as error:
            print(error)
        else:
            return encpwd
        

def password_input_masking(prompt:str):
    try:
        # Password masking
        #TODO Uncomment this and return the variable
        #pwd = maskpass.advpass(prompt)  
        # encoding the entered password
        encpwd = base64.b64encode("Aa142536*".encode("utf-8"))
    except Exception as error:
        print(error)
    else:
        return encpwd
        



            
            
