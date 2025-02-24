from colorama import Fore
import requests
import json
import os
import Weather
from dotenv import load_dotenv
load_dotenv

def get_user_info():

   try :
      with open("users_account_file.json","r",encoding="utf-8") as file:
       return json.load(file)
   except FileNotFoundError :
       return {}


def get_events(email,city,temperature):
   myKey=os.getenv("YELP_KEY")
   url="https://api.yelp.com/v3/businesses/search"
   headers={"Authorization":"bearer %s" % myKey}