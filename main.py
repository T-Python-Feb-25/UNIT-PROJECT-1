from colorama import Fore
from book_management import *
from member_management import *
from art import text2art
from tabulate import tabulate

def show_menu():
    art = text2art("Welcome to the Library Management System",font ='cybermedium')
    print(Fore.LIGHTCYAN_EX + art + Fore.RESET)
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
    user_input = input("Choose option:").strip()

    if user_input == "1":
        print("")
        title = input("Enter the book title : ").strip()
        author = input("Enter the book author : ").strip()
        category = input("Enter the book category : ").strip()
        while True:
            try:
                quantity = int(input("Enter the quantity : "))
                if quantity <= 0:
                    print(Fore.RED + "Quantity cannot be negative or zero. Please enter a valid number." + Fore.RESET)
                else:
                    break
            except ValueError:
                print(Fore.RED + "Enter valid number in quantity" + Fore.RESET)
            
        add_book(title,author,category,quantity)
        
    elif user_input == "2":
        list_book()
        print("")
        id = int(input("Enter the book title have been remove :"))
        remove_book(id)

    elif user_input == "3" :
        print("")
        list_book()
        
    
    elif user_input == "4":
        print("")
        while True:
            search = input("What would you like to search by? (title/author/category)").strip().lower()
            if search in ["title", "author", "category"]:
                break
            else:
                print(Fore.RED + "Invalid search option. Please choose 'title', 'author', or 'category'." + Fore.RESET)
            
        if search == "title":
            title = input("Enter the book title to search: ").strip()
            result = search_book(title)
        elif search == "author":
            author = input("Enter the author's name to search: ").strip()
            result = search_book(author)
        elif search == "category":
            category = input("Enter the category to search: ").strip()
            result = search_book(category)
        
        table_data = []
        
        if result:
            print(Fore.GREEN + "Books found:" + Fore.RESET)
            print("")
            for book in result:
                table_data.append([book['id'],book['title'],book['author'],book['category'],book['quantity']])
            headers = ["id","Title","Author","Category","quantity"]
            print(tabulate(table_data,headers=headers,tablefmt="double_grid"))
        else:
            print(Fore.RED + "No books found matching your search." + Fore.RESET)
        print("")
    
    elif user_input == "5":
        print("")
        list_book()
        title = int(input("Enter the book id : "))
        while True:
            try:
                quantity = int(input("Enter the quantity : "))
                if quantity < 0:
                    print(Fore.RED + "Quantity cannot be negative. Please enter a valid number." + Fore.RESET)
                else:
                    break
            except ValueError:
                print(Fore.RED + "Enter valid number in quantity" + Fore.RESET)
        update_quantity(title,quantity)
    
    elif user_input == "6":
        print("")
        name = input("Enter full name member : ").strip()
        add_member(name)

    elif user_input == "7":
        print("")
        list_member()
        name = input("Enter the member's name to remove: ").strip()
        remove_member(name)

    elif user_input == "8":
        print("")
        list_member()

    elif user_input == "9":
        print("")
        member_name = input("Enter member name : ").strip()
        list_book()
        book_id = int(input("Enter book id : "))
        borrow_book(member_name,book_id)
    
    elif user_input == "10":
        print("")
        member_name = input("Enter member name : ").strip()
        view_borrowing(member_name)
        book_id = int(input("Enter book id : "))
        return_book(member_name,book_id)

    elif user_input == "11":
        print("")
        member_borrow = input("Enter member name :").strip()
        view_borrowing(member_borrow)

    elif user_input == "12":
        print(Fore.GREEN + "Thank you for use Library Management System, Goodbye" + Fore.RESET)
        break
    else:
        print(Fore.RED + "Invalid choice! Please select a number between 1 and 12." + Fore.RESET)
