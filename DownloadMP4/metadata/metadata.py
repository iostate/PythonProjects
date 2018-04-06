# Python 2

import eyed3

# Dependencies for filename
import glob
import os

# Ask for user information



mp3files = glob.glob('/Users/qmtruong92/Music')
latest_file = max(mp3files, key=os.path.getctime)

# check typeof latest_file

# Print

# print(str(latest_file))




audio = eyed3.load(str(latest_file))

# Print current data
print audio.tag.artist
print audio.tag.title



#basically its eyed3.core.AudioFile.artist

# Change the data

audio.tag.artist = u"Berner"
audio.tag.title = u"Knock Phone"
print audio.tag.artist
print audio.tag.title

# Does this save the metadata to the actual MP3?
audio.tag.save()



# https://stackoverflow.com/questions/29544986/whats-the-difference-between-eyed3-and-eyed3-and-how-can-i-edit-mp3-tags-with
#Using eyed3 0.8??

# from eyed3 import id3

# This code works.
# tag = id3.Tag()
# tag.parse("/Users/qmtruong92/Music/BERNER ( KNOCK PHONE ) URBAN FARMER.mp3")
# print(tag.artist)
# print(tag.title)
