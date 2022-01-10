# Youtube Video Downloader Python Script
[![Build](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

---
## Description
This is a simple python script and it's used for mp4 type video downloading from youtube. also, it's used inbuilt python module "pytube". Furthermore, I know we have so many apps and online websites to do the same thing so it's just an experiment to study how to do those things in python.

----
## Feature
- Easy to download youtube videos
- You can choose a video format would you like
- MPEG4 format video

----
## Pre-Requests
- python 3.x
- python3-pip

#### How to Install Python (for windows)
[Installation Guide for python](https://www.python.org/downloads/)
[Installation Guide for GitBash terminal](https://git-scm.com/downloads) 
_once you have installed git bash then please use your windows command prompt with limited linux commands_


#### Pre-Requests (for RedHat-based-Linux)
```
yum install -y git
yum install -y python3
yum install -y python3-pip
```

#### Pre-Requests (for Debian-based-Linux)
````
apt install -y git
apt install -y python3
apt install -y python3-pip
````

#### Pre-Requests (for Termux-based-Linux)
````
pkg upgrade
pkg install git
pkg install python3
pkg install pip
````
> using termux who you guys please install requirements use `pip install -r requirements.txt` don't need to use pip3

----
## Modules Used
- [pytube](https://pytube.io/en/latest/)
- [os](https://docs.python.org/3/library/os.html)

---
## How to Get
```
git clone https://github.com/yousafkhamza/youtube-video-downloader-pyscript.git
cd https://github.com/yousafkhamza/youtube-video-downloader-pyscript.git
pip3 install -r requirements.txt
```

----
## How to execute
```
python3 youtube_downloader.py
```

----
## Output be like
```
C:\Users\yousaf>git clone https://github.com/yousafkhamza/youtube-video-downloader-pyscript.git
Cloning into 'youtube-video-downloader-pyscript'...
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 9 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.

C:\Users\yousaf>cd youtube-video-downloader-pyscript

C:\Users\yousaf\youtube-video-downloader-pyscript>pip3 install -r requirements.txt
Collecting pytube
  Downloading pytube-11.0.2-py3-none-any.whl (56 kB)
     |████████████████████████████████| 56 kB 654 kB/s
Installing collected packages: pytube
Successfully installed pytube-11.0.2

C:\Users\yousaf\youtube-video-downloader-pyscript>python3 youtube_downloader.py
Youtube URL: https://youtu.be/gJB3l7uc4RA                            <------------------- URL pasted here.

Fetching "Thathaka Theithare Video Song | Hridayam | Pranav | Vineeth | Prithviraj | Hesham |Visakh |Merryland"..
Information:
Highest Resolution: 720p
Author: Think Music India
Views: 1,312,619

Available Formats:
['360p', '720p']
Choose one format would you like to download (eg:360p): 720p        <------------------- Choose any resolution when available here.

Information about the video format you had selected:
File size: 13.6 MB
Selected Resolution: 720p

Downloading....
69.38%
100.00%
Download Successful
Please go and watch same under 'C:\Users\yousaf\youtube-video-downloader-pyscript/Downloads'....

C:\Users\yousaf\youtube-video-downloader-pyscript>dir Downloads
 Volume in drive C is Windows

 Directory of C:\Users\yousa\youtube-video-downloader-pyscript\Downloads

01/10/2022  08:49 AM        13,601,616 Thathaka Theithare Video Song  Hridayam  Pranav  Vineeth  Prithviraj  Hesham Visakh Merryland.mp4

C:\Users\yousa\youtube-video-downloader-pyscript>
```
_ScreenShots_

![alt_txt](https://i.ibb.co/yfSH8j4/Screenshot-1.png)
![alt_txt](https://i.ibb.co/8D0B9YS/Screenshot-2.png)

----
## Behind the code
````
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
            print("Choose a valid format from the available list mentioned above")
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
            print("Choose a valid format from the available list mentioned above")
            
if video_url.startswith("http"):
    yt=YouTube(video_url)
    main()
else:
    print("Please enter a valid URL.")
````

----
## Conclusion
This is a simple python script and it's used for mp4 type video downloading from youtube. 

### ⚙️ Connect with Me 

<p align="center">
<a href="mailto:yousaf.k.hamza@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/yousafkhamza"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a> 
<a href="https://www.instagram.com/yousafkhamza"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/></a>
<a href="https://wa.me/%2B917736720639?text=This%20message%20from%20GitHub."><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/></a><br />
