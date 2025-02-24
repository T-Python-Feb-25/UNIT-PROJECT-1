from FileHandeler import FileHandler
from datetime import datetime
from typing import Dict, Any


# to Handel all the common details between the Students And Employees cclass
class Person(FileHandler):
    """Represents a person with basic details."""

    #initate the person class
    def __init__(self, name: str, mem_id: str, dob: datetime, address: Dict[str, str]) -> None:
        super().__init__("persons.json")
        self.__name = name
        self.__mem_id = mem_id
        self.__dob = dob
        self.__address = address

    # to set the dictionary with the Base information details for the Employees and Students classes
    def to_dict(self) -> Dict[str, Any]:
        """Convert the person object to a dictionary."""
        return {
            "Name": self.__name,
            "ID": self.__mem_id,
            "DOB": self.__dob.isoformat(),
            "Address": self.__address
        }

    #Function to get the name
    @property
    def name(self) -> str:
        return self.__name

    # Function to get the member id
    @property
    def mem_id(self) -> str:
        return self.__mem_id

    # Function to get the date of birth
    @property
    def dob(self) -> datetime:
        return self.__dob

    # Function to get the address as a list
    @property
    def address(self) -> Dict[str, str]:
        return self.__address


'''
This is the Person class for University Application
By Mohammed Albushaier
Feb 24,2025
'''