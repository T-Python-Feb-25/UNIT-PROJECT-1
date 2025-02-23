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
            truck_db.assigin_truck((order_id,truck_id,))
            truck_db.update_truck(truck_id,availability=False)
            self.__connection.commit()
            self.close_connection()


            print("The order has been created successfully.")

        except Exception as error :
            print(error)
            print("Something went wrong while trying to create your order. Please try again later.")


    def update_order_status(self):
    
        updates = []
        params = []

        # if capacity is not None:
        #     updates.append("capacity = ?")
        #     params.append(capacity)
        # if availability is not None:
        #     updates.append("availability = ?")
        #     params.append(availability)

        update_clause = ', '.join(updates)
        sql = f"UPDATE orders SET {update_clause} WHERE order_id = ?"
        # params.append(truck_id)

        try:
            self.connect()
            self.__create_orders_table()
            self.__cursor.execute(sql, params)
            self.__connection.commit()
            # print(f"Truck {order_id}data updated successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            self.close_connection()   
           
    def retrive_all_orders(self)->list:

        self.connect()
        self.__create_orders_table()
        # Connect to the SQLite database
        conn = self.__connection
        # Set the row factory to return dictionaries
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")

        # Convert to list of dictionaries
        trucs=cursor.fetchall() 
        conn.close()

        trucks_list = [dict(truck) for truck in trucs] if trucs!=None else []
        if len(trucks_list)==0:
            print("No orders available in the system")
        return trucks_list
    
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
            print("No orders available in the system")
        return trucks_list
        
          
    def close_connection(self):
        self.__connection.close()
