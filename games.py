class Game:
    def __init__(self, name, description, price, file):
        self.name = name
        self.description = description
        self.price = price
        self.file = file

    def display(self):
        return f"{self.name}: {self.description}, Price: ${self.price:.2f}"
    