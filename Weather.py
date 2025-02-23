'''This file was created to fetch weather 
information in the city selected by the user and
 at the time specified by him.'''

from colorama import Fore
import requests
import os
from dotenv import load_dotenv
load_dotenv()
 
#دالة لجلب معلومات المدينة و تاريخ الذهاب و الاياب من المستخدم 
def get_trip_info(city , date ):
   city=input(Fore.BLUE+"Please enter the name of the city you would like to go to \n")
   date=input(Fore.BLUE+"What is the arrival date? (YYYY-MM-DD)\n")
   return (city, date )

#دالة لجلب معلومات الطقس 
def get_weather(city, date):
   myKey=os.getenv("API_KEY")
   url= "http://api.weatherapi.com/v1/forecast.json?key={}&q={}&dt={}".format(myKey,city,date)
   response=requests.get(url)
   weatherData=response.json()
   if "forecast" in weatherData:
      temperature=weatherData["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
      weatherCondition=weatherData["forecast"]["forecastday"][0]["day"]["condition"]["text"]
      print(Fore.LIGHTBLUE_EX+"The temperature will be at {} and the weather will be {}".format(temperature,weatherCondition))
#لاعطاء نصائح للملابس حسب درجة الحرارة
     
      if temperature<10:
         print(Fore.LIGHTBLACK_EX+"Based on the temperature it looks like the weather\nwill be very cold, so be sure to wear very heavy\nclothes such as woolen coats,gloves, scarves and hats.")
      elif 10<= temperature <=19:
         print(Fore.LIGHTBLACK_EX+"Based on the temperature it looks like the\nweather will be cold, so wear a light jacket\nor coat and add extra layers as needed")
      elif 20<= temperature <=25:
          print(Fore.LIGHTBLACK_EX+"Based on the temperature it looks like the weather will be\nmoderate,you can wear light clothes such as cotton shirts and\nregular pants and you can add a light jacket ")
      elif 26<= temperature <=32:
         print(Fore.LIGHTBLACK_EX+"Based on the temperature it looks like the weather\nwill be warm, wear very light clothing such as T-shirts\nand shorts and avoid heavy fabrics")
      elif temperature>32:
         print(Fore.LIGHTBLACK_EX+"Based on the temperature it looks like the weather \nwill bevery hot, wear light cotton clothes, a hat\n and sunglasses, and drink plenty of water.") 
         
      return temperature, weatherCondition
   else :
     print(Fore.RED+"Error getting weather data")
     return 



