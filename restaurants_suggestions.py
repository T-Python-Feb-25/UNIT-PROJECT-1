'''
This file was created to provide the user with the restaurants that 
are famous in the city he has chosen as his travel destination.

'''
from colorama import Fore
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

def get_user_info():

   try :
      with open("users_account_file.json","r",encoding="utf-8") as file:
       return json.load(file)
   except FileNotFoundError :
       return {}

def get_restaurant(email,city):
   myKey=os.getenv("YELP_KEY")
   url="https://api.yelp.com/v3/businesses/search"
   headers={"Authorization":"bearer %s" % myKey}

   params= {"location": city,
               "categories":"restaurants",
               "limit": 5 }
   response = requests.get(url, headers=headers, params=params)
   data=response.json()
   
   if "businesses" in data:
      restaurant=[
         {"name":restaurant["name"]}
         for restaurant in data["businesses"]
      ]
   else:
      print(Fore.RED+"Error getting restaurant data")
      return
   
   users_accounts=get_user_info()
   if email not in users_accounts:
      users_accounts[email]={}
      
   if "Travel Plans" not in users_accounts[email]:
            users_accounts=[email]["Travel Plans"]=[]
            users_accounts[email]["Travel Plans"].append({"restaurants":restaurant})
#اضافة معلومات لملف الجيسون
            with open("users_account_file.json", "w") as file:
                json.dump (users_accounts, file, indent=4) 
        
   return  restaurant    

  


                


