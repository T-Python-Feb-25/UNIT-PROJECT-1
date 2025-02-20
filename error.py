import json

class ErrorRebot:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.reports = []  

    def report(self): 
        self.name = input("What's your problem about: ")
        self.description = input("Describe your problem: ")
        self.reports.append({"name": self.name, "description": self.description}) 

    def display_error(self):
        return f"Your problem about '{self.name}' has reached us. Thank you for reporting!"

    def rebort_history(self):
        try:
            with open('rebort_history.json', 'w') as e:
                json_data = self.reports  
                json.dump(json_data, e)
           
        except Exception as e:
            print(f"Error saving report history: {e}")