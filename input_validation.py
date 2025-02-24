
from email_validator import validate_email, EmailNotValidError
import maskpass
import base64
import re
from openai import OpenAI
from config import API_CLIENT
import json
from data_config import get_all_governorates, get_all_provinces, load_data
from datetime import datetime, timedelta
from colorama import Fore, Style

pass_requirments='''Please create a strong password that meets the following requirements:
        1. At least 8 characters long.
        2. Contains at least one uppercase letter
        3. Contains at least one lowercase letter
        4. Contains at least one digit (0-9)
        5. Contains at least one special character (e.g., !@#$%^&*).
        6. Cannot contain spaces or tabs.'''

def llm_response(prompt):
    completion = API_CLIENT.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return completion.choices[0].message.content


def calculate_distance(from_city,to_city):
    prompt = f'''
    calculate the distance kilo by car from {from_city} , Saudi Arabia to {to_city} ,Saudi Arabia and the time taken by hours return max 
    follow the same format of the answer return
    "distance": km
    "hours": hours

    make sure to follow the output format with no extra text
    '''
    response = llm_response(prompt)
        
    try:
        response_data:dict = json.loads(response)
        return response_data.values()
    except json.JSONDecodeError:
        print("the system is out of service try again later.")

def get_number_input_with_limit(prompt:str, limit)->int:
    while True:
        try:
            user_input=input(prompt)
            if not (user_input.isnumeric()):
                raise Exception(Fore.RED+"Invalid input , Please enter a valid integer number.")
            elif int(user_input)>int(limit) or int(user_input)<=0:
                raise Exception(Fore.RED+"Invalid Choice.")

        except Exception as error:
            print(error)
        else:
            return int(user_input)
        
def get_number_input(prompt: str) :
    while True:
        user_input = input(prompt)
        try:
            number = float(user_input)
            return number  
        except ValueError:
            print(Fore.RED+"Invalid input. Please enter a valid number.")

def get_alphabetic_input(prompt: str) -> str:
    while True:
        user_input = input(prompt)
        if not user_input.strip() or not all(char.isalpha() or char.isspace() for char in user_input):
            print(Fore.RED+"Invalid input,"," please enter alphabetic characters only (spaces allowed).")
        else:
            return user_input

        
def get_email_input(prompt:str)->str:
    while True:
        try:
            user_input=input(prompt)
            emailinfo = validate_email(user_input, check_deliverability=True)           
        except EmailNotValidError as error:
            print(Fore.RED+str(error))
        else:
            return emailinfo.normalized

def get_phone_input(prompt:str)->str:
    while True:
        try:
            user_input=input(prompt)
            if not(len(user_input)==10 and user_input.isdigit() and user_input.startswith("05")):    
                raise Exception(Fore.RED+"This is invalid number.. try again")
        except Exception as error:
            print(error)
        else:
            return user_input
        
def get_password_input(prompt:str):
    while True:
        try:
            # Password masking
            pwd = maskpass.advpass(prompt)  
            if (len(pwd) < 8 or 
                re.search(r'\s', pwd) or 
                not re.search(r'[A-Z]', pwd) or 
                not re.search(r'[a-z]', pwd) or 
                not re.search(r'[0-9]', pwd) or 
                not re.search(r'[\W_]', pwd)):
                raise Exception(Fore.RED+"Invalid password,Please adhere to the requirements and try again.")

            # encoding the entered password
            encpwd = base64.b64encode(pwd.encode("utf-8"))
        except Exception as error:
            print(error)
        else:
            return encpwd
        

def password_input_masking(prompt:str):
    
    # Password masking
    pwd = maskpass.advpass(prompt)  
    # encoding the entered password
    encpwd = base64.b64encode(pwd.encode("utf-8"))

    return encpwd
    
def collect_order_info():
    from config import truck_db
    # Load provinces and pricing data
    provinces_list, pricing_list = load_data()
    order_info = {}
    
    # Display pricing information
    menu = f'''========================= Prices Menu ===========================
    - Kilo cost for closed truck: {pricing_list["cost_kilo_closed"]}
    - Kilo cost for open truck: {pricing_list["cost_kilo_open"]}'''
    
    print(menu,Fore.YELLOW+f"\nNote: Prices are excluding VAT {pricing_list["vat"] * 100}% and insurance cost {pricing_list['insurance']}")

    # Select service type
    order_info['service_type'] = "open" if get_number_input_with_limit("1 - Open truck\n2 - Closed truck\nEnter service type:", 2) == 1 else "closed"
    
    # Retrieve available trucks and filter based on service type
    trucks = truck_db.retrive_available_trucks()
    filtered_trucks = list(filter(lambda truck: truck["body_style"] == order_info['service_type'], trucks))
    
    if len(filtered_trucks) == 0:
        raise Exception(Fore.YELLOW+f"Sorry, no available {order_info['service_type']} trucks for the following three days.")

    else:
        order_info['assigined_truck'] = filtered_trucks[0]["truck_id"]
    # print("Available trucks:", filtered_trucks)
    
    # Get today's date
    today = datetime.now()
    print(Fore.YELLOW+"Delivery time takes from 1 to 2 days based on your destination.")
    
    # Display the next three days
    for i in range(1, 4):
        next_day = today + timedelta(days=i)
        print(f"{i} - {next_day.strftime('%Y-%m-%d')}")

    # Select pickup date
    selected_date = get_number_input_with_limit("Please select the pickup date :", 3)
    date = today + timedelta(days=selected_date)
    order_info['pickup_date'] = date.strftime('%Y-%m-%d')

    # Get pickup location
    get_all_provinces(provinces_list)
    keys_list = list(provinces_list.keys())
    province_num = get_number_input_with_limit("Choose the province number that you want to ship from:", len(provinces_list))
    selected_province = keys_list[province_num - 1]
    
    get_all_governorates(provinces_list, selected_province)
    govern_num = get_number_input_with_limit("Choose the governorate number that you want to ship from:", len(provinces_list[selected_province]))
    order_info['pickup'] = provinces_list[selected_province][govern_num - 1]
    provinces_list[selected_province].pop(govern_num - 1)  # Remove selected governorate

    # Get delivery location
    get_all_provinces(provinces_list)
    province_num = get_number_input_with_limit("Choose the province number that you want to ship to:", len(provinces_list))
    selected_province = keys_list[province_num - 1]
    
    get_all_governorates(provinces_list, selected_province)
    govern_num = get_number_input_with_limit("Choose the governorate number that you want to ship to:", len(provinces_list[selected_province]))
    order_info['delivery'] = provinces_list[selected_province][govern_num - 1]
    
    # Validate distance and hours
    order_info['distance'], order_info['hours'] = calculate_distance(order_info['pickup'], order_info['delivery'])
    total=(order_info['distance']*(pricing_list["cost_kilo_closed"] if order_info['service_type']=="closed" else pricing_list["cost_kilo_open"]))+pricing_list['insurance']
    order_info['price']= round((total*pricing_list["vat"])+total,2)

    # Collect car information
    order_info['car_make'] = get_alphabetic_input("Enter car make: ")
    order_info['car_model'] = input("Enter car model: ")
    order_info['car_year'] = get_number_input_with_limit("Enter car year:", 2026)
    
    # Return collected order information
    return order_info
        



            
