import json
import random
from DataStorage import load_data, save_data
from datetime import datetime



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
        "1": {"name": "Strength Training", "duration": "45-60 min", "calories_burned": "250-400 kcal"},
        "2": {"name": "Running", "duration": "30-45 min", "calories_burned": "400-800 kcal"},
        "3": {"name": "Obstacle Course Training", "duration": "45-60 min", "calories_burned": "500-1000 kcal"},
        "4": {"name": "Resistance Band Training", "duration": "30-45 min", "calories_burned": "200-400 kcal"},
        "5": {"name": "Calisthenics (Bodyweight Training)", "duration": "30-60 min", "calories_burned": "300-600 kcal"},
        "6": {"name": "Trampoline Workout", "duration": "20-40 min", "calories_burned": "250-500 kcal"},
        "7": {"name": "HIIT", "duration": "20-30 min", "calories_burned": "350-600 kcal"},
        "8": {"name": "Yoga", "duration": "30-60 min", "calories_burned": "150-300 kcal"},
        "9": {"name": "Cycling", "duration": "40-60 min", "calories_burned": "400-700 kcal"},
        "10": {"name": "Tennis", "duration": "50-60 min", "calories_burned": "600-900 kcal"},
        "11": {"name": "Jump Rope", "duration": "10-20 min", "calories_burned": "200-400 kcal"},
        "12": {"name": "Rowing", "duration": "30-45 min", "calories_burned": "300-600 kcal"},
        "13": {"name": "Swimming", "duration": "30-60 min", "calories_burned": "350-700 kcal"},
        "14": {"name": "Pilates", "duration": "30-45 min", "calories_burned": "200-400 kcal"},
        "15": {"name": "Boxing", "duration": "30-45 min", "calories_burned": "400-700 kcal"},
        "16": {"name": "Dance Workout", "duration": "30-60 min", "calories_burned": "300-600 kcal"},
        "17": {"name": "Hiking", "duration": "60-120 min", "calories_burned": "400-900 kcal"},
        "18": {"name": "Stair Climbing", "duration": "20-40 min", "calories_burned": "400-800 kcal"},
        "19": {"name": "CrossFit", "duration": "30-60 min", "calories_burned": "500-900 kcal"},
        "20": {"name": "Back to Main Menu"}
    }
    
    while True:
        print("\n📌 Workout Categories:")
        for key, workout in workouts.items():
            print(f"{key}. {workout['name']}")

        choice = input("\nSelect a workout (1-20): ").strip()
        
        if choice in workouts:
            if choice == "20":
                print("\nReturning to Main Menu...")
                break
            else:
                selected = workouts[choice]
                print(f"\n🏋️   Workout: {selected['name']}")
                print(f"⏳  Duration: {selected['duration']}")
                print(f"🔥  Estimated Calories Burned: {selected['calories_burned']}")
                print("💪  Just do it ")

        else:
            print("\n❌ Invalid choice. Please select a number from the list.")


def log_workout():
    exercise = string_input("\nEnter exercise name:\n ", 
                            "\nExercise name should only contain letters, hyphens, underscores, or spaces. Please try again.\n")

    sets = integer_input("\nEnter number of sets:\n ", 
                         "\nPlease enter a valid number for sets.\n")

    reps = integer_input("\nEnter repetitions per set:\n ", 
                         "\nPlease enter a valid number for repetitions.\n")

    weight = integer_input("\nEnter weight (kg/lbs):\n ", 
                           "\nPlease enter a valid number for weight.\n")
    
    workout_time = calculate_workout_time(sets, reps)
    print(f"\n🕒 Estimated Workout Time: {workout_time} minutes")


    while True:
        date_input = input("\nEnter workout date (YYYY-MM-DD):\n ").strip()
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d").strftime('%Y-%m-%d')
            break  
        except ValueError:
            print("\nInvalid date format. Please enter a valid date (YYYY-MM-DD).\n")

    calories = calculate_calories(exercise, sets, reps, weight)

    workout_entry = {
        "date": date,  
        "exercise": exercise,
        "sets": sets,
        "reps": reps,
        "weight": weight,
        "calories_burned": calories
    }

    data = load_data()
    data.append(workout_entry)
    save_data(data)
    
    print("\nWorkout has been logged successfully")

def view_workout():
    data = load_data()
    if not data:
        print("No workouts logged until now! ")
        return
    else:
         print("\n📜 Workout History:\n" + "-" * 32)  
    for workout in data:
        print(f"📅  Date: {workout['date']}")
        print(f"🏋️   Exercise: {workout['exercise']}")
        print(f"🔢  Sets: {workout['sets']} | Reps: {workout['reps']} | Weight: {workout['weight']}kg | 🔥 {workout['calories_burned']} cal")
        print("-" * 32)  

def search_workout():

    ''' Search for a workout by exercise name '''

    search_term = input("Enter exercise name to search: ").strip().lower()
    data = load_data()
    results = []

    for w in data:
        if w["exercise"].strip().lower() == search_term:  
            results.append(w)
        
    if results: 
        print("\n🔍 Search Results:\n" + "-" * 32)  
        for workout in results:
            print(f"📅  Date: {workout['date']}")
            print(f"🏋️   Exercise: {workout['exercise']}")
            print(f"🔢  Sets: {workout['sets']} | Reps: {workout['reps']} | Weight: {workout['weight']}kg")
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
    print("-" * 32)
    
    # Display workouts with an index
    for index, workout in enumerate(data, start=1):
        print(f"{index}. 📅 {workout['date']} | 🏋️ {workout['exercise']} | 🔢 {workout['sets']} sets x {workout['reps']} reps | ⚖ {workout['weight']} kg/lbs")

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

    # Confirm deletion
    confirm = input(f"\n⚠ Are you sure you want to delete workout {choice}? (yes/no): ").strip().lower()
    if confirm == "yes":
        deleted_workout = data.pop(choice - 1)
        save_data(data)
        print(f"\n✅ Workout '{deleted_workout['exercise']}' on {deleted_workout['date']} deleted successfully.")
    else:
        print("\n✅ Deletion cancelled.")



def calculate_calories(exercise, sets, reps, weight):
    
    MET_VALUES = {
        "running": 9.8, "cycling": 8.0, "jump rope": 12.0,
        "push-up": 4.0, "squats": 5.0, "pull-up": 5.0,
        "lunges": 5.5, "burpees": 8.0, "plank": 3.5
    }

    exercise_lower = exercise.lower()

    # Check if the exercise is bodyweight/cardio (no weight used)
    if exercise_lower in MET_VALUES:
        met = MET_VALUES[exercise_lower]
        duration_min = (sets * reps) / 30  # Estimate: 30 reps = 1 min
        calories_burned = met * 3.5 * 70 / 200 * duration_min  # 70kg as average body weight
    else:
        # Strength training calorie formula (if weight is used)
        calories_burned = (sets * reps * weight) * 0.1  

    return round(calories_burned, 2)

    
def calculate_workout_time(sets:int, time_per_set:int =1, rest_time:int = 30) -> int:
    """Estimate the total time spent on a workout based on sets and reps."""
    # Assuming 1 minute per set as a simple estimate
    total_time = (sets * time_per_set) + ((sets - 1) * rest_time / 60)  # Convert seconds to minutes
    return round(total_time)
