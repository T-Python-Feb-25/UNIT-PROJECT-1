import calendar
from datetime import datetime
from colorama import init, Fore, Back  # Import colorama for colored output

# Initialize colorama
init(autoreset=True)

def manage_events(logged_in_user):
    while True:
        print(Fore.LIGHTGREEN_EX + Back.LIGHTWHITE_EX +"\nHello! Ready to organise your events? Let’s go!")
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

def add_event(logged_in_user):
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
    # Loop until a valid date is entered for the event
    while True:
        date = input("Enter the date of the event to update (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
            break  # Exit the loop if the date is valid
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD")
    
    try:
        with open('events.txt', 'r') as file:
            events = file.readlines()
        
        updated_events = []
        updated = False
        
        for event in events:
            username, event_date, event_name = event.strip().split(',', 2)
            
            # Check if the event belongs to the logged-in user and matches the date
            if username == logged_in_user.username and datetime.strptime(event_date, "%Y-%m-%d") == date:
                
                # Loop until valid new event name is entered
                new_event = input("Enter the new event name: ")
                while not new_event.strip():
                    print("Event name cannot be empty. Please enter a valid event name.")
                    new_event = input("Enter the new event name: ")

                # Loop until a valid new date is entered
                while True:
                    new_date = input("Enter the new date (YYYY-MM-DD): ")
                    try:
                        new_date = datetime.strptime(new_date, "%Y-%m-%d")
                        break  # Exit the loop if the date is valid
                    except ValueError:
                        print("Invalid date format. Please enter the date in the format YYYY-MM-DD")
                
                # Append updated event with new details
                updated_events.append(f"{username},{new_date.strftime('%Y-%m-%d')},{new_event}\n")
                updated = True
                
            else:
                updated_events.append(event)
        
        # Write the updated events back to the file
        with open('events.txt', 'w') as file:
            file.writelines(updated_events)
        
        if updated:
            print("Event updated successfully!")
        else:
            print("Event not found.")
    
    except IOError as e:
        print(f"Error updating event: {e}")

def delete_event(logged_in_user):
    # Loop until a valid date is entered for the event
    while True:
        date = input("Enter the date of the event to delete (YYYY-MM-DD): ")
        try:
            # Normalize date to the correct format (YYYY-MM-DD)
            date = datetime.strptime(date, "%Y-%m-%d").strftime('%Y-%m-%d')
            break  # Exit the loop if the date is valid
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD")
    
    try:
        with open('events.txt', 'r') as file:
            events = file.readlines()
        
        updated_events = []
        deleted = False
        
        for event in events:
            username, event_date, event_name = event.strip().split(',', 2)
            # Normalize event date to the correct format
            event_date = datetime.strptime(event_date, "%Y-%m-%d").strftime('%Y-%m-%d')
            
            # Check if the event belongs to the logged-in user and matches the date
            if username == logged_in_user.username and event_date == date:
                deleted = True
            else:
                updated_events.append(event)
        
        # Write the updated events back to the file
        with open('events.txt', 'w') as file:
            file.writelines(updated_events)
        
        if deleted:
            print("Event deleted successfully!")
        else:
            print("Event not found.")
    
    except IOError as e:
        print(f"Error deleting event: {e}")

def display_calendar(logged_in_user):
    # User input for the year and month
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
    print(f"\nCalendar for {calendar.month_name[month]} {year}:")
    for week in cal.monthdayscalendar(year, month):
        for day in week:
            if day == 0:
                print("   ", end=" ")  # Print empty days
            elif day in event_days:
                print(Fore.LIGHTGREEN_EX + f"{day:2}", end=" ")  # Print event days in green
            else:
                print(f"{day:2}", end=" ")  # Print normal days
        print()  # Newline after each week

    # Print the events below the calendar
    print(f"\nThe events for {calendar.month_name[month]} are:")
    events_found = False
    for username, date_str, event_name in events:
        if username == logged_in_user.username:
            event_date = datetime.strptime(date_str, "%Y-%m-%d")
            if event_date.year == year and event_date.month == month:
                print(f" Day {event_date.day}: {event_name}")
                events_found = True

    if not events_found:
        print("No events found for this month.")

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
