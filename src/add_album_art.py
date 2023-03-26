"""
Author: Hasan Nahiyan Nobel
Copyright: Attribution 4.0 International (CC BY 4.0)
"""
import ntpath
from os import getcwd, scandir, path

# Declare the final variables
PATH_OF_ALBUM = '../input/album'
PATH_OF_ALBUM_ART = None  # Initializing with `None`
AUDIO_FILE_EXTENSIONS = ['.mp3', '.flac', '.m4a', '.wav', '.ogg', '.wma']
IMAGE_FILE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
CONFIG_FILE_EXTENSIONS = ['.ini', '.json', '.xml', '.yml', '.yaml', '.toml']

# Get the current working directory
current_dir = getcwd()

# Find the album art
def add_album_art(album_path):
    for file_path in scandir(album_path):
        if path.isdir(file_path):
            add_album_art(file_path)
        else:
            file_name = ntpath.basename(file_path)
            file_extension = ntpath.splitext(file_path)[1]

            if file_extension in AUDIO_FILE_EXTENSIONS:
                file_type = 'audio'
            elif file_extension in IMAGE_FILE_EXTENSIONS:
                file_type = 'image'
            elif file_extension in CONFIG_FILE_EXTENSIONS:
                file_type = 'config'
            else:
                raise Exception(f'Unknown file type: {file_path}')

            print(f'{file_name}: {file_type}')

# Run the function
add_album_art(PATH_OF_ALBUM)
