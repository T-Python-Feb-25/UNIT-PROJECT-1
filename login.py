from colorama import Fore, Back, Style
from art import *
import json
import os

users_file = "users.json"

# Load existing users from the file
def load_users():
    if not os.path.exists(users_file):
        return {}
    
    try:
        with open(users_file, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

# Save users to the file
def save_users(users):
    with open(users_file, "w") as file:
        json.dump(users, file, indent=4)

# Register a new user
def register_user():
    users = load_users()
    
    username = input("🆔 Enter a username: ").strip()
    
    if username in users:
        print("⭕️ Username already exists! Please choose a different one ⭕️")
        return None
    
    name = input("👤 Enter your name: ").strip()
    
    users[username] = {"name": name, "points": 0}
    save_users(users)
    
    print("✅ Registration successful! ✅")
    return username

# Login an existing user
def login_user():
    users = load_users()
    
    username = input("Enter your username: ").strip()
    
    if username in users:
        print(f"✅ Welcome back, {users[username]['name']}! ✅")
        return username
    else:
        print("❌ Username not found! Please register first.")
        login_menu()

# Login or Register Menu
def login_menu():
    tprint("-WELCOME QUESTION GAME-", font="cybermedium")
    while True:
        print("\n1️⃣  Register\n2️⃣  Login\n3️⃣  Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            return register_user()
        elif choice == "2":
            return login_user()
        elif choice == "3":
            print("👋 Goodbye!")
            exit()
        else:
            print("⛔️ Invalid choice, try again ⛔️")

