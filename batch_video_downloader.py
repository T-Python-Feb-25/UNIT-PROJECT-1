import yt_dlp
from colorama import Fore
from logger import save_to_history

def batch_download():
    number_of_url = int(input("How many Numbers Of URL?: "))

    video_urls = []
    while number_of_url > 0:
        video_urls_input = input("Enter YouTube video URLs : ").strip()
        video_urls.append(video_urls_input)
        number_of_url-=1
    
    options = {
        "quiet": True,
        "outtmpl": "downloads/%(title)s.%(ext)s"  
       
        }
    
    for video_url in video_urls:
        with yt_dlp.YoutubeDL(options) as downloader:  
            info_dict = downloader.extract_info(video_url, download=True)  
            print(Fore.GREEN + "Download completed successfully" + Fore.RESET)

            video_title = info_dict.get('title', 'Unknown Title')  
            video_url = info_dict.get('url', 'Unknown URL')  
            video_format = info_dict.get('ext', 'Unknown Format') 

            video_detailes = {
            "title" : video_title,
            "url" : video_url,
            "format" : video_format
            }
            save_to_history(video_detailes)


