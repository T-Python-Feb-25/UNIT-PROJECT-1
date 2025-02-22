from Person import Person
from typing import List, Dict, Any
from datetime import datetime


class Student(Person):
    """Represents a student with additional details like courses and balance."""

    def __init__(self, name: str, mem_id: str, dob: datetime, address: Dict[str, str], courses: List[str],
                 balance: float) -> None:
        super().__init__(name, mem_id, dob, address)
        self.__courses = courses
        self.__balance = balance

    def to_dict(self) -> Dict[str, Any]:
        """Convert the student object to a dictionary."""
        person_dict = super().to_dict()
        person_dict.update({
            "Courses": self.__courses,
            "Balance": self.__balance
        })
        return person_dict

    @property
    def courses(self) -> List[str]:
        return self.__courses

    @property
    def balance(self) -> float:
        return self.__balance

