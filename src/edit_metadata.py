"""
Author: Hasan Nahiyan Nobel
Copyright: Attribution 4.0 International (CC BY 4.0)
"""

import os
from mutagen.easyid3 import EasyID3
from utilities import (
    PATH_OF_SONGS,
    title,
    album,
    artist,
    albumartist,
    genre,
    date,
    originaldate,
)

# Print all the possible keys
# print(EasyID3.valid_keys.keys())

# Scan the directory and edit metadata
tracknumber = 1
for file_path in os.scandir(PATH_OF_SONGS):
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
