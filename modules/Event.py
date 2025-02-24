from datetime import datetime
from utils import generate_unique_id,USERS_FILEPATH,EVENTS_PATH,METADATA_PATH
from Exceptions import *
class Event:
    def __init__(self, title, description, location,date,time, 
                 id="new",  seats=0,regester_users=[]):
        # generate ID if id = "new"
        self.__id = generate_unique_id("event_id") if id == "new" else id
        self.__title = title
        self.__description = description 
        self.__location = location
        self.__date = date
        self.__time = time
        self.__seats = self.set_seats(seats)
        self.__regester_users = regester_users
        
    #getters
    def get_id(self):
        return self.__id
    def get_title(self):
        return self.__title
    def get_date(self):
        return f' {type(self.__date)} '
    def get_location(self):
        return self.__location
    def get_seats(self):
        return self.__seats
    def get_presentor(self):
        return self.__description
    
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
        if username in self.__regester_users:
            raise AllreadyBookedEvent("⚠️  You are already booked this event")
        if self.__seats - 1 >= 0:
            self.__seats -= 1 
            self.__regester_users.append(username)
        else:
            raise EmptySeats(f"No availble seats of your request. Availble seats are:{self.get_seats()}")
    def cancel_booking(self,username):
        try:
            self.__seats += 1
            if username in self.__regester_users:
                self.__regester_users.remove(username)
                return self
        except Exception as e:
            print(e)
 
    def to_dect(self):
        return   {
                'id':self.__id,
                "title" : self.__title,
                "description" : self.__description,
                "location" : self.__location,
                "date": {
                    "start_date": self.__date['start_date'],
                    "end_date": self.__date['end_date']
                },
                "time": {
                    "start_time": self.__time['start_time'],
                    "end_time": self.__time['end_time']
                },
                "seats" : self.__seats,
                "regester_users" : self.__regester_users
            }
    def display_event(self):
        print(f"---\nID: {self.__id}\ntitle: {self.__title}\npresentor: {self.__description}\ndate start: {self.__start}\nuntil:{self.__end}\n location: {self.__location}\n seats: {self.__seats}\n---\n")
        
        
