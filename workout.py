import random
import time
from DataStorage import load_data, save_data
from datetime import datetime, timedelta



def string_input(msg, error_msg):
    while True:
        output = input(msg).strip()
        if output.replace("-", "").replace("_", "").replace(" ", "").isalpha():
            return output
        else:
            print(error_msg)

def integer_input(msg, error_msg):
    while True:
        try:
            output = int(input(msg).strip())
            return output
        except ValueError:
            print(error_msg)

def random_workout_challenge():
    """
    The function randomly selects a workout challenge from a list of various exercises

    """
    challenges = [
        "💥 Do 20 push-ups!",
        "🏃 Run for 10 minutes!",
        "🔥 Hold a 60-second plank!",
        "🦵 Do 50 bodyweight squats!",
        "💪 Complete 3 sets of 15 bicep curls!",
        "🚴 Ride a bike for 15 minutes!",
        "🏋️ Try lifting 5kg more than usual!",
        "🧘 Hold a deep squat for 30 seconds!",
        "🤸 Do 20 jumping jacks to warm up!",
        "🏃 Run in place for 2 minutes!",
        "🧘 Stretch for 5 minutes before starting!",
        "🛑 Take a rest day if you need it!"
    ]

    challenge = random.choice(challenges)
    print("\n🎲 Random Workout Challenge 🎲")
    print("-" * 32)
    print(f"{challenge}")
    print("-" * 32)


def workout_categories():
    """
    Displays a list of workout categories and allows the user to select one to start a workout timer.
    """
    workouts = {
        "1": {"name": "Strength Training", "calories_burned": (250, 400)},
        "2": {"name": "Running", "calories_burned": (400, 800)},
        "3": {"name": "Obstacle Course Training", "calories_burned": (500, 1000)},
        "4": {"name": "Resistance Band Training", "calories_burned": (200, 400)},
        "5": {"name": "Calisthenics (Bodyweight Training)", "calories_burned": (300, 600)},
        "6": {"name": "HIIT", "calories_burned": (350, 600)},
        "7": {"name": "Yoga", "calories_burned": (150, 300)},
        "8": {"name": "Cycling", "calories_burned": (400, 700)},
        "9": {"name": "Jump Rope", "calories_burned": (200, 400)},
        "10": {"name": "Swimming", "calories_burned": (350, 700)},
        "11": {"name": "Boxing", "calories_burned": (400, 700)},
        "12": {"name": "Dance Workout", "calories_burned": (300, 600)},
        "13": {"name": "Hiking", "calories_burned": (400, 900)},
        "14": {"name": "CrossFit", "calories_burned": (500, 900)},
        "15": {"name": "Rowing Machine", "calories_burned": (300, 600)},
        "16": {"name": "Pilates", "calories_burned": (180, 350)},
        "17": {"name": "Martial Arts", "calories_burned": (500, 800)},
        "18": {"name": "Tennis", "calories_burned": (400, 700)},
        "19": {"name": "Stair Climbing", "calories_burned": (400, 800)},
        "20": {"name": "Elliptical Trainer", "calories_burned": (300, 600)},
        "21": {"name": "Powerlifting", "calories_burned": (250, 500)},
        "22": {"name": "Parkour", "calories_burned": (500, 1000)},
        "23": {"name": "Skating (Roller/Inline)", "calories_burned": (300, 700)},
        "24": {"name": "Wall Climbing (Indoor/Outdoor)", "calories_burned": (400, 800)},
        "25": {"name": "Football (Soccer)", "calories_burned": (450, 900)},
        "26": {"name": "Basketball", "calories_burned": (500, 800)},
        "27": {"name": "Badminton", "calories_burned": (350, 600)},
        "28": {"name": "Table Tennis", "calories_burned": (200, 400)},
        "29": {"name": "Horseback Riding", "calories_burned": (200, 500)},
        "30": {"name": "Golf (Walking & Carrying Clubs)", "calories_burned": (250, 500)},
        "31": {"name": "Surfing", "calories_burned": (250, 600)},
        "32": {"name": "Skiing/Snowboarding", "calories_burned": (400, 900)},
        "33": {"name": "Ultimate Frisbee", "calories_burned": (400, 700)},
        "34": {"name": "Wrestling", "calories_burned": (500, 900)},
        "35": {"name": "Back to Main Menu"}
    }
    
    
    
    while True:
        print("\n📌 Workout Categories:")
        for key, workout in workouts.items():
            print(f"{key}. {workout['name']}")

        choice = input("\nSelect a workout (1-35): ").strip()
        
        if choice in workouts:
            if choice == "35":
                print("\nReturning to Main Menu...")
                break

            workout_name = workouts[choice]["name"]
            calorie_range = workouts[choice]["calories_burned"]
            start_workout_timer(workout_name, calorie_range)
        else:
            print("\n❌ Invalid choice. Please select a number from the list.")

def start_workout_timer(workout_name, calorie_range):
    """
    Starts a workout timer for the specified workout, calculates the time spent and calories burned, 
    and saves the workout data.
    Args:
        workout_name (str): The name of the workout.
        calorie_range (tuple): A tuple containing the minimum and maximum calories burned per hour for the workout.
    Prints:
        A message indicating the start of the workout timer and prompts the user to press Enter to stop the timer.
        A message indicating the completion of the workout, the time spent, and the calories burned.
    Saves:
        The workout data including the date, workout type, workout name, time spent, and calories burned.
    """
    print(f"\n⏳ Starting {workout_name} workout timer... Press Enter to stop when you're done.")

    start_time = time.time()
    input()  
    end_time = time.time()

    elapsed_time = end_time - start_time  
    minutes = round(elapsed_time / 60, 2)

    calories_burned = round(random.uniform(*calorie_range) * (minutes / 60), 2)

    print(f"\n✅ Workout Completed! You spent {minutes} min on {workout_name}, burning 🔥 {calories_burned} kcal.")

    data = load_data()
    data.append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "type": "category",
        "workout": workout_name,
        "time_spent": f"{minutes} min",
        "calories_burned": f"{calories_burned} kcal"
    })
    save_data(data)



def log_workout():
    """
    Logs a workout session by prompting the user for exercise details, calculating calories burned,
    updating the best weight record, and saving the workout entry.
 
    """
    exercise = string_input("\nEnter exercise name:\n ", 
                            "\nExercise name should only contain letters, hyphens, underscores, or spaces. Please try again.\n")

    sets = integer_input("\nEnter number of sets:\n ", 
                         "\nPlease enter a valid number for sets.\n")

    reps = integer_input("\nEnter repetitions per set:\n ", 
                         "\nPlease enter a valid number for repetitions.\n")

    weight = integer_input("\nEnter weight (kg/lbs):\n ", 
                           "\nPlease enter a valid number for weight.\n")
    


    calories = calculate_calories(exercise, sets, reps, weight)
    best_weight = update_best_record(exercise, weight)


    workout_entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "type": "logged",
        "exercise": exercise,
        "sets": sets,
        "reps": reps,
        "weight": weight,
        "calories_burned": calories, 
        "best_weight": best_weight       
    }

    data = load_data()
    data.append(workout_entry)
    save_data(data)
    
    print("\nWorkout has been logged successfully")

def view_workout():
    """
    Displays the workout history by loading data from a data source.
    The function checks if there is any workout data available. If no data is found,
    it prints a message indicating that no workouts have been logged yet. If data is found,
    it prints the workout history in a formatted manner.
    
    """
    data = load_data()
    if not data:
        print("\n📂 No workouts logged yet!")
        return

    print("\n📜 Workout History:\n" + "-" * 40)
    for workout in data:
        print(f"📅  Date: {workout['date']}")

        if "type" in workout and workout["type"] == "logged":
            print(f"🏋️  Exercise: {workout['exercise']}")
            print(f"🔢  Sets: {workout['sets']} | Reps: {workout['reps']} | Weight: {workout['weight']} kg/lbs")
            print(f"🔥  Calories Burned: {workout.get('calories_burned', 'N/A')} kcal")
            print(f"🏆  Best Weight: {workout.get('best_weight', 'N/A')} kg/lbs")
        else:
            print(f"🏋️  Workout: {workout.get('workout', 'N/A')}")
            print(f"⏳ Time Spent: {workout.get('time_spent', 'N/A')} | 🔥 Calories Burned: {workout.get('calories_burned')}")

        print("-" * 40)



def search_workout():
    """
    Search for a workout by exercise or workout category name,
    Prompts the user to enter a workout or exercise name to search for. 
    The search term is then compared against the 'exercise' and 'workout' keys 
    in the data loaded from the data source. 
    """
    
    search_term = input("Enter workout/exercise name to search: ").strip().lower()
    data = load_data()
    results = []

    for w in data:
        workout_name = w.get("exercise", w.get("workout", "")).strip().lower()  
        if workout_name == search_term:
            results.append(w)

    if results: 
        print("\n🔍 Search Results:\n" + "-" * 32)  
        for workout in results:
            print(f"📅  Date: {workout['date']}")
            if "exercise" in workout:  
                print(f"🏋️  Exercise: {workout['exercise']}")
                print(f"🔢  Sets: {workout['sets']} | Reps: {workout['reps']} | Weight: {workout['weight']} kg")
            else:  
                print(f"🏋️  Workout: {workout.get('workout', 'N/A')}")
                print(f"⏳ Time Spent: {workout.get('time_spent', 'N/A')} | 🔥 Calories Burned: {workout.get('calories_burned', 'N/A')}")
            print("-" * 32) 
    else:
        print("\n❌ No matching workouts found.\n")

def delete_workout():
    """
    This function loads the workout data, displays the list of logged workouts,
    and prompts the user to select a workout to delete. The user can cancel the
    deletion process at any time. 
    """
    data = load_data()

    if not data:
        print("\n❌ No workouts logged yet!")
        return

    print("\n🗑 Delete a Workout")
    print("-" * 40)
    
    for index, workout in enumerate(data, start=1):
        date = workout.get("date", "N/A")
        if "exercise" in workout:  
            print(f"{index}. 📅 {date} | 🏋️ {workout['exercise']} | 🔢 {workout['sets']} sets x {workout['reps']} reps | ⚖ {workout['weight']} kg/lbs")
        else:  
            print(f"{index}. 📅 {date} | 🏋️ {workout.get('workout', 'N/A')} | ⏳ {workout.get('time_spent', 'N/A')} | 🔥 {workout.get('calories_burned')}")

    while True:
        try:
            choice = int(input("\nEnter the number of the workout to delete (press 0 to cancel): "))
            if choice == 0:
                print("\n✅ Deletion cancelled.")
                return  
            if 1 <= choice <= len(data):
                break
            else:
                print("\n❌ Invalid choice. Enter a valid number.")
        except ValueError:
            print("\n❌ Please enter a valid number.")

    confirm = input(f"\n⚠ Are you sure you want to delete workout {choice}? (yes/no): ").strip().lower()
    if confirm == "yes":
        deleted_workout = data.pop(choice - 1)
        save_data(data)
        print(f"\n✅ Workout '{deleted_workout.get('exercise', deleted_workout.get('workout', 'N/A'))}' on {deleted_workout.get('date', 'N/A')} deleted successfully.")
    else:
        print("\n✅ Deletion cancelled.")


def calculate_calories(exercise, sets, reps, weight):
    """
    Calculate the number of calories burned during a workout.
    - The MET (Metabolic Equivalent of Task) values are used to estimate the energy expenditure for different exercises.
    - If the exercise is not found in the predefined MET values, a default MET value of 5.0 is used.
    """
    
    MET_values = {
        "push-ups": 8.0,
        "running": 11.5,
        "plank": 3.8,
        "squats": 5.0,
        "bicep curls": 3.0,
        "cycling": 7.5,
        "lifting": 6.0,
        "jumping jacks": 8.0,
        "stretching": 2.5,
        "rest": 1.0
    }

    MET = MET_values.get(exercise.lower(), 5.0)  
    duration = (sets * reps) / 60  
    calories_burned = MET * 3.5 * weight / 200 * duration

    return round(calories_burned, 2)

    
def update_best_record(exercise, weight):
    """
    Updates the best record for a given exercise if the provided weight is higher than the current record.
    
    """
    data = load_data()
    
    best_records = {w["exercise"]: w["weight"] for w in data if "exercise" in w and "weight" in w}
    if exercise not in best_records or weight > best_records.get(exercise, 0):
        best_records[exercise] = weight
        print(f"\n🎯 New record for {exercise}! Highest weight lifted: {weight} kg/lbs\n")
        return weight
    return best_records[exercise]

def view_best_records():
    """
    Displays the best workout records from the logged data.
    This function loads workout data, processes it to find the best records
    for each exercise.
    """
    data = load_data()
    
    if not data:
        print("\nNo workouts logged yet! 🏋️‍♂️")
        return

    best_records = {}  

    for workout in data:
        exercise = workout.get("exercise")
        weight = workout.get("weight")
        if exercise is None or weight is None:
            continue

        if exercise not in best_records or weight > best_records[exercise]:
            best_records[exercise] = weight

    print("\n🏆 Best Workout Records 🏆")
    print("--------------------------------")
    for exercise, weight in best_records.items():
        print(f"🏋️ {exercise}: {weight} kg/lbs")
    print("--------------------------------")


def weekly_statistics():
    """
    Calculate and display weekly workout statistics based on logged workout data.
    This function loads workout data, filters it to include only the workouts
    from the last 7 days, and then calculates various statistics including:
    - Total number of workouts logged in the last week.
    - Total calories burned in the last week.
    - Most frequent exercise performed in the last week.
    - Most frequent workout category in the last week.
    - Best record based on weight and calories burned.
    """
    
    data = load_data()
    
    if not data:
        print("\nNo workouts logged yet! 🏋️‍♂️")
        return

    today = datetime.today()
    last_week = today - timedelta(days=7)
    
    weekly_data = [w for w in data if datetime.strptime(w["date"], "%Y-%m-%d") >= last_week]

    if not weekly_data:
        print("\nNo workouts recorded in the last 7 days! 📆")
        return

    total_workouts = len(weekly_data)
    

    def extract_calories(value):
        if isinstance(value, str):  
            return float(value.split()[0])  
        return float(value)  

    total_calories = sum(extract_calories(w["calories_burned"]) for w in weekly_data if "calories_burned" in w)

    exercise_counts = {}
    category_counts = {}

    for w in weekly_data:
        if "exercise" in w:
            exercise_counts[w["exercise"]] = exercise_counts.get(w["exercise"], 0) + 1
        
        if "workout" in w:
            category_counts[w["workout"]] = category_counts.get(w["workout"], 0) + 1

    most_frequent_exercise = max(exercise_counts, key=exercise_counts.get, default="N/A")
    most_frequent_category = max(category_counts, key=category_counts.get, default="N/A")

    best_record = max(weekly_data, key=lambda w: (float(w.get("weight", 0)), extract_calories(w.get("calories_burned", 0))), default=None)

    print("\n📊 Weekly Workout Statistics 📊")
    print("--------------------------------")
    print(f"📅 Workouts Logged: {total_workouts}")
    print(f"🔥 Total Calories Burned: {total_calories:.2f} kcal")
    print(f"🏋️ Most Frequent Exercise: {most_frequent_exercise}")
    print(f"🏆 Most Frequent Workout Category: {most_frequent_category}")
    
    if best_record:
        weight = best_record.get("weight", "N/A")
        calories_burned = extract_calories(best_record.get("calories_burned", 0))
        print(f"💪 Best Record: Exercise - {best_record['exercise']} | Weight: {weight} | Calories Burned: {calories_burned}")
    else:
        print("❌ No best record found.")
    print("--------------------------------")


