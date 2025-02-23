'''
This file was created to provide the user with the restaurants that 
are famous in the city he has chosen as his travel destination.

'''
import requests
import Weather
import json
import os
from dotenv import load_dotenv
load_dotenv

def restaurant():
   myKey=os.getenv("YELP_KEY")

   city=Weather.get_trip_info()
   url="https://api.yelp.com/v3/businesses/search"
   headers={"Authorization":"bearer %s" % myKey}

   parameters= {"location": city,
               "categories":"restaurants",
               "limit": 6 }
   response=requests.get(url,headers=headers,parameters=parameters)
   return(response)

print(restaurant())

                


