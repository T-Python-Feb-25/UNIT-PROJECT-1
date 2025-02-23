import sqlite3
import emoji
from users import Users
import getpass
from colorama import Fore, Style
from datetime import datetime


class CalorieTracker:
    def __init__(self, username):
        self.username = username
        try:
            self.total_calories, self.consumed_calories = self.get_user_calories()
            self.calories = self.get_user_calories()
            if self.total_calories is None:
                print("The user does not exist in the database!")
                return
            print(
                f"\nHello {self.username}! Total daily calories: {int(self.total_calories)} Kcal"
            )

            print(f"Previously consumed calories: {self.consumed_calories} Kcal")
            self.remaining_calories()
        except Exception as e:
            print(f"Error initializing tracker:{e}")

    def get_user_calories(self):
        # Connect to the SQLite database
        try:
            con = sqlite3.connect("tutorial.db")
            cur = con.cursor()
            cur.execute(
                "SELECT total_calories, consumed_calories, height, weight, age, gender, activate_level FROM users WHERE username = ?",
                (self.username,),
            )
            user_data = cur.fetchone()
            con.close()

            if user_data:
                self.height, self.weight, self.age, self.gender, self.activate_level = (
                    user_data[2],
                    user_data[3],
                    user_data[4],
                    user_data[5],
                    user_data[6],
                )
                return user_data[0], user_data[1]
            return None, None
        except Exception as e:
            print(f"Error fetching user data: {e}")
            return None, None

    def reset_calories_if_new_day(self):
        """
         Reset calories consumed to 0 if it's a new day.
        Raises:
           Exception: If an error occurs while resetting calories.
        """
        try:
            con = sqlite3.connect("tutorial.db")
            cur = con.cursor()
            cur.execute(
                "SELECT last_updated FROM users WHERE username = ?", (self.username,)
            )
            last_updated = cur.fetchone()

            #from datetime import datetime

            today = datetime.today().date()

            if last_updated:
                last_date = datetime.strptime(last_updated[0], "%Y-%m-%d").date()
                print(emoji.emojiz(f":calendar: Last updated date: {last_date}"))
                print(emoji.emojiz(f":calendar: Today's date: {today}"))

                if last_date < today:
                    cur.execute(
                        "UPDATE users SET consumed_calories = 0, last_updated = ? WHERE username = ?",
                        (today, self.username),
                    )
                    con.commit()
                    print("✅ Calories reset executed!")

            else:
                print("⚠️ No last_updated data found for this user!")

            con.close()
        except Exception as e:
            print(f"Error resetting calories: {e}")

    def track_meal(self, meal_name, meal_calories):
        """
        Track meal and add calories to calories consumed.
            Args:
             meal_name (str): The name of the meal.
             meal_calories (float): Calories for the meal.

            Raises:
                ValueError: If an error occurred in the calorie value.
                Exception: If an error occurred while tracking the meal.
        """
        try:
            self.consumed_calories += meal_calories
            self.update_consumed_calories()
            print(f"Added {meal_calories} calories for {meal_name}")
            self.remaining_calories()
        except ValueError as e:
            print(f"Error tracking meal: {e}")
        except Exception as e:
            print(f"Error tracking meal: {e}")

    def remaining_calories(self):
        """
        Calculate and display the user's remaining calories.
         Raises:
                Exception: If an error occurred while calculating the remaining calories.
        """
        try:
            remaining = self.total_calories - self.consumed_calories
            if remaining < 0:
                print(
                    emoji.emojize(
                        f"You have exceeded the permissible limit by {abs(remaining):.2f} Kcal :angry_face:"
                    )
                )
            else:
                print(
                    emoji.emojize(
                        f"You have {remaining:.2f} Kcal remaining for today :thumbs_up:"
                    )
                )
        except Exception as e:
            print(f"Error calculating remaining calories: {e}")

    def load_user_data(self):
        """
        Load user data from the database.
        """
        try:
            con = sqlite3.connect("tutorial.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE username = ?", (self.username,))
            user_data = cur.fetchone()
            con.close()

            if user_data:
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
                ) = user_data
            else:
                print(
                    Fore.RED + "User data not found in the database." + Style.RESET_ALL
                )

        except Exception as e:
            print(Fore.RED + f"Error loading user data: {e}" + Style.RESET_ALL)

    def update_calories_after_recipe(self):
        """
        Update user data after adding calories from a recipe.

        """
        self.load_user_data()

    def update_consumed_calories(self):
        """
        Update calories consumed in the database.
          Raises:
              Exception: If an error occurred while updating the database.
        """
        try:
            con = sqlite3.connect("tutorial.db")
            cur = con.cursor()
            cur.execute(
                "UPDATE users SET consumed_calories = ? WHERE username = ?",
                (self.consumed_calories, self.username),
            )
            con.commit()
            con.close()
        except Exception as e:
            print(f"Error updating consumed calories: {e}")
