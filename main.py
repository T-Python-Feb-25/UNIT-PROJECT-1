from colorama import Fore
from book_management import *
from member_management import *

def show_menu():
    print(Fore.GREEN + "Welcome to the Library Management System")
    print(Fore.RESET)
    print("1. Add a new book")
    print("2. Remove a book")
    print("3. List all book")
    print("4. Search for a book")
    print("5. Add new member")
    print("6. Remove member")
    print("7. List member")
    print("8. Exit.")

while True:
    show_menu()
    print("")
    user_input = input("Choose option:")

    if user_input == "1":
        title = input("Enter the book title : ")
        author = input("Enter the book author : ")
        category = input("Enter the book category : ")
        while True:
            try:
                quantity = int(input("Enter the quantity : "))
                break
            except ValueError:
                print(Fore.RED + "Enter valid number in quantity" + Fore.RESET)
            
        add_book(title,author,category,quantity)
        
    elif user_input == "2":
        title = input("Enter the book title have been remove :")
        remove_book(title)

    elif user_input == "3" :
        books = list_book()
        
    
    elif user_input == "4":
        print("")
        title = input("Enter the book title to search :")
        result = search_book(title)
        if result:
            print(Fore.GREEN + "Books found:" + Fore.RESET)
            print("")
            for book in result:
                print(f"{book['title']} -  {book['author']} -  {book['category']} - {book['quantity']} available")
        else:
            print(Fore.RED + "No books found matching your search." + Fore.RESET)
        print("")
    elif user_input == "5":
        print("")
        name = input("Enter name member : ")
        add_member(name)

    elif user_input == "6":
        print("")
        name = input("Enter the member's name to remove: ")
        remove_member(name)

    elif user_input == "7":
        list_member()

    elif user_input == "8":
        print(Fore.GREEN + "Thank you for use Library Management System, Goodbye" + Fore.RESET)
        break
    else:
        print(Fore.RED + "Invalid choice! Please select a number between 1 and 5." + Fore.RESET)