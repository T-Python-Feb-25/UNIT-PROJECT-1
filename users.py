
from file_manager import load_data, save_data
from colorama import Fore,Back

class User:
    def __init__(self):
        self.users = load_data("dataStorage/users.json")
        self.current_user = None

    def register(self):
        """
        Registers a new user account by asking for a username and password.
        Parameters:
            None
        Returns:
            None: If registration is successful, the user is added to the users list and saved to a file.
                  If the username already exists, a ValueError is raised.
        """
        print(Fore.YELLOW + "=" * 40)
        print(Fore.GREEN+"--- Register a New Account ---")
        print(Fore.YELLOW + "=" * 40)

        username = input(Fore.LIGHTBLUE_EX+"Enter username: ")

        for user in self.users:
            if user['username'] == username:
                raise ValueError(Fore.RED+"Username is already taken")


        password = input(Fore.LIGHTBLUE_EX+"Enter password: ")

        self.users.append({"username": username, "password": password})
        save_data("dataStorage/users.json", self.users)
        print(Fore.GREEN+"Registration successful! You can now log in.")

    def login(self):
        """
        Logs in a user by verifying their username and password.
        Parameters:
            None
        Returns:
            bool: Returns True if login is successful and sets `current_user` to the username.
        """
        print(Fore.YELLOW+"=" * 40)
        print(Fore.GREEN+"--- Login ---")
        print(Fore.YELLOW+"=" * 40)

        username = input(Fore.LIGHTBLUE_EX+"Enter username: ")
        password = input(Fore.LIGHTBLUE_EX+"Enter password: ")

        for user in self.users:
            if user['username'] == username and user['password'] == password:
                self.current_user = username
                print(Fore.LIGHTCYAN_EX + "=" * 40)
                print(Fore.LIGHTMAGENTA_EX + f"Welcome to RecipeFit! {username}")
                print(Fore.LIGHTCYAN_EX + "=" * 40)
                return True
        else:
            raise ValueError(Fore.RED+"Invalid username or password.")



