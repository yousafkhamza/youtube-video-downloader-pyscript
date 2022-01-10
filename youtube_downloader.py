import pytube  
from pytube import YouTube  
import os


current_path = os.getcwd()
if not os.path.exists("./Downloads"):
    os.makedirs("./Downloads")

video_url = input("Youtube URL: ")
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    formated_percentage = "{:.2f}".format(percentage_of_completion)
    print(formated_percentage+"%")
        
def main():
    chunk_size = 1024
    video = yt.streams.get_highest_resolution()
    title = video.title
    print(f"\nFetching \"{video.title}\"..")
    print(f"Information: \n"
          f"Highest Resolution: {video.resolution}\n"
          f"Author: {yt.author}")
    print("Views: {:,}".format(yt.views))

    print("\nAvailable Formats: ")
    A=[]
    res=yt.streams.filter(progressive=True, file_extension='mp4')
    if res.filter(resolution="360p"):
        A.append("360p")

    if res.filter(resolution="480p"):
        A.append("480p")

    if res.filter(resolution="720p"):
        A.append("720p")

    if res.filter(resolution="1080p"):
        A.append("1080p")

    if res.filter(resolution="1440p"):
        A.append("1440p")
    print(A)
    
    format_res = input("Chosse one format would you like to download (eg:360p): ")
    if format_res.endswith("p"):
        if format_res in A:
            video = yt.streams.filter(res=format_res, file_extension = "mp4").first()
            print(f"\nInformation about the video format you had selected: \n"
                  f"File size: {round(video.filesize * 0.000001, 2)} MB\n"
                  f"Selected Resolution: {video.resolution}\n")
            print("Downloading....")
            yt.register_on_progress_callback(on_progress)
            yt.streams.filter(res=format_res, file_extension = "mp4").first().download("./downloads")
            print("Download Successful")
            print("Please go and watch same under '{}/Downloads'....".format(current_path))
        else:
            print("Choose a valid format from available list mentioned above")
    else:
        format_res=format_res+"p"
        if format_res in A:
            video = yt.streams.filter(res=format_res, file_extension = 'mp4').first()
            print(f"\nInformation of the current video format: \n"
                  f"File size: {round(video.filesize * 0.000001, 2)} MB\n"
                  f"Selected Resolution: {video.resolution}\n")
            print("Downloading....")
            yt.register_on_progress_callback(on_progress)
            yt.streams.filter(res=format_res, file_extension = 'mp4').first().download("./downloads")
            print("Download Successful")
            print("Please go and watch the same under '{}/Downloads'....".format(current_path))
        else:
            print("Choose a valid format from available list mentioned above")
            
if video_url.startswith("http"):
    yt=YouTube(video_url)
    main()
else:
    print("Please enter a vaild URL.")
