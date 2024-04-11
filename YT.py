from pytube import YouTube

def download_youtube_video(link, download_path):
    try:
        yt = YouTube(link)
        print("Title:", yt.title)
        print("Views:", yt.views)
        
        yd = yt.streams.get_highest_resolution()
        yd.download(download_path)
        print("Video downloaded successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    video_link = input("enter the YouTube link you cocksucker: ")
    download_directory = '/Users/Leon/Downloads/YouTube Downloads'  # Update the download directory as needed
    
    download_youtube_video(video_link, download_directory)