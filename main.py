from home import load_users, register, login, manage_events, display_calendar, reminders_main

def main():
    
    '''This is the main function that runs the Virtual Assistant program.'''
    
    users = load_users()  # Load existing users
    print("Welcome! I am your Virtual Assistant.\nDesigned to assist you with your daily tasks. Please register or log in to proceed.")
    
    while True:
        choice = input("Type 'r' to register, 'l' to login, 'e' to exit: ").strip().lower()
        
        if choice == 'r' or choice == 'register':
            users = register(users)  # Register a new user
        elif choice == 'l' or choice == 'login':
            users, logged_in_user = login(users)
            if logged_in_user:
                print("\nChoose an action:")
                print("1. Manage Events")
                print("2. View Calendar with Events")
                print("3. Check reminders")
                print("4. Logout")
                        
                while True:
                    action_choice = input("Enter your choice: ").strip()
                    if action_choice == '1':
                        manage_events(logged_in_user)  # Manage user events
                        break
                    elif action_choice == '2':
                        display_calendar(logged_in_user)  # Display calendar with events
                        choice = input("\nType 'v' to view calendar again, 'e' to exit: ")
                        if choice == 'v':
                            display_calendar(logged_in_user)
                            break
                        elif choice == 'e':
                            break
                        else:
                            print("Invalid input, Type 'v' to view calendar again, 'e' to exit.")
                    elif action_choice == '3':
                        reminders_main()  # Check reminders
                        break
                    elif action_choice == '4':
                        print("Logging out...")
                        break  # Exit the inner loop to log out
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
