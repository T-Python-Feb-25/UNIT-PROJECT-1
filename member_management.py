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
    
    for books in data['books']:
        if books['title'].lower() == title.lower():
            return books
    return None



def add_member(name):
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

def remove_member(name):
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
        list: A list of dictionaries containing members details.
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

