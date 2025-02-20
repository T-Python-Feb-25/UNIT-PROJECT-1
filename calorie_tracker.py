from datetime import datetime,timedelta
from file_manager import load_data, save_data
from tabulate import tabulate

def log_meal(current_user):
    """Logs a new meal for the current user."""
    if not current_user:
        print("You must log in first.")
        return

    meal_name = input("Enter meal name: ").strip().title().lower()
    if not meal_name:
        raise ValueError("Meal name cannot be empty.")

    while True:
        try:
            calories = int(input("Enter calorie count: ").strip())
            if calories <= 0:
                print("Calories must be a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")


    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%I:%M %p")

    calorie_logs = load_data("dataStorage/calorie_log.json")

    new_meal = {
        "user": current_user,
        "meal": meal_name,
        "calories": calories,
        "date": current_date,
        "time": current_time
    }

    calorie_logs.append(new_meal)
    save_data("dataStorage/calorie_log.json", calorie_logs)

    print(f"Meal '{meal_name}' logged successfully at {current_time}.")



def view_meal(current_user):
    if not current_user:
        print("You must log in first.")
        return
    calorie_logs = load_data("dataStorage/calorie_log.json")

    try:
        c= int(input("\nDo you want to view meals:\n(1) Today\n(2)By a specific date\nChoice (1 or 2): "))
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")
        return

    if c == 1:
        todaydate =datetime.now().strftime("%Y-%m-%d")
        today_meals = []
        for meal in calorie_logs:
            if meal["user"] == current_user and meal["date"] == todaydate :
                today_meals.append(meal)
        if not today_meals:
            print("\nNo meals logged for today.")
            return

        print(f"\nMeals logged for today ({todaydate}):\n")

        table=[]
        headers = ["Meal", "Calories (kcal)", "Time"]

        today_calories=0
        for meal in today_meals:
            today_calories+=meal["calories"]
            table.append([meal["meal"], meal["calories"], meal["time"]])
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
        print(f"\nYou have consumed a total of **{today_calories} kcal** today.")
        print("-" * 40)
    elif c == 2:

        date1 = input("enter the date you want to view meals for: in this format please: YYYY-MM-DD : ")
        try:
            datetime.strptime(date1, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        date_meals=[]
        for meal in calorie_logs:
            if meal["user"] == current_user and meal["date"] == date1:
                date_meals.append(meal)
        if not date_meals:
            print("\nNo meals logged for this date.")
            return



        print(f"\nMeals logged for today ({date1}):\n")

        tablee = []
        headerss = ["Meal", "Calories (kcal)", "Time"]

        for meal in date_meals:
            tablee.append([meal["meal"], meal["calories"], meal["time"]])
        print(tabulate(tablee, headers=headerss, tablefmt="fancy_grid"))
        print("-" * 40)

    else:
        print("Invalid input. Please enter a valid number (1 or 2)")
