# Importing Libraries and modules
from single_video_downloader import download
from logger import view_history
from colorama import Fore
from audio_downloader import audio_download
from batch_video_downloader import batch_download


menu:str ='''
------------------------------
YouTube Downloader Menu:
1- Download a Single Video
2- Download Multiple Videos
3- Download Audio
4- View Download History
5- Exit 
------------------------------
''' 
while True:
    print(menu.strip())
    choice:str = input("Enter Your Choice: ").strip()
    if choice == "1":
        video_url:str = input("Enter the YouTube video URL: ")
        download(video_url)
    elif choice == "2":
        batch_download()
    elif choice == "3":
        video_url:str = input("Enter the YouTube video URL: ")
        audio_download(video_url)
    elif choice == "4":
        view_history()
    elif choice == "5":
        print("Goodbye See You Soon")
        break
    else:
        print(Fore.RED + "Invalid Choice - Try Again" + Fore.RESET)
