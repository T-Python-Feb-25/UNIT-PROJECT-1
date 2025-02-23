import json
from getpass import getpass
from colorama import Fore, Back, Style
import time
import hashlib
class User:
    def __init__(self):
        self.__user_username=None
        self.__user_password=None
        self.__users_data=None
        self.__users_data_login=None #Stores the data of the currently logged in user
        self.load_data()

    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()
    def get_user_useername(self):
        return self.__user_username
    def get_user_password(self):
        return self.__user_password
    def get_user_data(self):
        return self.__users_data
    def get_user_data_login(self):
        return self.__users_data_login
    
    def login(self):
        '''login the user by checking the username and password'''
        username=input(f"{Fore.CYAN}please enter username:{Fore.YELLOW}{Style.RESET_ALL}")  
        password=self.hash_password(getpass(f"{Fore.CYAN}please enter password:{Style.RESET_ALL}"))
        if username in self.__users_data and password in self.__users_data[username]:
            self.__user_username=username
            self.__user_password=password
            self.__users_data_login=self.__users_data[username][self.__user_password]
            print(f"{Fore.GREEN}Your login is successful{Style.RESET_ALL}")
            time.sleep(1)
            print("\n"*20)
        else:
            print(f"{Fore.RED}Invalid username or password. Please try again.{Style.RESET_ALL}")
    def logout(self):
        '''logout the currnet user'''
        self.__user_username=None
        self.__user_password=None
        print(f"{Fore.GREEN}You have been logged out successfully!{Style.RESET_ALL}")
    def register(self):
        '''register a new user'''
        username=input(f"{Fore.CYAN}please enter username:{Fore.YELLOW}{Style.RESET_ALL}")
        password=getpass(f"{Fore.CYAN}please enter password:")
        if username in self.__users_data:
            print(f"{Fore.RED}Sorry, the username '{username}' is already taken. Please choose a different one.{Style.RESET_ALL}")
        elif len(username) < 4 or len(password)<4:
            print(f"{Fore.RED}Username and passowrd must be at least 4 characters long.{Style.RESET_ALL}")
        elif " " in username:
            print(f"{Fore.RED}Username cannot contain spaces.{Style.RESET_ALL}")
        else:
            self.__users_data[username]={self.hash_password(password):{
                "movie":{"rating":[],"movie_watch_list":[]},
                "tv":{"rating":[],"tv_watch_list":[]}   
                }
                }
            self.save_data()
            print(f"{Fore.GREEN}Your register is successful.{Style.RESET_ALL}")
    def load_data(self):
        '''load data from data.json and create one if data.json dosent exist'''
        try:
            with open("data.json","r") as file:
                self.__users_data=json.load(file)
        except:
            self.__users_data={}
    def save_data(self):
        '''save data to data.json'''
        data=self.__users_data
        with open("data.json","w") as file:
            json.dump(data,file,indent=4)
   