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
    exercise = string_input("Enter exercise name: ", 
                            "\nExercise name should only contain letters, hyphens, underscores, or spaces. Please try again.\n")

    sets = integer_input("Enter number of sets: ", 
                         "\nPlease enter a valid number for sets.\n")

    reps = integer_input("Enter repetitions per set: ", 
                         "\nPlease enter a valid number for repetitions.\n")

    weight = integer_input("Enter weight (kg/lbs): ", 
                           "\nPlease enter a valid number for weight.\n")

    while True:
        date_input = input("Enter workout date (YYYY-MM-DD): ").strip()
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d").strftime('%Y-%m-%d')
            break  
        except ValueError:
            print("\nInvalid date format. Please enter a valid date (YYYY-MM-DD).\n")

    workout_entry = {
        "date": date,  
        "exercise": exercise,
        "sets": sets,
        "reps": reps,
        "weight": weight
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
        print(f"🔢  Sets: {workout['sets']} | Reps: {workout['reps']} | Weight: {workout['weight']}kg")
        print("-" * 32)  

def search_workout():
    ''' Search for a workout by exercies name '''

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
            print("-" * 32)  # Divider after each result
    else:
        print("\n❌ No matching workouts found.\n")


