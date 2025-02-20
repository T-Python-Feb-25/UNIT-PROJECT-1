
from users import Users
from calorie_tracker import CalorieTracker

def main():
    username = Users.login()  

    if username: 
        calorie_tracker = CalorieTracker(username)  
        while True:
            print("\nMenu:")
            print("1. Add food")
            print("2. View calories")
            print("3. Exit")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                calorie_tracker.add_food()
            elif choice == "2":
                calorie_tracker.view_calories()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")
    else:
        print("Login failed. Please try again.")

if __name__ == "__main__":
    main()
