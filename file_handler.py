import json,os
from setteings import *

def load_file(filepath):
    """loading from a file and return what is in the file 

    Args:
        filepath (the path of the file , default it will be events.json): _description_. Defaults to EVENTS_DB_PATH.

    Returns:
        list or dict : _what is i the file
    """
    try:
        # create file and put epmty list if deosnt exsist 
        if not os.path.exists(filepath):
            with open(filepath, "w") as file:
                json.dump( [] , file)
        with open(filepath,"r") as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except FileNotFoundError:
        print("File not found.")
    
def add_to_file(data,filepath):
    loaded_data = list(load_file(filepath))
    loaded_data.append(data)
    try:
        with open(filepath,"w") as file:
            json.dump(loaded_data,file,indent=4)
    except Exception as e:
        print(e)

def save_file(new_data,filepath):
    try:
        with open(filepath,"w") as file:
            json.dump(new_data,file,indent=4)
    except Exception as e:
        print(e)
    
def generate_unique_id(name,type=0,file_path=METADATA_PATH):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump({name: 0}, file)

    with open(file_path, "r+") as file:
        data = dict(json.load(file))
        if name not in data:
            data[name] = 0  
        data[name] += 1
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    return data[name]    
 
 

# def list_events():
#     events = dict(load_events())
#     for id,value in events:
#         print(f'{id} **** \n {value} ')
# def event_to_dict(event):
#     return {
#         event.get_id():
#         {
#             "date" : event.get_date(),
#             "location" : event.get_location(),
#             "seats" : event.get_seats()
#         }
#     }
    
