import  smtplib
from auth import login,sign_up
from input_validation import *

current_user=None

menu= '''
1- login
2- sign up

'''
is_valid=False
while not is_valid:
    try:
        user_input=input(menu+"Enter your choice: ")
        if user_input=='1':
            email=email_input_validation("Enter your email adress:")
            encoded_pass= password_input_masking("Enter your password: ")
            current_user=login(email,encoded_pass)
            is_valid=False if current_user==None else True
        elif user_input=='2':
            first_name=text_input_validation("Enter your first name: ")
            last_name=text_input_validation("Enter your last name: ")
            email=email_input_validation("Enter your email adress:")
            print(pass_requirments)
            encoded_pass= password_input_Validation("Enter your password: ")
            phone=phone_input_validation("Enter your phone number (e.g. 05xxxxxxxx):")
            
            current_user=sign_up(first_name,last_name,email,encoded_pass,phone)
            is_valid=False if current_user==None else True
        
        else:
            raise TypeError("invalid input , please enter a valid number from the menu")
    except TypeError as error:
        print(error)
    except Exception as error :
        # print("somthing went wrong main ")
        print(error)

print("-----welcome to Fazaa------")

print(current_user.user_role())
if current_user.user_role()=="Admin":
    print('''1- Add Truck
2-Remove Truck
3-Update Price
4-Update order status
5-Add Employee
6-remove Employeee
7-update locations
''')
elif current_user.user_role()=="Employee":
    print('''1- Add Truck
2-Remove Truck
3-Update Price
4-Update order status
''')
elif current_user.user_role()=="Client":
    print('''1- Profile
          2-Make an order
          3-Track an order
          4-view history
''')
else:
    print("Thank for for visiting fazaa , hope to see you soon again ")


        

