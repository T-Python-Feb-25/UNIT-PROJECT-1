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

def calculate_calories(exercise, sets, reps, weight):
    
    MET_values = {} # Metabolic Equivalent of Task

    MET = MET_values.get(exercise.lower(), 5.0)  
    duration = (sets * reps) / 30  # Estimation duration in minutes
    calories_burned = MET * 3.5 * weight / 200 * duration  # Basic calorie formula

    return round(calories_burned, 2)

    
def calculate_workout_time(sets:int, time_per_set:int =1, rest_time:int = 30) -> int:
    """Estimate the total time spent on a workout based on sets and reps."""
    # Assuming 1 minute per set as a simple estimate
    total_time = (sets * time_per_set) + ((sets - 1) * rest_time / 60)  # Convert seconds to minutes
    return round(total_time)


