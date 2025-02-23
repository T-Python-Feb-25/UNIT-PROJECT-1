import sqlite3

class TruckDB:
    
    def __init__(self,db_url):
        self.__db_url=db_url
        self.__connection=None
        self.__cursor=None

    def connect(self):
        self.__connection=self.__create_connection()
        self.__cursor=self.__connection.cursor()

    def __create_connection(self):
        return sqlite3.connect(self.__db_url)
    
    def __create_truck_table(self):
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS trucks(
                                truck_id INTEGER PRIMARY KEY,
                                model TEXT, 
                                body_style TEXT,
                                capacity INTEGER, 
                                availability BOOLEAN 
                                )''')   
        
    def drop_truck_table(self):
        self.connect()

        self.__cursor.execute('''DROP TABLE IF EXISTS trucks''')  
    def insert_truck(self,truck_data):
        try:
            self.connect()
            self.__create_truck_table()
            self.__cursor.execute("INSERT INTO trucks (model,body_style,capacity,availability) VALUES(?,?,?,?)",truck_data)
            self.__connection.commit()
            self.close_connection()
            print("The Truck has been added to the system successfully.")

        except Exception as error :
            print(error)
            print("Something went wrong while trying to add the truck to the system. Please try again later.")


    def is_truck_registered(self,truck_id)->bool:
        self.connect()
        self.__create_truck_table()
        self.__cursor.execute("SELECT truck_id FROM trucks")
        truck_list=self.__cursor.fetchall()
        if any(truck[0] == truck_id for truck in truck_list):
           return True
        return False

    def remove_truck(self,truck_id):
        try:
            self.connect()
            self.__create_truck_table()
            if self.is_truck_registered(truck_id):
                self.__cursor.execute("DELETE FROM trucks WHERE truck_id = ? ",(truck_id,))
                self.__connection.commit() 
                print("The truck has been deleted from the system successfully.")
            else:
                print("Faild to remove the truck , Invalid truck number.")

        except Exception as err:
            #TODO delete thi print
            print(err)
            print("Something went wrong while trying to remove the truck from the system. Please try again later.")
        finally:
            self.close_connection()


    def update_truck(self,truck_id, capacity=None, availability=None):
    
        updates = []
        params = []

        if capacity is not None:
            updates.append("capacity = ?")
            params.append(capacity)
        if availability is not None:
            updates.append("availability = ?")
            params.append(availability)

        update_clause = ', '.join(updates)
        sql = f"UPDATE Trucks SET {update_clause} WHERE truck_id = ?"
        params.append(truck_id)

        try:
            self.connect()
            self.__create_truck_table()
            self.__cursor.execute(sql, params)
            self.__connection.commit()
            print(f"Truck {truck_id} status updated successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            self.close_connection()   
    
    def retrive_trucks(self)->list:

        self.connect()
        self.__create_truck_table()
        # Connect to the SQLite database
        conn = self.__connection
        # Set the row factory to return dictionaries
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trucks")

        # Convert to list of dictionaries
        trucs=cursor.fetchall() 
        conn.close()

        trucks_list = [dict(truck) for truck in trucs] if trucs!=None else []
        if len(trucks_list)==0:
            print("No trucks available in the system")
        return trucks_list
    
    def retrive_available_trucks(self):
        self.connect()
        self.__create_truck_table()
        # Connect to the SQLite database
        conn = self.__connection
        # Set the row factory to return dictionaries
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trucks WHERE availability= 1")

        # Convert to list of dictionaries
        trucs=cursor.fetchall() 
        conn.close()

        trucks_list = [dict(truck) for truck in trucs] if trucs!=None else []
        if len(trucks_list)==0:
            print("No trucks available in the system")
        return trucks_list

    def __create_truck_assignments_table(self):
        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS truck_assignments (
        assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        truck_id INTEGER,
        assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (truck_id) REFERENCES trucks(truck_id)
    )
    ''')
    


    def assigin_truck(self,truck_data):
        try:
            self.connect()
            self.__create_truck_assignments_table()
            self.__cursor.execute("INSERT INTO truck_assignments(order_id,truck_id) VALUES(?,?)",truck_data)
            self.__connection.commit()
            self.close_connection()

        except Exception as error :
            print(error)
            print("Something went wrong while trying to assigne the truck to the order . Please try again later.")

   
    
    def close_connection(self):
        self.__connection.close()
