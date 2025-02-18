from Person import Person
from Classes import Course
from files_handelers import FilesHandlers


class Student(Person, Course):
    def __int__(self, courses: dict, account_balance: float):
        self.__courses = courses
        self.__account_balance = account_balance

    def set_number_of_course(self, courses):
        self.__coursese= courses

    def set_account_balance(self, account_balance):
        courses_cost = Course.get_price_per_class() * len(self.__courses)

    def add_student_details(self, per_id, number_of_course: int, account_balance: float):
        '''try:
            with open ()
        if (student_id)'''
    def registered_courses(self, crn):
        FilesHandlers.add_to_file("Student.json")

