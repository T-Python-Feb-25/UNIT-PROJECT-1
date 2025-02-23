'''This file was created to fetch weather 
information in the city selected by the user and
 at the time specified by him.'''

from colorama import Fore
import requests
#المفتاح الخاص بمكتبة الطقس
apiKey="11b1953aab3d44f3824193935251902"
#دالة لجلب معلومات المدينة و تاريخ الذهاب و الاياب من المستخدم 
def get_trip_info(city , date ):
   city=input(Fore.MAGENTA+"Please enter the name of the city you would like to go to \n")
   arrivlDate=input(Fore.MAGENTA+"What is the arrival date? (YYYY-MM-DD)\n")
   return (city, date )

#دالة لجلب معلومات الطقس 
def get_weather(city, date):
   url= "http://api.weatherapi.com/v1/forecast.json?key={}&q={}&dt={}".format(apiKey,city,date)
   response=requests.get(url)
   weatherData=response.json()
   if "forecast" in weatherData:
      temperature=weatherData["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
      weatherCondition=weatherData["forecast"]["forecastday"][0]["day"]["condition"]["text"]
#لاعطاء نصائح للملابس حسب درجة الحرارة 
      if temperature<10.00:
         print('''The weather will be very cold, so be sure to 
               wear very heavy clothes such as woolen coats,
                gloves, scarves and hats.''')
      elif temperature>=10.00 & temperature<=19.00:
         print('''The weather will be cold, so wear a light 
               jacket or coat and add extra layers as needed''')
      elif temperature>=20.00 & temperature<=25.00:
          print('''The weather will be moderate,
                 you can wear light clothes such as cotton shirts and 
                regular pants and you can add a light jacket ''')
      elif temperature>=20.00 & temperature<=32.00:
         print('''The weather will be warm, wear very light clothing 
               such as T-shirts and shorts and avoid heavy fabrics''') 
      elif temperature>32.00:
         print('''The weather will be very hot, 
               wear light cotton clothes, a hat and sunglasses,
                and drink plenty of water.''') 
         
      return temperature, weatherCondition
   else :
     print(Fore.RED+"Error getting weather data")
     return 


print(get_weather("Riyadh","2025-02-24"))


