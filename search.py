from logger import load_json_data
from colorama import Fore

def search(word:str):
    list_of_data = load_json_data()
    while True:
        count = 1
        choice = input("Do you want Exact Match or Partial Match - E for Exact - P for Partial: ")
        if choice.lower() == "e":
            for item in list_of_data:
                if word.lower() == item['title'].lower():
                    print(f"{Fore.CYAN}{count}- {item['title']}{Fore.RESET}")
                    count+=1
            break
        elif choice.lower() == "p":
            for item in list_of_data:
                if word.lower() in item['title'].lower():
                    print(f"{Fore.CYAN}{count}- {item['title']}{Fore.RESET}")
                    count+=1
            break
        else:
            print(Fore.RED + "Invalid Choice" + Fore.RESET)




