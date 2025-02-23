from game_store import Store
from error import ErrorReport
from rich.console import Console
from rich.theme import Theme
from colorama import *
from art import *
from User_data import UserData

custom_theme = Theme({"success": "bold yellow", "error": "bold red"})
console = Console(theme=custom_theme)

def main():
    print(Fore.BLUE + Style.BRIGHT)
    tprint("Welcome to my Maze Game!")
    print(Style.RESET_ALL)

    input("PRESS ANY KEY TO CONTINUE... ")
    user_data = UserData()

    user_name = console.input("[bold blue]Enter your username to login: [/]")

    while True:
        password = console.input("[bold blue]Enter your password (only numbers): [/]")
        if user_data.has_only_numbers(password):
            break
        console.print("The password needs to be numbers only.", style="error")

    user_data.save_login_data(user_name, password)
    store = Store()  

    error_report= ErrorReport()

    while True:
        console.print("1. Browse Games\n2. Checkout\n3. View Purchase History\n4. Play Game\n5. Report an Issue\n6. Exit")
        choice = console.input("[bold blue]Select an option: [/]")

        try:
            
            if choice == "1":
                store.browse_games()
                game_name = input("Enter the name of the game you want to add to the cart: ")
                game = next((game for game in store.games if game.name.lower() == game_name.lower()), None)
                if game:
                    store.add_to_cart(game)  
                    console.print("Game added successfully.", style="success")
                else:
                    console.print("Game not found. Please check the name and try again.", style="error")
                input("Press any key to return to the main menu...")

            elif choice == "2":
                store.checkout()
                input("Press any key to return to the main menu...")

            elif choice == "3":
                store.view_purchase_history()
                input("Press any key to return to the main menu...")

            elif choice == "4":
                if not store.purchase_history:
                    console.print("You have no purchased games to play.", style="error")
                else:
                    game_name = input("Enter the name of the game you want to play: ")
                    game = next((game for game in store.purchase_history if game.name.lower() == game_name.lower()), None)
                    if game:
                        store.play_game(game)
                    else:
                        console.print("Game not found in your purchase history.", style="error")
                input("Press any key to return to the main menu...")

            elif choice == "5":
                error_report.report()
                print(error_report.display_error())
                continue_reporting = input("Do you want to report another issue? (y/n): ").lower()
                if continue_reporting != 'y':
                    input("Press any key to return to the main menu...")
                else:
                    error_report.report()
                

            elif choice == "6":
                console.print("\n[bold magenta]Thank you! Please come again 🤍[/]", justify="center")
                break

            else:
                console.print("Invalid option. Please try again.", style="error")

        except Exception as e:
            console.print(f"An error occurred: {e}", style="error")

main()