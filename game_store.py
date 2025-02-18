import json
from games import Game  

class Store:
    def __init__(self):
        self.games = []  
        self.cart = []   
        self.purchase_history = []
        self.load_games()

    def load_games(self):
        self.add_game(Game("guees the word", "A funny game to play", 12.99, "game.game1.py"))
        self.add_game(Game("maze", "An exciting adventure game", 19.99, "game.game2.py"))

    def add_game(self, game: Game):
        self.games.append(game)  

    def browse_games(self):
        for index, game in enumerate(self.games, start=1):
            print(f"{index}. {game.display()}")  

    def add_to_cart(self, game_index: int):
        if 0 <= game_index < len(self.games):
            self.cart.append(self.games[game_index]) 

    def remove_from_cart(self, game_index: int):
        if 0 <= game_index < len(self.cart):
            removed_game = self.cart.pop(game_index)
            print(f"Removed {removed_game.name} from cart.")
        else:
            print("Invalid game selection to remove.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for index, game in enumerate(self.cart, start=1):
                print(f"{index}. {game.display()}")  

    def checkout(self):
        pass

    def save_purchase_history(self):
        pass

    def view_purchase_history(self):
        pass

    def play_game(self, game: Game):
      pass