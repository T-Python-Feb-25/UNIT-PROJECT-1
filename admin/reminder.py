import time
from datetime import datetime
import threading

# List to store reminders (each item is a tuple of (message, reminder_time))
reminders = []
reminders_lock = threading.Lock()  # Lock for thread-safe access to reminders

def set_reminder():
    """Function to add a new reminder."""
    reminder_message = input("Enter your reminder message: ")
    while True:
        reminder_time_str = input("Enter reminder time (format: YYYY-MM-DD HH:MM:SS): ")
        try:
            reminder_time = datetime.strptime(reminder_time_str, "%Y-%m-%d %H:%M:%S")
            if reminder_time < datetime.now():
                print("Reminder time cannot be in the past!")
            else:
                with reminders_lock:
                    reminders.append((reminder_message, reminder_time))
                print(f"Reminder set for {reminder_time}.")
                break  # Exit the loop after setting the reminder
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS'.")

def check_reminders():
    """Function to check reminders and notify the user."""
    while True:
        current_time = datetime.now()
        with reminders_lock:
            # Loop through reminders and check if the reminder time has passed
            for reminder in reminders[:]:
                message, reminder_time = reminder
                if current_time >= reminder_time:
                    print(f"Reminder: {message} (Time: {reminder_time})")
                    reminders.remove(reminder)  # Remove the reminder after it's triggered
        time.sleep(60)  # Check every minute

def display_reminders():
    """Display all current reminders."""
    with reminders_lock:
        if not reminders:
            print("No reminders set.")
        else:
            print("Current Reminders:")
            for message, reminder_time in reminders:
                print(f"{message} at {reminder_time}")

def reminders_main():
    """Main function to interact with the user and set reminders."""
    print("Welcome to the Reminder System!")
    
    # Start the reminder checking in a separate thread
    reminder_thread = threading.Thread(target=check_reminders, daemon=True)
    reminder_thread.start()

    while True:
        print("\n1. Set a new reminder")
        print("2. View all reminders")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            set_reminder()
        elif choice == '2':
            display_reminders()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    reminders_main()
