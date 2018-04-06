#!/usr/local/bin/python

from pytube import YouTube

# from pprint import pprint

print('Enter the YouTube URL: ')
url=str(input())
yt = YouTube(url)

# Print all the video and audio codecs available
# print(*(yt.streams.all()), sep='\n')

# Query streams that contain only the audio track
print(*yt.streams.filter(only_audio=True).all(), sep='\n')

stream = yt.streams
stream.first().download()



# print('Commencing download... \n')

# BUG: This line saves with .webm extension
# Is it fixed?

# DROPS IT IN THE CURRENT DIRECTORY
#########yt.streams.first().download(None, filename="tds.mp4")



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
