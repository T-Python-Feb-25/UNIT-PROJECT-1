class ErrorRebot:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def rebort(self):
        self.name = input("What's your problem about: ")
        self.description = input("Describe your problem: ")

    def display_error(self):
        return f"Your problem '{self.name}' has reached us. Thank you for reporting!"