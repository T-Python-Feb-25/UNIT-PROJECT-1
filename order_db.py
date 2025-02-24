import sqlite3

class OrderDB:
    
    def __init__(self,db_url):
        self.__db_url=db_url
        self.__connection=None
        self.__cursor=None

    def connect(self):
        self.__connection=self.__create_connection()
        self.__cursor=self.__connection.cursor()

    def __create_connection(self):
        return sqlite3.connect(self.__db_url)
    
    def __create_orders_table(self):
        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            car_make TEXT,
            car_model TEXT,
            car_year INTEGER,
            price REAL ,
            pickup_location,
            delivery_location,
            pickup_date TEXT,
            status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'in transit', 'completed')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
            )''')

        
    def drop_orders_table(self):
        self.connect()
        self.__cursor.execute('''DROP TABLE IF EXISTS orders''')  

    def insert_order(self, user_id,truck_id ,car_make, car_model, car_year, price,pickup_location,delivery_location ,pickup_date,status='pending'):
        from config import truck_db

        try:

            self.connect()
            self.__create_orders_table()
            self.__cursor.execute('''INSERT INTO orders (user_id, car_make, car_model, car_year, price,pickup_location,delivery_location, pickup_date, status) VALUES (?, ?, ?, ?, ?, ?,?,?, ?)''',(user_id,car_make,car_model,car_year,price,pickup_location,delivery_location,pickup_date,status,))
            order_id= self.__cursor.lastrowid
            self.__connection.commit()
            self.close_connection()
            truck_db.assigin_truck((order_id,truck_id,))
            truck_db.update_truck(truck_id,availability=False)
        


            print("The order has been created successfully.")

        except Exception as error :
            print("Something went wrong while trying to create your order. Please try again later.")


    def update_order_status(self,order_id,status):
    

        sql = f"UPDATE orders SET status = ? WHERE order_id = ?"

        try:
            self.connect()
            self.__create_orders_table()
            self.__cursor.execute(sql, [status,order_id])
            self.__connection.commit()
             # Get the user email associated with the updated order
            self.__cursor.execute("""
            SELECT u.email
            FROM orders o
            JOIN users u ON o.user_id = u.id
            WHERE o.order_id = ?;
            """, (order_id,))
                 # Fetch the result
            result = self.__cursor.fetchone()
            print(result)

            if result:
                user_email = result[0]
                print(f"Order updated. ")
                
            else:
                print("No user found for this order.")
    
            # Get the truck ID assigned to the order
            self.__cursor.execute("""
            SELECT ta.truck_id
            FROM truck_assignments ta
            WHERE ta.order_id = ?;
            """, (order_id,))
    
            # Fetch the result
            result = self.__cursor.fetchone()
            print(result)
            if result:
                truck_id = result[0]
            else:
                print("No truck assigned to this order.")
            return user_email,truck_id

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            self.close_connection()   
    


    def retrive_active_order(self)->list:

        self.connect()
        self.__create_orders_table()
        # Connect to the SQLite database
        conn = self.__connection
        # Set the row factory to return dictionaries
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT order_id, status FROM orders WHERE status != 'completed'")
        # Convert to list of dictionaries
        orders=cursor.fetchall() 
        conn.close()

        orders_list = [dict(order) for order in orders] if orders!=None else []
        if len(orders_list)==0:
            print("No active orders available in the system")
        return orders_list
    
    def retrive_user_orders(self,user_id)->list:

        self.connect()
        self.__create_orders_table()
        # Connect to the SQLite database
        conn = self.__connection
        # Set the row factory to return dictionaries
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id =?",(user_id,))

        # Convert to list of dictionaries
        trucs=cursor.fetchall() 
        conn.close()

        trucks_list = [dict(truck) for truck in trucs] if trucs!=None else []
        if len(trucks_list)==0:
            print("No orders available for you")

        return trucks_list
        
          
    def close_connection(self):
        self.__connection.close()
