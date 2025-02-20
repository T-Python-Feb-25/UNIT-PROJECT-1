import os
import subprocess
from colorama import Fore

def open_audio_folder(folder_path):
    '''
    Opens the folder containing audio files in the file explorer.
    Args:
        folder_path (str): The path to the audio folder.
    Returns:
        None
    '''
    if os.path.exists(folder_path):
        subprocess.run(['explorer', folder_path])  # Opens the folder in Explorer
        print(Fore.GREEN + "Opening the audio folder..." + Fore.RESET)
    else:
        print(Fore.RED + "Audio folder not found!" + Fore.RESET)
