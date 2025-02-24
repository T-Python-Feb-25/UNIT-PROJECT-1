import json
from datetime import datetime

file_name = 'user_info.json'
doctor_clinic_file = 'doctor_clinics.json'  
appointments_file = 'appointments.json'

class User:
    """
    This class represents a user with their personal information, including username, password, email, and age. 
    It also provides methods for managing the user's data and checking whether they are an adult.
    """
    def __init__(self, username, password, email, age):
        """
        Initializes a new User object.

        Parameters:
        username (str): The username of the user.
        password (str): The password of the user.
        email (str): The email address of the user.
        age (int): The age of the user.
        """
        self.username = username
        self.password = password
        self.email = email
        self.age = age
        
    def display_info(self):
        """
        Displays the user's information including username, email, and age.
        """
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
    
    def set_id(self, id):
        """
        Sets a 10-digit ID for the user.

        Parameters:
        id (int): The ID to be assigned to the user. Must be an integer of exactly 10 digits.

        Raises:
        Exception: If the ID is not an integer or does not have exactly 10 digits.
        """
        if not isinstance(id, int):
            raise Exception("ID can only be int")
        if len(str(id)) != 10:
            raise Exception("ID must be 10 numbers")
        self.__id = id

    def get_id(self):
        """
        Retrieves the user's ID.

        Returns:
        int: The ID of the user.
        """
        return self.__id

    def change_password(self, new_password):
        """
        Changes the user's password.

        Parameters:
        new_password (str): The new password to be set.
        """
        self.password = new_password
        print("Password updated successfully!")

    def is_adult(self):
        """
        Checks if the user is an adult based on their age.

        Prints a message indicating whether the user is an adult or not.
        """
        if self.age >= 18:
            print(f"{self.username} is an adult.")
        else:
            print(f"{self.username} is not an adult.")

def load_data():
    """
    Loads user data from the JSON file.

    Returns:
    dict: A dictionary of users and their information, or an empty dictionary if the file doesn't exist.
    """
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def load_doctor_clinics():
    """
    Loads doctor clinic data from the JSON file.

    Returns:
    dict: A dictionary of clinics and their available doctors, or an empty dictionary if the file doesn't exist.
    """
    try:
        with open(doctor_clinic_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def load_appointments():
    """
    Loads appointment data from the JSON file.

    Returns:
    list: A list of appointments, or an empty list if the file doesn't exist.
    """
    try:
        with open(appointments_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    """
    Saves user data to the JSON file.

    Parameters:
    data (dict): The user data to be saved.
    """
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def save_doctor_clinics():
    """
    Saves a predefined list of doctor clinics to the JSON file.
    """
    data_doctor = {
        "Clinic A": ["Dr. Ahmed", "Dr. Sara"],
        "Clinic B": ["Dr. Youssef", "Dr. Mona"]
    }
    with open(doctor_clinic_file, 'w') as file:
        json.dump(data_doctor, file, indent=4)

def save_appointments(appointments):
    """
    Saves appointment data to the JSON file.

    Parameters:
    appointments (list): A list of appointments to be saved.
    """
    with open(appointments_file, 'w') as file:
        json.dump(appointments, file, indent=4)

def login(users_info):
    """
    Prompts the user to enter their username and password and attempts to log them in.

    Parameters:
    users_info (dict): A dictionary containing user data.

    Returns:
    User or None: A User object if the login is successful, otherwise None.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users_info and users_info[username]['password'] == password:
        user = User(username, users_info[username]['password'], users_info[username]['email'], users_info[username]['age'])
        print("Login successful!")
        user.display_info()
        user.is_adult()
        return user 
    else:
        print("Incorrect username or password.")
        return None

def register(users_info):
    """
    Registers a new user by prompting for username, password, email, and age.

    Parameters:
    users_info (dict): A dictionary containing user data.
    """
    username = input("Enter a new username: ")
    if username in users_info:
        print("Username already exists.")
    else:
        password = input("Enter your password: ")
        email = input("Enter your email: ")
        age = int(input("Enter your age: "))
        
        user = User(username, password, email, age)
        users_info[username] = {'password': password, 'email': email, 'age': age}
        save_data(users_info)
        print("Account created successfully!")

appointments = load_appointments()

def booking_appointment():
    """
    Allows a user to book an appointment with a doctor at a clinic on a specific date.

    Prompts the user for the appointment date, clinic, and doctor, then checks availability.
    If available, the appointment is saved.
    """
    global appointments
    current_date = datetime.now()
    print(current_date.strftime('%A, %Y-%m-%d'))
    
    while True:  
        try:
            user_booking = input("Enter the date for your appointment (YYYY-MM-DD): ")
            user_date = datetime.strptime(user_booking, "%Y-%m-%d")
            
            if user_date < current_date:
                raise Exception("The appointment date must be after the current date!")
            
            doctor_clinics = load_doctor_clinics()
            
            print("Available Clinics:")
            for clinic in doctor_clinics:
                print(f"- {clinic}")
            
            clinic_name = input("Enter the clinic you want to book an appointment at: ").strip()
            
            clinic_name = next((clinic for clinic in doctor_clinics if clinic.lower() == clinic_name.lower()), None)
            
            if not clinic_name:
                print("Clinic not found!")
                return
            
            print(f"Available Doctors at {clinic_name}:")
            for doctor in doctor_clinics[clinic_name]:
                print(f"- {doctor}")
            
            doctor_name = input("Enter the doctor's name: ").strip()
            
            if doctor_name not in doctor_clinics[clinic_name]:
                print("Doctor not found!")
                return
            
            for appointment in appointments:
                if appointment["date"] == user_date.strftime('%Y-%m-%d') and appointment["doctor"] == doctor_name:
                    print(f"Sorry, Dr. {doctor_name} already has an appointment scheduled for {user_date.strftime('%Y-%m-%d')}.")
                    print("Please choose a different date.")
                    break  
            else:
                appointment = {
                    "date": user_date.strftime('%Y-%m-%d'),
                    "doctor": doctor_name,
                    "clinic": clinic_name
                }
                appointments.append(appointment)
                save_appointments(appointments)  
                print(f"Appointment scheduled for {user_date.strftime('%Y-%m-%d')} with Dr. {doctor_name} at {clinic_name}")
                break  
        
        except Exception as e:
            print(e)

def change_appointment():
    """
    Allows a user to change the date of an existing appointment.

    Prompts the user to select an appointment and choose a new date. It checks availability for the new date and doctor.
    """
    global appointments
    
    if not appointments:
        print("No appointments available to change.")
        return
    
    print("Your current appointments:")
    for idx, appointment in enumerate(appointments, 1):
        print(f"{idx}. {appointment['date']} - Dr. {appointment['doctor']} at {appointment['clinic']}")
    
    try:
        appointment_index = int(input("Enter the number of the appointment you want to change: ")) - 1
        if appointment_index < 0 or appointment_index >= len(appointments):
            print("Invalid selection!")
            return
        
        appointment_to_change = appointments[appointment_index]
        print(f"You selected to change: {appointment_to_change['date']} with Dr. {appointment_to_change['doctor']} at {appointment_to_change['clinic']}")
        
        current_date = datetime.now()
        while True:
            new_booking_date = input("Enter the new date for your appointment (YYYY-MM-DD): ")
            new_date = datetime.strptime(new_booking_date, "%Y-%m-%d")
            
            if new_date < current_date:
                print("The new appointment date must be after the current date!")
                continue

            for appointment in appointments:
                if appointment["date"] == new_date.strftime('%Y-%m-%d') and appointment["doctor"] == appointment_to_change['doctor']:
                    print(f"Sorry, Dr. {appointment_to_change['doctor']} already has an appointment scheduled for {new_date.strftime('%Y-%m-%d')}.")
                    print("Please choose a different date.")
                    break
            else:
                appointment_to_change["date"] = new_date.strftime('%Y-%m-%d')
                print(f"Appointment successfully updated to {new_date.strftime('%Y-%m-%d')}")
                break
        
        save_appointments(appointments)
    
    except Exception as e:
        print(f"Error: {e}")

def delete_appointment():
    """
    Allows a user to delete an existing appointment.

    Prompts the user to select an appointment and confirms the deletion before removing it.
    """
    global appointments
    
    if not appointments:
        print("No appointments available to delete.")
        return
    
    print("Your current appointments:")
    for idx, appointment in enumerate(appointments, 1):
        print(f"{idx}. {appointment['date']} - Dr. {appointment['doctor']} at {appointment['clinic']}")
    
    try:
        appointment_index = int(input("Enter the number of the appointment you want to delete: ")) - 1
        if appointment_index < 0 or appointment_index >= len(appointments):
            print("Invalid selection!")
            return
        
        appointment_to_delete = appointments[appointment_index]
        print(f"You selected to delete: {appointment_to_delete['date']} with Dr. {appointment_to_delete['doctor']} at {appointment_to_delete['clinic']}")
        
        confirm = input("Are you sure you want to delete this appointment? (yes/no): ").strip().lower()
        if confirm == 'yes':
            del appointments[appointment_index]
            save_appointments(appointments)
            print("Appointment successfully deleted.")
        else:
            print("Appointment deletion cancelled.")
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    """
    The main function that runs the program. It allows the user to login or register, and choose options for managing appointments.
    """
    users_info = load_data()

    print("Choose an option:")
    print("1. Login")
    print("2. Register a new account")
    choice = input("Enter the option number: ")

    if choice == '1':
        user = login(users_info)
        if user:
            print("Choose an option:")
            print("1. Add an appointment")
            print("2. Change an appointment")
            print("3. Delete an appointment")
            choice1 = input("Enter the option number: ")
            if choice1 == '1':
                save_doctor_clinics()
                booking_appointment()
            elif choice1 == '2':
                save_doctor_clinics()
                change_appointment()
            elif choice1 == '3':
                delete_appointment()
            else:
                print("Invalid choice.")
        
    elif choice == '2':
        register(users_info)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
