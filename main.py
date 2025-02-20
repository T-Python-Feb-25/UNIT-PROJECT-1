# Importing Libraries and modules
from check_url import check_url
from colorama import Fore
from art import text2art
from video_downloader import download, batch_download
from audio_downloader import audio_download, batch_download as batch_download_audio
from view import view , view_history
from search import search

welcome = text2art("Welcome To Youtube Downloader",font="doom")
print(Fore.RED + welcome + Fore.RESET)
menu:str ='''
------------------------------
YouTube Downloader Menu:

1- Download a Single Video
2- Download Multiple Videos
3- Download Audio (Form Video)
4- Download Multiple Audios (From Videos)
5- View Download History
6- View Audios or Videos Downloaded 
7- Search for Downloaded Videos or Audios
8- Exit 
------------------------------
'''
while True:
	print(menu.strip())
	choice:str = input("Enter Your Choice: ").strip()
	if choice == "1":
			while True:
				try:
					video_url:str = input("Enter the YouTube video URL: ").strip()
					check_url(video_url)
					download(video_url)
					input("Enter to continue")
					break
				except ValueError as e:
					print(e)
				except Exception:
					print(Fore.RED + "Something Wrong Happen" + Fore.RESET)
	elif choice == "2":
		try:
			batch_download()
			input("Enter to continue")
		except Exception:
				print(Fore.RED + "Something Wrong Happen" + Fore.RESET)
	elif choice == "3":
		while True:
			try: 
				video_url:str = input("Enter the YouTube video URL: ").strip()
				check_url(video_url)
				audio_download(video_url)
				input("Enter to continue")
				break
			except ValueError as e:
				print(e)
			except Exception:
				print(Fore.RED + "Something Wrong Happen" + Fore.RESET)
	elif choice == "4":
		try:
			batch_download_audio()
			input("Enter to continue")
		except Exception:
			print(Fore.RED + "Something Wrong Happen" + Fore.RESET)
	elif choice == "5":
		view_history()
		input("Enter to continue")
	elif choice == "6":
		view()
		input("Enter to continue")
	elif choice == "7":
		word = input("Enter word or phrase to search for: ")
		search(word)
		input("Enter to continue")
	elif choice == "8":
		print(Fore.CYAN + "Goodbye See You Soon" + Fore.RESET)
		break
	else:
		print(Fore.RED + "Invalid Choice - Try Again" + Fore.RESET)



# https://youtu.be/7LxA9qXUY5k?si=898kZs_R7GgWoc4H
# https://youtu.be/QG5aEmS9Fu0?si=ZYrGNoZeIQC5-kRm