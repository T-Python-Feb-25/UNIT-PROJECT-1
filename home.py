import msvcrt
import hashlib
from admin.events import manage_events, display_calendar
from web_developer.meetings import manage_meetings
from datetime import datetime

class User:
    def __init__(self, username, password, user_type, is_hashed=False):
        self.username = username
        # If password is not hashed, hash it before storing
        self.password = self.hash_password(password) if not is_hashed else password
        self.user_type = user_type

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

def custom_getpass(prompt='Password: ', mask='*'):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        ch = msvcrt.getch()
        if ch == b'\r':  # Enter key is pressed
            break
        elif ch == b'\x08':  # Backspace is pressed
            if password:
                password = password[:-1]  # Remove last character from password
                print('\b \b', end="", flush=True)  # Remove last masked character on screen
        else:
            password += ch.decode('utf-8')  # Add the character to the password
            print(mask, end="", flush=True)  # Print mask symbol instead of the character
    print()  # Move to the next line
    return password

def register(users):
    username = input("Enter username: ")

    # Check if the username already exists in the users dictionary
    if username in users:
        print("Username already exists! Please choose a different username.")
        return users  # Return users without changes
    
    password = custom_getpass("Enter password: ")
    while True:
        user_type = input("Enter user type (Type 'w' for Web developer, 'a' for Admin): ").strip().lower()
        if user_type == 'w':
            user_type = "Web developer"
            break
        elif user_type == 'a':
            user_type = "Admin"
            break
        else:
            print("Invalid user type. Please enter 'w' for Web developer or 'a' for Admin.")
    
    # Create a new User instance with the password hashed
    users[username] = User(username, password, user_type, is_hashed=False)

    try:
        # Save the user data to 'logins.txt' file
        with open('logins.txt', 'a') as file:
            file.write(f"{username},{users[username].password},{user_type}\n")
        print("You have been registered successfully!")
    except IOError as e:
        print(f"Error saving user data: {e}")

    return users

def login(users):
    username = input("Enter username: ")
    password = custom_getpass("Enter password: ")

    # Check if username exists and the password matches the hashed password
    if username in users and users[username].password == hashlib.sha256(password.encode()).hexdigest():
        print(f"Login successful! You are logged in as a {users[username].user_type}.")
        return users, users[username]
    else:
        print("Incorrect username or password.")
        password_reset_choice = input("Do you want to reset your password? (yes/no): ").strip().lower()
        if password_reset_choice == 'yes':
            password_reset(users, username)
        return users, None  # Return None for logged_in_user if login fails


def password_reset(users, username):
    if username in users:
        new_password = custom_getpass("Enter a new password: ").strip()
        # Update password with the hashed version
        users[username].password = users[username].hash_password(new_password)
        print(f"Password for {username} has been reset successfully.")
        update_logins_file(users)  # Update the logins.txt file with the new password
    else:
        print("Username not found.")

def update_logins_file(users):
    # Rewrite the logins.txt file with updated user information
    with open('logins.txt', 'w') as file:
        for username, user in users.items():
            file.write(f"{username},{user.password},{user.user_type}\n")

def load_users():
    users = {}
    try:
        with open('logins.txt', 'r') as file:
            for line in file:
                username, password, user_type = line.strip().split(',')
                # Load users with their password already hashed
                users[username] = User(username, password, user_type, is_hashed=True)
    except FileNotFoundError:
        pass  # File does not exist yet, return empty dictionary
    return users
def main():
    users = load_users()
    print("Welcome! I am your Virtual Assistant, designed to assist you with your daily tasks. Please register or log in to proceed.")
    
    while True:
        choice = input("Type 'r' to register, 'l' to login, 'e' to exit: ").strip().lower()
        
        if choice == 'r' or choice == 'register':
            users = register(users)  # Call register function to add a new user
        elif choice == 'l' or choice == 'login':
            users, logged_in_user = login(users)
            
            if logged_in_user:
                print(f"Logged in as {logged_in_user.username} with user type {logged_in_user.user_type}")
                
                # Debugging line to check if we are entering the correct block for Web Developer
                if logged_in_user.user_type.lower() == 'admin' or logged_in_user.user_type.lower() == 'a':
                    print("Welcome Admin! Ready to manage your events.")
                    while True:
                        print("\nChoose an action:")
                        print("1. Manage Events")
                        print("2. View Calendar with Events")
                        print("3. Logout")
                        
                        action_choice = input("Enter your choice: ").strip()
                        if action_choice == '1':
                            manage_events(logged_in_user)  # Call manage_events function from admin.services module
                        elif action_choice == '2':
                            display_calendar(logged_in_user)  # Display the calendar with events
                        elif action_choice == '3':
                            print("Logging out...")
                            break  # Exit the loop to log out
                        else:
                            print("Invalid choice. Please try again.")
                
                elif logged_in_user.user_type.lower() == 'web developer' or logged_in_user.user_type.lower() == 'w':
                    print("Welcome Web Developer! Ready to manage your meetings.")
                    while True:
                        print("\nChoose an action:")
                        print("1. Manage Meetings")
                        print("2. View Calendar with Meetings")
                        print("3. Logout")
                        
                        action_choice = input("Enter your choice: ").strip()
                        if action_choice == '1':
                            manage_meetings()
                        elif action_choice == '2':
                            display_calendar(logged_in_user)
                        elif action_choice == '3':
                            print("Logging out...")
                            break
                        else:
                            print("Invalid choice. Please try again.")
            else:
                print("Login failed. Please try again.")
        
        elif choice == 'e':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter 'r' to register or 'l' to login.")

if __name__ == "__main__":
    main()
