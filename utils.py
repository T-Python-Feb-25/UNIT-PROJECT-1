from setteings import * 
import os,json,datetime
from Exceptions import * 
def generate_unique_id(name,type=0,file_path=METADATA_PATH):
    
    
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump({name: 0}, file)

    with open(file_path, "r+") as file:
        data = dict(json.load(file))
        if name not in data:
            data[name] = 0  
        data[name] += 1
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    return data[name]   

def is_valid_future_date(date,today='today'):
    try:
        event_date = datetime.strptime(date, "%Y-%m-%d")
        if today == 'today':
            start = datetime.today()
        else:
            start = today
        if event_date < start:
            return False
        return True
    except Exception:
        print("❌ wrong date format. Use YYYY-M-D.")
        return False


def is_valid_date(prompt):
    """Prompt the admin for a valid future date (YYYY-M-D)."""
    while True:
        date_str = input(prompt).strip()
        try:
            event_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            if event_date >= datetime.today().date():
                return event_date
            else:
                raise DateError("❌ Date must be today or in the future!")
        except ValueError:
            print("❌ Invalid format! Use YYYY-M-D.")

def is_valid_time(prompt):
    """Prompt the admin for a valid time (HH:MM, 24-hour format)."""
    while True:
        time_str = input(prompt).strip()
        try:
            event_time = datetime.strptime(time_str, "%H:%M").time()
            return event_time  # ✅ Valid time
        except ValueError:
            print("❌ Invalid format! Use HH:MM (24-hour format).")

def get_event_datetime():
    """Prompt admin to enter event start & end datetime with validation."""
    try:
        start_date = is_valid_date("🔹 Enter start date (YYYY-M-D): ")
        end_date = is_valid_date("🔹 Enter end date (YYYY-M-D): ")
        start_time = is_valid_time("⏰ Enter start time (HH:MM, 24-hour format): ")
        end_time = is_valid_time("⏰ Enter end time (HH:MM, 24-hour format): ")
        if end_date > start_date or end_time > start_time:
            return True 
        else:
            raise DateError("❌  End date & time must be after the start date & time!")
    except Exception as e:
        print(e)
