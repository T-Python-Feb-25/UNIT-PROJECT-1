import hashlib
import sqlite3
import os
import matplotlib.pyplot as plt
from colorama import Fore, Style, init
from modules.email_sender import send_email
from modules.export_excel import export_to_excel
import pandas as pd
 
"""
Main module for the Civil Defense Safety Tracker.

This script initializes the SQLite database, creates necessary tables,
and imports required modules for data handling, visualization, and email notifications.
"""


init(autoreset=True)

DB_NAME = "safety_tracker.db"
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS risks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        risk_type TEXT,
        level TEXT,
        location TEXT,
        date TEXT
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS email_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    risk_id INTEGER,
    recipient TEXT,
    timestamp TEXT,
    status TEXT
)
""")
conn.commit()







#conn.commit()

def register():
    """
    Registers a new user by storing a hashed password in the database.

    Prompts the user to enter a username and password, then hashes the password 
    and saves it in the database. If the username already exists, an error message is displayed.
    """
    username = input("Enter new username: ").strip()
    password = input("Enter new password: ").strip()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print(Fore.GREEN + "Registration successful! You can now log in.")
    except sqlite3.IntegrityError:
        print(Fore.RED + "Username already exists. Please try a different one.")

def login():
    """
    Authenticates a user by verifying their username and hashed password.

    Prompts the user for their username and password, hashes the password, 
    and checks it against the stored credentials in the database.
    
    Returns:
        bool: True if login is successful, False otherwise.
    """

    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    user = cursor.fetchone()

    if user:
        print(Fore.GREEN + f"Welcome, {username}! You have successfully logged in.")
        input(Fore.YELLOW + "\nPress Enter to continue to the menu...")  
        return True
    else:
        print(Fore.RED + "Incorrect username or password.")
        return False

def add_risk():
    """
    Adds a new risk entry to the database.

    Prompts the user to enter details about the risk, including type, level, location, and date.
    If the user confirms, the risk is inserted into the database.
    """

    risk_type = input("Enter risk type: ").strip()
    level = input("Enter risk level (Low/Medium/High): ").strip()
    location = input("Enter location: ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()

    confirm = input("Are you sure you want to save this risk? (yes/no): ").strip().lower()
    
    if confirm == "yes":
        cursor.execute("INSERT INTO risks (risk_type, level, location, date) VALUES (?, ?, ?, ?)",
                       (risk_type, level, location, date))
        conn.commit()

        risk_id = cursor.lastrowid  
        print(f"✔ Risk added successfully! (ID: {risk_id})")

        if level.lower() == "high":
            email_status = send_email(risk_id, risk_type, level, location, date)

            cursor.execute("INSERT INTO email_logs (risk_id, recipient, timestamp, status) VALUES (?, ?, datetime('now'), ?)",
                           (risk_id, "recipient_email@example.com", email_status))
            conn.commit()
            print("📧 Email notification sent!")

        else:
            print("ℹ No email sent, as risk level is not High.")

    else:
        print("❌ Operation canceled. Risk not saved.")
    input(Fore.GREEN+"Risk added successfully! Press Enter to continue..."+Fore.GREEN)



def list_risks():
    """
    Displays all recorded risks from the database.

    Prompts the user to press Enter to display all risks or type 'exit' to cancel.
    Retrieves and prints all risks stored in the database.

    Returns:
        None
    """
    confirm = input("Press Enter to display all recorded risks or type 'exit' to cancel: ").strip().lower()
    if confirm == "exit":
        return

    cursor.execute("SELECT * FROM risks")
    risks = cursor.fetchall()

    if risks:
        print(Fore.CYAN + "\nRecorded Risks:")
        for risk in risks:
            print(f"- ID: {risk[0]}, Type: {risk[1]}, Level: {risk[2]}, Location: {risk[3]}, Date: {risk[4]}")
    else:
        print(Fore.YELLOW + "No risks recorded yet.")

    input("\nEnd of the list. Press Enter to return to the menu...")

    

def search_risk():
    """
    Searches for risks based on a specific location.

    Prompts the user to enter a location, then retrieves and displays 
    all risks that match the entered location.

    Returns:
        None
    """
    location = input("Enter location to search for risks: ").strip()
    cursor.execute("SELECT * FROM risks WHERE location = ?", (location,))
    risks = cursor.fetchall()

    if risks:
        print(Fore.CYAN + f"\nRisks in {location}:")
        for risk in risks:
            print(f" - ID: {risk[0]}, Type: {risk[1]}, Level: {risk[2]}, Date: {risk[4]}")
    else:
        print(Fore.YELLOW + f"No risks found in {location}.")
    input( "\nPress Enter to return to the menu..."  )  

def generate_report():
    """
    Generates a text report containing all recorded risks.

    Fetches all risks from the database and writes them into a file 
    named 'risk_report.txt'. The report includes risk type, level, 
    location, and date.

    Returns:
        None
    """

    cursor.execute("SELECT * FROM risks")
    risks = cursor.fetchall()

    with open("risk_report.txt", "w") as file:
        file.write("Risk Report\n===================\n")
        for risk in risks:
            file.write(f"Risk: {risk[1]}, Level: {risk[2]}, Location: {risk[3]}, Date: {risk[4]}\n")
    
    print(Fore.GREEN + "Report generated successfully (risk_report.txt).")
    input( "\nPress Enter to return to the menu..."  )  



def plot_risks():
    """
    Generates a bar chart displaying the distribution of risks by level.

    Fetches the count of each risk level from the database and visualizes it
    using a bar chart with different colors for each level.

    Returns:
        None
    """
    cursor.execute("SELECT level, COUNT(*) FROM risks GROUP BY level")
    data = cursor.fetchall()

    if data:
        levels, counts = zip(*data)
        


        plt.bar(levels, counts, color=['green', 'orange', 'red'])
        plt.xlabel("Risk Level")
        plt.ylabel("Count")
        plt.title("Risk Distribution")
        plt.show()
    else:
        print(Fore.YELLOW + "No risk data available for plotting.")


 #from colorama import Fore, Style

def update_risk():
    """
    Updates an existing risk in the database.

    Prompts the user to enter the ID of the risk to update, then allows modifying
    the risk type, level, location, and date. The updated values are then saved to the database.

    Returns:
        None
    """
    list_risks()
    risk_id = input(Fore.YELLOW + "Enter the ID of the risk to update: " + Style.RESET_ALL).strip()
    new_type = input(Fore.CYAN + "Enter new risk type: " + Style.RESET_ALL).strip()
    new_level = input(Fore.CYAN + "Enter new risk level (Low/Medium/High): " + Style.RESET_ALL).strip()
    new_location = input(Fore.CYAN + "Enter new location: " + Style.RESET_ALL).strip()
    new_date = input(Fore.CYAN + "Enter new date (YYYY-MM-DD): " + Style.RESET_ALL).strip()
    
    cursor.execute("UPDATE risks SET risk_type = ?, level = ?, location = ?, date = ? WHERE id = ?", 
                   (new_type, new_level, new_location, new_date, risk_id))
    conn.commit()
    print(Fore.GREEN + "Risk updated successfully!" + Style.RESET_ALL)
    input(Fore.YELLOW + "Press Enter to return to the menu..." + Style.RESET_ALL)


def delete_risk():
    """
    Deletes a risk entry from the database.

    Asks the user for the ID of the risk to be deleted. 
    Confirms the deletion before removing the record from the database.

    Returns:
        None
    """
    list_risks()
    risk_id = input(Fore.YELLOW + "Enter the ID of the risk to delete: " + Style.RESET_ALL).strip()
    confirmation = input(Fore.RED + "Are you sure you want to delete this risk? (yes/no): " + Style.RESET_ALL).strip().lower()
    
    if confirmation == 'yes':
        cursor.execute("DELETE FROM risks WHERE id = ?", (risk_id,))
        conn.commit()
        print(Fore.RED + "Risk deleted successfully!" + Style.RESET_ALL)
    else:
        print(Fore.BLUE + "Deletion cancelled." + Style.RESET_ALL)
    
    input(Fore.YELLOW + "Press Enter to return to the menu..." + Style.RESET_ALL)


def display_menu():

    """
    Displays the main menu options for the Civil Defense Safety Tracker.

    Shows a numbered list of available actions, allowing the user to select
    operations such as adding, updating, deleting, or viewing risks.

    Returns:
        None
    """

    print(Fore.CYAN + "\n" + "=" * 50)
    print(Fore.BLUE + " Civil Defense Safety Tracker")
    print(Fore.CYAN + "=" * 50)
    print(f"{Fore.GREEN}1.{Fore.RESET} Add a new risk")
    print(f"{Fore.GREEN}2.{Fore.RESET} List all recorded risks")
    print(f"{Fore.GREEN}3.{Fore.RESET} Search for a risk by location")
    print(f"{Fore.GREEN}4.{Fore.RESET} Update a risk")
    print(f"{Fore.GREEN}5.{Fore.RESET} Delete a risk")
    print(f"{Fore.GREEN}6.{Fore.RESET} Generate a report")
    print(f"{Fore.GREEN}7.{Fore.RESET} Plot risk chart")
    print(f"{Fore.GREEN}8.{Fore.RESET} Export risks to Excel (Formatted)")
    print(f"{Fore.RED}0.{Fore.RESET} Exit")

def main():
    def main():
     """
    Main function to run the Civil Defense Safety Tracker.

    This function provides a user interface for logging in, registering, and navigating 
    through the available features such as adding, listing, searching, updating, deleting, 
    and exporting risks.

    The function runs an infinite loop that:
        - Prompts the user to log in or register.
        - If login is successful, displays the main menu.
        - Handles user inputs to execute the corresponding functions.

    Returns:
        None
        """

    print(Fore.YELLOW + "=" * 50)
    print(Fore.MAGENTA + " Welcome to the Civil Defense Safety Tracker!")
    print(Fore.YELLOW + " Manage and analyze risks efficiently.")
    print(Fore.YELLOW + "=" * 50)

    while True:
        print("\n1. Login")
        print("2. Register")
        print("0. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            if login():
                break
        elif choice == "2":
            register()
        elif choice == "0":
            print("Exiting... Stay Safe!")
            exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")

    while True:
        display_menu()
        try:
            choice = input("\nEnter your choice: ").strip()
            if choice == "1":
                add_risk()
            elif choice == "2":
                list_risks()
            elif choice == "3":
                search_risk()
            elif choice == "4":
                update_risk()
            elif choice == "5":
                delete_risk()
            elif choice == "6":
                generate_report()
            elif choice == "7":
                plot_risks()
            elif choice == "8":
                export_to_excel()   
            elif choice == "0":
                print("Exiting... Stay Safe!")
                break
            else:
                print(Fore.RED + "Invalid choice! Please enter a number between 0-7.")
        except KeyboardInterrupt:
            print(Fore.RED + "\nProgram interrupted. Exiting safely.")
            break

if __name__ == "__main__":
    main()
