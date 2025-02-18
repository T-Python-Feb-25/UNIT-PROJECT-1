import yt_dlp
from colorama import Fore
from logger import save_to_history

def audio_download(video_url:str):
  
  video_title:str = '%(title)s'  
  audio_extension:str = 'mp3'  
  output_path:str= f"audio/{video_title}.{audio_extension}"

  options:dict = {
    'outtmpl': output_path,
    'quiet' : True,
    'no_warnings' : True,
    }
  
  with yt_dlp.YoutubeDL(options) as downloader:
    downloader.download([video_url])

    info_dict = downloader.extract_info(video_url, download=True)  

    audio_title = info_dict.get('title', 'Unknown Title')  
    audio_url = info_dict.get('url', 'Unknown URL')  

  audio_detailes = {
    "title" : audio_title,
    "url" : audio_url,
    "format" : "mp3"
  } 
  save_to_history(audio_detailes)

  print(Fore.GREEN + "Audio downloaded completed successfully" + Fore.RESET)



  