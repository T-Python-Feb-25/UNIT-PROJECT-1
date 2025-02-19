from colorama import Fore
from book_management import *
from member_management import *
from art import text2art

def show_menu():
    art = text2art("Welcome to the Library Management System",font ='cybermedium')
    print(Fore.LIGHTCYAN_EX + art)
    print(Fore.RESET)
    print("1. Add a new book")
    print("2. Remove a book")
    print("3. List all book")
    print("4. Search for a book")
    print("5. Update quantity")
    print("6. Add new member")
    print("7. Remove member")
    print("8. List member")
    print("9. Borrow a book ")
    print("10. return a book ")
    print("11. View borrowing history")
    print("12. Exit.")

while True:
    show_menu()
    print("")
    user_input = input("Choose option:")

    if user_input == "1":
        print("")
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
        print("")
        title = input("Enter the book title have been remove :")
        remove_book(title)

    elif user_input == "3" :
        print("")
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
        title = input("Enter the book title : ")
        while True:
            try:
                quantity = int(input("Enter the quantity : "))
                break
            except ValueError:
                print(Fore.RED + "Enter valid number in quantity" + Fore.RESET)
        update_quantity(title,quantity)
    
    elif user_input == "6":
        print("")
        name = input("Enter name member : ")
        add_member(name)

    elif user_input == "7":
        print("")
        name = input("Enter the member's name to remove: ")
        remove_member(name)

    elif user_input == "8":
        print("")
        list_member()

    elif user_input == "9":
        print("")
        member_name = input("Enter member name : ")
        book_name = input("Enter book title : ")
        borrow_book(member_name,book_name)
    
    elif user_input == "10":
        print("")
        member_name = input("Enter member name : ")
        book_name = input("Enter book title : ")
        return_book(member_name,book_name)

    elif user_input == "11":
        member_borrow = input("Enter member name :")
        view_borrowing(member_borrow)

    elif user_input == "12":
        print(Fore.GREEN + "Thank you for use Library Management System, Goodbye" + Fore.RESET)
        break
    else:
        print(Fore.RED + "Invalid choice! Please select a number between 1 and 12." + Fore.RESET)