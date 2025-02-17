
'''from Classes import Course
from Person import Person
from Student import Student
from professor import Professor
'''
def login(choice):
    try:
        user_id = int(input("Enter Your ID number "))

        if choice.upper() == 'S':
            print("welcome Students")
        if choice.upper() == 'A':
            print("welcome Admin")

        if choice.upper() == "P":
            print("welcome Professor")
            print ("What would you like to do today?")
            print ("(1) Add")
            print ("(2) Modify/update")
            print ("(3) Delet")
            user_choice=int(input("choose one from the Previous lest"))
            if user_choice==1: 
                add_record()
    except ValueError:
        print ("You have entered a wrong value")

def add_record()
 user_choice=str(input ("Who would you like to add? \'S\' for Students, \'P\'for Professor OR \'C'\ for Courses"))
                if user_choice.upper()=='S':
                    print ("Welcome to the Students Add menue")()

def main():


    while True:
        choice = (input("Are you a Student \'S\', Professor\'P\' or Admin\'A\'?"))
        if choice.upper()!="e":
            login(choice)
        if choice.upper() == "E":
            print ("Thak you for using the uni App")
            break







main()