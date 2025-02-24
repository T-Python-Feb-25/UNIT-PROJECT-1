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
         outdoor_events.append(event)
      else:
         indoor_events.append(event)
      return outdoor_events,indoor_events

def add_events(city,temperature):
   events=get_events(city)
   if events:
      outdoor_events,indoor_events= classified_activities(events,temperature)
      print ()