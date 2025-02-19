
from colorama import *
from art import *
from game_store import Store
from error import ErrorRebot

def main():
    print(Fore.BLUE + Style.BRIGHT)
    tprint("Welcome to the Game Store!")
    print(Style.RESET_ALL)


    input("PRESS ANY KEY TO CONTINUE... ")

    email = input("Enter your email: ")
    password = input("Enter your password: ")
    store = Store(email, password)  
    print(input(""))

 


    while True:
        print("\n1. Browse Games\n2. View Cart\n3. Remove from Cart\n4. Checkout\n5. View Purchase History\n6. Play Game\n7. more option \n8. Exit")
        choice = input("Select an option: ")
       
        try:
            if choice == "1":
                store.browse_games()
                cart_choice = input("Would you like to add a game to the cart (y or n)? ").lower()
                if cart_choice == "y":
                    game_index = int(input("Enter the game number to add to cart: ")) - 1
                     
                    store.add_to_cart(game_index)  
                    print("Game added successfully.")
                    print(input(""))
                elif cart_choice == "n":
                    input("Press any key to return to the main menu...")  

            elif choice == "2":
                
                store.view_cart()
                input("Press any key to countenu...")  
            elif choice == "3":
                store.view_cart()
                game_index = int(input("Enter the game number to remove from cart: ")) - 1
                store.remove_from_cart(game_index)
                input("Press any key to return to the main menu...")  
            elif choice == "4":
                store.checkout()
                
            elif choice == "5":
                store.view_purchase_history()
                input("Press any key to return to the main menu...")  
            elif choice == "6":
                store.view_purchase_history()
                game_index = int(input("Enter the game number to play: ")) - 1
                if 0 <= game_index < len(store.purchase_history):
                    store.play_game(store.purchase_history[game_index])  
                else:
                    print("Invalid game selection.")

            elif choice == "7":
                pass

            elif choice == "8":
                print("Thank you! Please come again!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")



main()