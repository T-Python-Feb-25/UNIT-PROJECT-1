import json

data_file = "data.json"

def load_data():
    ''' Load the workout data from json file'''
    try:
        with open(data_file, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_data(data):
    ''' Save workouts data to json file'''
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)
        
