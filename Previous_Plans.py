import json

def get_Previous_Plans():
    try :
        with open("users_account_file.json","r") as file:
            return json.load(file)
    except FileNotFoundError :
        return {}
    
def view_Previous_Plans(email):
    users_accounts=get_Previous_Plans():
    
    if email in users_accounts:
        users_accounts= users_accounts[email]
        if users_accounts["Travel Plans"] is None:
            print("You don't have any Plans yet")
        else:
            print({users_accounts["Travel Plans"]})