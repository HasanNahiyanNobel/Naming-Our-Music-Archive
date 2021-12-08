"""
Author: Hasan Nahiyan Nobel
Copyright: Attribution 4.0 International (CC BY 4.0)
"""
import os
from utilities import PATH_OF_SONGS
from mutagen.easyid3 import EasyID3

# Print all the possible keys
# print(EasyID3.valid_keys.keys())

path_of_songs = PATH_OF_SONGS

# Data to be added
title = ''
album = 'The Velvet Underground'
artist = 'The Velvet Underground'
albumartist = 'The Velvet Underground'
genre = 'Folk rock; Rock; Pop'
date = '1969'
originaldate = '1969'

# Scan the directory and edit metadata
tracknumber = 1
for file_path in os.scandir(path_of_songs):
    # Load the file
    audio = EasyID3(file_path)

    # Show it in console
    print('Processing: ' + audio.filename)
    print('Old data  : ' + str(audio))

    # Clear existing metadata
    for key in audio.keys():
        audio[key] = ''

    # Add new data
    audio['title'] = title
    audio['album'] = album
    audio['artist'] = artist
    audio['albumartist'] = albumartist
    audio['genre'] = genre
    audio['date'] = date
    audio['originaldate'] = originaldate
    audio['tracknumber'] = str(tracknumber)

    # Save the file
    audio.save()

    # Show in console
    print('New data  : ' + str(audio) + '\n')

    # Increase track number
    tracknumber += 1
