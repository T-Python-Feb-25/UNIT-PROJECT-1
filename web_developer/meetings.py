import calendar
from datetime import datetime
from colorama import init, Fore  # Import colorama for colored output

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