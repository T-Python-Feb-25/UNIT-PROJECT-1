from downloader import download
from logger import view_history
from colorama import Fore


menu:str ='''
------------------------------
YouTube Downloader Menu:
1- Download a video
2- View download history
3- Exit 
------------------------------
''' 
while True:
    print(menu.strip())
    choice:str = input("Enter Your Choice: ").strip()
    if choice == "1":
        video_url:str = input("Enter the YouTube video URL: ")
        download(video_url)
    elif choice == "2":
        view_history()
    elif choice == "3":
        print("Goodbye See You Soon")
        break
    else:
        print("Invalid Choice - Try Again")
