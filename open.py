import subprocess
from colorama import Fore
import os

def open_media_folder():
    '''
    Opens a media folder based on user input.

    Args:
        None

    Returns:
        None
    '''
    while True:
        user_choice = input("Do You Want to Play Audio or Video? (y/n): ").strip().lower()
        
        if user_choice not in ("y", "n"):
            print(Fore.RED + "Invalid Choice - Try Again" + Fore.RESET)
            continue
        
        if user_choice == "n":
            break
        
        media_choice = input("For audio press 'a' - For videos press 'v': ").strip().lower()
        
        if media_choice == "a":
            folder_path = r"E:\My-journey\Full-Stack Journey\Tuwaiq\Camp\Project\UNIT-PROJECT-1\audios"
        elif media_choice == "v":
            folder_path = r"E:\My-journey\Full-Stack Journey\Tuwaiq\Camp\Project\UNIT-PROJECT-1\videos"
        else:
            print(Fore.RED + "Invalid Media Choice - Try Again" + Fore.RESET)
            continue
        if not os.path.exists(folder_path):
            print(Fore.RED + "Error: Folder does not exist." + Fore.RESET)
            continue
        subprocess.run(f'explorer "{folder_path}"')
        break

