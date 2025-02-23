
import json
from config import DATA

def load_data():
    try:
        with open(DATA, "r", encoding="utf-8") as json_file:
            content=json.load(json_file)
            return content['province'] ,content['prices'] 
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def update_data(province_list:dict,pricing_list:dict):
    with open(DATA, "w", encoding="utf-8") as json_file:
        content={
            "province":province_list,
            "prices":pricing_list
                }
        json.dump(content, json_file, indent=4)

def get_all_provinces(province_list:dict):
    for index,province, in enumerate(province_list,start=1):
        print(f"{index} - {province}")
    
def get_all_governorates(province_list:dict,province:str ):
    for index,governorate, in enumerate(province_list[province],start=1):
        print(f"{index} - {governorate}")
def get_all_prices(pricing_list:dict):
    for index,(title,cost) in enumerate(pricing_list.items(),start=1):
        print(f"{index} - {title} current price: {cost}")






