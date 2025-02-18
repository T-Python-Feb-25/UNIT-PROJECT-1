import sqlite3
from user import User

class DatabaseConnector:

    def __init__(self,db_url):
        self.__db_url=db_url
        self.__connection=None
        self.__cursor=None


    def connect(self):
        self.__connection=self.__create_connection()
        self.__cursor=self.__connection.cursor()


    def __create_connection(self):
        return sqlite3.connect(self.__db_url)
    
    def insert_user(self,data):
        try:
            self.__cursor.execute("INSERT INTO users (fisrt_name, last_name,email,encoded_pass, phone , role) VALUES(?,?,?,?,?,?)",data)
            self.__connection.commit()
            self.__connection.close()
        except sqlite3.IntegrityError as message:
            if message.sqlite_errorname=='SQLITE_CONSTRAINT_UNIQUE':
                print("This email already have an account, Try to login")
            else:
                print(message)
        except Exception :
            print("Regestration faild please try again.")


    def create_table(self):
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                                id INTEGER PRIMARY KEY,
                                fisrt_name TEXT, 
                                last_name TEXT, 
                                email TEXT UNIQUE NOT NULL, 
                                encoded_pass TEXT NOT NULL,
                                phone TEXT, 
                                role TEXT
                                )''')    
         

    # def retrive_user(self)->User:
    def retrive_user(self,email):
        
        return self.__cursor.execute("SELECT * FROM users WHERE email= ?",email)
