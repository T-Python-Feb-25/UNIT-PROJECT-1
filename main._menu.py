from game_store import Store
from error import ErrorRebot
from rich.console import Console
from rich.theme import Theme
from colorama import *
from art import *
from User_data import UserData

costom_theme = Theme({"success": "green", "error": "bold red"})
console = Console (theme=costom_theme)


def main():
    
    print(Fore.BLUE + Style.BRIGHT)
    tprint("Welcome to my Maze Game !")
    print(Style.RESET_ALL)

    input("PRESS ANY KEY TO CONTINUE... ")

    user_data = UserData()
    
    email = input("enter your user name to login ")
    
    while True:
        password = input("inter your password( just number): ")
        if user_data.has_numbers(password):
            break
        print("the password need to be numbers")
    
    user_data.save_login_data(email, password)
    store = Store()  
    
    
    error = ErrorRebot("", "")
 
# add more try & except
    while True:
        print("\n1. Browse Games\n2. View Cart\n3. Remove from Cart\n4. Checkout\n5. View Purchase History\n6. Play Game\n7. rebort an issuu\n8. Exit")
        choice = input("Select an option: ")
       
        try:
            if choice == "1":
                store.browse_games()
                cart_choice = input("Would you like to add a game to the cart (y or n)? ").lower()
                if cart_choice == "y":
                    game_index = int(input("Enter the game number to add to cart: ")) - 1
                     
                    store.add_to_cart(game_index)  
                    console.print("Game added successfully.", style="success")
                    print(input("")) 
                elif cart_choice == "n":
                    input("Press any key to return to the main menu...")  

            elif choice == "2":
                
                store.view_cart()
                input("Press any key to back to the main menu..")  
            elif choice == "3":
                store.view_cart()
                game_index = int(input("Enter the game number to remove from cart: ")) - 1
                store.remove_from_cart(game_index)
                input("Press any key to return to the main menu...")  

            elif choice == "4":
                store.checkout()
                print(input(""))

            elif choice == "5":
                store.view_purchase_history() 
                print(input(""))

            elif choice == "6":
                store.view_purchase_history()
                game_index = int(input("Enter the game number to play: ")) - 1
                if 0 <= game_index < len(store.purchase_history):
                    store.play_game(store.purchase_history[game_index])
                    
            elif choice == "7":
                error.report()
                print(error.display_error())
                continue_reporting = input("Do you want to report another issue? (y/n): ").lower()
                if continue_reporting == 'y':
                    error.report()
                    
                if continue_reporting != 'y':
                      continue
                else:
                    print(error.display_error())
                    input("Press any key to return to the main menu...") 

            elif choice == "8":
                console.print("Thank you! Please come again 🤍")
                break
            else:
                console.print("Invalid option. Please try again.", style="error")
        except ValueError:
            console.print("Invalid input. Please enter a number.", style="error")

main()