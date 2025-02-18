from Classes import Course
from Person import Person
from Student import Student
from professor import Professor
from datetime import date
#import maskpass


def login(choice):
    try:
        user_id = int(input("Enter Your ID number "))
        #password = maskpass.askpass(prompt="Password:", mask="#")

        if choice.upper() == 'S':
            print("welcome Students")
        if choice.upper() == 'A':
            print("welcome Admin")
            print("Which record will you work on today ?")
            user_choice=str(input("(P) Professors\n (S) Students (C) Courses"))
            if user_choice.upper() == "P":
                print("What would you like to do today with the professors records?")
                print("(1) Add a professor?")
                print("(2) Modify/update professor record?")
                print("(3) Delete professor record?")
                user_choice = int(input("choose one from the Previous lest"))

            elif user_choice.upper() == "S":
                print("What would you like to do today with Students Records?")
                print("(1) Add a Students?")
                print("(2) Modify/update Student record?")
                print("(3) Delete Student record?")
                user_choice = int(input("choose one from the Previous lest"))
            elif user_choice.upper() == "C":
                print("What would you like to do today with Courses Records?")
                print("(1) Add a Course?")
                print("(2) Modify/update Courses record?")
                print("(3) Delete Course record?")
                user_choice = int(input("choose one from the Previous lest"))

        if choice.upper() == "P":
            print("welcome Professor")
            print ("What would you like to do today with your courses?")
            print ("(1) Add")
            print ("(2) Modify/update")
            print ("(3) Delete")
            user_choice = int(input("choose one from the Previous lest"))
            if user_choice == 1:
                add_record()
    except ValueError:
        print("You have entered a wrong value")


def add_record(user_choice):

    if user_choice.upper() == 'S':
        print("Welcome to the Students Add menu")
        fname = str(input("Enter student first name "))
        lname = str(input("Enter student first name"))
        dob = date(input("The students date of birth as (yyyy,mm,dd): "))
        city = str(input("Enter City: "))
        country = str(input("Enter Country: "))
        zip_code = str(input("Enter Zip Code: "))


def main():


    while True:
        choice = (input("Are you a Student \'S\', Professor\'P\' or Admin\'A\'?"))
        if choice.upper() != "E":
            login(choice)
        if choice.upper() == "E":
            print ("Thank you for using the Uni App")
            break







main()