import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "modules")))

from risk_manager import add_risk, list_risks, search_risk
from safety_recommendations import get_recommendations
from report_generator import generate_report
from graph_generator import plot_risks

def display_menu():
    print(f"\n{Fore.CYAN}{'=' * 45}")
    print(f"{Fore.BLUE}Civil Defence Safety Tracker - Menu")
    print(f"{Fore.CYAN}{'=' * 45}")
    print(f"{Fore.GREEN}1.{Fore.RESET} Add a new risk")
    print(f"{Fore.GREEN}2.{Fore.RESET} List all recorded risks")
    print(f"{Fore.GREEN}3.{Fore.RESET} Search for a risk by location")
    print(f"{Fore.GREEN}4.{Fore.RESET} Get safety recommendations")
    print(f"{Fore.GREEN}5.{Fore.RESET} Generate a report")
    print(f"{Fore.GREEN}6.{Fore.RESET} Plot risks chart")
    print(f"{Fore.RED}0.{Fore.RESET} Exit")

def main():
    print(f"{Fore.YELLOW}{'=' * 50}")

    print(f"{Fore.MAGENTA}Welcome to the Civil Defence Safety Tracker!")
    print(f"{Fore.YELLOW}Manage and analyze risks efficiently.")
    
    print(f"{Fore.YELLOW}{'=' * 50}")

    while True:
        display_menu()
        
        try:
            choice = input(f"\n{Fore.CYAN}Enter your choice: {Fore.RESET}").strip()
            
            if not choice:
                print(f"{Fore.RED}Error: No input provided. Please enter a valid option.")
                continue

            if choice == "1":
                print(f"\n{Fore.GREEN}Adding a new risk...{Fore.RESET}")
                risk_type = input("Enter risk type: ")
                level = input("Enter risk level (Low/Medium/High): ")
                location = input("Enter location: ")
                date = input("Enter date (YYYY-MM-DD): ")
                add_risk(risk_type, level, location, date)

            elif choice == "2":
                print(f"\n{Fore.GREEN}Listing all recorded risks...{Fore.RESET}")
                list_risks()

            elif choice == "3":
                print(f"\n{Fore.GREEN}Searching for risks...{Fore.RESET}")
                location = input("Enter location to search for risks: ")
                search_risk(location)

            elif choice == "4":
                print(f"\n{Fore.GREEN}Getting safety recommendations...{Fore.RESET}")
                risk_type = input("Enter risk type for recommendations: ")
                print("\n".join(get_recommendations(risk_type)))

            elif choice == "5":
                print(f"\n{Fore.GREEN}Generating risk report...{Fore.RESET}")
                generate_report()

            elif choice == "6":
                print(f"\n{Fore.GREEN}Generating risk chart...{Fore.RESET}")
                plot_risks()

            elif choice == "0":
                print(f"\n{Fore.RED}Exiting program. Stay safe!{Fore.RESET}")
                break

            else:
                print(f"{Fore.RED}Invalid choice! Please enter a number between 0-6.{Fore.RESET}")

        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Program interrupted. Exiting safely.{Fore.RESET}")
            break

if __name__ == "__main__":
    main()
