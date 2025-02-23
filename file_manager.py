import json
import os

def load_data(file_path):
    """ to load the data from json file """
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_data(file_path, data):
    """To save data to a json file"""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)