from utils import *
class User:
    def __init__(self,email,username,password,id='new',role='user'):
        self._role = role
        self._id = generate_unique_id("user_id") if id == "new" else id
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
        self._id = generate_unique_id("admin_id") if id == "new" else id
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
        import file_handler 
        events = list(file_handler.load_file(file_handler.EVENTS_PATH))
        events.append(event)
        file_handler.save_file(events,file_handler.EVENTS_PATH)
        # testing
    def add_event2(title,presenter,location,date,time,seats=0):
        import file_handler as f
        import Event
        try:
            events = list(f.load_file(EVENTS_PATH)) 
            list_events = [Event(**event_data).to_dect() for event_data in events]
            event = Event(title,presenter,location,date,time,seats=seats)
            list_events.append(event.to_dect())
            f.save_file(events,EVENTS_PATH)
        except Exception as e:
            print(e)
            
        
        
        
    def delete_event(self,event_id):
        import file_handler
        event_id = int(event_id)
        event_index = None
        deleted_event = None
        events = list(file_handler.load_file(file_handler.EVENTS_PATH))
        for index,event in enumerate(events):
            if event_id == event['id']:
                event_index = index
                deleted_event = events.pop(event_index)
                file_handler.save_file(events,file_handler.EVENTS_PATH)
                # print(f"Event {deleted_event['id']} is Deleted. ")
                break
        return deleted_event
    def edit_event(self,new_data:list,event):
        pass
        
        