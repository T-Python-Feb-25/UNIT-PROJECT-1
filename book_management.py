from data_handler import load_data,save_data
from colorama import Fore
from tabulate import tabulate

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

    new_id = 1
    if data['books']:
        max_id = 0
        for book in data['books']:
            max_id = book['id']
        new_id = max_id + 1

    for book in data['books']:
        if book['title'] == title:
            print(Fore.RED + f"the book {title} is already exists in the library." + Fore.RESET)
            return

    data['books'].append({
        "id" : new_id,
        "title" : title,
        "author" : author,
        "category" : category,
        "quantity" : quantity
    })
    print(Fore.GREEN + "Book Added." + Fore.RESET)
    save_data(data)

def remove_book(id:int):
    """
    This function is used to remove a book in the library.

    args:
        title(str): the title of the book to be removed.
    returns:
        bool: True if the book was removed, False if the book was not found.
    """
    data = load_data()
    
    for member in data['members']:
        for borrowed_book in member['borrowed_books']:
            if borrowed_book['id'] == id:
                print(Fore.RED + f"The book '{borrowed_book['title']}' is currently borrowed by a member. Please ask them to return it first." + Fore.RESET)
                return
    for book in data['books']:
        if book['id'] == id:
            data['books'].remove(book)
            break
    else:
        print(Fore.RED + "The book was not found in the library." + Fore.RESET)
    
    save_data(data)
    print(Fore.GREEN + f"the book {id} is has been removed successfully!"+ Fore.RESET)



def list_book():
    """
    This function returns the list of books in the library.

    returns:
        none. Prints the book details to the console.
    """
    data = load_data()
    books = data.get('books', [])
    
    if not books:
        print(Fore.RED + "No books available in the library." + Fore.RESET)
    else:
        print(Fore.GREEN + "The book available in Library :" + Fore.RESET)
        table_data = []
        for book in books:
            table_data.append([book['id'], book['title'],book['author'],book['category'],book['quantity']])
        headers = ["id","Title","Author","Category","quantity"]
        print(tabulate(table_data,headers=headers,tablefmt="double_grid"))
    print("")


def search_book(query:str):
    """
    This function searches for books in the library by title, author, or category.
    
    args:
        query(str): The search term entered by the user.
    returns:
        list: A list of books matching the search criteria.
    """
    data = load_data()
    result = []
    
    for book in data['books']:
        if book['title'].lower().startswith(query.lower()) or book['author'].lower().startswith(query.lower()) or book['category'].lower().startswith(query.lower()) :
            result.append(book)
    return result

def update_quantity (id:int,new_quantity:int):
    """
    This function updates the quantity of a specific book in the library.
    
    args:
        title (str): The title of the book to update.
        new_quantity (int): The new quantity of the book.
    returns:
        None.
    """
    data = load_data()
    for book in data['books']:
        if book['id'] == id:
            book['quantity'] = new_quantity
            save_data(data)
            print(Fore.GREEN + f"The quantity of '{book['title']}' has been updated to {new_quantity}." + Fore.RESET)
            return