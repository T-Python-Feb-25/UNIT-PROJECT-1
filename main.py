from colorama import Fore
from book_management import *

def show_menu():
    print(Fore.GREEN + "Welcome to the Library Management System")
    print(Fore.RESET)
    print("1. Add a new book")
    print("2. remove a book")
    print("3. Exit.")

while True:
    show_menu()
    user_input = input("Choose option:")

    if user_input == "1":
        title = input("enter the book title : ")
        author = input("enter the book author : ")
        category = input("enter the book category : ")
        while True:
            try:
                quantity = int(input("enter the quantity : "))
                break
            except ValueError:
                print(Fore.RED + "enter valid number in quantity")
                print(Fore.RESET)
            
        add_book(title,author,category,quantity)
        
    elif user_input == "2":
        title = input("enter the book title have been remove :")
        remove_book(title)
    
    elif user_input == "3":
        print(Fore.GREEN + "Thank you for use Library Management System, Goodbye")
        print(Fore.RESET)
        break