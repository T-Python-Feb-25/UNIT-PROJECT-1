# Importing Libraries and modules
import yt_dlp
from check_url import check_url
from colorama import Fore
from logger import save_to_history


# Function For Downloading A Single Video
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
    'quiet' : True,
    'no_warnings' : True,
    }

  with yt_dlp.YoutubeDL(options) as downloader:  
    info_dict = downloader.extract_info(video_url, download=True)  
    video_title = info_dict.get('title', 'Unknown Title')  
    video_url = info_dict.get('url', 'Unknown URL')  
    video_format = info_dict.get('ext', 'Unknown Format')  

  print(Fore.GREEN + "Download completed successfully" + Fore.RESET)
  

  video_detailes = {
    "title" : video_title,
    "url" : video_url,
    "format" : video_format
  }
  save_to_history(video_detailes)

# Function For Downloading A Mulitple Videos
def batch_download():
  '''
  Downloads multiple YouTube videos based on user input.
  Args: 
      None
  Returns:
      None
  '''
  while True: 
    try:
      number_of_url = int(input("How many Numbers Of URL?: "))
      break
    except Exception:
      print(Fore.RED +"Invalid Value - Please Enter a Number" + Fore.RESET)


  video_urls = []
  count = 1
  while number_of_url > 0:
    try:
      while True:
        video_urls_input = input(f"Enter YouTube video URL {count} : ").strip()
        check_url(video_urls_input)
        video_urls.append(video_urls_input)
        number_of_url-=1
        count+=1
        break
    except ValueError as e:
              print(e)


  
  options = {
      "quiet": True,
      "outtmpl": "downloads/%(title)s.%(ext)s",
      'no_warnings' : True,
      }
  for video_url in video_urls:
    with yt_dlp.YoutubeDL(options) as downloader:  
      info_dict = downloader.extract_info(video_url, download=True)  
      video_title = info_dict.get('title', 'Unknown Title')  
      video_url = info_dict.get('url', 'Unknown URL')  
      video_format = info_dict.get('ext', 'Unknown Format') 

      video_detailes = {
      "title" : video_title,
      "url" : video_url,
      "format" : video_format
      }
      save_to_history(video_detailes)
  print(Fore.GREEN + "All Videos Downloaded successfully" + Fore.RESET)


