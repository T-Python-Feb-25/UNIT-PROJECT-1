# Importing Libraries and modules
import yt_dlp
from check_url import check_url
from colorama import Fore
from logger import save_to_history

# Function For Downloading A Single Audio
def audio_download(video_url:str):
  '''
  Downloads audio from a YouTube video and saves it as an MP3 file.
    Args:
        video_url (str): The URL of the YouTube video.
    Returns:
        None
  '''
  video_title:str = '%(title)s'  
  audio_extension:str = 'mp3'  
  output_path:str= f"audio/{video_title}.{audio_extension}"
  # Options for downloading 
  options:dict = {
    'outtmpl': output_path,
    'quiet' : True,
    'no_warnings' : True,
    }
  # Download video and extract video details
  with yt_dlp.YoutubeDL(options) as downloader:
    info_dict = downloader.extract_info(video_url, download=True)  
    audio_title = info_dict.get('title', 'Unknown Title')  
    audio_url = info_dict.get('url', 'Unknown URL')  

  audio_detailes = {
    "title" : audio_title,
    "url" : audio_url,
    "format" : "mp3"
  } 
  save_to_history(audio_detailes)
  print(Fore.GREEN + "Audio downloading completed successfully" + Fore.RESET)

# Function For Downloading A Multiple Audios
def batch_download():
  '''
  Downloads multiple YouTube audios based on user input.
  Args: 
      None
  Returns:
      None
  '''
  # Ashing user how many urls 
  while True: 
    try:
      number_of_url = int(input("How many Numbers Of URL?: "))
      if number_of_url >= 1:
         break
      else:
         raise Exception()
    except Exception:
      print(Fore.RED +"Invalid Value - Please Enter a Number and must be Above 0" + Fore.RESET)

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

  # Options for downloading 
  options = {
      "quiet": True,
      "outtmpl": "audio/%(title)s.mp3",
      'no_warnings' : True,
      }
  # Download video and extract video details
  for video_url in video_urls:
      with yt_dlp.YoutubeDL(options) as downloader:  
        info_dict = downloader.extract_info(video_url, download=True)  
        audio_title = info_dict.get('title', 'Unknown Title')  
        audio_url = info_dict.get('url', 'Unknown URL')  

      audio_detailes = {
        "title" : audio_title,
        "url" : audio_url,
        "format" : "mp3"
      } 
      save_to_history(audio_detailes)
  print(Fore.GREEN + "All Audios Downloaded successfully" + Fore.RESET)
