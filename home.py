import msvcrt
import hashlib

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
    user_type = input("Enter user type (Type 'w' for Web developer, 'a' for Admin): ").strip().lower()
    if user_type == 'w':
        user_type = "Web developer"
    elif user_type == 'a':
        user_type = "Admin"
    else:
        print("Invalid user type. Please enter 'w' for Web developer or 'a' for Admin.")
        return users  # Return users without changes
    

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
    else:
        print("Incorrect username or password.")
        password_reset_choice = input("Do you want to reset your password? (yes/no): ").strip().lower()
        if password_reset_choice == 'yes':
            password_reset(users, username)
        else:
            return login(users)  # Recursively call login if credentials are incorrect

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

if __name__ == "__main__":
    users = load_users()
    while True:
        choice = input("Do you want to register or login? (r/l): ").strip().lower()
        if choice == 'r':
            users = register(users)  # Call register function to add a new user
        elif choice == 'l':
            login(users)  # Call lo
