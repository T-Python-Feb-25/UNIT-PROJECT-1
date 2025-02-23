from config import  truck_db
from input_validation import number_input_validation
from province_mangement import load_province

class TruckManagementMixin:
    Provinces=load_province()
    def register_truck(self):  
        print("Adding a truck...")
        model=input("Enter the Truck Model Name:")
        body_style=input("Enter the truck body style (Closed or Open):")
        capacity=number_input_validation("Enter the capacity of this truck:",up_to=6)
        availability=True
        truck_db.insert_truck((model,body_style.lower(),capacity,availability,))

    def unregister_truck(self):
        print("Removing a truck...")
        self.display_trucks()
        print("Enter the truck number that you want to deleat from the system")
        truck_id=input("TRK-")
        truck_db.remove_truck(truck_id)

    def update_truck_status(self,truck_id,is_available):
        print("Updating truck status...")
        truck_db.update_truck(truck_id,availability=is_available)

    def display_trucks(self):
        trucks_list:list=truck_db.retrive_trucks()
        for truck in trucks_list:
            truck_id,model,style,capacity,availability=truck.values()
            print(f"TRK-{truck_id} - model: {model} ,style: {style} , capacity: {capacity} , availability: {True if availability else False}" )
            
    def update_price(self):
        print("Updating price...")

    def update_order_status(self):
        print("Updating order status...")