from rich.console import Console
from rich.theme import Theme
import json
import subprocess
from games import Game 
import os 

custom_theme = Theme({"success": "green", "error": "bold red"})
console = Console(theme=custom_theme)

class Store:
    def __init__(self):
        self.games = []  
        self.cart = []   
        self.purchase_history = []
        self.load_games()

    def load_games(self):
        self.add_game(Game("Maze Game", "A funny game to play", 12.99, "maze.py"))

    def add_game(self, game: Game):
        self.games.append(game)  

    def browse_games(self):
        for game in self.games:
            console.print(game.display())  

    def add_to_cart(self, game: Game):
        self.cart.append(game)
        console.print(f"Added '{game.name}' to your cart!", style="success")

    def checkout(self):
        if not self.cart:
            console.print("Your cart is empty!!", style="error")
            console.print("Why haven't you bought the game yet? 🤨", style= "error")
            return
        
        total_price = sum(game.price for game in self.cart)
        console.print(f"The total price is ${total_price:.2f}")
        
        confirm = input("Do you want to proceed with the payment? (y/n): ").lower()
        if confirm == "y":
            self.purchase_history.extend(self.cart)  
            self.cart.clear()  
            console.print("\nCheckout complete! Thank you for your purchase 🥳✨", style="success")
            console.print("You can now play your game!", style="success")
        else:
            console.print("Checkout cancelled.", style="error")

    def save_purchase_history(self):
        try:
            with open('purchase_history.json', 'w') as e:
                json_data = [game.__dict__ for game in self.purchase_history]
                json.dump(json_data, e)
            console.print("Purchase history saved successfully!", style="success")
        except Exception as e:
            console.print(f"Error saving purchase history: {e}", style="error")

    def view_purchase_history(self):
        if not self.purchase_history:
            console.print("No purchase history found.", style="error")
        else:
            console.print("Your Purchase History:")
            for game in self.purchase_history:
                console.print(game.display()) 

    def play_game(self, game: Game):
        game_file_path = os.path.join(os.getcwd(), game.file)   
        try:
            subprocess.run(['python', game_file_path])  
        except FileNotFoundError:
            console.print(f"Error: Game file '{game_file_path}' not found.", style="error")
        except Exception as e:
            console.print(f"Error running the game: {e}", style="error")

    