from pytube import YouTube

i = input("Enter the url: ")
url = str(i)
i2 = input("Enter the extension of file: ")
if i2.lower() == "mp3" or i2.lower() == "wav":
    yt = YouTube(url)
    stream = yt.streams.get_audio_only()
    i3 = input("Enter the file name: ")
    stream.download(filename=f"{str(i3)}.{str(i2)}")
elif i2.lower() == "mp4":
    yt = YouTube(url)
    i3 = input("Download highest or lowest resolution: ")
    if i3.lower() == "highest":
        i4 = input("Enter the file name: ")
        stream = yt.streams.get_highest_resolution()
        stream.download(filename=f"{str(i4)}.{str(i2)}")
    elif i3.lower() == "lowest":
        i4 = input("Enter the file name: ")
        stream = yt.streams.get_lowest_resolution()
        stream.download(filename=f"{str(i4)}.{str(i2)}")
    else:
        pass
else:
    pass
