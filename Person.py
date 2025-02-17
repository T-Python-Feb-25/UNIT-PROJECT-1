from datetime import date


class Person:

    def __int__(self, name: str, dob: date, address: dict):
        self.__name = name
        self.__dob = dob
        self.__address = address

    ########### Setters ##############
    def set_name(self, fname, lname):
        self.__name = fname+lname

    def set_dob(self, dob:date):
        self.__dob = dob

    def set_address(self, city: str, country: str, zip_code: str):
        self.__address = {"city": city,
                          "country": country,
                          "zip_code": zip_code}

    ########### Getters ##############
    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_address(self):
        return self.__address

    

