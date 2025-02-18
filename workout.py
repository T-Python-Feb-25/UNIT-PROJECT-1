import json
from DataStorage import load_data, save_data
from datetime import datetime, timedelta

def log_workout():
    while True:
        exercise = input("Enter exercise name: ")
        if exercise.isalpha():
            break
        else:
            print("Exercise name should not contain numbers. Please enter a valid exercise name.")
    
    while True:
        try:
            sets = int(input("Enter number of sets: "))
            break
        except ValueError:
            print("Please enter a valid number for sets.")

    while True:
        try:
            reps = int(input("Enter repetition per set: "))
            break
        except ValueError:
            print("Please enter a valid number for repetitions.")

    while True:
        try:
            weight = float(input("Enter weight (kg/lbs): "))
            break
        except ValueError:
            print("Please enter a valid number for weight.")

    while True:
        try:
            day = int(input("Enter the day (DD): "))
            if 1 <= day <= 31:
                date = (datetime.now().replace(day=day)).strftime('%Y-%m-%d')
                break
            else:
                print("Please enter a day between 1 and 31.")
        except ValueError:
            print("Please enter a valid number for days.")

    workout_entry = {
        "date": date,
        "exercise": exercise,
        "sets": sets,
        "reps": reps,
        "weight": weight
    }

    