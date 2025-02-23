from workout import *
from art import tprint
from colorama import Fore, Style, init

import workout

def menu():
    random_workout_challenge()
    
    while True:
        tprint("Workout Tracker", font="small")
        print(Fore.GREEN + "1️⃣  Workout Categories")
        print(Fore.BLUE + "2️⃣  Log a New Workout")
        print(Fore.MAGENTA + "3️⃣  Search Workout by Exercise Name")
        print(Fore.CYAN + "4️⃣  View Workout History")
        print(Fore.RED + "5️⃣  Delete Workout")
        print(Fore.WHITE+ "6️⃣  View Best Records")
        print(Fore.YELLOW +"7️⃣  Weekly Statistics") 
        print(Fore.LIGHTBLACK_EX + "8️⃣  Exit\n")

        choice = input(Fore.WHITE + "👉 Choose an option: ")
        
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
            view_best_records()
        elif choice == "7":  
            weekly_statistics()
        elif choice == "8":
            print("\nThank you .. Stay strong and fit!")
            break
        else:
            print("\n❌ Invalid choice number. Please try again.\n")
        
menu()