from logging import exception

from file_manager import load_data, save_data


class User:
    def __init__(self):
        self.users = load_data("dataStorage/users.json")
        self.current_user = None

    def register(self):
        print("\n--- Register a New Account ---")
        username = input("Enter username: ")

        for user in self.users:
            if user['username'] == username:
                raise ValueError("Username is already taken")


        password = input("Enter password: ")

        self.users.append({"username": username, "password": password})
        save_data("dataStorage/users.json", self.users)
        print("✅ Registration successful! You can now log in. ✅")

    def login(self):
        print("\n--- Login ---")
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in self.users:
            if user['username'] == username and user['password'] == password:
                self.current_user = username
                print(f" Welcome to RecipeFit, {username}!")
                return True
        else:
            raise ValueError("Invalid username or password.")


user1 = User()

