from home import load_users, register, login, reminders_main
from admin.events import manage_events, display_calendar
import unittest

def main():
    '''This is the main function that runs the Virtual Assistant program.'''
    
    users = load_users()  # Load existing users
    print("Welcome! I am your Virtual Assistant.\nDesigned to assist you with your daily tasks. Please register or log in to proceed.")
    
    while True:
        choice = input("Type 'r' to register, 'l' to login, 'e' to exit, 't' to run tests: ").strip().lower()
        
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
                        while True:
                            display_calendar(logged_in_user)  # Display calendar with events
                            choice = input("\nType 'v' to view calendar again, 'e' to exit: ").strip().lower()
                            if choice == 'v':
                                continue
                            elif choice == 'e':
                                break
                            else:
                                print("Invalid input, Type 'v' to view calendar again, 'e' to exit.")
                        break
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
        elif choice == 't':
            print("Running tests...")
            # Adjust the import path for the test module
            unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromName('test.home_test.TestHomeFunctions'))
        else:
            print("Invalid choice. Please enter 'r' to register, 'l' to login, 'e' to exit, or 't' to run tests.")

if __name__ == "__main__":
    main()
