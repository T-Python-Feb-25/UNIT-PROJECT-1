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

   parameters= {"location": city,
               "limit": 5}
   response=requests.get(url,headers=headers,params=parameters)
   
   if response.status_code==200:
      events_suggestions= response.json()
      return events_suggestions.get("events",[])
   else:
      return []
   
def classified_activities(events,temperature):
   outdoor_events=[]
   indoor_events=[]
   for event in events:
      if temperature>25:
         outdoor_events.append(events)
      else:
         indoor_events.append(events)
      return outdoor_events,indoor_events

def add_events(email,city,temperature):
   events=get_events(email,city,temperature)
   if events:
      outdoor_events,indoor_events= classified_activities(events,temperature)

      print ("proposed Outdoor Events in {} Based on temperature {}c are:\n".format(city,temperature))
      for event in outdoor_events:
         print(Fore.LIGHTBLACK_EX+"{} event ".format(["name"]))

      print ("Proposed indoor Events in {} Based on temperature {}c are:\n".format(city,temperature))
      for event in indoor_events:
         print(Fore.LIGHTBLACK_EX+"{} event ".format(["name"]))

   users_accounts=get_user_info()

   for email in users_accounts:
         if "Travel Plans" not in users_accounts[email]:
            users_accounts["Events"] = {"Outdoor": outdoor_events, "Indoor": indoor_events}
            break

         #اضافة معلومات لملف الجيسون
   with open("users_account_file.json", "w") as file:
         json.dump (users_accounts, file, indent=4) 

   return print(events)