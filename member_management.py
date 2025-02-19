from data_handler import load_data,save_data
from colorama import Fore

def find_member(name:str):
    """
    This function checks if the member exists or not.

    args:
        name(str): Name of the member you are looking for
    returns:
    dict or None: The member data if found, otherwise None.
    """
    data = load_data()
    
    for member in data['members']:
        if member['name'].lower() == name.lower():
            return member
    return None

def find_book(title:str):
    """
    This function checks if the book exists or not.

    args:
        title(str): Name of the title you are looking for
    returns:
    dict or None: The book data if found, otherwise None.
    """
    data = load_data()
    
    for book in data['books']:
        if book['title'].lower() == title.lower():
            return book
    return None



def add_member(name:str):
    """
    This function is used to add new member.
    
    args:
        name(str): Name of the member 
    returns:
    bool: True if the member was added, False if the member already exists
    """
    data = load_data()

    if find_member(name):
        print(Fore.RED + f"Member '{name}' already exists!" + Fore.RESET)
        return
    
    new_member = {
        "name" : name,
        "borrowed_books" : []
    }

    data['members'].append(new_member)
    save_data(data)
    print(Fore.GREEN + f"Member '{name}' added successfully!" + Fore.RESET)

def remove_member(name:str):
    """
    This function is used to remove a member.

    args:
        name(str): the name of member need remove.
    returns:
        bool: True if the user was removed, False if the user was not found.
    """
    data = load_data()
    member = find_member(name)

    if member:
        data['members'].remove(member)
        save_data(data)
        print(Fore.GREEN + f"Member '{name}' has been remove successfully!" + Fore.RESET)
    else:
        print(Fore.RED + f"Member '{name}' not found!" + Fore.RESET)

def list_member():
    """
    This function returns the list of members.

    returns:
        None. Prints the member names to the console.
    """
    data = load_data()
    members = data.get('members',[])
    if not members:
        print(Fore.RED + "No members found." + Fore.RESET)
    else:
        print(Fore.GREEN + "Registered Members:" + Fore.RESET)
        for member in members:
            print(f"{member['name']}")
    print("")

def borrow_book(member_name: str, title: str):
    """
    This function is used to borrow books.

    Args:
        member_name: The name of the member.
        title: The title of the book.
    returns:
        none
    """
    data = load_data()
    members = find_member(member_name)
    books = find_book(title)

    if not members:
        print(Fore.RED + "Member not found!" + Fore.RESET)
        return
    if not books:
        print(Fore.RED + "Book not found!" + Fore.RESET)
        return
    if books['quantity'] <= 0:
        print(Fore.RED + "The book is currently unavailable!" + Fore.RESET)
        return
    if title in members['borrowed_books']:
        print(Fore.RED + f"You already borrowed the book '{title}'!" + Fore.RESET)
        return


    books['quantity'] -= 1

    members['borrowed_books'].append(title)

    for book in data['books']:
        if book['title'] == title:
            book['quantity'] = books['quantity']

    for member in data['members']:
        if member['name'].lower() == member_name.lower():
            member['borrowed_books'] = members['borrowed_books']

    save_data(data)
    print(Fore.GREEN + f"'{title}' has been borrowed by {member_name}." + Fore.RESET)

def return_book(member_name:str ,title:str):
    """
    This function is used to return borrowed books.

    Args:
        member_name: The name of the member.
        title: The title of the book.
    Returns:
        None.
    """
    data = load_data()
    members = find_member(member_name)
    books =  find_book(title)

    if not members:
        print(Fore.RED + "Member not found!" + Fore.RESET)
        return
    if title not in members['borrowed_books']:
        print(Fore.RED + f"{member_name} has not borrowed '{title}'!" + Fore.RESET)
        return
    
    books['quantity'] += 1
    members['borrowed_books'].remove(title)
    for book in data['books']:
        if book['title'] == title:
            book['quantity'] = books['quantity']

    for member in data['members']:
        if member['name'].lower() == member_name.lower():
            member['borrowed_books'] = members['borrowed_books']
    
    save_data(data)
    print(Fore.GREEN + f"'{title}' has been returned successfully!" + Fore.RESET)

def view_borrowing(member_name):
    """
    This function is used to display the borrowed books of the user.
    
    Args:
        member_name: The name of the member.
    Returns:
        None.
    """
    member = find_member(member_name)

    if not member:
        print(Fore.RED + f"Member '{member_name}' not found!" + Fore.RESET)
        return
    
    if member['borrowed_books']:
        print(Fore.GREEN + f"\n📖 {member_name}'s Borrowing History:" + Fore.RESET)
        for book in member['borrowed_books']:
            print(f"- {book}")
    else:
        print(Fore.RED + f"No borrowing history found for {member_name}." + Fore.RESET)