
def main():
    while True:
        print("\nWorkout Tracker")
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
            print("Thank you .. Stay strong and fit")
            break
        else:
                print("Invalid choice. Please choose again")
    
main()
