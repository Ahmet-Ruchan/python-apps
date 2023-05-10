import pytube

url = input("Enter video url: ")
path = "C:/Users/LENOVO/Desktop/HelloPython/YouTubeDownloader/Videos"
pytube.YouTube(url).streams.get_highest_resolution().download(path)
