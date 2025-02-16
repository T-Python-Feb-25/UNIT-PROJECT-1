from datetime import datetime
from Classes import Course
import json
import os


class FilesHandelers(Course):
    def __int__(self,  file_name: str):
        self.__file_name=file_name

    def set_file_name(self, file_name: str):
        self.__file_name = file_name

    def get_file_name(self):
        return self.__file_name

    def add_to_file(self, file_name: str):
        if file_name == "Corses.jason":
            courses = self._read_accounts_file()
        # Check if account already exists
            for course in courses:
                if course["CRN"] == self.__crn:
                    print("The course already exists.")
                    return
            # Add new account
            course.append({
                "name": self.__course_name,
                "CRN": self.__crn,
                "start_date": self.__start_date,
                "end_date": self.__end_date,
                "start_time": self.__start_time,
                "end_time": self.__endtime
            })
            self._write_accounts_file(courses)

    def _write_accounts_file(self, file_name: str):
        with open(f"{file_name}.json", "w", encoding="UTF-8") as f:
            for f"{file_name}" in accounts:
                f.write(json.dumps(account) + "\n")