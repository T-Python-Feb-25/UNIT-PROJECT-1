from Person import Person
from typing import List, Dict, Any
from datetime import datetime


#This is the students class
class Student(Person):
    """Represents a student with additional details like courses and balance."""

    # to Initiate the Students Class
    def __init__(self, name: str, mem_id: str, dob: datetime, address: Dict[str, str], courses: List[str],
                 balance: float) -> None:
        super().__init__(name, mem_id, dob, address)
        self.__courses = courses
        self.__balance = balance

    # Function to set the dictionary with all the students information
    def to_dict(self) -> Dict[str, Any]:
        """Convert the student object to a dictionary."""
        person_dict = super().to_dict()
        person_dict.update({
            "Courses": self.__courses,
            "Balance": self.__balance
        })
        return person_dict

    # Function to get the courses the students has registered
    @property
    def courses(self) -> List[str]:
        return self.__courses

    # Function to get the balance of the studnt account
    @property
    def balance(self) -> float:
        return self.__balance


'''
This is the Students Class for University Application
By Mohammed Albushaier
Feb 24,2025
'''