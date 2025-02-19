def welcome():
    print("Welcom I am your Virtual Assistant\n I am here to help you with your daily tasks")
         # \n1. I want to know the weather\n2. I want to know the news
def login():
    print("Please enter your username and password to login")
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "admin":
        print(f"Welcome back, {username}")
    elif username == "elaf" and password == "user":
        print(f"Welcome back, {username}")
    else:
        print("Invalid username or password")
        login()
        
if __name__ == "__main__":
    welcome(),
    login()