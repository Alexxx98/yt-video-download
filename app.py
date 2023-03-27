from tkinter import *
from PIL import Image, ImageTk
from pytube import YouTube


root = Tk()
root.geometry("720x360")
   
image = ImageTk.PhotoImage(Image.open("/home/aleksander/Documents/Programming/Python/Projects/YouTubeVideoDownloader/Assets/youtube-logo.png").resize((200,100)))
    
label = Label(root, image=image)
label.pack()
    
urlEntry = Entry(root, width=50, borderwidth=5)
urlEntry.pack()

def download_video():
    yt = YouTube(urlEntry.get())
    stream = yt.streams.get_highest_resolution()
    stream.download("/home/aleksander/Videos/YouTube")
    
downlaodButton = Button(root, text="Download", command=download_video)
downlaodButton.pack()

root.mainloop()