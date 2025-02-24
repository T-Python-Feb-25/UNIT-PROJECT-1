from utils import *
from colorama import Fore, Style,Back,init
from Event import Event
from user import User,Admin
from Exceptions import * 
import file_handler as file_handler,os,re
import datetime 
from prompt_toolkit import prompt
from rich.console import Console
from rich.table import Table


init(autoreset=True)
def is_username_unique(username):
    users = file_handler.load_file(file_handler.USERS_FILEPATH)
    list_users = [User(**user_data).to_dict() for user_data in users]
    for user in list_users:
        if user['username'] == username:
            return False
    return True

def display_events(title='null',username='all'):
    events = file_handler.load_file(file_handler.EVENTS_PATH)
    # *** convert JsON to event objects for using to_dict() func 
    list_events = [Event(**event_data).to_dect() for event_data in events]
    console = Console()
    if title == 'null':
        title = f"📅 Available Events({len(list_events)})"
    table = Table(title=title,show_lines=True)
    
    table.add_column("ID", justify="center", style="black", no_wrap=True)
    table.add_column("Title", style="blue")
    table.add_column("Description", justify="center", style="blue")
    table.add_column("Date", justify="center",style='bright_magenta')
    table.add_column("Time", justify="center", style='magenta')
    table.add_column("Location", style="blue")
    table.add_column("Seats", justify="center", style="yellow")
    table.add_column("registered users",justify="center",style="green")
    try:
        if username == 'all':
            for event in list_events:
                date = f"Start date: {event['date']['start_date']}\nEnd date: {event['date']['end_date']}"
                time = f"Start time: {event['time']['start_time']}\nEnd time: {event['time']['end_time']}"

                table.add_row(
                    str(event["id"]),
                    event["title"],
                    event["description"],
                    date,
                    time,
                    event["location"],
                    str(event["seats"]),
                    str(event['regester_users'])
                )
        else:
            for event in list_events:
                if username in event['regester_users']:
                    date = f"Start date:{event['date']['start_date']}\nEnd date:{event['date']['end_date']}"
                    time = f"Start time:{event['time']['start_time']}\nEnd date:{event['time']['end_time']}"
                    table.add_row(
                        str(event["id"]),
                        event["title"],
                        event["description"],
                        date,
                        time,
                        event["location"],
                        str(event["seats"]),
                        str(event['regester_users'])
                    )
        console.print(table)
    except Exception as e:
        print(e)
def display_event(massage,id):
    events = file_handler.load_file(file_handler.EVENTS_PATH)
    # *** convert JsON to event objects for using to_dict() func 
    list_events = [Event(**event_data).to_dect() for event_data in events]
    console = Console()
    table = Table(title=f"📅 {massage} ")

    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", style="bold magenta")
    table.add_column("Description", justify="center", style="green")
    table.add_column("Start Date", justify="center", style="yellow")
    table.add_column("End Date", justify="center", style="yellow")
    table.add_column("Location", style="blue")
    table.add_column("Seats", justify="center", style="red")
    table.add_column("registered users",justify="center",style="green")


    for event in list_events:
        date = f"Start date:{event['date']['start_date']}\nEnd date:{event['date']['end_date']}"
        time = f"Start time:{event['time']['start_time']}\nEnd date:{event['time']['end_time']}"
        if str(event['id']) == str(id):
            table.add_row(
                str(event["id"]),
                event["title"],
                event["description"],
                date,
                time,
                event["location"],
                str(event["seats"]),
                str(event['regester_users'])
            )
    console.print(table)

def display_events_by_title(title):
    events = file_handler.load_file(file_handler.EVENTS_PATH)
    # *** convert JsON to event objects for using to_dict() func 
    list_events = [Event(**event_data).to_dect() for event_data in events]
    console = Console()
    table = Table(title=f"📅 {title}",show_lines=True)

    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Title", style="bold magenta")
    table.add_column("Description", justify="center", style="green")
    table.add_column("Start Date", justify="center", style="yellow")
    table.add_column("End Date", justify="center", style="yellow")
    table.add_column("Location", style="blue")
    table.add_column("Seats", justify="center", style="red")
    for event in events:
        if title.lower() in event['title'].lower():
            date = f"Start date:{event['date']['start_date']}\nEnd date:{event['date']['end_date']}"
            time = f"Start time:{event['time']['start_time']}\nEnd date:{event['time']['end_time']}"
            table.add_row(
                str(event["id"]),
                event["title"],
                event["description"],
                date,
                time,
                event["location"],
                str(event["seats"]),
                str(event['regester_users'])
            )
    console.print(table)


def login_page(error_msg=""):        
    """Displays the login page."""
    print_header("🔐 Login page")
    if error_msg:
        print(f"⚠️  {error_msg}\n Enter(r) for register. ")
    username = input("👤 Enter Username: ").strip()
    if username == 'r':
        register_page()
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
                login_page("wrong password. Try again! ")
    else:
        login_page("Username not found! Try again.")
    
    
def register_page(error_msg=""):
    """Displays the register page."""
    print_header("📝 Register page")
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
    user = file_handler.add_user(email,username,password)
    user_page(user.to_dict())
def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def print_header(title):
    """prints a header with a border."""
    clear_screen()
    print("-" * 30)
    print(f"{title.center(30)}")
    print("-" * 30 + "\n")

def main():
    """main function to run the program ."""
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
    """Display the user menu options

    Args:
        user (dict): user dict in the json file
    """
    user_menu = '''
    1️⃣  list availbe events
    2️⃣  list booked events
    3️⃣  book an event 
    4️⃣  cancel event
    5️⃣  search by title
    6️⃣  main page
    (exit) to end the program.
        
     choice: '''
    welcoming = f"👤 Welcom {Fore.GREEN}{user['username']}"
    while(True):
        try:
            print_header(welcoming)
            choice = input(user_menu)
            if choice == '1':
                print_header(welcoming)
                display_events()
                input("press Enter to go back to main page... ")
            elif choice == '2':
                print_header(welcoming)
                display_events(title="booked events ",username=user['username'])
                input("press Enter to go back to main page... ")
            elif choice == '3':
                print_header(welcoming)
                display_events()
                event_id = input("Provide Event ID: ")
                is_booked = file_handler.book_seat(event_id,str(user["username"]))
                if is_booked:
                    print_header(f"👤 Welcom {Fore.GREEN}{user['username']}")
                    print(f"{Fore.GREEN }event {event_id} is booked successfuly")
                    display_event("Booked event",event_id)
                else:
                    print("❌  Wrong input, please prive ID from the table")
                input("press Enter to go back to main page... ")
            elif choice =='4':
                print_header(welcoming)
                display_events(title="booked events ",username=user['username'])
                event_id = input("Provide Event ID: ")
                is_canceled = file_handler.cancel_seat(event_id,str(user["username"]))
                if is_canceled:
                    print_header(f"👤 Welcom {Fore.GREEN}{user['username']}")
                    print(f"{Fore.RED }event {event_id} canceled successfuly")
                    display_event("Cancled event",event_id)
                else:
                    print("❌  Wrong input, please prive ID from the table")
                input("press Enter to go back to main page... ")
            elif choice == '5':
                print_header(welcoming)
                title = input("Provide title for search: ")
                display_events_by_title(title)
                input("press Enter to go back to main page... ")
            elif choice =='6':
                main()
            elif choice == 'exit':
                print("\n👋 Goodbye!")
                exit()
        except Exception as e:
            print(e)
            input("press Enter to go back to main menu ... ")
def admin_page(user):
    """Display the user menu options

    Args:
        user (dict): admin dict in the json file

    """
    admin_menu = '''
    1️⃣  list availbe events
    2️⃣  add event
    3️⃣  modify event 
    4️⃣  delete event
    5️⃣  main page
    (exit) to end the program.
    
     choice: '''
    welcoming = f"⚜️  Welcom Admin {Fore.BLACK} {Style.BRIGHT}{Back.GREEN}{user['username']}{Back.RESET}  ⚜️"
    admin = Admin()
    while(True):
        print_header(welcoming)
        choice = input(admin_menu)
        if choice == '1':
            print_header(welcoming)
            display_events()
            input("press Enter to go back to main page... ")
        elif choice == '2':
            print_header(welcoming + "\n➕  ADD EVENT\n")
            try:
                title = input("🗂️  Enter title: ")
                description = input("🗂️  Enter description: ")
                location = input("📍  Enter Location: ")
                start_date = is_valid_date("🔹 Enter start date (YYYY-M-D): ")
                end_date = is_valid_date("🔹 Enter end date (YYYY-M-D): ")
                start_time = is_valid_time("⏰ Enter start time (HH:MM, 24-hour format): ")
                end_time = is_valid_time("⏰ Enter end time (HH:MM, 24-hour format): ")
                seats = int(input("🪑 Enter available seats: "))
                date = {
                    'start_date':str(start_date),
                    'end_date':str(end_date)
                    }
                time = {
                    'start_time':str(start_time),
                    'end_time':str(end_time)
                    }
                if end_date < start_date or end_time < start_time:
                    raise DateError("❌  End date & time must be after the start date & time!")
                event_id = file_handler.add_event(title,description,location,date,time,seats)
                print_header(welcoming)
                print(f"{Fore.GREEN }{event_id}:{title} is added successfuly ")
                display_event("Added event",event_id)
            except Exception as e:
                print(e)
            input("press Enter to go back to main page... ")
        
        elif choice == '3':
            print_header(welcoming + "Modify event")
            display_events()

            event_id = input("Provide Event ID you want to modify: ")
            events = list(file_handler.load_file(file_handler.EVENTS_PATH))
            list_events = [Event(**event_data).to_dect() for event_data in events]
            
            for index,event in enumerate(list_events):
                if str(event['id']) == str(event_id):
                    event_index = index
            print_header(welcoming + "Modify event")
            display_event("Modify event",event_id)
            p = f'''
            provide what you want to modify 
            from: (title,description,loation,date,time,seats) seperated by space 
            for example: {Fore.BLUE} title time
            {Fore.RESET} --> '''
            list_to_modify = input(p).split(' ')
            for modify in list_to_modify:
                if modify in list_events[event_index]:
                    if modify == 'date':
                        start_date = is_valid_date("🔹 Enter new start date (YYYY-M-D): ")
                        end_date = is_valid_date("🔹 Enter new end date (YYYY-M-D): ")
                        list_events[event_index]['date'] = {
                        'start_date':str(start_date),
                        'end_date':str(end_date)
                        }
                    elif modify == 'time':   
                        start_time = is_valid_time("⏰ Enter new start time (HH:MM, 24-hour format): ")
                        end_time = is_valid_time("⏰ Enter new end time (HH:MM, 24-hour format): ")
                        list_events[event_index]['time'] = {
                            'start_time':str(start_time),
                            'end_time':str(end_time)
                            }
                    elif modify == 'seats':
                        list_events[event_index][modify] = int(input(f"{Fore.RED}{list_events[event_index][modify]}{Fore.RESET} to : "))
                    else:
                        list_events[event_index][modify] = input(f"{Fore.RED}{list_events[event_index][modify]}{Fore.RESET} to : ")
                else:
                    print(f"⚠️  {modify} is not in [title,description,location,date,time,seats] ")
            file_handler.save_file(list_events,EVENTS_PATH)
            print_header(welcoming + "Modify event")
            display_event("Modified event ",event_id)
            input("press Enter to go back to main page... ")
            
            #######################################################################
        elif choice == '4':
            print_header(welcoming)
            display_events()
            event_id = input("Provide Event ID for delete: ")
            is_deleted = admin.delete_event(event_id)
            if is_deleted:
                print_header(welcoming)
                print(f"{Fore.GREEN }{event_id} is deleted successfuly ")
                display_event("Deleted event",event_id)
            else:
                print("❌  Wrong input, please provide ID from the table")
            input("press Enter to go back to main page... ")
        
        
        elif choice == '5':
            main()
        elif choice == 'exit':
            print("\n👋 Goodbye!")
            exit()



def is_valid_date(date):
    """make sure the admin give a valid future date (YYYY-M-D)."""
    while True:
        date_str = input(date).strip()
        try:
            event_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            if event_date >= datetime.datetime.today().date():
                return event_date
            else:
                raise DateError("❌ Date must be today or in the future!")
        except ValueError:
            print("❌ Invalid format! Use YYYY-M-D.")

def is_valid_time(time):
    """maake sure the admin give for a valid time (HH:MM, 24-hour format)."""
    while True:
        time_str = input(time).strip()
        try:
            event_time = datetime.datetime.strptime(time_str, "%H:%M").time()
            return event_time
        except ValueError:
            print("❌ Invalid format! Use HH:MM (24-hour format).")

def get_event_datetime():
    """require admin to enter event start & end datetime with validation."""
    try:
        start_date = is_valid_date("🔹 Enter start date (YYYY-M-D): ")
        end_date = is_valid_date("🔹 Enter end date (YYYY-M-D): ")
        start_time = is_valid_time("⏰ Enter start time (HH:MM, 24-hour format): ")
        end_time = is_valid_time("⏰ Enter end time (HH:MM, 24-hour format): ")
        if end_date > start_date or end_time > start_time:
            return True 
        else:
            raise DateError("❌  End date & time must be after the start date & time!")
    except Exception as e:
        print(e)


main()