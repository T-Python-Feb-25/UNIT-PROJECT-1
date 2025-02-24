import sys
from auth import login,sign_up
from input_validation import *
from user import Client,Admin,Employee
from colorama import Fore, init
from art import text2art

current_user=None

def user_role_converter(current_user: dict):
    """Convert a user dictionary to a user role object.

    This function takes a dictionary representing the current user, retrieves the user's 
    role, and creates an instance of the corresponding user class. If the user is not 
    found it returns None.

    Args:
        current_user (dict): A dictionary containing user information. The expected keys are:
            - 'role': The role of the user (admin, client or employee).
            - 'id': The unique identifier of the user.
            - 'first_name': The user's first name.
            - 'last_name': The user's last name.
            - 'phone': The user's phone number.
            - 'email': The user's email address.

    Returns:
        object: An instance of the user class corresponding to the user's role, or None if 
        the current_user is None.

    """
    role = {
    "Client": Client,
    "Employee": Employee,
    "Admin": Admin}
    if current_user is not None:
        user_class = role.get(current_user['role'], "Client")
        user_id = current_user['id']
        first_name = current_user['first_name']
        last_name = current_user['last_name']
        phone = current_user['phone']
        email = current_user['email']
        return user_class(user_id, first_name, last_name, phone, email)
    return None

def main():
    init(autoreset=True)
    print(Fore.CYAN +text2art("Nafzaealuk"))
    menu = f"""
=========================== Menu ===========================
        1. Login
        2. Sign Up
        3. Exit
============================================================
"""

    is_valid=False
    while not is_valid:
        try:
            user_input=input(menu+"Please choose an option: ")
            if user_input=='1':
                email=get_email_input("Enter your email adress:")
                encoded_pass= password_input_masking("Enter your password: ")
                user_dict=login(email,encoded_pass)
                current_user=user_role_converter(user_dict)
                is_valid=False if current_user==None else True
            elif user_input=='2':
                first_name=get_alphabetic_input("Enter your first name: ")
                last_name=get_alphabetic_input("Enter your last name: ")
                email=get_email_input("Enter your email adress:")
                print(pass_requirments)
                encoded_pass= get_password_input("Enter your password: ")
                phone=get_phone_input("Enter your phone number (e.g. 05xxxxxxxx):")
                user_dict=sign_up(first_name,last_name,email,encoded_pass,phone)
                current_user=user_role_converter(user_dict)

                is_valid=False if current_user==None else True
            elif user_input=='3':
                print("Thank for for using Nafzaealuk , hope to see you soon again ")
                sys.exit(0)

            else:
                raise ValueError(Fore.RED+"Invalid input , please enter an option number from the menu")
        except ValueError as error:
            print(error)
        except Exception as error :
            print(Fore.RED+"Something went wrong try again later")


    if current_user.user_role() in["Admin","Employee", "Client"]:
        while True:
            try:
                user_selection=input(current_user.display_menu()+"\nPlease choose an option: ")
                current_user.call_functionality(user_selection)
            except ValueError as error:
                print(error)



if __name__ == "__main__":
    main()