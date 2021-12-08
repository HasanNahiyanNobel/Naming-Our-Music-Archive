"""
Author: Hasan Nahiyan Nobel
Copyright: Attribution 4.0 International (CC BY 4.0)
"""
import os

from mutagen.easyid3 import EasyID3

# Print all the possible keys
# print(EasyID3.valid_keys.keys())

# Directory of the songs
path_of_songs = "G:\গীতাঞ্জলি\উত্তম সঙ্গীত\_উর্ধ্বগামী\Robert Johnson"

# Data to be added
title = ""
album = "The Complete Recordings"
artist = "Robert Johnson"
albumartist = "Robert Johnson"
genre = "Delta Blues"
date = "1990"
originaldate = "1936-1937"

# Scan the directory and edit metadata
tracknumber = 1
for file_path in os.scandir(path_of_songs):
    # Load the file
    audio = EasyID3(file_path)

    # Show it in console
    print("Processing: " + audio.filename)
    print("Old data  : " + str(audio))

    # Clear existing metadata
    for key in audio.keys():
        audio[key] = ""

    # Add new data
    audio["title"] = title
    audio["album"] = album
    audio["artist"] = artist
    audio["albumartist"] = albumartist
    audio["genre"] = genre
    audio["date"] = date
    audio["originaldate"] = originaldate
    audio["tracknumber"] = str(tracknumber)

    # Save the file
    audio.save()

    # Show in console
    print("New data  : " + str(audio) + '\n')

    # Increase track number
    tracknumber += 1
