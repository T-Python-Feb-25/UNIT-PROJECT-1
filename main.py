# Importing Libraries and modules
from check_url import check_url
from colorama import Fore
from video_downloader import download, batch_download
from logger import view_history
from audio_downloader import audio_download


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
			while True:
					try:
							video_url:str = input("Enter the YouTube video URL: ")
							check_url(video_url)
							download(video_url)
							break
					except ValueError as e:
							print(e)
					except Exception:
							print(Fore.RED + "Something Wrong Happen" + Fore.RESET)
	elif choice == "2":
					try:
							batch_download()
					except Exception:
							print(Fore.RED + "Something Wrong Happen" + Fore.RESET)
	elif choice == "3":
			while True:
					try: 
							video_url:str = input("Enter the YouTube video URL: ")
							check_url(video_url)
							audio_download(video_url)
							break
					except ValueError as e:
							print(e)
					except Exception:
							print(Fore.RED + "Something Wrong Happen" + Fore.RESET)
	elif choice == "4":
			view_history()
	elif choice == "5":
			print(Fore.CYAN + "Goodbye See You Soon" + Fore.RESET)
			break
	else:
			print(Fore.RED + "Invalid Choice - Try Again" + Fore.RESET)
