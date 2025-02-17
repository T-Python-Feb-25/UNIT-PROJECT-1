from datetime import datetime,date,time
from Student import Student
from files_handelers import FilesHandelers


# class to handel all the functions related to the univirsity courses
class Course(FilesHandelers):

    #function to initiate the class
    def __int__(self, course_name: str, crn: str,start_date: date, end_date: date, start_time: time, end_time: time,
                price_per_class:float, number_of_students: int):
        self.__course_name = course_name
        self.__crn = crn
        self.__start_date = start_date
        self.__end_date = end_date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__price_per_class= price_per_class
        self.__number_of_students=number_of_students

    ################### Setters ############################
    #function to set the name of the course
    def set_course_name(self, course_name: str):
        self.__course_name = course_name

    #function to set the Course registration number
    def set_crn(self, crn: str):
        self.__crn = crn

    #function to set the Section number
    """"def set_section(self, section: str):
        self.__section = section""""

    #function to set the Starting date of the class
    def set_start_date(self, start_date: str):
        self.__start_date = start_date

    # function to set the end date of the class
    def set_end_date(self,end_date:str):
        self.__end_date = end_date

    # function to set the Starting time of the class
    def set_start_time(self,start_time:time):
        self.__start_time = start_time

    # function to set the end time of the class
    def set_end_time(self, end_time: str):
        self.__end_time = end_time

    def set_price_per_class(self, price_per_class):
        self.__price_per_class = price_per_class

    def set_number_of_students(self,number_of_students):
        self.__number_of_students = number_of_students

    ########################## Getters ###################
    #function to return the Course name
    def get_name(self):
        return self.__name

    #function to return the Course Registration number
    def get_crn(self):
        return self.__crn

    # function to return The course starting date
    def get_start_date(self):
        return self.__start_date

    # function to return The course end date
    def get_end_date(self):
        return self.__end_date

    # function to return The course starting time
    def get_start_time(self):
        return self.__start_time

    # function to return The course end date
    def get_end_time(self):
        return self.__end_time

    def get_price_per_class(self):
        return self.__price_per_class

    def get_number_of_students(self):
        return self.__number_of_students
