# Importing Libraries and modules
from logger import load_json_data
from colorama import Fore
import json

def view_videos():
    '''
    Displays a list of downloaded video files in MP4 format.
    Args:
        None
    Returns:
        None
    '''
    try:
      count = 1
      list_of_data = load_json_data()
      for item in list_of_data:
          if item["format"] == "mp4":
              print(f"{Fore.CYAN}{count}- {item['title']}{Fore.RESET}")
              count+=1
      if count == 1:
        print(Fore.RED + "No Viedos Downloaded" + Fore.RESET)
    except Exception:
	    print(Fore.RED + "There is no download history" + Fore.RESET)

def view_audios():
    '''
    Displays a list of downloaded audio files in MP3 format.
    Args:
        None
    Returns:
        None
    '''
    try:
      count = 1
      list_of_data = load_json_data()
      for item in list_of_data:
          if item["format"] == "mp3":
              print(f"{Fore.CYAN}{count}- {item['title']}{Fore.RESET}")
              count+=1
      if count == 1:
        print(Fore.RED + "No Audios Downloaded" + Fore.RESET)
    except Exception:
	    print(Fore.RED + "There is no download history" + Fore.RESET)

def view_history():
	'''
  Displays the download history from the 'history.json' file.
	Args:
			None
	Returns:
			None
	'''
	try:
			with open("history.json" ,"r", encoding="UTF-8") as log:
				all_json_data = json.load(log)
				for videos in all_json_data:
					for video in videos:
						print(f"- {video.capitalize() }: {videos[video]}")
					print(Fore.LIGHTBLUE_EX + ("-" * 150) + Fore.RESET)
	except Exception:
		print(Fore.RED + "There is no download history" + Fore.RESET)

def view():
    '''
    Prompts the user to select whether to view downloaded videos or audios.
    Args:
        None
    Returns:
        None
    '''
    while True:
      choice = input("Do you want to search for 'video or audio' v for video - a for audio: ")
      if choice == "a":
          view_audios()
          break
      elif choice == "v":
          view_videos()
          break
      else:
          print(Fore.RED + "Invalid Choice" + Fore.RESET)
