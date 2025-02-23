import json
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({"success": "bold yellow", "error": "bold red"})
console = Console(theme=custom_theme)

class ErrorReport:
    def __init__(self, name='', description=''):
        self.name = name
        self.description = description
        self.reports = []  

    def report(self): 
        self.name = input("What's your problem about: ")
        self.description = input("Describe your problem: ")
        self.reports.append({"name": self.name, "description": self.description}) 
        self.report_history()  

    def display_error(self):
        return f"Your problem about '{self.name}' has reached us. Thank you for reporting!"

    def report_history(self):
        try:
            with open('report_history.json', 'w') as e:
                json_data = self.reports  
                json.dump(json_data, e, indent=4)  
            console.print("Report history saved successfully!", style="success")
        except Exception as e:
            console.print(f"Error saving report history: {e}", style="error")
