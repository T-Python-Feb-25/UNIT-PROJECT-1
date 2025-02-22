import requests
import json
from getpass import getpass
class User:
    def __init__(self):
        self.__user_username=None
        self.__user_password=None
        self.__users_data=None
        self.__users_data_login=None
        self.load_data()

        
    def get_user_useername(self):
        return self.__user_username
    def get_user_password(self):
        return self.__user_password
    def get_user_data(self):
        return self.__users_data
    def get_user_data_login(self):
        return self.__users_data_login
    
    def login(self):
        username=input("please enter username:")  
        password=getpass("please enter password:")
        if username in self.__users_data and password in self.__users_data[username]:
            self.__user_username=username
            self.__user_password=password
            self.__users_data_login=self.__users_data[username][password]
            print("\n"*15)
            print("Your login is successful.")
    def logout(self):
        self.__user_username=None
        self.__user_password=None
    def register(self):
        username=input("please enter username:")
        password=getpass("please enter password:")
        if username in self.__users_data:
            print(f"Sorry, the username '{username}' is already taken. Please choose a different one.")
        elif len(username) < 6 or len(password)<6:
            print("Username and passowrd must be at least 6 characters long.")
        elif " " in username:
            print("Username cannot contain spaces.")
        else:
            self.__users_data[username]={password:{
                "movie":{"rating":[],"movie_watch_list":[]},
                "tv":{"rating":[],"tv_watch_list":[]}   
                }
                }
            self.save_data()
            print("Your register is successful.")
    def load_data(self):
        try:
            with open("data.json","r") as file:
                self.__users_data=json.load(file)
        except:
            self.__users_data={}
    def save_data(self):
        data=self.__users_data
        with open("data.json","w") as file:
            json.dump(data,file,indent=4)
   