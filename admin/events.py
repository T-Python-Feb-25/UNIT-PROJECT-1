import calendar
from datetime import datetime
from colorama import init, Fore, Back, Style
import json
import os

# Initialize colorama
init(autoreset=True)

EVENTS_FILE = 'events.json'

def manage_events(logged_in_user):
    '''This function allows the user to manage their events using multiple options.'''
    while True:
        print("\nHello! Ready to organise your events? Let’s go!")
        print("1. Add Event")
        print("2. Search for an event")
        print("3. View Events")
        print("4. Update Event")
        print("5. Delete Event")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue  # Continue the loop to ask for the input again

        if choice == 1:
            add_event(logged_in_user)
        elif choice == 2:
            search_event(logged_in_user)
        elif choice == 3:
            view_events(logged_in_user)
        elif choice == 4:
            update_event(logged_in_user)
        elif choice == 5:
            delete_event(logged_in_user)
        elif choice == 6:
            print("Exiting the event manager. Goodbye!")
            break  # Exit the loop if the user chooses option 6
        else:
            print("Invalid choice. Please try again.")

def load_events():
    '''Load events from the events.json file.'''
    if not os.path.exists(EVENTS_FILE):
        return []

    try:
        with open(EVENTS_FILE, 'r') as file:
            events = json.load(file)
        return events
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading events: {e}")
        return []

def save_events(events):
    '''Save the events to the events.json file.'''
    try:
        with open(EVENTS_FILE, 'w') as file:
            json.dump(events, file, indent=4)
    except IOError as e:
        print(f"Error saving events: {e}")

def add_event(logged_in_user):
    '''This function allows the user to add an event to the events.json file.'''
    while True:
        date_str = input("Enter the date (YYYY-MM-DD): ")
        try:
            # Validate the date format
            date = datetime.strptime(date_str, "%Y-%m-%d")

            # Check if the date is in the past
            if date < datetime.now():
                print("You cannot add events for past dates. Please enter a future date.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD")

    event = input("Enter the event name: ")
    
    events = load_events()
    events.append({
        'username': logged_in_user.username,
        'date': date_str,
        'event': event
    })
    
    save_events(events)
    print("Event added successfully!")

def search_event(logged_in_user):
    '''This function allows the user to search for an event in the events.json file.'''
    search = input("Enter the event name to search: ")
    
    events = load_events()
    found = False
    
    for event in events:
        if event['username'] == logged_in_user.username and search.lower() in event['event'].lower():
            print(f"{event['date']}: {event['event']}")
            found = True
    
    if not found:
        print("Event not found.")

def view_events(logged_in_user):
    '''This function allows the user to view their events from the events.json file.'''
    events = load_events()
    user_events = [event for event in events if event['username'] == logged_in_user.username]
    
    if not user_events:
        print("No events found for the current user.")
    else:
        for event in user_events:
            print(f"{event['date']}: {event['event']}")

def update_event(logged_in_user):
    '''This function allows the user to update an event in the events.json file.'''
    
    while True:
        date_str = input("Enter the date of the event to update (YYYY-MM-DD): ")
        try:
            # Validate the date format
            date = datetime.strptime(date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD")
    
    events = load_events()
    updated_events = []
    updated = False
    
    for event in events:
        if event['username'] == logged_in_user.username and event['date'] == date_str:
            new_event = input("Enter the new event name: ")
            
            while not new_event.strip():
                print("Event name cannot be empty. Please enter a valid event name.")
                new_event = input("Enter the new event name: ")

            while True:
                new_date_str = input("Enter the new date (YYYY-MM-DD): ")
                try:
                    new_date = datetime.strptime(new_date_str, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format. Please enter the date in the format YYYY-MM-DD")
            
            # Update event details
            event['event'] = new_event
            event['date'] = new_date_str
            updated = True
        
        updated_events.append(event)
    
    save_events(updated_events)
    
    if updated:
        print("Event updated successfully!")
    else:
        print("Event not found.")

def delete_event(logged_in_user):
    '''This function allows the user to delete an event from the events.json file.'''
    
    while True:
        date_str = input("Enter the date of the event to delete (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").strftime('%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD")
    
    events = load_events()
    updated_events = []
    deleted = False
    
    for event in events:
        if event['username'] == logged_in_user.username and event['date'] == date_str:
            deleted = True
        else:
            updated_events.append(event)
    
    save_events(updated_events)
    
    if deleted:
        print("Event deleted successfully!")
    else:
        print("Event not found.")

def display_calendar(logged_in_user):
    '''This function displays a calendar for the given month and year with events highlighted.'''
    
    while True:
        try:
            year = int(input("Enter year (e.g. 2025): "))
            month = int(input("Enter month (1-12): "))
            if month < 1 or month > 12:
                print("Invalid month. Please enter a number between 1 and 12.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numeric values for year and month.")
            continue

    events = load_events()
    event_days = set()
    
    for event in events:
        if event['username'] == logged_in_user.username:
            try:
                event_date = datetime.strptime(event['date'], "%Y-%m-%d")
                if event_date.year == year and event_date.month == month:
                    event_days.add(event_date.day)
            except ValueError:
                print(f"Skipping invalid date format: {event['date']}")

    cal = calendar.TextCalendar(calendar.SUNDAY)
    print(f"\nCalendar for {calendar.month_name[month]} {year}:")
    header = "Su Mo Tu We Th Fr Sa"
    print(header)
    print("-" * len(header))

    for week in cal.monthdayscalendar(year, month):
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            elif day in event_days:
                print(Fore.RESET)
                week_str += Back.LIGHTCYAN_EX+ Fore.BLACK + f"{day:2}" + Style.RESET_ALL + " "
            else:
                week_str += f"{day:2} "
        print(week_str)

    print(f"\nThe events for {calendar.month_name[month]} {year}:")
    events_found = False
    for event in events:
        if event['username'] == logged_in_user.username:
            event_date = datetime.strptime(event['date'], "%Y-%m-%d")
            if event_date.year == year and event_date.month == month:
                print(f"  Day {event_date.day}: {event['event']}")
                events_found = True

    if not events_found:
        print("No events found for this month.")

# Example usage
if __name__ == "__main__":
    class User:
        def __init__(self, username):
            self.username = username

    logged_in_user = User(username="test_user")
    display_calendar(logged_in_user)
