#!/usr/local/bin/python
from pytube import YouTube

print('Enter the YouTube URL: ')

# Fixes the "wanted a string" error?
# url = str(raw_input())
# Works for almost all URLS.. See OneNote for links
# that do not work
url = str(input())
yt = YouTube(url)
title = yt.title

# Print the title of the pytube_dl_video
# print("Title: " + title)
print("Downloading: " + title)

# Change the filename
yt.streams.first().download(None, filename=title)
print("Download finished!")

print("*****************BEGIN BASH SCRIPT*****************")



# Download the first stream of this file and save it as craptds (the slashes
# are not recognized) in the current directory. .
# The downloaded stream will either be a .webm or .mp4
# yt.streams.first().download(None, filename='\/crap\/tds')
# print('Download finished!')

# Improvements that need to be made:
# Learn to save the resulting mp3 file as the name of the YouTube title
# Learn how to create the bash script (check below) and to run it in python

# Does this code open up a different shell?
# !/bin/sh
# python3 /Users/qmtruong92/Code/PythonProjects/DownloadMP4/pytube_dl_video.py
# ffmpeg -i tds.mp4 filename.mp3
