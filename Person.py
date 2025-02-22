from FileHandeler import FileHandler
from datetime import datetime
from typing import Dict, Any


class Person(FileHandler):
    """Represents a person with basic details."""

    def __init__(self, name: str, mem_id: str, dob: datetime, address: Dict[str, str]) -> None:
        super().__init__("persons.json")
        self.__name = name
        self.__mem_id = mem_id
        self.__dob = dob
        self.__address = address

    def to_dict(self) -> Dict[str, Any]:
        """Convert the person object to a dictionary."""
        return {
            "Name": self.__name,
            "ID": self.__mem_id,
            "DOB": self.__dob.isoformat(),
            "Address": self.__address
        }

    @property
    def name(self) -> str:
        return self.__name

    @property
    def mem_id(self) -> str:
        return self.__mem_id

    @property
    def dob(self) -> datetime:
        return self.__dob

    @property
    def address(self) -> Dict[str, str]:
        return self.__address

