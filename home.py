import msvcrt
import hashlib
from admin.events import manage_events, display_calendar
from admin.reminder import reminders_main
from datetime import datetime

class User:
    def __init__(self, username, password, is_hashed=False):
        self.username = username
        # If password is not hashed, hash it before storing
        self.password = self.hash_password(password) if not is_hashed else password

    def hash_password(self, password):
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
    # Create a new User instance with the password hashed
    users[username] = User(username, password, is_hashed=False)

    try:
        # Save the user data to 'logins.txt' file
        with open('logins.txt', 'a') as file:
            file.write(f"{username},{users[username].password}\n")
        print("You have been registered successfully! login to start using the VA")
    except IOError as e:
        print(f"Error saving user data: {e}")

    return users

def login(users):
    while True:  # Keep asking for login until successful or user decides to exit
        username = input("Enter username: ")
        password = custom_getpass("Enter password: ")

        # Check if username exists and the password matches the hashed password
        if username in users and users[username].password == hashlib.sha256(password.encode()).hexdigest():
            print(f"You have logged in successsfully! Welcome {username}")
            return users, users[username]
        else:
            print("Incorrect username or password.")
            password_reset_choice = input("Do you want to reset your password? (yes/no): ").strip().lower()
            if password_reset_choice == 'yes':
                password_reset(users, username)
                # After password reset, we want to allow the user to log in again
            elif password_reset_choice == 'no':
                print("Okay then try to login again")
                continue  # Keep the loop running to allow retrying the login
            else:
                print("Invalid choice. Please choose 'yes' or 'no'.")
    
        return users, None  # In case of failed login or invalid input

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
    '''This function is used to update the logins.txt file with the new password after a password reset.'''
    # Rewrite the logins.txt file with updated user information
    with open('logins.txt', 'w') as file:
        for username, user in users.items():
            file.write(f"{username},{user.password}\n")

def load_users():
    '''This function is used to load the user data from the logins.txt file.'''
    users = {}
    try:
        with open('logins.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    username, password = parts
                    # Load users with their password already hashed
                    users[username] = User(username, password, is_hashed=True)
                else:
                    print(f"Skipping invalid line in logins.txt: {line.strip()}")
    except FileNotFoundError:
        pass  # File does not exist yet, return empty dictionary
    return users

def main():
    '''This is the main function that runs the Virtual Assistant program.'''
    users = load_users()
    print("Welcome! I am your Virtual Assistant.\nDesigned to assist you with your daily tasks. Please register or log in to proceed.")
    
    while True:
        choice = input("Type 'r' to register, 'l' to login, 'e' to exit: ").strip().lower()
        
        if choice == 'r' or choice == 'register':
            users = register(users)  # Call register function to add a new user
        elif choice == 'l' or choice == 'login':
            users, logged_in_user = login(users)
            if logged_in_user:
                print("\nChoose an action:")
                print("1. Manage Events")
                print("2. View Calendar with Events")
                print("3. Check reminders")
                print("4. Chat with VA")
                print("5. Logout")
                        
                while True:
                    action_choice = input("Enter your choice: ").strip()
                    if action_choice == '1':
                        manage_events(logged_in_user)  # Call manage_events function from admin.services module
                        break
                    elif action_choice == '2':
                        display_calendar(logged_in_user)  # Display the calendar with events
                        choice = input("\nType 'v' to view calendar again, 'e' to exit: ")
                        if choice == 'v':
                            display_calendar(logged_in_user)
                            break
                        elif choice == 'e':
                            break
                        else:
                            print("invalid input, Type 'v' to view calendar again, 'e' to exit: ")
                        break
                    elif action_choice == '3':
                        reminders_main()
                        break
                    elif action_choice == '4':
                        print("Chat with VA")
                        break
                    elif action_choice == '5':
                        print("Logging out...")
                        break  # Exit the loop to log out
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

