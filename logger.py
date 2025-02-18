import json
from colorama import Fore
def save_to_history(dictionary:dict):
	'''
	The save_to_history function takes a dictionary containing video data and stores it 
	in a JSON file called `history.json`. If the file doesn't exist or is empty, 
	it creates a new file and stores the data as a list.
	

	Args: 
			dictionary (dict):A dictionary containes video data 
			it includes 'title', 'url', 'format'
	Return:
			None
	'''
	try:
			with open("history.json" ,"r", encoding="UTF-8") as log:
					all_json_data = json.load(log)
	except Exception:
			all_json_data = []
	
	all_json_data.append(dictionary)
	with open("history.json" ,"w", encoding="UTF-8") as log:
		json.dump(all_json_data, log)
def view_history():
	'''
	It iterates over data saved in history.json file and print it to user

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