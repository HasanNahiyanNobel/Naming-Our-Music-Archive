"""
Author: Hasan Nahiyan Nobel
Copyright: Attribution 4.0 International (CC BY 4.0)
"""
import ntpath
from os import getcwd, scandir, path

from mutagen.id3 import ID3, APIC

# Declare the final variables
PATH_OF_ALBUM = '../input/album'
PATH_OF_ALBUM_ART = None  # Initializing with `None`
AUDIO_FILE_EXTENSIONS = ['.mp3', '.flac', '.m4a', '.wav', '.ogg', '.wma']
IMAGE_FILE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
CONFIG_FILE_EXTENSIONS = ['.ini', '.json', '.xml', '.yml', '.yaml', '.toml']

# Get the current working directory
current_dir = getcwd()



# Find the album art
def find_album_art_for_current_file(file_path):
    directory_of_current_file = ntpath.dirname(file_path)
    for file_path in scandir(directory_of_current_file):
        file_extension = ntpath.splitext(file_path)[1]
        if file_extension in IMAGE_FILE_EXTENSIONS:
            return file_path
    raise Exception(f'No album art found for: {file_path}')



# Change the album art
def change_album_art(file_path, album_art_path):
    audio = ID3(file_path)
    audio.setall('APIC', [])
    print(audio.filename)
    album_art_extension = ntpath.splitext(album_art_path)[1]  # Get the extension of the album art
    album_art_mime_type = f'image/{album_art_extension[1:]}'  # Remove the dot
    with open(album_art_path, 'rb') as album_art_file:
        print(album_art_file.name)
        audio.add(
            APIC(
                encoding=3,  # 3 is for utf-8
                mime=album_art_mime_type,
                type=3,  # 3 is for the cover image
                desc=u'Cover',
                data=album_art_file.read()
            )
        )
    audio.setall('APIC', [])
    audio.save()



# Associate album art to all audio files
def add_album_art(album_path):
    album_art = None
    for file_path in scandir(album_path):
        if path.isdir(file_path):
            print(f'Processing directory: {ntpath.basename(file_path)}')
            add_album_art(file_path)
        else:
            if album_art is None:
                album_art = find_album_art_for_current_file(file_path)
            file_extension = ntpath.splitext(file_path)[1]
            if file_extension in AUDIO_FILE_EXTENSIONS:
                album_art_path = ntpath.relpath(album_art, current_dir)
                change_album_art(file_path, album_art_path)



# Run the function
add_album_art(PATH_OF_ALBUM)
