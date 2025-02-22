from config import  truck_db

class TruckManagementMixin:

    def add_truck(self):

        truck_db.insert_truck("Private",1,True)
        print("Adding a truck...")

    def remove_truck(self):

        truck_db.remove_truck(1)
        print("Removing a truck...")

    def update_truck_status(self):


        print("updating truck status")
    
    def update_price(self):
        print("Updating price...")

    def update_order_status(self):
        print("Updating order status...")