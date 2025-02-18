class Game:
    def __init__(self, name, description, price, file):
        self.name = name
        self.description = description
        self.price = price
        self.file = file
        

    def __display__(self):
        return f"{self.name}: {self.description}, Price: ${self.price}"
    

game1 = Game("game1", "a funny game to play", 12.99, "game.game1.py") 
game2 = Game("game2", "a funny game to play", 12.99, "game.game2.py") 
print(game1.__display__())