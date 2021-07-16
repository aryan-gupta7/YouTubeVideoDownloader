import os
import pytube
save_path = "C:\\Users\\User\\Desktop\\songs\\playlist" #Enter path where to save
links = [
    {"link": "https://youtu.be/xCBUG-hyKnc?list=PLVJX5FVbNKoLsXh-IGcLP2Jin9OHijNC9", "type": "playlist", "extension": "mp3"}
]#Enter links of youtube video in format of dict. {"link": videoLink, "type": "playlist or video", "extension": "mp3 or mp4 in which to download"}

def download(video_link, extension):
    try:
        youtube = pytube.YouTube(video_link)
    except:
        print("Invalid Link provided")
        quit()

    try:
        os.chdir(save_path)
    except:
        print("Wrong path provided!")
        quit()
    try:
        if extension == "mp3":
            video = youtube.streams.filter(only_audio=True).first()
        elif extension == "mp4":
            video = youtube.streams.first()
        else:
            print(f"Invalid extension = {extension}")
            print("Extension should be any of 'mp3' or 'mp4'")
            quit()
    except Exception as e:
        print(f"Error = {e}")
        print("Check your network connection")
        quit()

    try:
        video.download(save_path)
        print(f'{video.title[:40]} - {extension} downloaded to {save_path}')
    except: 
        print(f"{video.title[:40]} - Some Error!")

if __name__ == "__main__":
    print("A youtube video/audio downloader for you made by aryan with collab. of akshat(jrke)!")
    for download_ in links:
        try:
            if download_["type"] == "video":
                download(download_["link"], download_["extension"])
            elif download_["type"] == "playlist":
                playlist = pytube.Playlist(download_["link"])
                print(f"Downloading {len(playlist.video_urls)} songs from playlist {playlist.title} by {playlist.owner}!")
                for link in playlist.video_urls:
                    download(link, download_["extension"])
            else:
                print(f"Invalid type = {download_['type']}")
                print("Type should be any of 'video' or 'playlist'")
        except Exception as E:
            print("Unexpected Error =", E)
            print("Check your network, typos, links, etc.")
