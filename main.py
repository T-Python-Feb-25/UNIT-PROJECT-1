from art import text2art
from utils import *
from colorama import Fore, Style,Back,init
from modules.Event import Event
from modules.user import *
from Exceptions import * 
import file_handler,os,time,getpass,re,utils
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError
from rich.console import Console
from rich.table import Table
from email_validator import validate_email, EmailNotValidError
# USERS_FILEPATH  = r"C:\Users\Mohamed\tuwaiq\projects\EventManagement\UNIT-PROJECT-1\data\users.json"
# EVENTS_PATH = r"C:\Users\Mohamed\tuwaiq\projects\EventManagement\UNIT-PROJECT-1\data\events.json"
init(autoreset=True)
def is_username_unique(username):
    users = file_handler.load_file(file_handler.USERS_FILEPATH)
    list_users = [User(**user_data).to_dict() for user_data in users]
    for user in list_users:
        if user['username'] == username:
            return False
    return True
def get_event_by_id():
    pass
# def print_first_line(message):
#     os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
#     print(message)  # First line stays
def display_events(title='null',username='all'):
    print(username)
    events = file_handler.load_file(file_handler.EVENTS_PATH)
    # *** convert JsON to event objects for using to_dict() func 
    list_events = [Event(**event_data).to_dect() for event_data in events]
    console = Console()
    if title == 'null':
        title = f"📅 Available Events({len(list_events)})"

    table = Table(title)

    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", style="bold magenta")
    table.add_column("presentor", justify="center", style="green")
    table.add_column("Start Date", justify="center", style="yellow")
    table.add_column("End Date", justify="center", style="yellow")
    table.add_column("Location", style="blue")
    table.add_column("Seats", justify="center", style="red")
    table.add_column("registered users",justify="center",style="green")
    print(username)
    if username == 'all':
        print("in all ")
        for event in list_events:
            table.add_row(
                str(event["id"]),
                event["title"],
                event["presenter"],
                event["start"],
                event["end"],
                event["location"],
                str(event["seats"]),
                str(event['regester_users'])
            )
    else:
        print("in " , username)
        for event in list_events:
            if username in event['regester_users']:
                table.add_row(
                    str(event["id"]),
                    event["title"],
                    event["presenter"],
                    event["start"],
                    event["end"],
                    event["location"],
                    str(event["seats"]),
                    str(event['regester_users'])
                )
    console.print(table)
def display_event(title,id):
    events = file_handler.load_file(file_handler.EVENTS_PATH)
    # *** convert JsON to event objects for using to_dict() func 
    list_events = [Event(**event_data).to_dect() for event_data in events]
    console = Console()
    table = Table(title=f"📅 {title} ")

    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", style="bold magenta")
    table.add_column("presentor", justify="center", style="green")
    table.add_column("Start Date", justify="center", style="yellow")
    table.add_column("End Date", justify="center", style="yellow")
    table.add_column("Location", style="blue")
    table.add_column("Seats", justify="center", style="red")
    table.add_column("registered users",justify="center",style="green")

    for event in events:
        if str(event['id']) == str(id):
            table.add_row(
                str(event["id"]),
                event["title"],
                event["presenter"],
                event["start"],
                event["end"],
                event["location"],
                str(event["seats"]),
                str(event['regester_users'])
            )
            break
    console.print(table)



def login_page(error_msg=""):        
    """Displays the login page."""
    print_header("🔐 LOGIN PAGE")
    if error_msg:
        print(f"⚠️  {error_msg}\n")
    username = input("👤 Enter Username: ").strip()
    password = prompt("🔑 Enter Password: ",is_password=True)
    Users = file_handler.load_file(file_handler.USERS_FILEPATH)    
    users_list = [User(**user_data).to_dict() for user_data in Users]
    for user in users_list:
        if username == user['username']:
            if password == user['password']:
                loged_in = user
                if loged_in['role'] == 'admin':
                    admin_page(loged_in)
                elif loged_in['role'] == 'user':
                    user_page(loged_in)
                else: print("error in login page . ")
                break
            else:
                print("wrong password.Try again! ")
    else:
        login_page("Username not found! Try again.")
    
    
def register_page(error_msg=""):
    """Displays the register page."""
    print_header("📝 REGISTER PAGE")
    if error_msg:
        print(f"⚠️  {error_msg}\n")

    username = input('Enter your username:').strip()
    if len(username) < 3:
        register_page("Username must be at least 3 characters long!")
        return
    if not is_username_unique(username):
        register_page(Fore.RED + username + Style.RESET_ALL + " is register give another username.")
        return
    email = input('Enter your email: ')
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, email):
        register_page("❌ Invalid email. Try again.")
        return
    password = prompt("🔑 Enter Password: ",is_password=True)
    file_handler.add_user(email,username,password)
def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def print_header(title):
    """Prints a styled header with a border."""
    clear_screen()
    print("-" * 30)
    print(f"{title.center(30)}")
    print("-" * 30 + "\n")

def main():
    """welcome to event management program ."""
    print_header("🏠 Main page")
    print("1️⃣  Login")
    print("2️⃣  Register")
    print("3️⃣  Exit")
    choice = input("\n choice: ").strip()
    if choice == "1":
        login_page()
    elif choice == "2":
        register_page()
    elif choice == "3":
        print("\n👋 Goodbye!")
        exit()
    else:
        print("\n⚠️  Invalid choice, try again!")
        main()
  
        
def user_page(user):
    user_menu = '''
    1️⃣  list availbe events
    2️⃣  list booked events
    3️⃣  book an event 
    4️⃣  cancel event
    5️⃣  search by title
    6️⃣  main page
    
     choice: '''
    welcoming = f"👤 Welcom {Fore.GREEN}{user['username']}"
    while(True):
        try:
            print_header(welcoming)
            choice = input(user_menu)
            if choice == '1':
                print_header(welcoming)
                display_events()
                input("press any button to go back to main page... ")
            elif choice == '2':
                print_header(welcoming)
                display_events(title="booked events ",username=user['username'])
                input("press any button to go back to main page... ")
            elif choice == '3':
                print_header(welcoming)
                display_events()
                event_id = input("Privide Event ID: ")
                is_booked = file_handler.book_seat(event_id,str(user["username"]))
                if is_booked:
                    print_header(f"👤 Welcom {Fore.GREEN}{user['username']}")
                    print(f"{Fore.GREEN }successfuly booking of event {event_id}")
                    display_event("Booked event",event_id)
                else:
                    print("❌  Wrong input, please prive ID from the table")
                input("press any button to go back to main page... ")
            elif choice =='4':
                print_header(welcoming)
                display_events(title="booked events ",username=user['username'])
                event_id = input("Privide Event ID: ")
                is_canceled = file_handler.cancel_seat(event_id,str(user["username"]))
                if is_canceled:
                    print_header(f"👤 Welcom {Fore.GREEN}{user['username']}")
                    print(f"{Fore.GREEN }canceling successfuly of event {event_id}")
                    display_event("Cancled event",event_id)
                else:
                    print("❌  Wrong input, please prive ID from the table")
                input("press any button to go back to main page... ")
            elif choice =='5':
                pass
            elif choice =='6':
                main()
        except Exception as e:
            print(e)
            input("press any button to go back to main menu ... ")
def admin_page(user):
    admin_menu = '''
    1️⃣  list availbe events
    2️⃣  add event
    3️⃣  modify event 
    4️⃣  delete event
    5️⃣  main page
     choice: '''
    welcoming = f"⚜️  Welcom Admin {Fore.BLACK} {Style.BRIGHT}{Back.GREEN}{user['username']}{Back.RESET}  ⚜️"
    while(True):
        print_header(welcoming)
        choice = input(admin_menu)
        if choice == '1':
            print_header(welcoming)
            display_events()
            input("press any button to go back to main page... ")
        elif choice == '2':
            print_header(welcoming + "\n➕  ADD EVENT\n")
            try:
                title = input("🗂️  Enter title: ")
                presenter = input("🧑‍💼  Enter presenter: ")
                location = input("📍  Enter Location: ")
                start_date = is_valid_date("🔹 Enter start date (YYYY-M-D): ")
                end_date = is_valid_date("🔹 Enter end date (YYYY-M-D): ")
                start_time = is_valid_time("⏰ Enter start time (HH:MM, 24-hour format): ")
                end_time = is_valid_time("⏰ Enter end time (HH:MM, 24-hour format): ")
                seats = int(input("🪑 Enter available seats: "))
                if seats <=0:
                    raise ValueError("❌  seats must be more than zero!")
                if end_date < start_date or end_time < start_time:
                    raise DateError("❌  End date & time must be after the start date & time!")
                file_handler.add_event()
            except Exception as e:
                print(e)
            input("press any button to go back to main page... ")
        elif choice == '3':
            print_header(f"👤 Welcom {Fore.GREEN}{user['username']}")
            display_events()
            event_id = input("Privide Event ID: ")
            is_booked = file_handler.book_seat(event_id,str(user["username"]))
            if is_booked:
                print_header(f"👤 Welcom {Fore.GREEN}{user['username']}")
                print(f"{Fore.GREEN }successful booking of event:{event_id}")
                display_event("Booked event",event_id)
            input("press any button to go back to main page... ")

main()