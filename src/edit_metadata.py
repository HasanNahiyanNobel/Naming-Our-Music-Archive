"""
Author: Hasan Nahiyan Nobel
Copyright: Attribution 4.0 International (CC BY 4.0)
"""

from os import scandir
from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3
from utilities import (
    PATH_OF_SONGS,
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
for file_path in scandir(PATH_OF_SONGS):
    # Load the file
    audio = EasyID3(file_path)
    file = ID3(file_path)

    # Show it in console
    print('Processing: ' + audio.filename)
    print('Old data  : ' + str(audio))

    # Extract title from filename
    file_name_with_extension = audio.filename.split(
        '. ', 1
    )[1]  # The second argument inside split function is needed to ensure that any period in title is preserved. For details: https://stackoverflow.com/a/6903597
    title = file_name_with_extension.split('.mp3')[0]

    # Clear existing metadata
    file.delete()

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
