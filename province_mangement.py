
import json
from config import PROVINCE
province_list=[]
def load_province():
    try:
        with open(PROVINCE, "r", encoding="utf-8") as json_file:
            #content = file.read()
            #return json.loads(content)
            return json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 
    
def add_province(province_list:list,new_province:str):
    province_list.append(new_province)
    update_province(province_list)

def update_province(province_list:list):
    with open(PROVINCE, "w", encoding="utf-8") as json_file:
        json.dump(province_list, json_file, indent=4)

def delete_province(province_list:list,province_id:int):
    province_list.pop(province_id-1)
    update_province(province_list)

def get_all_provinces(privince_list:list):
    for index,province in enumerate(privince_list,start=1):
        print(f"{index} - {province}")

