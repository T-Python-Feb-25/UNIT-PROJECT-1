import calendar
from datetime import datetime
from colorama import init, Fore  # Import colorama for colored output
from admin.events import display_calendar

def manage_meetings():
    while True:
        print("\nHello! Ready to organise your meetings? Let’s go!")
        print("1. Add Meeting")
        print("2. View Meetings")
        print("3. Update Meeting")
        print("4. Delete Meeting")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_meeting()
        elif choice == 2:
            view_meetings()
        elif choice == 3:
            update_meeting()
        elif choice == 4:
            delete_meeting()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again")

def add_meeting():
    date_str = input("Enter the date (YYYY-MM-DD): ")
    try:
        # Validate the date format
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD")
        return

    meeting = input("Enter the meeting name: ")
    try:
        with open('meetings.txt', 'a') as file:
            file.write(f"{date_str},{meeting}\n")
        print("Meeting added successfully!")
    except IOError as e:
        print(f"Error adding meeting: {e}")

def view_meetings():
    try:
        with open('meetings.txt', 'r') as file:
            meetings = file.readlines()
            if not meetings:
                print("No meetings found")
            else:
                for meeting in meetings:
                    date, meeting_name = meeting.strip().split(',', 1)
                    print(f"{date}: {meeting_name}")
    except IOError as e:
        print(f"Error viewing meetings: {e}")

def update_meeting():
    date_str = input("Enter the date of the meeting to update (YYYY-MM-DD): ")
    try:
        with open('meetings.txt', 'r') as file:
            meetings = file.readlines()
            updated_meetings = []
            for meeting in meetings:
                meeting_date, meeting_name = meeting.strip().split(',', 1)
                if meeting_date == date_str:
                    new_meeting_name = input(f"Enter the new name for the meeting on {date_str}: ")
                    updated_meetings.append(f"{date_str},{new_meeting_name}\n")
                else:
                    updated_meetings.append(f"{meeting_date},{meeting_name}\n")
        with open('meetings.txt', 'w') as file:
            file.writelines(updated_meetings)
        print("Meeting updated successfully!")
    except IOError as e:
        print(f"Error updating meeting: {e}")

def delete_meeting():
    date_str = input("Enter the date of the meeting to delete (YYYY-MM-DD): ")
    try:
        with open('meetings.txt', 'r') as file:
            meetings = file.readlines()
            updated_meetings = []
            deleted = False
            for meeting in meetings:
                meeting_date, meeting_name = meeting.strip().split(',', 1)
                if meeting_date == date_str:
                    deleted = True
                else:
                    updated_meetings.append(f"{meeting_date},{meeting_name}\n")
        if deleted:
            with open('meetings.txt', 'w') as file:
                file.writelines(updated_meetings)
            print("Meeting deleted successfully!")
        else:
            print("Meeting not found")
    except IOError as e:
        print(f"Error deleting meeting: {e}")
        
def load_meetings():
    meetings = []
    try:
        with open('meetings.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',', 2)  # Split only on the first two commas
                if len(parts) == 3:
                    username, date_str, meeting_name = parts
                    meetings.append((username, date_str, meeting_name))
    except IOError as e:
        print(f"Error loading meetingss: {e}")
    return meetings

def display_calendar(logged_in_user):
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    cal = calendar.TextCalendar(calendar.SUNDAY)
    meetings = load_meetings()

    # Create a set of event days for the given month and year
    meeting_days = set()
    for username, date_str, meeting_name in meetings:
        if username == logged_in_user.username:
            try:
                meeting_date = datetime.strptime(date_str, "%Y-%m-%d")
                if meeting_date.year == year and meeting_date.month == month:
                    meeting_days.add(meeting_date.day)
            except ValueError:
                print(f"Skipping invalid date format: {date_str}")

    # Print the calendar with colored event days
    for day in cal.itermonthdays(year, month):
        if day == 0:
            print("   ", end=" ")  # Print empty days
        elif day in meeting_days:
            print(Fore.GREEN + f"{day:2}", end=" ")  # Print event days in green
        else:
            print(f"{day:2}", end=" ")  # Print normal days
        if (day + cal.firstweekday) % 7 == 0:
            print()  # Newline after each week
    print()

    # Print the events below the calendar
    print(f"\nThe events for {calendar.month_name[month]} are:")
    for username, date_str, meeting_name in meetings:
        if username == logged_in_user.username:
            meeting_date = datetime.strptime(date_str, "%Y-%m-%d")
            if meeting_date.year == year and meeting_date.month == month:
                print(f"Day {meeting_date.day}: {meeting_name}")