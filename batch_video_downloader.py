import yt_dlp
from check_url import check_url
from colorama import Fore
from logger import save_to_history

def batch_download():
    number_of_url = int(input("How many Numbers Of URL?: "))


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
        except Exception:
            raise Exception

    
    options = {
        "quiet": True,
        "outtmpl": "downloads/%(title)s.%(ext)s",
        'no_warnings' : True,
        }
    for video_url in video_urls:
        with yt_dlp.YoutubeDL(options) as downloader:  
            info_dict = downloader.extract_info(video_url, download=True)  
            print(Fore.GREEN + "All Videos Downloaded successfully" + Fore.RESET)

            video_title = info_dict.get('title', 'Unknown Title')  
            video_url = info_dict.get('url', 'Unknown URL')  
            video_format = info_dict.get('ext', 'Unknown Format') 

            video_detailes = {
            "title" : video_title,
            "url" : video_url,
            "format" : video_format
            }
            save_to_history(video_detailes)


