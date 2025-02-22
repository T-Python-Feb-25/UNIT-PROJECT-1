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
                                capacity INTEGER, 
                                availability BOOLEAN, 
                                )''')  
    def insert_truck(self,truck_data):
        try:
            self.connect()
            self.__create_truck_table()
            self.__cursor.execute("INSERT INTO trucks (model,capacity,availability) VALUES(?,?,?)",truck_data)
            self.__connection.commit()
            self.close_connection()
        except Exception as error :
            print("Somthing went wrong while trying to add new truck to the system")

    def remove_truck(self,truck_id):
        try:
            self.connect()
            self.__create_truck_table()
            self.__cursor.execute("DELETE FROM trucks WHERE truck_id = ? ",(truck_id,))
            self.__connection.commit() 
            print("The truck has been deleted from the system successfully.")

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
            print("Truck data updated successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            self.close_connection()   
    

           
    def retrive_truck(self):

        self.connect()
        self.__create_truck_table()
        # Connect to the SQLite database
        conn = self.__connection
        # Set the row factory to return dictionaries
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trucks")

        # Convert to list of dictionaries
        # result = [dict(row) for row in current_user]
        trucs=cursor.fetchall() 
        conn.close()

        trucks_list = [dict(truck) for truck in trucs] if trucs!=None else []
        if len(trucks_list)==0:
            print("No trucks available in the system")
            return None
        else:
            return trucks_list
        
          
    def close_connection(self):
        self.__connection.close()
