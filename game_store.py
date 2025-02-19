import json
import subprocess
from games import Game 
import os 

class Store:
    def __init__(self, email, password):
        self.password = password
        self.email = email

        self.games = []  
        self.cart = []   
        self.purchase_history = []
        
        self.load_games()
        self.save_login_data()
        
    def load_games(self):
        self.add_game(Game("guees the word", "A funny game to play", 12.99, "game1.py"))

    def add_game(self, game: Game):
        self.games.append(game)  

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
                    print(f"Removed {removed_game.name} from cart.")
                else:
                    print("Removal cancelled.")
            else:
                print("Invalid game selection to remove.")
        except Exception as e:
            print(f"An error occurred while removing the game: {e}")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for index, game in enumerate(self.cart, start=1):
                print(f"{index}. {game.display()}")  

    def play_game(self, game: Game):
      pass
    
    def checkout(self):
        if not self.cart:
            print("Your cart is empty. Cannot proceed to checkout.")
            return
        total_price = sum(game.price for game in self.cart) 
        print(f"Total amount due: ${total_price:.2f}")

        confirm = input("Do you want to proceed with the payment? (y/n): ").lower()
        if confirm == "y":
            self.purchase_history.extend(self.cart)  
            self.cart.clear()  
            print("Checkout complete! Thank you for your purchase.")
            self.save_purchase_history()
        else:
            print("Checkout cancelled.")

    def save_purchase_history(self):
        try:
            with open('purchase_history.json', 'w') as e:
                json_data = [game.__dict__ for game in self.purchase_history]
                json.dump(json_data, e)
            print("Purchase history saved")
        except Exception as e:
            print(f"Error saving purchase history: {e}")

    def view_purchase_history(self):
        if not self.purchase_history:
            print("No purchase history found.")
        else:
            print("Purchase History:")
            for index, game in enumerate(self.purchase_history, start=1):
                print(f"{index}. {game.display()}")  

    def play_game(self, game: Game):
        game_file_path = os.path.join(os.getcwd(), game.file)  # استخدام المسار الحالي
        print(f"Trying to run the game from: {game_file_path}")  # طباعة المسار لمحاولة فهم الخطأ
        try:
            subprocess.run(['python', game_file_path])  
        except FileNotFoundError:
            print(f"Error: Game file '{game_file_path}' not found.")
        except Exception as e:
            print(f"Error running the game: {e}")

    def save_login_data(self):
        login_data = {
            'email': self.email,
            'password': self.password,
        }
        try:
            with open('login_data.json', 'w') as f:
                json.dump(login_data, f)
            print("Login data saved successfully.")
        except Exception as e:
            print(f"Error saving login data: {e}")