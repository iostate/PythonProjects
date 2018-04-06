#!/usr/local/bin/python

from pytube import YouTube

print('Enter the YouTube URL: ')
url=str(input())
yt = YouTube(url)

# print('Commencing download... \n')

# BUG: This line saves with .webm extension
# Is it fixed?

# query the streams for this video, save filename as tds.mp4

# Not recognizing the slashes
yt.streams.first().download(None, filename='\/crap\/tds')



# Use following line if you want to save
# as an MP3
# yt.streams.first().download()

# print('Download finished!')

# Improvements that need to be made:
# Learn to save the resulting mp3 file as the name of the YouTube title
# Learn how to create the bash script (check below) and to run it in python

# Does this code open up a different shell?
# !/bin/sh
# python3 /Users/qmtruong92/Code/PythonProjects/DownloadMP4/pytube_dl_video.py
# ffmpeg -i tds.mp4 filename.mp3
