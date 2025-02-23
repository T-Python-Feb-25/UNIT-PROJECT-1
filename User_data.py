import json
from rich.console import Console
from rich.theme import Theme


custom_theme = Theme({"success": "bold yellow", "error": "bold red"})
console = Console(theme=custom_theme)


class UserData:
    def __init__(self):
        self.file_name = 'login_data.json'

    def has_only_numbers(self, password):
        return password.isdigit()  

    def load_data(self):
        try:
            with open(self.file_name, 'r') as f:
                return json.load(f)  
        except (FileNotFoundError, json.JSONDecodeError):
            return {}  

    def save_login_data(self, user_name, password):
        existing_data = self.load_data()  
        existing_data[user_name] = password  

        with open(self.file_name, 'w') as f:
            json.dump(existing_data, f, indent=4)  

        console.print("Login data saved successfully.", style= "success")
