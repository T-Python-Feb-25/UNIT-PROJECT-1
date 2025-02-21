'''This file was created to fetch weather 
information in the city selected by the user and
 at the time specified by him.'''


import requests

apiKey="11b1953aab3d44f3824193935251902"

#دالة لجلب معلومات الطقس 
def get_weather(city, date):
   url= "http://api.weatherapi.com/v1/forecast.json?key={}&q={}&dt={}".format(apiKey,city,date)
   response=requests.get(url)
   weather_data=response.json()
   

