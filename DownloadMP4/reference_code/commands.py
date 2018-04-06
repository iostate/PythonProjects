#!/bin/sh
python3 /Users/qmtruong92/Code/PythonProjects/DownloadMP4/sample.py
# ffmpeg -i tds.mp4 newsong.mp3

# disable video recording
# ffmpeg -i -vn -ab tds.mp4 newsong.mp3

# convert the tds .webm to an mp3 using a wildcard
# ffmpeg -i *.webm -ab 128k newsong.mp3

# Delete all .webm files in the directory
# so that ffmpeg is able to convert more .webm files using the wildcard
# find . -name "*.webm" -type f -delete

# Delete all .mp4 files in the DIRECTORY
# so that ffmpeg is able to convert more .mp4 files using the wildcard
# find . -name "*.mp4" -type f -delete
