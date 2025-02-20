from rich.console import Console
from rich.theme import Theme
import json
import subprocess
from games import Game 
import os 

costom_theme = Theme({"success": "green", "error": "bold red"})
console = Console (theme=costom_theme)

class Store:
    def __init__(self, email, password):
        self.password = password
        self.email = email
        self.games = []  
        self.cart = []   
        self.purchase_history = []
        
        
        self.load_games()
        self.save_login_data()
        

    def set_user(self):
        if not isinstance ():
            pass



    def load_games(self):
        self.add_game(Game("maze game", "A funny game to play", 12.99, "maze.py"))

    def add_game(self, game: Game):
        self.games.append(game)  
    #set & get
    def browse_games(self):
        for index, game in enumerate(self.games, start=1):
            print(f"{index}. {game.display()}")  

    def add_to_cart(self, game_index: int):
        if 0 <= game_index < len(self.games):
            self.cart.append(self.games[game_index]) 

    def remove_from_cart(self, game_index: int):
        try:
            if 0 <= game_index < len(self.cart):
                confirm = input(f"Are you sure you want to remove {self.cart[game_index].name} from the cart? (y/n): ").lower()
                if confirm == 'y':
                    removed_game = self.cart.pop(game_index)
                    console.print(f"Removed {removed_game.name} from cart.", style="success")
                else:
                    print("Removal cancelled.", style="error")
        except Exception as e:
            console.print(f"An error occurred while removing the game: {e}", style="error")

    def view_cart(self):
        if not self.cart:
            console.print("Your cart is empty 😞")
        else:
            print("Your cart contains:")
            for index, game in enumerate(self.cart, start=1):
                print(f"{index}. {game.display()}")  

    def checkout(self):
        if not self.cart:
            console.print("Your cart is empty!!")
            console.print("like why you didn't buy yet 🤨")
            return
        total_price = sum(game.price for game in self.cart) 
        print(f"Total amount due: ${total_price:.2f}")
        confirm = input("Do you want to proceed with the payment? (y/n): ").lower()
        if confirm == "y":
            self.purchase_history.extend(self.cart)  
            self.cart.clear()  
            console.print("\nCheckout complete! Thank you for your purchase 🥳✨")
            console.print("you can play the game now")
            self.save_purchase_history()
        else:
            console.print("Checkout cancelled.", style = "error")

    def save_purchase_history(self):
        try:
            with open('purchase_history.json', 'w') as e:
                json_data = [game.__dict__ for game in self.purchase_history]
                json.dump(json_data, e)
        
        except Exception as e:
            print(f"Error saving purchase history: {e}", style="error")

    def view_purchase_history(self):
        if not self.purchase_history:
            console.print("No purchase history found.", style="error")
        else:
            print("Purchase History:")
            for index, game in enumerate(self.purchase_history, start=1):
                print(f"{index}. {game.display()}")  

    def play_game(self, game: Game):
        game_file_path = os.path.join(os.getcwd(), game.file)   
        try:
            subprocess.run(['python', game_file_path])  
        except FileNotFoundError:
            print(f"Error: Game file '{game_file_path}' not found." ,style="error")
        except Exception as e:
            print(f"Error running the game: {e}" ,style="error")

    def save_login_data(self):
        login_data = {
            'email': self.email,
            'password': self.password,
        }
        try:
            with open('login_data.json', 'w') as f:
                json.dump(login_data, f)
            console.print("Login data saved successfully.", style="success")
        except Exception as e:
            print(f"Error saving login data: {e}", style="error")
    
    
