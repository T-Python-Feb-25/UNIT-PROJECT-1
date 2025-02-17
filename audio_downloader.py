import yt_dlp
from colorama import Fore

def audio_download(video_url:str):
  
  video_title:str = '%(title)s'  
  video_extension:str = '.mp3'  
  output_path:str= f"video/{video_title}.{video_extension}"

  options:dict = {
    'outtmpl': output_path,
    'quiet' : True,
    'format': 'bestvideo/best'
    }
  
  with yt_dlp.YoutubeDL(options) as downloader:
    downloader.download([video_url])
    print(Fore.GREEN + "Audio downloaded completed successfully" + Fore.RESET)



  