
from db_connector import DatabaseConnector as database
from input_validation import *
def sign_up(fisrt_name, last_name, email,encoded_pass,phone ):
    db =database("SMB.db") 
    db.connect()
    db.create_table()
    db.insert_user((fisrt_name, last_name, email ,encoded_pass,phone, "Admin"))
 #  db.insert_user(("sabreen", "binsalman", "sabreenbinsalman@hotmail.com" ,encoded_pass,"0595543693", "Admin"))




print("welcome")

menu= '''
1- login
2- sign up
'''

while True:
    user_input=input(menu)
    if user_input=='1':
        pass
    elif user_input=='2':

        fisrt_name=text_validation("Enter your first name: ")
        last_name=text_validation("Enter your last name: ")
        email=email_validation("Enter your email adress:")
        print('''Please create a strong password that meets the following requirements:
        1. At least 8 characters long.
        2. Contains at least one uppercase letter
        3. Contains at least one lowercase letter
        4. Contains at least one digit (0-9)
        5. Contains at least one special character (e.g., !@#$%^&*).
        6. Cannot contain spaces or tabs.''')
        encoded_pass= password_Validation("Enter your password: ")
        phone=phone_validation("Enter your phone number (e.g. 05xxxxxxxx):")
     
        sign_up(fisrt_name,last_name,email,encoded_pass,phone)
    else:
        break

