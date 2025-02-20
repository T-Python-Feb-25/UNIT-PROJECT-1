import json
import os

users_file = "users.json"
leaderboard_file = "leaderboard.json"

# Function to load user data from the file
def load_users():
    """Load the list of users from the JSON file."""
    try:
        with open(users_file, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save user data to the file
def save_users(users):
    """Save the list of users to the JSON file."""
    with open(users_file, "w") as file:
        json.dump(users, file, indent=4)

# Function to load leaderboard from a file
def load_leaderboard():
    """Load the leaderboard data from the JSON file."""
    try:
        with open("users.json", "r") as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            return dict()
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(e)
        return []

# Function to save leaderboard data
def save_leaderboard(data):
    """Save the leaderboard data to the JSON file."""
    with open(leaderboard_file, "w") as file:
        json.dump(data, file, indent=4)

# Default leaderboard data
Theleaderboard = [
    {"Rank 🏆": "1️⃣", "UserName": "Ahmed-707", "Points": 450},
    {"Rank 🎖": "2️⃣", "UserName": "Laila20", "Points": 420},
    {"Rank 🏅": "3️⃣", "UserName": "Khaledd1222", "Points": 390},
    {"Rank 🥈": "4️⃣", "UserName": "NouraXkiller", "Points": 360},
    {"Rank 🥉": "5️⃣", "UserName": "Majed00-sniper", "Points": 330}
]

# Save default leaderboard if the file doesn't exist
if not os.path.exists(leaderboard_file):
    save_leaderboard(Theleaderboard)
