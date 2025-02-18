from colorama import Fore
import validators

def check_url(url:str):
    if not validators.url(url):
        raise ValueError(Fore.RED + "Invalid URL" + Fore.RESET)
