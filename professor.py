#to set the Professor Class as child class to the person, courses and FilesHandlers
from Person import Person
from Classes import Course
from files_handelers import FilesHandlers


class Professor(Person, Course, FilesHandlers):
    def __int__(self, number_of_teaching_course: int, salary: float):

        self.__number_of_teaching_course = number_of_teaching_course
        self.__salary = salary

    ########### Setters ##############

    def set_number_of_course(self, number_of_course):
        self.__number_of_course = number_of_course

    def set_salary(self, salary: float):
        salary = self.__number_of_teaching_course * 100

    ########### Getters ##############

    def get_number_of_course(self):
        return self.__number_of_teaching_course

    def get_salary(self):
        return self.__number_of_teaching_course

    def add_professor(self):

        FilesHandlers.add_to_file("Professor.Json")
