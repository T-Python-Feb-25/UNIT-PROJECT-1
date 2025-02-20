from home import register, login, load_users

users = load_users()
print("Welcome! I am your Virtual Assistant.\nI am here to help you with your daily tasks.\nPlease register or login to continue.")

while True:
    choice = input("Enter 'r' to register and 'l' to login: ").strip().lower()
    if choice == 'r':
        users = register(users)  # Call register function to add a new user
    elif choice == 'l':
        login(users)  # Call login function to log in the user
    else:
        print("Invalid choice. Please enter 'r' to register or 'l' to login.")
