
from game_store import Store    
from art import *
from colorama import Fore, Style, init


menu = '''
    1. Browse Games 
    2. View Cart
    3. Checkout
    4. View Purchase History
    5. Play a Game
    6. Exit
'''

def Main_menu():
    print(Fore.BLUE + Style.BRIGHT)  
    tprint("Welcome to the Game Store!")   

    print(Style.RESET_ALL)  
    print(menu)  

def handle_choice(choice):
    try:
        if choice == "1":
            game_choice = int(input("Select a game to add to cart (number): ")) 
            Store.browse_games()

        elif choice == "2":
          Store.view_cart() 
            
        elif choice == "3":
           Store.checkout()
            
        elif choice == "4":
            Store.view_purchase_history()
             
        elif choice == "5":
            game_name = input("Enter the name of the game you want to play: ")

        elif choice == "6":
            print("Thank you! Please come again!")
            return False  
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return True  

if __name__ == "__main__":
    while True:
        Main_menu()
        user_choice = input("Please select an option: ")
        if not handle_choice(user_choice):
            break