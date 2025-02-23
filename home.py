import msvcrt
import hashlib
import json
from admin.reminder import reminders_main

class User:
    def __init__(self, username, password, is_hashed=False):
        self.username = username
        # If password is not hashed, hash it before storing
        self.password = self.hash_password(password) if not is_hashed else password

    def hash_password(self, password):
        '''This function is used to hash the password using SHA-256 algorithm and return the hashed password as a hexadecimal string.'''
        return hashlib.sha256(password.encode()).hexdigest()

def custom_getpass(prompt='Password: ', mask='*'):
    '''This function is used to get the password from the user without showing it on the screen. 
    It uses msvcrt.getch() to get the input character by character and prints a mask symbol instead of the actual character. 
    The function returns the password entered by the user.'''
    print(prompt, end="", flush=True)
    password = ""
    while True:
        ch = msvcrt.getch()  # Get one character from the user input without showing it
        if ch == b'\r':  # Enter key is pressed (byte)
            break
        elif ch == b'\x08':  # Backspace is pressed
            if password:
                password = password[:-1]  # Remove last character from password if backspace is pressed
                print('\b \b', end="", flush=True)  # Remove last masked character on screen
        else:
            password += ch.decode('utf-8')  # Add the character to the password
            print(mask, end="", flush=True)  # Print mask symbol instead of the character
    print()  # Move to the next line
    return password

def register(users):
    '''This function is used to register a new user by taking the username and password as input from the user.
    It checks if the username already exists in the users dictionary and if not, it creates a new User instance with the hashed password.
    It then saves the user data to the 'logins.json' file and returns the updated users dictionary.'''
    username = input("Enter username: ")

    # Check if the username already exists in the users dictionary
    if username in users:
        print("Username already exists! Please choose a different username.")
        return users  # Return users without changes
    
    password = custom_getpass("Enter password: ")
    # Create a new User instance with the password hashed
    users[username] = User(username, password, is_hashed=False)

    try:
        # Save the user data to 'logins.json' file
        with open('logins.json', 'w') as file:
            json.dump({user.username: user.password for user in users.values()}, file)
        print("You have been registered successfully! Login to start using the VA.")
    except IOError as e:
        print(f"Error saving user data: {e}")

    return users

def login(users):
    '''This function is used to log in a user by checking the username and password entered by the user.
    It returns the updated users dictionary and the logged-in user object if the login is successful.
    If the login fails, it returns the users dictionary and None for the user object.'''
    while True:  # Keep asking for login until successful or user decides to exit
        username = input("Enter username: ")
        password = custom_getpass("Enter password: ")

        # Check if username exists and the password matches the hashed password
        if username in users and users[username].password == hashlib.sha256(password.encode()).hexdigest():
            print(f"You have logged in successfully! Welcome {username}")
            return users, users[username]
        else:
            print("Incorrect username or password.")
            password_reset_choice = input("Do you want to reset your password? (yes/no): ").strip().lower()
            if password_reset_choice == 'yes':
                password_reset(users, username)
                # After password reset, we want to allow the user to log in again
            elif password_reset_choice == 'no':
                print("Okay, try to login again")
                continue  # Keep the loop running to allow retrying the login
            else:
                print("Invalid choice. Please choose 'yes' or 'no'.")
                
        return users, None  # In case of failed login or invalid input

def password_reset(users, username):
    '''This function is used to reset the password for a user by updating the password in the users dictionary and the logins.json file.'''
    if username in users:
        new_password = custom_getpass("Enter a new password: ").strip()
        # Update password with the hashed version
        users[username].password = users[username].hash_password(new_password)
        print(f"Password for {username} has been reset successfully.")
        update_logins_file(users)  # Update the logins.json file with the new password
    else:
        print("Username not found.")

def update_logins_file(users):
    '''This function is used to update the logins.json file with the new password after a password reset.'''
    # Rewrite the logins.json file with updated user information
    with open('logins.json', 'w') as file:
        json.dump({user.username: user.password for user in users.values()}, file)

def load_users():
    '''This function is used to load the user data from the logins.json file.'''
    users = {}
    try:
        with open('logins.json', 'r') as file:
            user_data = json.load(file)
            for username, password in user_data.items():
                # Load users with their password already hashed
                users[username] = User(username, password, is_hashed=True)
    except FileNotFoundError:
        pass  # File does not exist yet, return empty dictionary
    return users
