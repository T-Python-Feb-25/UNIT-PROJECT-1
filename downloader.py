import yt_dlp
def down(video_url):
  video_title:str = '%(title)s'  
  video_extension:str = '%(ext)s'  
  output_path:str= f"downloads/{video_title}.{video_extension}"

  options:dict = {
    'outtmpl': output_path,
    'quiet' : True
    }

  with yt_dlp.YoutubeDL(options) as downloader:  
      downloader.download([video_url])

  print("Download completed successfully")