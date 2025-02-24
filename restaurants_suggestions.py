'''
This file was created to provide the user with the restaurants that 
are famous in the city he has chosen as his travel destination.

'''
from colorama import Fore
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv

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

   parameters= {"location": city,
               "categories":"restaurants",
               "limit": 4 }
   
   response=requests.get(url,headers=headers,params=parameters)
   data=response.json()
   if "businesses" in data:
      restaurant=[
         {"name":restaurant["name"]}
         for restaurant in data["businesses"]
      ]

      users_accounts=get_user_info()
      
      if "Travel Plans" not in users_accounts[email]:
            users_accounts=[email]["Travel Plans"]=[]
            users_accounts[email]["Travel Plans"].append({"restaurants":restaurant})

    #فتح ملف جيسون لكتابة او اضافة معلومات المستخدم الجديد فيه
            with open("users_account_file.json", "w") as file:
                json.dump (users_accounts, file, indent=4) 
   else:
       print(Fore.RED+"Error getting restaurant data")
       return 
   return restaurant      

  


                


