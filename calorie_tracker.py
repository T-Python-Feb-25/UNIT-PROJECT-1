from datetime import datetime, timedelta
from file_manager import load_data, save_data
from tabulate import tabulate
import matplotlib.pyplot as plt
from colorama import Fore


def log_meal(current_user):
    """Logs a new meal entry for the current user, recording meal name, calorie count,
    date, and time.

    Parameters:
    current_user (str): The username of the logged-in user.

    Returns:
    None: Displays messages and updates the log file but does not return a value.
    """
    if not current_user:
        print(Fore.RED+"You must log in first.")
        return

    meal_name = input(Fore.BLUE+"Enter meal name: ").strip().title().lower()
    if not meal_name:
        raise ValueError(Fore.RED+"Meal name cannot be empty.")

    while True:
        try:
            calories = int(input(Fore.BLUE+"Enter calorie : ").strip())
            if calories <= 0:
                print(Fore.RED+"Calories must be a positive number.")
            else:
                break
        except ValueError:
            print(Fore.RED+"Invalid input. Please enter a number.")


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

    print(Fore.LIGHTGREEN_EX+f"Meal '{meal_name}' logged successfully at {current_time}.")



def view_meal(current_user):
    """
    Displays the logged meals for the current user based on the selected date.

    Parameters:
        current_user (str): The username of the logged-in user.

    Returns:
        None: The function prints meal data but does not return any values.
    """

    if not current_user:
        print(Fore.RED+"You must log in first.")
        return
    calorie_logs = load_data("dataStorage/calorie_log.json")

    try:
        c= int(input(Fore.BLUE+"\nDo you want to view meals:\n(1) Today\n(2) By a specific date\nChoice (1 or 2): "))
    except ValueError:
        print(Fore.RED+"Invalid input. Please enter 1 or 2.")
        return

    if c == 1:
        todaydate =datetime.now().strftime("%Y-%m-%d")
        today_meals = []
        for meal in calorie_logs:
            if meal["user"] == current_user and meal["date"] == todaydate :
                today_meals.append(meal)
        if not today_meals:
            print(Fore.RED+"\nNo meals logged for today.")
            return

        print(Fore.MAGENTA+f"\nMeals logged for today ({todaydate}):\n")

        table=[]
        headers = [Fore.YELLOW+"Meal", "Calories (kcal)", "Time"]

        today_calories=0
        for meal in today_meals:
            today_calories+=meal["calories"]
            table.append([Fore.MAGENTA+meal["meal"], Fore.MAGENTA+str(meal["calories"]), Fore.MAGENTA+str(meal["time"])])
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
        print(Fore.MAGENTA+f"\nYou have consumed a total of **{today_calories} kcal** today.")
        print("-" * 40)
    elif c == 2:

        date1 = input(Fore.GREEN+"enter the date you want to view meals for: in this format please: YYYY-MM-DD : ")
        try:
            datetime.strptime(date1, "%Y-%m-%d")
        except ValueError:
            print(Fore.RED+"Invalid date format. Please use YYYY-MM-DD.")
            return

        date_meals=[]
        for meal in calorie_logs:
            if meal["user"] == current_user and meal["date"] == date1:
                date_meals.append(meal)
        if not date_meals:
            print(Fore.RED+"\nNo meals logged for this date.")
            return



        print(Fore.MAGENTA+f"\nMeals logged for today ({date1}):\n")

        tablee = []
        headerss = [Fore.YELLOW+"Meal", "Calories (kcal)", "Time"]

        for meal in date_meals:
            tablee.append([meal["meal"], meal["calories"], meal["time"]])
        print(tabulate(tablee, headers=headerss, tablefmt="fancy_grid"))
        print("-" * 40)

    else:
        print(Fore.RED+"Invalid input. Please enter a valid number (1 or 2)")



def edit_delete_meal(current_user):
    """
    Allows the current user to edit or delete a meal they logged.

    Parameters:
        current_user (object): The logged-in user. If no user is logged in, the function prompts to log in.

    Returns:
        None: If the user is logged in, it allows them to edit or delete a meal. If the meal is edited or deleted, the calorie log is updated accordingly.
    """

    if not current_user:
        print(Fore.RED+"You must log in first.")
        return
    calorie_logs = load_data("dataStorage/calorie_log.json")
    print(Fore.YELLOW + "=" * 40)
    print("----Editing or Deleting a Meal----")
    print(Fore.YELLOW + "=" * 40)

    try:
        e = int(input(Fore.BLUE +"Do you want to edit or delete a meal?\n(1) Edit\n(2) Delete\nChoice (1 or 2): "))
    except ValueError:
        print(Fore.RED +"Invalid input. Please enter 1 or 2.")
        return
    if e == 1:
        meal = input(Fore.BLUE +"Enter meal name to edit: ").strip().lower()
        found=False
        for m in calorie_logs:
            if meal == m["meal"].lower():
                found=True
                c=int(input(Fore.BLUE +"What do you want to change:\n(1) Meal Name\n(2) Calories\nChoice: "))
                if c == 1:
                    m["meal"] = input(Fore.BLUE +"Enter new meal name: ").strip().lower()
                elif c == 2:
                    try:
                        m["calories"] = int(input(Fore.BLUE +"Enter new calories: "))
                    except ValueError:
                        print(Fore.RED +"Invalid input. Please enter a number.")
                save_data("dataStorage/calorie_log.json", calorie_logs)
                print(Fore.GREEN +f"Meal '{meal}' edited successfully.")
                break
        if not found:
            print(Fore.RED +"Meal not found in your logs..")



        elif e == 2:
            meal = input(Fore.BLUE +"Enter meal name to delete: ").strip().lower()
            found_meal = None
            for m in calorie_logs:
                if meal == m["meal"].lower():
                    found_meal = m
                    break
            if found_meal:
                confirm = input(Fore.YELLOW + f"Are you sure you want to delete '{found_meal['meal']}'? (yes/no): ").lower()
                if confirm == 'yes':
                    calorie_logs.remove(found_meal)
                    save_data("dataStorage/calorie_log.json", calorie_logs)
                    print(Fore.GREEN +f"Meal '{meal}' deleted successfully.")
                else:
                    print(Fore.RED +"Deletion cancelled. ")
            else:
                print(Fore.RED +"Meal not found in your logs.")


def plot_calories(current_user):
    """
    Generates and displays a line graph showing the total calories consumed by the current user
    over the past 5 days, including today.


    Parameters:
        current_user (str): The username of the user whose calorie intake will be plotted.

    Returns:
        None: Displays a matplotlib graph.
    """

    calorie_logs = load_data("dataStorage/calorie_log.json")

    todaydate = datetime.now().date()

    fivedaysago = todaydate - timedelta(days=6)

    caloriesum = {}

    for meal in calorie_logs:
        if meal["user"] == current_user:
            meal_date = datetime.strptime(meal["date"], "%Y-%m-%d").date()
            if fivedaysago <= meal_date <= todaydate:
                if meal_date in caloriesum:
                    caloriesum[meal_date] += meal["calories"]
                else:
                    caloriesum[meal_date] = meal["calories"]

    dates = []
    calories = []

    for i in range(7):
        date = fivedaysago + timedelta(days=i)
        dates.append(date)
        calories.append(caloriesum.get(date, 0))

    plt.figure(figsize=(10, 7))

    plt.plot(dates, calories, marker='o', markerfacecolor='k', linestyle='-', color='c')
    plt.title(f"Calories Consumed Last week for {current_user}", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Calories (kcal)", fontsize=12)
    plt.ylim(0, 2500)

    plt.grid(True)
    plt.show()

