# Standard library imports
import sys
# Third-party imports

# Local application imports
from input_validation import *
from truck_management_mixin import *
class User:
    def __init__(self, id, first_name, last_name, phone,email, role):
        self.id= id
        self.first_name=first_name
        self.last_name=last_name
        self.phone=phone
        self.email=email
        self.role=role
        self.menu=""
        self.functionality = {} 
    
    def user_info(self):
        return self.id ,self.first_name, self.last_name, self.email ,self.phone,self.role
    
    def user_role(self):
        return self.role
    
    def display_menu(self):
        return self.menu

    def call_functionality(self, selection):
        if selection in self.functionality:
            return self.functionality[selection]()  # Call the corresponding method
        else:
            raise TypeError("Invalied Selection , please choose a number from the menu list")
    
    def user_logout(self):
        print("Thank for for visiting fazaa , hope to see you soon again ")      
        return sys.exit(0)




class Client(User):
    def __init__(self, id, first_name, last_name, phone,email):
        super().__init__(id, first_name, last_name, phone,email,role="Client")
        self.history=[]
        self.menu='''1- Profile
2-Make an order
3-Track an order
4-view history
5-logout
'''
        self.functionality={
            "1":self.profile,
            "2":self.make_order,
            "3":self.track_order,
            "4":self.view_history,
            "5":self.user_logout
        }
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
        self.menu='''1- Add Truck
2-Remove Truck
3-Update Price
4-Update order status
5-logout
'''
        self.functionality={
            "1":self.add_truck,
            "2":self.remove_truck,
            "3":self.update_price,
            "4":self.update_order_status,
            "5":self.user_logout
        }
class Admin(User,TruckManagementMixin):

    def __init__(self, id, first_name, last_name, phone,email ):
        super().__init__(id, first_name, last_name, phone,email,role="Admin")
        self.menu='''1-Add Employee
2-remove Employeee
3-update locations
4- Add Truck
5-Remove Truck
6-Update Price
7-Update order status
8-logout
'''
        self.functionality={
            "1":self.add_employee,
            "2":self.remove_employee,
            "3":self.update_locations,
            "4":self.add_truck,
            "5":self.remove_truck,
            "6":self.update_price,
            "7":self.update_order_status,
            "8":self.user_logout
        }
    def add_employee(self):
        from auth import sign_up

        print("To add an employee please enter his information")

        first_name=text_input_validation("First name: ")
        last_name=text_input_validation("Last name: ")
        email=email_input_validation("Email adress:")
        print(pass_requirments)
        encoded_pass= password_input_Validation("Password: ")
        phone=phone_input_validation("Phone number (e.g. 05xxxxxxxx):")
        
        added_user=sign_up(first_name,last_name,email,encoded_pass,phone,"Employee")
        print(added_user)
        print(f"{first_name} {last_name} has been added to the system successfully.")

    def remove_employee(self):
        from config import user_db

        print("Removing an employee...")

        email=email_input_validation("To remove an employee please enter his/her email adress:")
        user_db.remove_user(email)
        
    def update_locations(self):
        print("Updating locations...")
        







