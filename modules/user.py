import file_handler 
from setteings import *
class User:
    def __init__(self,email,username,password,id='new',role='user'):
        self._role = role
        self._id = file_handler.generate_unique_id("user_id") if id == "new" else id
        self._email = email
        self._username = username
        self._password = password
    def to_dict(self):
        return {
            "id":self._id,
            "role":self._role,
            "email":self._email,
            "username":self._username,
            "password":self._password
        }
    def get_id(self):
        return self._id
    def set_email(self):
        pass
class Admin(User):
    def __init__(self,email='admin@admin.com',username='admin', password='dadmin',id='new',role='admin'):
        self._id = file_handler.generate_unique_id("admin_id") if id == "new" else id
        self.__role = 'admin'
        super().__init__(email,username, password,id=self._id)
    
    def to_dict(self):
        return {
            "id":self._id,
            "role":self.__role,
            "email":self._email,
            "username":self._username,
            "password":self._password
        }
    def add_event(self,event):
        events = list(file_handler.load_file(EVENTS_PATH))
        events.append(event)
        file_handler.save_file(events,EVENTS_PATH)
        
    def delete_event(self,event_id):
        event_id = int(event_id)
        event_index = None
        deleted_event = "No deleted event"
        events = list(file_handler.load_file(EVENTS_PATH))
        for index,event in enumerate(events):
            if event_id == event['id']:
                event_index = index
                deleted_event = events.pop(event_index)
                file_handler.save_file(events,EVENTS_PATH)
                print(f"Event {deleted_event['id']} is Deleted. ")
                break
        return deleted_event
    def edit_event(self):
        pass
        