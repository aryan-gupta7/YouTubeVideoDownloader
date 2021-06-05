# Importing Required Packages.
import os
import time
import pytube
import subprocess
from tqdm import tqdm


print("Hey there...\nThis is a python program developed by Aryan Gupta to download youtube video through links.")

# Getting Video link through input/
video_link = input("Enter the link for the video to download - ")

# Checking if link is INVALID
try:
    youtube = pytube.YouTube(video_link)
except:
    if len(video_link) < 35:
        print("Invalid Link provided")
        quit()
    else:
        print("Connect to Internet first!")
        quit()

# Getting the save path
save_path = input("Enter the save path (format - 'disk:/folder/name' e.g. 'E:/yt_downloads') - ") 
# Checking if the path is valid.
try:
    os.chdir(save_path)
except:
    print("Wrong path provided!")
    quit()

# Getting the first video of all the streams
try:
    video = youtube.streams.first()
except:
    print("Please connect to internet first!")
    quit()

title = video.title

# Creating a loading bar.
for i in tqdm(range(100),desc=f'Downloading {title[:20]}...'):
    try:
        # Downloading video to the save path
        if i == 0: video.download(save_path) 
    except: 
        print("Some Error!")
        break
    time.sleep(.1)

# Getting the Filename.
files_in_dir = os.listdir(save_path)
for i in files_in_dir:
    if not i.endswith(".mp4"):
        files_in_dir.pop(files_in_dir.index(i))
filename = ''
for video in files_in_dir:
    if video[:5] == title[:5]:
        filename = video

# Opening the file explorer with selected downloaded video.
filepath = os.path.abspath(filename)
print(f'Video downloaded to {filepath}')
subprocess.Popen(f'explorer /select, "{filepath}"')
