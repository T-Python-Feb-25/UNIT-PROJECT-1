from modules.Event import Event
from modules.user import *
import file_handler
USERS_FILEPATH  = r"C:\Users\Mohamed\tuwaiq\projects\EventManagement\UNIT-PROJECT-1\data\users.json"
EVENTS_PATH = r"C:\Users\Mohamed\tuwaiq\projects\EventManagement\UNIT-PROJECT-1\data\events.json"


def test2():
    events = file_handler.load_file()

    
    # *** convert JDON to event objects 
    input("continue ... ")
    list_events = [Event(**event_data) for event_data in events]
    for event in list_events:
        event.display_event()



def add_event():
    admin =  Admin()
    event = Event("event 5","mohammed","riyadh",seats=50)
    admin.add_event(event.to_dect())

def add_admin():
    users = list(file_handler.load_file(USERS_FILEPATH))
    admin = Admin(username="admin3")
    users.append(admin.to_dict())
    file_handler.save_file(users,USERS_FILEPATH)

def add_user():
    users = list(file_handler.load_file(USERS_FILEPATH))
    user = User("khalid@gmail.com","khalid","123123")
    users.append(user.to_dict())
    file_handler.save_file(users,USERS_FILEPATH)

def delete_event():
    admin = Admin()
    admin.delete_event(84)

def display():
    users = file_handler.load_file(USERS_FILEPATH)
    events = file_handler.load_file(EVENTS_PATH)
    # *** convert JDON to event objects 
    list_events = [Event(**event_data) for event_data in events]
    list_users = [User(**user_data) for user_data in users]
    print(f"Events({len(list_events)})")
    for event in list_events:
        print(event.to_dect())
    print(f"Users({len(list_users)}): ")
    for user in list_users:
        print(user.to_dict())

def book_seat(event_id,user_id):
    users = file_handler.load_file(USERS_FILEPATH)
    events = file_handler.load_file(EVENTS_PATH)
    # *** convert JDON to event objects 
    list_events = [Event(**event_data) for event_data in events]

    #test 
    list_events[-1].book_seat(user_id)
    # saving to file
    new_events = []
    for event in list_events:
        new_events.append(event.to_dect())
    print(new_events)
    file_handler.save_file(new_events,EVENTS_PATH)

add_event()
