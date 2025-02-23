import bcrypt
import sqlite3
import getpass
import emoji
from datetime import datetime
from colorama import Fore, Style
import re


con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        name TEXT,
        password TEXT,
        gender TEXT,
        height REAL,
        weight REAL,
        age INTEGER,
        activate_level TEXT,
        calories REAL,
        total_calories REAL,
        consumed_calories REAL DEFAULT 0,
        last_updated TEXT DEFAULT (DATE('now'))
    )
"""
)
con.commit()
con.close()


class Users:
    """
    A class to manage users, including registration, login, and calorie calculation.
    """

    def __init__(self, username, name, password):
        """
        Initializes a User object.
        Args:
            username (str): The username.
            name (str): The user's real name.
            password (str): The password (unhashed).
        """
        if self.check_user_exists(username):
            print(
                Fore.RED
                + "Username already exists. Please choose another name. Or try login."
                + Style.RESET_ALL
            )
            return

        if not re.match(r"^[A-Za-z]+\d+$", username):
            print(
                Fore.RED
                + "Invalid username! It must contain letters followed by numbers."
                + Style.RESET_ALL
            )
            return

        if not password.isdigit():
            print(
                Fore.RED
                + "Invalid password! It must contain only numbers."
                + Style.RESET_ALL
            )
            return

        self.username = username
        self.name = name
        self.password = self.hash_password(password)
        try:
            self.gender = input("Enter your gender (Male or Female): ").strip().lower()
            self.height = float(input("Enter your height in cm: "))
            self.weight = float(input("Enter your weight in kg: "))
            self.age = int(input("Enter your age: "))
        except ValueError:
            print(
                Fore.RED
                + "Invalid input! Please enter valid numbers for height, weight, and age."
                + Style.RESET_ALL
            )
            return None
        self.activate_level = (
            input(
                "Enter your activity level (sedentary, light, moderate, active, very active): "
            )
            .strip()
            .lower()
        )
        self.calories = None
        self.total_calories = None
        self.consumed_calories = 0
        self.last_updated = datetime.today().strftime("%Y-%m-%d")

        self.calculate_calories()
        self.save_to_db()

    def hash_password(self, password):
        """
        Hashes the password using bcrypt.
        Args:
            password (str): The password (unhashed).
        Returns:
            str: The hashed password.
        """

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    @staticmethod
    def check_password(stored_password, entered_password):
        """
        Checks if the entered password matches the stored password.
        Args:
            stored_password (str): The stored password (hashed).
            entered_password (str): The entered password (unhashed).
        Returns:
            bool: True if the password is correct, False otherwise.
        """

        if isinstance(stored_password, str):
            stored_password = stored_password.encode("utf-8")
        return bcrypt.checkpw(entered_password.encode("utf-8"), stored_password)

    @staticmethod
    def login():
        """
        Logs in a user.
        Returns:
            str: The username if login is successful, None otherwise.
        """
        try:
            username = input("Enter your username: ").strip()
            password = getpass.getpass("Enter your password: ")

            con = sqlite3.connect("tutorial.db")
            cur = con.cursor()

            cur.execute(
                "SELECT password, last_updated FROM users WHERE username = ?",
                (username,),
            )
            user = cur.fetchone()
            con.close()

            if user:
                stored_password, last_updated = user
                if Users.check_password(stored_password, password):
                    print(
                        emoji.emojize(Fore.GREEN + "Login successful :OK_hand:")
                        + Style.RESET_ALL
                    )
                    print(f"\U0001f4c5 Last updated: {last_updated}")

                    # Check if a day has passed since last update
                    today = datetime.today().strftime("%Y-%m-%d")
                    if last_updated != today:
                        # If the last update date is not today, reset consumed_calories to 0
                        con = sqlite3.connect("tutorial.db")
                        cur = con.cursor()
                        cur.execute(
                            "UPDATE users SET consumed_calories = 0, last_updated = ? WHERE username = ?",
                            (today, username),
                        )
                        con.commit()
                        con.close()
                        print("Your consumed calories have been reset to 0 for today.")

                    # Display the total daily calories
                    con = sqlite3.connect("tutorial.db")
                    cur = con.cursor()
                    cur.execute(
                        "SELECT total_calories FROM users WHERE username = ?",
                        (username,),
                    )
                    total_calories = cur.fetchone()[0]
                    con.close()

                    return username
                else:
                    print(
                        emoji.emojize(
                            Fore.RED + "The password is incorrect :thumbs_down:"
                        )
                        + Style.RESET_ALL
                    )
                    return None
            else:
                print(Fore.RED + "Username not found!" + Style.RESET_ALL)
                return None
        except sqlite3.Error as e:
            print(Fore.RED + f"Database error: {e}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}" + Style.RESET_ALL)

    def check_user_exists(self, username):
        """
        Checks if a user exists in the database.
        Args:
            username (str): The username.
        Returns:
            bool: True if the user exists, False otherwise.
        """
        try:
            con = sqlite3.connect("tutorial.db")
            cur = con.cursor()
            cur.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
            user_count = cur.fetchone()[0]
            con.close()
            return user_count > 0
        except sqlite3.Error as e:
            print(Fore.RED + f"Database error: {e}" + Style.RESET_ALL)
            return False

    def calculate_calories(self):
        """
        Calculates the daily required calories based on gender and activity level.
        """
        try:
            if self.gender == "male":
                bmr = (
                    88.362
                    + (13.397 * self.weight)
                    + (4.799 * self.height)
                    - (5.677 * self.age)
                )
            elif self.gender == "female":
                bmr = (
                    447.593
                    + (9.247 * self.weight)
                    + (3.098 * self.height)
                    - (4.330 * self.age)
                )
            else:
                print(Fore.RED + "Invalid gender" + Style.RESET_ALL)
                return None

            activity_multipliers = {
                "sedentary": 1.2,
                "light": 1.375,
                "moderate": 1.55,
                "active": 1.75,
                "very active": 1.9,
            }
            multiplier = activity_multipliers.get(self.activate_level, None)
            if multiplier is None:
                print(Fore.RED + "Invalid activity level" + Style.RESET_ALL)
                return None

            self.calories = bmr * multiplier
            self.total_calories = self.calories
        except ValueError as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def save_to_db(self):
        """
        Saves the user data to the database.
        """
        if self.calories is None:
            print("Calories not calculated. Call calculate_calories() first.")
            return
        try:
            con = sqlite3.connect("tutorial.db")
            cur = con.cursor()

            cur.execute(
                """INSERT INTO users (username, name, password, gender, height, weight, age, activate_level, calories, total_calories, consumed_calories, last_updated) 
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    self.username,
                    self.name,
                    self.password,
                    self.gender,
                    self.height,
                    self.weight,
                    self.age,
                    self.activate_level,
                    self.calories,
                    self.total_calories,
                    self.consumed_calories,
                    self.last_updated,
                ),
            )
            con.commit()
            con.close()

            print(Fore.GREEN + "User data saved successfully!" + Style.RESET_ALL)
            print(f"\nYour daily required calories: {self.calories:.2f} Kcal")
        except Exception as e:
            print(Fore.RED + f"Error saving data: {e}" + Style.RESET_ALL)
