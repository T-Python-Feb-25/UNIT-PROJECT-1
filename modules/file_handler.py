import json,os
from user import User,Admin
from Event import Event
METADATA_PATH  = r"C:\Users\Mohamed\tuwaiq\projects\EventManagement\UNIT-PROJECT-1\data\metadata.json"
EVENTS_PATH = r"C:\Users\Mohamed\tuwaiq\projects\EventManagement\UNIT-PROJECT-1\data\events.json"
USERS_FILEPATH  = r"C:\Users\Mohamed\tuwaiq\projects\EventManagement\UNIT-PROJECT-1\data\users.json"

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
 
def add_user(email,username,password):
    try:
        users = list(load_file(USERS_FILEPATH))
        user = User(email,username,password)
        users.append(user.to_dict())
        save_file(users,USERS_FILEPATH)
        return user
    except Exception as e:
        print(f'In add_user : {e}') 
 
def add_event(title,presenter,location,date,time,seats=0):
    try:
        events = load_file(EVENTS_PATH)
        # *** convert JDON to event objects 
        list_events = [Event(**event_data) for event_data in events]
        admin =  Admin()
        event = Event(title,presenter,location,date,time,seats=seats)
        admin.add_event(event.to_dect())
        return event.get_id()
    except Exception as e:
        print(e)
 
def book_seat(event_id:str,username:str) -> bool:
    events = load_file(EVENTS_PATH)
    # *** convert JSON to event objects 
    list_events = [Event(**event_data) for event_data in events]
    #get the index of the booked event  
    for index,event in enumerate(list_events):
        if str(event.get_id()) == event_id:
            booked_event_index = index
            list_events[booked_event_index].book_seat(username)
            break
    else:
        return False
    # saving to file
    new_events = []
    for event in list_events:
        new_events.append(event.to_dect())
    save_file(new_events,EVENTS_PATH)
    return True


def cancel_seat(event_id,username):
    events = load_file(EVENTS_PATH)
    # *** convert JSON to event objects 
    list_events = [Event(**event_data) for event_data in events]
    #get the index of the booked event  
    for index,event in enumerate(list_events):
        # print(f"event: {str(event.get_id())}:{type(str(event.get_id()))} || {event_id}:{type(event_id)}")
        if str(event.get_id()) == event_id:
            cancel_booked_event_index = index
            list_events[cancel_booked_event_index].cancel_booking(username)
            break
    else:
        return False
    # saving to file
    new_events = []
    for event in list_events:
        new_events.append(event.to_dect())
    save_file(new_events,EVENTS_PATH)
    return True
    
 

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
    
