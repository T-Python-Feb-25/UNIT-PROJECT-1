# Standard library imports
import sys
# Third-party imports
from colorama import Fore

# Local application imports
from input_validation import *
from data_config import get_all_governorates, get_all_provinces, update_data
from truck_management_mixin import *
from config import order_db
class User:
    """Represents a user in the system."""
    def __init__(self, id, first_name, last_name, phone, email, role):
        self.__id = id
        self.first_name = first_name
        self.last_name = last_name
        self.__phone = phone
        self.__email = email
        self.__role = role
        self.menu = ""
        self.functionality = {}

    def user_info(self):
        """Returns the user's information.

        Returns:
            tuple: A tuple containing the user's id, first name, last name,
                   email, phone number, and role.
        """
        return self.__id, self.first_name, self.last_name, self.__email, self.__phone, self.__role

    def user_role(self):
        """Returns the user's role.

        Returns:
            str: The role of the user.
        """
        return self.__role

    def display_menu(self):
        """Displays the menu based on the user.

        Returns:
            str: The menu as a string.
        """
        return self.menu

    def call_functionality(self, selection):
        """Calls the functionality associated with the selected menu item.

        Args:
            selection (str): The menu selection to be executed.

        Returns:
            Any: The result of the function associated with the selection.

        """
        if selection in self.functionality:
            return self.functionality[selection]()  
        else:
            raise ValueError(Fore.RED+"Invalid Selection, please choose a number from the menu list")
        

    def user_logout(self):
        """Logs the user out and displays a farewell message.

        Prints a thank you message and exits the application.
        """
        print(Style.BRIGHT+"Thank for for using Nafzaealuk , hope to see you soon again ")
        return sys.exit(0)




class Client(User):
    def __init__(self, id, first_name, last_name, phone,email):
        super().__init__(id, first_name, last_name, phone,email,role="Client")
        self.menu='''
1-Make an order
2-Track an order
3-View history
4-Logout
'''
        self.functionality={
            "1":self.make_order,
            "2":self.track_order,
            "3":self.view_history,
            "4":self.user_logout
        }

    def make_order(self):
        from auth import send_email_notification
        print("Making an order...")
        order_info=collect_order_info()
        user_id=self.__id
        truck_id=order_info['assigined_truck']
        car_make=order_info['car_make']
        car_model= order_info['car_model']
        car_year=order_info['car_year']
        price=order_info['price']
        pickup_location=order_info['pickup']
        delivery_location=order_info['delivery'] 
        pickup_date=order_info['pickup_date']
        order_db.insert_order( user_id, truck_id,car_make, car_model, car_year, price,pickup_location,delivery_location ,pickup_date, status='pending')
        send_email_notification(
        "Order Confirmation",
        "Thank you for trusting us! Your order has been created. "
        "Please track your order status through the system or through the sent email. "
        "Your order status: pending.\n We will contact you soon to get the detailed address."
        "Nefzalek Team",
        self.__email)



    def track_order(self):
        user_orders=order_db.retrive_user_orders(self.__id)
        filtered_active_orders = list(filter(lambda order: order["status"] !="completed", user_orders))
        print(f"You have {len(filtered_active_orders)} active orders")

        for order in filtered_active_orders:
            print(f"order #{order['order_id']} - status :{order['status']}")


    def view_history(self):
        print("Your order history")
        user_orders=order_db.retrive_user_orders(self.__id)
        for order in user_orders:
            print(f"order #{order['order_id']} - status :{order['status']}")
            print(f"From {order['pickup_location']} to {order['delivery_location']}")
            print(f"Total price :{order['price']}")
            print()




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
        self.menu='''
========================= Admin Menu ===========================
        1-Add Employee
        2-Remove Employeee
        3-Update provinces
        4-Display Trucks
        5-Register a Truck
        6-Unregister a Truck
        7-Update Price
        8-Update order status
        9-Logout
================================================================'''
     
        self.functionality={
            "1":self.add_employee,
            "2":self.remove_employee,
            "3":self.update_domain,
            "4":self.display_trucks,
            "5":self.register_truck,
            "6":self.unregister_truck,
            "7":self.update_price,
            "8":self.update_order_status,
            "9":self.user_logout
        }
    def add_employee(self):
        from auth import sign_up

        print(Fore.BLUE+"To add an employee please enter his information")

        first_name=get_alphabetic_input("First name: ")
        last_name=get_alphabetic_input("Last name: ")
        email=get_email_input("Email adress:")
        print(pass_requirments)
        encoded_pass= get_password_input("Password: ")
        phone=get_phone_input("Phone number (e.g. 05xxxxxxxx):")
        
        added_user=sign_up(first_name,last_name,email,encoded_pass,phone,"Employee")
        print(Fore.GREEN+f"{first_name} {last_name} has been added to the system successfully.")

    def remove_employee(self):
        from config import user_db
        email=get_email_input(Fore.BLUE+"To remove an employee please enter his/her email adress:")
        user_db.remove_user(email)

    def update_domain(self):
        """Update the list of covered locations by adding or removing governorates.

        This method allows the user to add or remove governorates from a selected province. 
        It prompts the user for their choice, displays available provinces and governorates, 
        and updates the data accordingly.
        """
        print(Fore.BLUE + "Updating covered locations")
        while True:
            option = get_alphabetic_input("Do you want to add or remove? ")

            if option.lower() == "remove":
                get_all_provinces(self.provinces_list)

                province_num = get_number_input_with_limit("Choose the province number that you want to modify: ", len(self.provinces_list))
                keys_list = list(self.provinces_list.keys())

                selected_province = keys_list[province_num - 1]
                get_all_governorates(self.provinces_list, selected_province)
                govern_num = get_number_input_with_limit("Choose the governorate number that you want to remove: ", len(self.provinces_list[selected_province]))
                self.provinces_list[selected_province].pop(govern_num - 1)
                update_data(self.provinces_list, self.pricing_list)
                print(Fore.GREEN + "The governorate has been removed successfully")
                break
            elif option.lower() == "add":
                get_all_provinces(self.provinces_list)

                province_num = get_number_input_with_limit("Choose the province number that you want to modify: ", len(self.provinces_list))
                new_govern = get_alphabetic_input("Enter the governorate name: ")
                keys_list = list(self.provinces_list.keys())
                selected_province = keys_list[province_num - 1]

                self.provinces_list[selected_province].append(new_govern)
                update_data(self.provinces_list, self.pricing_list)
                print(Fore.GREEN + "The governorate has been added successfully")
                break
            else:
                print(Fore.RED + "Invalid input")

    def update_price(self):
        print(Fore.BLUE+"Updating Prices")

        get_all_prices(self.pricing_list)
    
        num=get_number_input_with_limit("Enter the number of selection that you want to update its price:",len(self.pricing_list))
        titles_list=list(self.pricing_list.keys())

        new_price=get_number_input("Enter the updated price: ")
        self.pricing_list[titles_list[num-1]]=new_price
        update_data(self.provinces_list,self.pricing_list)

        print(Fore.GREEN+f"The price of {titles_list[num-1]} has been updated")

    







