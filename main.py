from auth import login,sign_up
from input_validation import *
from user import Client,Admin,Employee

current_user=None
Provinces=["Mecca Province","Medina Province","Eastern Province","Riyadh Province"]
role = {
"Client": Client,
"Employee": Employee,
"Admin": Admin}
menu= '''
1- login
2- sign up

'''
def user_role_converter(current_user:dict):
    if current_user!=None:
        user_class = role.get(current_user['role'], "Client") 
        user_id = current_user['id']
        first_name = current_user['first_name']
        last_name = current_user['last_name']
        phone = current_user['phone']
        email = current_user['email']
        return user_class(user_id, first_name, last_name, phone, email)
    return None
is_valid=False
while not is_valid:
    try:
        user_input=input(menu+"Enter your choice: ")
        if user_input=='1':
            email=email_input_validation("Enter your email adress:")
            encoded_pass= password_input_masking("Enter your password: ")
            user_dict=login(email,encoded_pass)
            current_user=user_role_converter(user_dict)

            is_valid=False if current_user==None else True
        elif user_input=='2':
            first_name=text_input_validation("Enter your first name: ")
            last_name=text_input_validation("Enter your last name: ")
            email=email_input_validation("Enter your email adress:")
            print(pass_requirments)
            encoded_pass= password_input_Validation("Enter your password: ")
            phone=phone_input_validation("Enter your phone number (e.g. 05xxxxxxxx):")
            
            user_dict=sign_up(first_name,last_name,email,encoded_pass,phone)
            current_user=user_role_converter(user_dict)

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
if current_user.user_role()in["Admin","Employee", "Client"]:
    while True:
        try:
            user_selection=input(current_user.display_menu()+"\n Enter your choice: ")
            current_user.call_functionality(user_selection)
        except TypeError as error:
            print(error)
    
else:
    print("Thank for for visiting fazaa , hope to see you soon again ")


        

