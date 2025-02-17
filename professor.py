#to set the Professor Class as child class to the person, courses and FilesHandelers
from Person import Person
from Classes import Course
from files_handelers import FilesHandelers


class Professor(Person,Course, FilesHandelers):
    def __int__(self,prof_id: int, number_of_course: int, salary: float):
        self.__prof_id = prof_id
        self.__number_of_course = number_of_course
        self.__salary = salary

    ########### Setters ##############
    def set_student_id(self,student_id):
        self.__student_id = student_id

    def set_number_of_course(self, number_of_course):
        self.__number_of_course = number_of_course

    def set_salary(self, salary: float):
        salary = self.__number_of_course * 100

    ########### Getters ##############
    def get_student_id(self):
        return self.__student_id

    def get_number_of_course(self):
        return self.__number_of_course

    def get_salary(self):
        return self.__number_of_course

    def add_professor(self):

        FilesHandelers.add_to_file("Professor.Json")
