from Person import Person
from Classes import Course
from files_handelers import FilesHandelers


class Student(Person, Course):
    def __int__(self, student_id: int, number_of_course: int, account_balance: float):
        self.__student_id = student_id
        self.__number_of_course = number_of_course
        self.__account_balance = account_balance

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_number_of_course(self,number_of_course):
        self.__number_of_course= number_of_course

    def set_account_balance(self,account_balance):
        courses_cost = Course.get_price_per_class() * self.__number_of_course

    def add_student_details(self, student_id: int, number_of_course: int, account_balance: float):
        '''try:
            with open ()
        if (student_id)'''
    def registerd_courses(self, crn):



        FilesHandelers.add_to_file("Student.json")

