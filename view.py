from logger import load_json_data
from colorama import Fore

def view_videos():
    count = 1
    list_of_data = load_json_data()
    for number, item in enumerate(list_of_data):
        if item["format"] == "mp4":
            print(f"{Fore.CYAN}{count}- {item["title"]}{Fore.RESET}")
            count+=1

def view_audios():
    count = 1
    list_of_data = load_json_data()
    for item in list_of_data:
        if item["format"] == "mp3":
            print(f"{Fore.CYAN}{count}- {item["title"]}{Fore.RESET}")
            count+=1


def view():
    choice = input("Do you want to search for 'video or audio' v for video - a for audio: ")
    if choice == "a":
        view_audios()
    elif choice == "v":
        view_videos()
    else:
        print(Fore.RED + "Invalid Choice" + Fore.RESET)

