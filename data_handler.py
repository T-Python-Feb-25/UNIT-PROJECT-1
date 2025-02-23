import json


def load_data(file_name="library_data.json"):
    try:
        with open(file_name,'r',encoding="UTF-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {'books' : [] , 'members' : []}
    
def save_data(data,file_name="library_data.json"):
    with open(file_name,'w',encoding="UTF-8") as file:
        json.dump(data,file,ensure_ascii=False,indent=4)