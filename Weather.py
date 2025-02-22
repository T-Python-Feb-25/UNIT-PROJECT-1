'''This file was created to fetch weather 
information in the city selected by the user and
 at the time specified by him.'''


import requests
#المفتاح الخاص بمكتبة الطقس
apiKey="11b1953aab3d44f3824193935251902"
#دالة لجلب معلومات المدينة و تاريخ الذهاب و الاياب من المستخدم 
def get_trip_info(city , arrivlDate ,departureDate):
   city=input("Please enter the name of the city you would like to go to \n")
   arrivlDate=input("What is the arrival date? (YYYY-MM-DD)\n")
   departureDate=input("What is the departure date? (YYYY-MM-DD)\n")
   return (city, arrivlDate,departureDate )

#دالة لجلب معلومات الطقس 
def get_weather(city, date):
   url= "http://api.weatherapi.com/v1/forecast.json?key={}&q={}&dt={}".format(apiKey,city,date)
   response=requests.get(url)
   weatherData=response.json()
   if "forecast" in weatherData:
      temperature=weatherData["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
      weatherCondition=weatherData["forecast"]["forecastday"][0]["day"]["condition"]["text"]
      
      return temperature, weatherCondition
   else :
     print("Error getting weather data")
     return 

def restaurant(city): 

