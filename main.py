
from pytube import YouTube
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

Folder_Name = ""

def openLocation():
    global Folder_Name 
    Folder_Name = filedialog.askdirectory()
    if( len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg="green")
    else:
        locationError.config(text="Please Choose Folder!", fg="red")

def downloadVideo():
    choice = ytdChoices.get()
    url = ytdEntry.get()
    if len(url) > 1:
        ytdError.config(text="")
        yt = YouTube(url)
        if choice == choices[0]:
            select = yt.streams.filter(progressive=True).first()
        elif choice == choices[1]:
            select = yt.streams.filter(progressive=True).last()
        elif choice == choices[2]:
            select = yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Error!", fg="red")
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!")

root = Tk()
root.title("Youtube Downloader")
root.geometry("350x400")
root.columnconfigure(0, weight =1)

ytdLabel = Label(root, text="Enter URL:", font=("jost", 15))
ytdLabel.grid()

ytdEntryBox = StringVar()
ytdEntry = Entry(root, width=50, textvariable=ytdEntryBox)
ytdEntry.grid()

ytdError = Label(root, text="", fg="red", font=("jost", 10))
ytdError.grid()

saveLabel = Label(root, text="Save Location", font=("jost", 15, "bold"))
saveLabel.grid()

saveEntry = Button(root, width=15, bg="red", fg="white", text="Choose Path", command=openLocation)
saveEntry.grid()

locationError = Label(root, text="", fg="red", font=("jost", 10))
locationError.grid()

ytdQuality = Label(root, text="Select Quality", font=("jost", 15))
ytdQuality.grid()

choices = ["144p", "720p", "Only Audio"]
ytdChoices = ttk.Combobox(root, values=choices)
ytdChoices.grid()

downloadbtn = Button(root, text="Download", width=15, bg="red", fg="white", command=downloadVideo)
downloadbtn.grid()

developerLabel = Label(root, text="Saif ©2021 ", font=("jost", 10))
developerLabel.grid()


root.mainloop()