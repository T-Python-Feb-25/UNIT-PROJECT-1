from data_handler import load_data,save_data
from colorama import Fore

def add_book(title:str,author:str,category:str,quantity:int):
    """
    This function is used to add books to the library.

    args:
        title(str): the title of the book.
        author(str): the author of the book.
        category(str): the category of the book.
        quantity(int) : Quantity of books available
    returns:
        bool: True if the book was added, False if the book already exists
    """
    data = load_data()
    for book in data['books']:
        if book['title'] == title:
            print(f"the book {title} is already exists in the library.")
            return

    data['books'].append({
        "title" : title,
        "author" : author,
        "category" : category,
        "quantity" : quantity
    })
    print(Fore.GREEN + "Book Added.")
    print(Fore.RESET)
    save_data(data)

def remove_book(title):
    """
    This function is used to remove a book in the library.

    args:
        title(str): the title of the book to be removed.
    returns:
        bool: True if the book was removed, False if the book was not found.
    """
    data = load_data()
    
    for book in data['books']:
        if book['title'] == title:
            data['books'].remove(book)
            save_data(data)
            print(Fore.GREEN + f"the book {title} is has been removed successfully!")
            print(Fore.RESET)
            break
    else:
        print(Fore.RED + "The book was not found in the library.")
        print(Fore.RESET)
