#!/usr/bin/python3
from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Error downloading!")
    else:
        print("Dowmnload has completed!")

link = input("Enter youtube url link you'd like to download: ")
Download(link)
