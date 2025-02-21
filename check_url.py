# Importing Libraries and modules
from colorama import Fore
import validators

def check_url(url:str):
	'''
	Check if URL from youtube and Validates a given URL 

  Args:
        url (str): The URL to validate.
	Returns
				None
	'''
	if url.find("youtu") > 0:
		if not validators.url(url):
			raise ValueError(Fore.RED + "Invalid URL" + Fore.RESET)
	else:
		raise ValueError(Fore.RED + "Invalid URL - It is not a youtube url" + Fore.RESET)


