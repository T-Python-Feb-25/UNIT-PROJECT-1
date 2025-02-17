# Importing Libraries and modules
import yt_dlp
from colorama import Fore
from logger import save_to_history
def download(video_url:str):
  '''
  Downloads a YouTube video from the given URL and logs the video data using `save_to_history' 

  Args: 
    video_url (str): A string containes youtube url  
  Returns:
    None
  '''
  video_title:str = '%(title)s'  
  video_extension:str = '%(ext)s'  
  output_path:str= f"downloads/{video_title}.{video_extension}"

  options:dict = {
    'outtmpl': output_path,
    'quiet' : True
    }

  with yt_dlp.YoutubeDL(options) as downloader:  
    info_dict = downloader.extract_info(video_url, download=True)  # Extract details and download the video

    video_title = info_dict.get('title', 'Unknown Title')  # Get the title
    video_url = info_dict.get('url', 'Unknown URL')  # Get the video URL
    video_format = info_dict.get('ext', 'Unknown Format')  # Get the format (file extension)


  print(Fore.GREEN + "Download completed successfully" + Fore.RESET)
  

  video_detailes = {
    "title" : video_title,
    "url" : video_url,
    "format" : video_format
  }
  save_to_history(video_detailes)


