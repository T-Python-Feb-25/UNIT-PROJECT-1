import bcrypt
import sqlite3
import getpass 
import emoji

class Users:
    def __init__(self, username, name, password):
        if self.check_user_exists(username):
            print("Username already exists. Please choose another name. Or try login.")
            return
        
        self.username = username
        self.name = name 
        self.password = self.hash_password(password)  
        
        self.gender = input("Enter your gender (Male or Female): ").strip().lower()
        self.height = float(input("Enter your height in cm: "))
        self.weight = float(input("Enter your weight in kg: "))
        self.age = int(input("Enter your age: "))
        self.activate_level = input("Enter your activity level (sedentary, light, moderate, active, very active): ").strip().lower()
        self.calories = None
        self.total_calories = None
        self.consumed_calories = 0
        
        self.calculate_calories()
        self.save_to_db()

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')  

    def check_password(stored_password, entered_password):
        if isinstance(stored_password, str):
            stored_password = stored_password.encode('utf-8')  
        return bcrypt.checkpw(entered_password.encode('utf-8'), stored_password)
    @staticmethod
    def login():
        username = input("Enter your username: ").strip()
        password = getpass.getpass("Enter your password: ")

        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()

        cur.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = cur.fetchone()
        con.close()

        if user:
            stored_password = user[0]
            if Users.check_password(stored_password, password):
                print(emoji.emojize("Login successful :OK_hand:"))
                return username
            else:
                print(emoji.emojize("The password is incorrect :thumbs_down:"))
                return None
        else:
            print("Username not found!")
            return None

    def check_user_exists(self, username):
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
        user_count = cur.fetchone()[0]
        con.close()
        return user_count > 0

    def calculate_calories(self):
        if self.gender == "male":
            bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        elif self.gender == "female":
            bmr = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)
        else:
            print("Invalid gender")
            return None

        activity_multipliers = {
            "sedentary": 1.2,
            "light": 1.375, 
            "moderate": 1.55, 
            "active": 1.75,
            "very active": 1.9
        }
        multiplier = activity_multipliers.get(self.activate_level, None)
        if multiplier is None:
            print("Invalid activity level")
            return None

        self.calories = bmr * multiplier
        self.total_calories = self.calories

    def save_to_db(self):
        if self.calories is None:
            print("Calories not calculated. Call calculate_calories() first.")
            return 
        
        con = sqlite3.connect("tutorial.db")
        cur = con.cursor()

        cur.execute('''INSERT INTO users (username, name, password, gender, height, weight, age, activate_level, calories, total_calories, consumed_calories) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (self.username, self.name, self.password, self.gender, self.height, self.weight, self.age, self.activate_level, self.calories, self.total_calories, self.consumed_calories))
        con.commit()
        con.close()
        
        print("User data saved successfully!")
        print(f"\nYour daily required calories: {self.calories:.2f} Kcal")


if __name__ == "__main__":
    choice = input("Do you want to register (1) or login (2)? ").strip()
    
    if choice == "1":
        username = input("Enter username: ").strip()
        name = input("Enter your name: ").strip()
        password = getpass.getpass("Enter your password: ")

        user = Users(username, name, password)

    elif choice == "2":
        username = Users.login()
        if username:
            print(f"Welcome back, {username}!")
    else:
        print("Invalid choice. Exiting...")
 
   