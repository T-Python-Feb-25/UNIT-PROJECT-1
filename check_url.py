from colorama import Fore
import validators

def check_url(url:str):
	'''
	Validates a given URL

    Args:
        url (str): The URL to validate.
		Returns
				None
	'''
	if not validators.url(url):
		raise ValueError(Fore.RED + "Invalid URL" + Fore.RESET)