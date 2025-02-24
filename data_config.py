import json
from config import DATA

def load_data():
    """Load data from a JSON file.

    Reads a JSON file specified by the DATA variable and returns the 
    provinces and prices contained in the file.

    Returns:
        tuple: A tuple containing two dictionaries: 
               - provinces
               - prices
        If the file is not found or contains invalid JSON, returns an empty dictionary.
    """
    try:
        with open(DATA, "r", encoding="utf-8") as json_file:
            content = json.load(json_file)
            return content['province'], content['prices'] 
    except (FileNotFoundError, json.JSONDecodeError):
        return {},{}

def update_data(province_list: dict, pricing_list: dict):
    """Update the JSON file with new province and pricing data.

    Args:
        province_list (dict): A dictionary of provinces.
        pricing_list (dict): A dictionary of prices associated with titles.
    """
    with open(DATA, "w", encoding="utf-8") as json_file:
        content = {
            "province": province_list,
            "prices": pricing_list
        }
        json.dump(content, json_file, indent=4)

def get_all_provinces(province_list: dict):
    """Print all provinces with their corresponding index.

    Args:
        province_list (dict): A dictionary of provinces.
    """
    print("====================== Provinces =============================")
    for index, province in enumerate(province_list, start=1):
        print(f"{index} - {province}")

def get_all_governorates(province_list: dict, province: str):
    """Print all governorates for a specified province.

    Args:
        province_list (dict): A dictionary of provinces with their governorates.
        province (str): The name of the province to list governorates for.
    """
    print("==================== Governorates =========================")

    for index, governorate in enumerate(province_list[province], start=1):
        print(f"{index} - {governorate}")

def get_all_prices(pricing_list: dict):
    """Print all prices with their corresponding index.

    Args:
        pricing_list (dict): A dictionary of prices associated with titles.
    """
    print("========================= Prices ===========================")
    for index, (title, cost) in enumerate(pricing_list.items(), start=1):
        print(f"{index} - {title} current price: {cost}")