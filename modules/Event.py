from datetime import datetime
import utils
from Exceptions import *
class Event:
    last_id = 0
    def __init__(self, title, presenter, location, id="new", 
                start=None, end=None, seats=0,regester_users=[]):
        # generate ID if id = "new"
        self.__id = utils.generate_unique_id("event_id") if id == "new" else id
        self.__title = title
        self.__presenter = presenter 
        self.__location = location
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.__start = start if start else now
        self.__end = end if end else now
        self.__seats = self.set_seats(seats)
        self._regester_users = regester_users
        
    #getters
    def get_id(self):
        return self.__id
    def get_title(self):
        return self.__title
    def get_date(self):
        return f' {type(self.__start)} >> {self.__start}\n{self.__end}'
    def get_location(self):
        return self.__location
    def get_seats(self):
        return self.__seats
    def get_presentor(self):
        return self.__presenter
    
    #setters
    def set_seats(self,seats):
        if not isinstance(seats,int):
            raise Exception("Please provide an integer number for seats. ")
        if seats < 0:
            raise Exception("number of seat should be more than zero")
        self.__seats = seats
        return self.__seats
    # solving ...
    def book_seat(self,username):
        if username in self._regester_users:
            raise AllreadyBookedEvent("⚠️  You are already booked this event")
        if self.__seats - 1 >= 0:
            self.__seats -= 1 
            self._regester_users.append(username)
        else:
            raise EmptySeats(f"No availble seats of your request. Availble seats are:{self.get_seats()}")
    def cancel_booking(self,username):
        try:
            self.__seats += 1
            if username in self._regester_users:
                self._regester_users.remove(username)
                return self
        except Exception as e:
            print(e)
    #solving ...
    def set_datetieme(self,start,end):
        
        self.__start = start
        self.__end = end
    def to_dect(self):
        return   {
                'id':self.__id,
                "title" : self.__title,
                "presenter" : self.__presenter,
                "location" : self.__location,
                "start" : self.__start,
                "end": self.__end,
                "seats" : self.__seats,
                "regester_users" : self._regester_users
            }
    def to_dect2(self):
        return   {
                'id':self.__id,
                "title" : self.__title,
                "presenter" : self.__presenter,
                "location" : self.__location,
                "date" : {self.__start},
                "time": {self.__end},
                "seats" : self.__seats,
                "regester_users" : self._regester_users
            }
    def display_event(self):
        print(f"---\nID: {self.__id}\ntitle: {self.__title}\npresentor: {self.__presenter}\ndate start: {self.__start}\nuntil:{self.__end}\n location: {self.__location}\n seats: {self.__seats}\n---\n")
        
        
