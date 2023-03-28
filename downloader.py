from pytube import YouTube


def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    return stream.download("./Downloads")