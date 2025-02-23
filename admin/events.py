import calendar
from datetime import datetime
from colorama import init, Fore
import json
import os
import unittest

# Initialize colorama
init(autoreset=True)

EVENTS_FILE = 'events.json'

def manage_events(logged_in_user):
    '''This function allows the user to manage their events using multiple options.'''
    while True:
        print("\nHello! Ready to organise your events? Let’s go!")
        print("1. Add Event")
        print("2. View Events")
        print("3. Update Event")
        print("4. Delete Event")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue  # Continue the loop to ask for the input again

        if choice == 1:
            add_event(logged_in_user)
        elif choice == 2:
            view_events(logged_in_user)
        elif choice == 3:
            update_event(logged_in_user)
        elif choice == 4:
            delete_event(logged_in_user)
        elif choice == 5:
            print("Exiting the event manager. Goodbye!")
            break  # Exit the loop if the user chooses option 5
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
    # Loop until a valid date is entered for the event
    while True:
        date = input("Enter the date of the event to update (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
            break  # Exit the loop if the date is valid
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD")
    
    events = load_events()
    updated_events = []
    updated = False
    
    for event in events:
        if event['username'] == logged_in_user.username and event['date'] == date.strftime('%Y-%m-%d'):
            new_event = input("Enter the new event name: ")
            while not new_event.strip():
                print("Event name cannot be empty. Please enter a valid event name.")
                new_event = input("Enter the new event name: ")

            while True:
                new_date = input("Enter the new date (YYYY-MM-DD): ")
                try:
                    new_date = datetime.strptime(new_date, "%Y-%m-%d")
                    break  # Exit the loop if the date is valid
                except ValueError:
                    print("Invalid date format. Please enter the date in the format YYYY-MM-DD")
            
            event['event'] = new_event
            event['date'] = new_date.strftime('%Y-%m-%d')
            updated = True
        
        updated_events.append(event)
    
    save_events(updated_events)
    
    if updated:
        print("Event updated successfully!")
    else:
        print("Event not found.")

def delete_event(logged_in_user):
    '''This function allows the user to delete an event from the events.json file.'''
    # Loop until a valid date is entered for the event
    while True:
        date = input("Enter the date of the event to delete (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date, "%Y-%m-%d").strftime('%Y-%m-%d')
            break  # Exit the loop if the date is valid
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD")
    
    events = load_events()
    updated_events = []
    deleted = False
    
    for event in events:
        if event['username'] == logged_in_user.username and event['date'] == date:
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
        # User input for the year and month with validation
        try:
            year = int(input("Enter year (e.g. 2025): "))
            month = int(input("Enter month (1-12): "))
            if month < 1 or month > 12:
                print("Invalid month. Please enter a number between 1 and 12.")
                continue
            break  # Exit the loop if valid input
        except ValueError:
            print("Invalid input. Please enter numeric values for year and month.")
            continue

    events = load_events()

    # Set of event days for the given month and year
    event_days = set()
    for event in events:
        if event['username'] == logged_in_user.username:
            try:
                event_date = datetime.strptime(event['date'], "%Y-%m-%d")
                if event_date.year == year and event_date.month == month:
                    event_days.add(event_date.day)
            except ValueError:
                print(f"Skipping invalid date format: {event['date']}")

    # Print the calendar for the month
    cal = calendar.TextCalendar(calendar.SUNDAY)
    print(f"\nCalendar for {calendar.month_name[month]} {year}:")

    for week in cal.monthdayscalendar(year, month):
        for day in week:
            if day == 0:
                print("   ", end=" ")  # Empty days
            elif day in event_days:
                print(Fore.LIGHTGREEN_EX + f"{day:2}", end=" ")  # Event days in green
            else:
                print(f"{day:2}", end=" ")  # Normal days
        print()  # Newline after each week

    # Print the events for the month
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
