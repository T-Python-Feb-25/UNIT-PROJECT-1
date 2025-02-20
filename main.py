from workout import *
from art import tprint
from colorama import Fore, Style, init

def menu():
    random_workout_challenge()
    
    while True:
        tprint("Workout Tracker", font="small")
        print(Fore.GREEN + "1️⃣  Workout Categories")
        print(Fore.BLUE + "2️⃣  Log a New Workout")
        print(Fore.MAGENTA + "3️⃣  Search Workout by Exercise Name")
        print(Fore.CYAN + "4️⃣  View Workout History")
        print(Fore.RED + "5️⃣  Delete Workout")
        print(Fore.LIGHTBLACK_EX + "6️⃣  Exit\n")

        choice = input(Fore.WHITE + "👉 Choose an option (1-6): ")
        
        if choice == "1":
            workout_categories()
        elif choice == "2":
            log_workout()
        elif choice == "3":
            search_workout()
        elif choice == "4":
            view_workout()
        elif choice == "5":
            delete_workout()
        elif choice == "6":
            print("\nThank you .. Stay strong and fit!")
            break
        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.")
        
menu()
