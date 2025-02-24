from auth import send_email_notification
from config import  DATABASE, truck_db,order_db
from input_validation import get_number_input, get_number_input_with_limit
from data_config import get_all_prices, load_data
from colorama import Fore, Style


class TruckManagementMixin:
    provinces_list, pricing_list=load_data()
    
    def register_truck(self):  
        print(Fore.BLUE+"Adding a new truck")
        model=input("Enter the Truck Model Name:")
        body_style=input("Enter the truck body style (Closed or Open):")
        capacity=get_number_input_with_limit("Enter the capacity of this truck:",6)
        availability=True
        truck_db.insert_truck((model,body_style.lower(),capacity,availability,))

    def unregister_truck(self):
        print(Fore.BLUE+"Removing a truck")
        self.display_trucks()
        print("Enter the truck number that you want to deleat from the system")
        truck_id=get_number_input("TRK-")
        truck_db.remove_truck(truck_id)



    def display_trucks(self):
        trucks_list:list=truck_db.retrive_trucks()
        print("============================= Trucks =============================")
        from prettytable import PrettyTable

        table = PrettyTable()

        # Add columns
        table.field_names = ["TRK-ID", "model", "style","capacity","availabile"]

        # Print the table
        for truck in trucks_list:
            truck_id,model,style,capacity,availability=truck.values()
            table.add_row([truck_id,model ,style , capacity, "Yes" if availability else "No" ])
        print(table)

    def update_order_status(self):
        

        active_orders=order_db.retrive_active_order()
        if len(active_orders)==0:
            return
        for order in active_orders:
            order_id,status=order.values()
            print(f"order #{order_id} - status: {status}" )
            

        order_id=get_number_input("Enter the order number to update its status: ")
        filtered_orders=list(filter(lambda order: order['order_id']==order_id,active_orders))
        if filtered_orders:
            status= filtered_orders[0]['status']
            if status=='pending':
                new_status='in transit'
                message = f'''Thank you for trusting us! Your order is currently {new_status}. 
You can track your order status through the system or the email we sent. 
We appreciate your patience and look forward to delivering your car soon!
\nNafzaealuk Team'''
            
            else:
                new_status='completed'
                message = f'''Thank you for trusting us! Your order has been successfully {new_status}.\n
We appreciate your business and look forward to serving you again!
\nNafzaealuk Team'''
            
            user_email,truck_id= order_db.update_order_status(order_id,new_status)
            if new_status=='completed':
                truck_db.update_truck(truck_id,availability=True)
            send_email_notification("Order Updates",message,to=user_email)            
                
        else:
            print("invalid order number")