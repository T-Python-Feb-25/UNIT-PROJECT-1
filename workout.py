import json
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
    """ Suggests a random workout challenge """
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
    """ Search for a workout by exercise or workout category name """
    
    search_term = input("Enter workout/exercise name to search: ").strip().lower()
    data = load_data()
    results = []

    for w in data:
        workout_name = w.get("exercise", w.get("workout", "")).strip().lower()  # Check both keys
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
    """Deletes a workout entry based on user selection."""
    data = load_data()

    if not data:
        print("\n❌ No workouts logged yet!")
        return

    print("\n🗑 Delete a Workout")
    print("-" * 40)
    
    for index, workout in enumerate(data, start=1):
        date = workout.get("date", "N/A")
        if "exercise" in workout:  # Logged workout
            print(f"{index}. 📅 {date} | 🏋️ {workout['exercise']} | 🔢 {workout['sets']} sets x {workout['reps']} reps | ⚖ {workout['weight']} kg/lbs")
        else:  # Workout category
            print(f"{index}. 📅 {date} | 🏋️ {workout.get('workout', 'N/A')} | ⏳ {workout.get('time_spent', 'N/A')} | 🔥 {workout.get('calories_burned', 'N/A')} kcal")

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
    
    MET_values = {} 

    MET = MET_values.get(exercise.lower(), 5.0)  
    duration = (sets * reps) / 30  
    calories_burned = MET * 3.5 * weight / 200 * duration  

    return round(calories_burned, 2)

    
def update_best_record(exercise, weight):
    data = load_data()
    
    best_records = {w["exercise"]: w["weight"] for w in data if "exercise" in w and "weight" in w}
    if exercise not in best_records or weight > best_records.get(exercise, 0):
        print(f"\n🎯 New record for {exercise}! Highest weight lifted: {weight} kg/lbs\n")
        return weight
    return best_records[exercise]

def view_best_records():
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

    





