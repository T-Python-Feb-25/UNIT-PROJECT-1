# Standard library imports
# (Add any standard library imports here if applicable)

# Third-party imports
# (Add any third-party imports here if applicable)

# Local application imports
from input_validation import *
from TruckManagementMixin import *
class User:
    def __init__(self, id, first_name, last_name, phone,email, role):
        self.id= id
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone
        self.email=email
        self.role=role
    def user_info(self):
        return self.first_name, self.last_name, self.email ,self.phone,self.role
    def user_role(self):
        return self.role


class Client(User):
    def __init__(self, id, first_name, last_name, phone,email):
        super().__init__(id, first_name, last_name, phone,email,role="Client")
        self.history=[]
    def profile(self):
        print("Viewing profile...")

    def make_order(self):
        print("Making an order...")

    def track_order(self):
        print("Tracking an order...")

    def view_history(self):
        print("Viewing order history...")

class Employee(User,TruckManagementMixin):
    def __init__(self, id, first_name, last_name, phone,email ):
        super().__init__(id, first_name, last_name, phone,email,role="Employee")

class Admin(User,TruckManagementMixin):

    def __init__(self, id, first_name, last_name, phone,email ):
        super().__init__(id, first_name, last_name, phone,email,role="Admin")

    def add_employee(self):
        from auth import sign_up

        # Admin-specific implementation
        print("To add an employee please enter his information")

        first_name=text_input_validation("First name: ")
        last_name=text_input_validation("Last name: ")
        email=email_input_validation("Email adress:")
        print(pass_requirments)
        encoded_pass= password_input_Validation("Password: ")
        phone=phone_input_validation("Phone number (e.g. 05xxxxxxxx):")
        
        sign_up(first_name,last_name,email,encoded_pass,phone,"Employee")
        print(f"{first_name} {last_name} has been added to the system successfully.")

    def remove_employee(self):
        from config import db

        # Admin-specific implementation
        print("Removing an employee...")

        email=email_input_validation("To remove an employee please enter his/her email adress:")
        db.remove_user(email)
        
    def update_locations(self):
        # Admin-specific implementation
        print("Updating locations...")
        







