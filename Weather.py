'''This file was created to fetch weather 
information in the city selected by the user and
 at the time specified by him.'''

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
   

#دالة لجلب معلومات الطقس بناءا على اسم المدينة و تاريخ الوصول اللذان تم ادخالهما من المستخدم 
def get_weather(email,city, date):

   myKey=os.getenv("API_KEY")
   url= "http://api.weatherapi.com/v1/forecast.json?key={}&q={}&dt={}".format(myKey,city,date)
   response=requests.get(url)
   weatherData=response.json()
   if "forecast" in weatherData:
      temperature=weatherData["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
      weatherCondition=weatherData["forecast"]["forecastday"][0]["day"]["condition"]["text"]
      print(Fore.LIGHTBLUE_EX+"The temperature in {} will be at {}, and the weather will be {}".format(city,temperature,weatherCondition))
#لاعطاء نصائح للملابس حسب درجة الحرارة
     
      if temperature<10:
         clothingTypeAdvice="Based on the temperature it looks like the weather\nwill be very cold, so be sure to wear very heavy\nclothes such as woolen coats,gloves, scarves and hats."
      elif 10<= temperature <=19:
         clothingTypeAdvice="Based on the temperature it looks like the\nweather will be cold, so wear a light jacket\nor coat and add extra layers as needed"
      elif 20<= temperature <=25:
          clothingTypeAdvice="Based on the temperature it looks like the weather will be\nmoderate,you can wear light clothes such as cotton shirts and\nregular pants and you can add a light jacket "
      elif 26<= temperature <=32:
          clothingTypeAdvice="Based on the temperature it looks like the weather\nwill be warm, wear very light clothing such as T-shirts\nand shorts and avoid heavy fabrics"
      elif temperature>32:
         clothingTypeAdvice="Based on the temperature it looks like the weather \nwill bevery hot, wear light cotton clothes, a hat\n and sunglasses, and drink plenty of water."
         
      print(Fore.LIGHTBLUE_EX+"Regarding the clothes you should wear \n"+Fore.LIGHTBLACK_EX+clothingTypeAdvice)
      users_accounts=get_user_info()
         
      if email in users_accounts:

         Travel_Plans={"city": city,
                         "date": date,
                         "temperatur":temperature,
                         "weather Condition":weatherCondition,
                         "clothing Type Advice":clothingTypeAdvice

          }
         users_accounts=get_user_info()
         if "Travel Plans" not in users_accounts[email]:
           users_accounts=[email]["Travel Plans"]=[]
         users_accounts[email]["Travel Plans"].append(Travel_Plans)

#فتح ملف جيسون لكتابة او اضافة معلومات المستخدم الجديد فيه
         with open("users_account_file.json", "w") as file:
            json.dump (users_accounts, file, indent=4)
      else:
         print("user not found in the system")   
         
      return temperature, weatherCondition
   else :
     print(Fore.RED+"Error getting weather data")
     return 
