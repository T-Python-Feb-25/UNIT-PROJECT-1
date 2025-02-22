import sqlite3


class UserDB:

    def __init__(self,db_url):
        self.__db_url=db_url
        self.__connection=None
        self.__cursor=None

    def connect(self):
        self.__connection=self.__create_connection()
        self.__cursor=self.__connection.cursor()

    def __create_connection(self):
        return sqlite3.connect(self.__db_url)
    
    def __create_user_table(self):
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                                id INTEGER PRIMARY KEY,
                                first_name TEXT, 
                                last_name TEXT, 
                                email TEXT UNIQUE NOT NULL, 
                                encoded_pass TEXT NOT NULL,
                                phone TEXT, 
                                role TEXT
                                )''')    
         
    def is_user_registered(self,user_to_find)->bool:
        self.connect()
        self.__create_user_table()
        self.__cursor.execute("SELECT email FROM users")
        User_list=self.__cursor.fetchall()
        if any(user[0] == user_to_find for user in User_list):
           return True
        return False

    def insert_user(self,user_data):
        try:
            self.connect()
            self.__create_user_table()
            self.__cursor.execute("INSERT INTO users (first_name, last_name,email,encoded_pass, phone , role) VALUES(?,?,?,?,?,?)",user_data)
            user_id= self.__cursor.lastrowid
            self.__connection.commit()
            first_name ,last_name ,email,encoded_pass, phone ,role=user_data
            
            self.close_connection()
            return {
                'id':user_id,
                'first_name':  first_name ,
                'last_name':last_name,
                'phone':phone,
                'email':email,
                'role':role
            }

        except sqlite3.IntegrityError as message:
            if message.sqlite_errorname=='SQLITE_CONSTRAINT_UNIQUE':
                print("This email already have an account, Try to login")
            else:
                print("Regestration faild please try again.")
        except Exception as err :
            print("Regestration faild please try again.")
          
    def retrive_user(self,email,encoded_pass):

        self.connect()
        self.__create_user_table()
        # Connect to the SQLite database
        conn = self.__connection
        # Set the row factory to return dictionaries
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? ",(email,))

        # Convert to list of dictionaries
        value=cursor.fetchone() 
        conn.close()
        current_user = dict(value) if value!=None else {}

        if len(current_user)==0:
            print("This email is not registered try to sign up.")
            return None
        elif current_user['encoded_pass']==encoded_pass:
            return current_user
        else:
            print("wrong passward please try again")
    def remove_user(self,email):
        try:
            self.connect()
            self.__create_user_table()
            if self.is_user_registered(email):
                self.__cursor.execute("DELETE FROM users WHERE email = ? ",(email,))
                self.__connection.commit() 
                print("The use has been deleted from the system successfully.")
            else:
                print("This user does not have an accoount")

        except Exception as err:
            print("Something went wrong while trying to remove the user from the system. Please try again.")
        finally:
            self.close_connection()


        
        
    def close_connection(self):
        self.__connection.close()

         

