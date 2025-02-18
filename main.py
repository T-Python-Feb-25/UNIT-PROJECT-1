from workout import log_workout, view_workout, search_workout

def main():
    
    while True:
        print("\nWelcome to Workouts Tracker\n")
        print("1- Log a new workout")
        print("2- Search workout")
        print("3- View workout history")
        print("4- Exit")

        choice = input("Choose an option from 1 to 4: ")

        if choice == "1":
            log_workout()
        elif choice == "2":
            search_workout()
        elif choice == "3":
            view_workout()
        elif choice == "4":
            print("\nThank you .. Stay strong and fit!")
            break
        else:
                print("Invalid choice number. Please choose again")
main()
