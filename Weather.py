'''This file was created to fetch weather 
information in the city selected by the user and
 at the time specified by him.'''

import json
import datetime as dt
import requests

base_url= "http://api.openweathermap.org/data/2.5/weather?"
apiKey="2d57597160ec1cc3856f1cafd93ca85f"
url=base_url+"appid="+apiKey+"&q="+ city
response= requests.get(url).json

#دالة لجلب معلومات الطقس 
def get_weather(city, date):
    



