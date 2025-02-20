import calendar
from datetime import datetime
from colorama import init, Fore  # Import colorama for colored output

# Initialize colorama
init(autoreset=True)

def manage_events(logged_in_user):
    while True:
        print("\nHello! Ready to organise your events? Let’s go!")
        print("1. Add Event")
        print("2. View Events")
        print("3. Update Event")
        print("4. Delete Event")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_event(logged_in_user)
        elif choice == 2:
            view_events(logged_in_user)
        elif choice == 3:
            update_event(logged_in_user)
        elif choice == 4:
            delete_event(logged_in_user)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again")

def add_event(logged_in_user):
    date_str = input("Enter the date (YYYY-MM-DD): ")
    try:
        # Validate the date format
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD")
        return

    event = input("Enter the event name: ")
    try:
        with open('events.txt', 'a') as file:
            file.write(f"{logged_in_user.username},{date_str},{event}\n")
        print("Event added successfully!")
    except IOError as e:
        print(f"Error adding event: {e}")

def view_events(logged_in_user):
    try:
        with open('events.txt', 'r') as file:
            events = file.readlines()
            if not events:
                print("No events found")
            else:
                user_events = [event for event in events if event.startswith(logged_in_user.username)]
                if not user_events:
                    print("No events found for the current user")
                else:
                    for event in user_events:
                        _, date, event_name = event.strip().split(',', 2)
                        print(f"{date}: {event_name}")
    except IOError as e:
        print(f"Error viewing events: {e}")

def update_event(logged_in_user):
    date = input("Enter the date of the event to update (YYYY-MM-DD): ")
    try:
        with open('events.txt', 'r') as file:
            events = file.readlines()
        with open('events.txt', 'w') as file:
            updated = False
            for event in events:
                username, event_date, event_name = event.strip().split(',', 2)
                if username == logged_in_user.username and event_date == date:
                    new_event = input("Enter the new event name: ")
                    new_date = input("Enter the new date (YYYY-MM-DD): ")
                    try:
                        # Validate the new date format
                        datetime.strptime(new_date, "%Y-%m-%d")
                        file.write(f"{username},{new_date},{new_event}\n")
                        updated = True
                    except ValueError:
                        print("Invalid date format. Please enter the date in the format YYYY-MM-DD")
                        file.write(event)  # Write the original event back if the new date is invalid
                else:
                    file.write(event)
            if updated:
                print("Event updated successfully!")
            else:
                print("Event not found")
    except IOError as e:
        print(f"Error updating event: {e}")

def delete_event(logged_in_user):
    date = input("Enter the date of the event to delete (YYYY-MM-DD): ")
    try:
        with open('events.txt', 'r') as file:
            events = file.readlines()
        with open('events.txt', 'w') as file:
            deleted = False
            for event in events:
                username, event_date, event_name = event.strip().split(',', 2)
                if username == logged_in_user.username and event_date == date:
                    deleted = True
                else:
                    file.write(event)
            if deleted:
                print("Event deleted successfully!")
            else:
                print("Event not found")
    except IOError as e:
        print(f"Error deleting event: {e}")

# Function to display the calendar
def display_calendar(logged_in_user):
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    cal = calendar.TextCalendar(calendar.SUNDAY)
    events = load_events()

    # Create a set of event days for the given month and year
    event_days = set()
    for username, date_str, event_name in events:
        if username == logged_in_user.username:
            try:
                event_date = datetime.strptime(date_str, "%Y-%m-%d")
                if event_date.year == year and event_date.month == month:
                    event_days.add(event_date.day)
            except ValueError:
                print(f"Skipping invalid date format: {date_str}")

    # Print the calendar with colored event days
    for day in cal.itermonthdays(year, month):
        if day == 0:
            print("   ", end=" ")  # Print empty days
        elif day in event_days:
            print(Fore.GREEN + f"{day:2}", end=" ")  # Print event days in green
        else:
            print(f"{day:2}", end=" ")  # Print normal days
        if (day + cal.firstweekday) % 7 == 0:
            print()  # Newline after each week
    print()

    # Print the events below the calendar
    print(f"\nThe events for {calendar.month_name[month]} are:")
    for username, date_str, event_name in events:
        if username == logged_in_user.username:
            event_date = datetime.strptime(date_str, "%Y-%m-%d")
            if event_date.year == year and event_date.month == month:
                print(f"{event_date.day}: {event_name}")

# Load events from the events.txt file
def load_events():
    events = []
    try:
        with open('events.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',', 2)  # Split only on the first two commas
                if len(parts) == 3:
                    username, date_str, event_name = parts
                    events.append((username, date_str, event_name))
    except IOError as e:
        print(f"Error loading events: {e}")
    return events
