import json

def get_Previous_Plans():
    try :
        with open("users_account_file.json","r") as file:
            return json.load(file)
    except FileNotFoundError :
        return {}
    
def view_Previous_Plans(email):
    