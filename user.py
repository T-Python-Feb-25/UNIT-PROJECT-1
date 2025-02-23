# Standard library imports
import sys
# Third-party imports

# Local application imports
from input_validation import *
from province_mangement import get_all_governorates, get_all_provinces, update_data
from truck_management_mixin import *
from config import order_db

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
            return self.functionality[selection]()  
        else:
            raise TypeError("Invalied Selection , please choose a number from the menu list")
    



    def user_logout(self):
        print("Thank for for visiting fazaa , hope to see you soon again ")      
        return sys.exit(0)




class Client(User):
    def __init__(self, id, first_name, last_name, phone,email):
        super().__init__(id, first_name, last_name, phone,email,role="Client")
        self.history=[]
        self.menu='''
1-Make an order
2-Track an order
3-view history
4-logout
'''
        self.functionality={
            "1":self.make_order,
            "2":self.track_order,
            "3":self.view_history,
            "4":self.user_logout
        }

    def make_order(self):
        print("Making an order...")
        order_info=collect_order_info()
        user_id=self.id
        truck_id=order_info['assigined_truck']
        car_make=order_info['car_make']
        car_model= order_info['car_model']
        car_year=order_info['car_year']
        price=order_info['price']
        pickup_location=order_info['pickup']
        delivery_location=order_info['delivery'] 
        pickup_date=order_info['pickup_date']
        order_db.insert_order( user_id, truck_id,car_make, car_model, car_year, price,pickup_location,delivery_location ,pickup_date, status='pending')

    def track_order(self):
        print("Tracking an order...")

    def view_history(self):
        print("Viewing order history...")

class Employee(User,TruckManagementMixin):
    def __init__(self, id, first_name, last_name, phone,email ):
        super().__init__(id, first_name, last_name, phone,email,role="Employee")
        self.menu='''1-Register a Truck
2-Unregister a Truck
3-Update order status
4-Logout
'''
        self.functionality={
            "1":self.register_truck,
            "2":self.unregister_truck,
            "3":self.update_order_status,
            "4":self.user_logout
        }
class Admin(User,TruckManagementMixin):

    def __init__(self, id, first_name, last_name, phone,email ):
        super().__init__(id, first_name, last_name, phone,email,role="Admin")
        self.menu='''1-Add Employee
2-Remove Employeee
3-Update provinces
4-Register a Truck
5-Unregister a Truck
6-Update Price
7-Update order status
8-Logout
'''
     
        self.functionality={
            "1":self.register_truck,
            "2":self.unregister_truck,
            "3":self.update_domain,
            "4":self.update_price,
            "5":self.register_truck,
            "6":self.unregister_truck,
            "7":self.update_order_status,
            "8":self.user_logout
        }
    def add_employee(self):
        from auth import sign_up

        print("To add an employee please enter his information")

        first_name=get_alphabetic_input("First name: ")
        last_name=get_alphabetic_input("Last name: ")
        email=get_email_input("Email adress:")
        print(pass_requirments)
        encoded_pass= get_password_input("Password: ")
        phone=get_phone_input("Phone number (e.g. 05xxxxxxxx):")
        
        added_user=sign_up(first_name,last_name,email,encoded_pass,phone,"Employee")
        print(added_user)
        print(f"{first_name} {last_name} has been added to the system successfully.")

    def remove_employee(self):
        from config import user_db

        print("Removing an employee...")

        email=get_email_input("To remove an employee please enter his/her email adress:")
        user_db.remove_user(email)
        
    def update_domain(self):
        print("Updating covered locations ...")
        while True:

            option=get_alphabetic_input("Do you want to add or remove? ")

            if option.lower()=="remove":
                get_all_provinces(self.provinces_list)

                province_num=get_number_input_with_limit("choose the province number that you want to remove from :",len(self.provinces_list))
                keys_list=list(self.provinces_list.keys())

                selected_province=keys_list[province_num-1]
                get_all_governorates(self.provinces_list,selected_province)
                govern_num=get_number_input_with_limit("choose the governorate number that you want to remove :",len(self.provinces_list[selected_province]))
                self.provinces_list[selected_province].pop(govern_num-1)
                update_data(self.provinces_list,self.pricing_list)
                print("The governorate has been removed")
                break
            elif option.lower()=="add":
                get_all_provinces(self.provinces_list)

                province_num=get_number_input_with_limit("choose the province number that you want to add to it :",len(self.provinces_list))
                new_govern=get_alphabetic_input("Enter the governorate name: ")
                keys_list=list(self.provinces_list.keys())
                selected_province=keys_list[province_num-1]

                self.provinces_list[selected_province].append(new_govern)
                update_data(self.provinces_list,self.pricing_list)
                # add_province(self.provinces_list,new_province)
                print("The governorate has been added")
                break
            else:
                print("invalid input")


    def update_price(self):
        print("Updating prices...")

        get_all_prices(self.pricing_list)
    
        num=get_number_input_with_limit("Enter the number of selection that you want to update its price:",len(self.pricing_list))
        titles_list=list(self.pricing_list.keys())

        new_price=get_number_input("Enter the updated price: ")
        self.pricing_list[titles_list[num-1]]=new_price
        update_data(self.provinces_list,self.pricing_list)

        print(f"The price of {titles_list[num-1]} has been updated")

    







