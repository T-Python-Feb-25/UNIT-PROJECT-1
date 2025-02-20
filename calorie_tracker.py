import sqlite3
import emoji
from users import Users
import getpass
class CalorieTracker:
  def __init__(self, username):
    self.username = username
    self.total_calories, self.consumed_calories = self.get_user_calories()
    #self.calorie_goal = self.get_user_goal()
    self.calories = self.get_user_calories()

    if self.total_calories is None:
      print("The user does not exist in the database!")
      return 
    print(f"\nHello {self.username}! Total daily calories: {self.total_calories} Kcal")
    print(f"\nHello {self.username}! Total daily calories: {self.calories} Kcal")

    print(f"Previously consumed calories: {self.consumed_calories} Kcal")
    self.remaining_calories()

  def get_user_calories(self):
    # Connect to the SQLite database
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("SELECT total_calories, consumed_calories, height, weight, age, gender, activate_level FROM users WHERE username = ?", (self.username,))
    user_data = cur.fetchone()
    con.close()

    if user_data:
      self.height, self.weight, self.age, self.gender, self.activate_level = user_data[2], user_data[3], user_data[4], user_data[5], user_data[6]
      return user_data[0], user_data[1]
    return None, None


  def track_meal(self, meal_name, meal_calories):
    # Fuction that allows the user to enter the calories of this meals
    self.consumed_calories += meal_calories
    self.update_consumed_calories()
    print(f"Added {meal_calories} calories for {meal_name}")
    self.remaining_calories()

  def remaining_calories(self):
    remaining = self.total_calories - self.consumed_calories
    if remaining < 0:
     print(emoji.emojize(f"You have exceeded the permissible limit by {abs(remaining):.2f} Kcal :angry_face:"))
    else:
      print(emoji.emojize(f"You have {remaining:.2f} Kcal remaining for today :thumbs_up:"))

  def update_consumed_calories(self):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("UPDATE users SET consumed_calories = ? WHERE username = ?", (self.consumed_calories, self.username))
    con.commit()
    con.close()




username = Users.login()  

if username:
    tracker = CalorieTracker(username)
    while True:
        menu = {
            1: "Add meal", 
            2: "View remaining calories",
            3: "View consumed calories",
            4: "Exit"
        }
        print("\nMenu")
        choice = input("Enter your choice: ")

        if choice == "1":
            meal_name = input("Enter meal name (e.g., Breakfast, Lunch, Dinner): ")
            calorie = int(input(f"Enter your calorie for {meal_name}: "))
            tracker.track_meal(meal_name, calorie)
        
        elif choice == "2":
            tracker.remaining_calories()
        
        elif choice == "3":
            print(f"Consumed calories so far: {tracker.consumed_calories} Kcal")
        
        elif choice == "4":
            print("Thank you for using the app!")
            break
        else:
            print("Invalid choice")
else:
    print("Invalid username or password.")
