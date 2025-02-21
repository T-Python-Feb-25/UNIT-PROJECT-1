# Importing Libraries and modules
from logger import load_json_data
from colorama import Fore

def search(word:str):
    '''
    Searches for a word or phrase in the titles of the downloaded history.
    Args:
        word (str): The word or phrase to search for in the history titles.
    Returns:
        None
    '''
    try:
        list_of_data = load_json_data()
        while True:
            count = 1
            choice = input("Do you want Exact Match or Partial Match - E for Exact - P for Partial: ")
            if choice.lower() == "e":
                for item in list_of_data:
                    if word.lower().strip() == item['title'].lower():
                        print(f"{Fore.CYAN}{count}- {item['title']} | {item['format']} {Fore.RESET}")
                        count+=1
                if count == 1:
                    print(f"{Fore.RED}No Record Found For '{word}'{Fore.RESET}")
                break
            elif choice.lower() == "p":
                for item in list_of_data:
                    if word.lower() in item['title'].lower():
                        print(f"{Fore.CYAN}{count}- {item['title']} | {item['format']}{Fore.RESET}")
                        count+=1
                if count == 1:
                    print(f"{Fore.RED}No Record Found For '{word}' {Fore.RESET}")
                break
            else:
                print(Fore.RED + "Invalid Choice" + Fore.RESET)
    except Exception:
            print(Fore.RED + "There is no download history" + Fore.RESET)
            return 




