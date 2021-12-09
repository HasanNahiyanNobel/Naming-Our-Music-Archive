"""
Author: Hasan Nahiyan Nobel
Copyright: Attribution 4.0 International (CC BY 4.0)
"""

from os import system, path, mkdir
from shutil import move
from utilities import (
    PATH_OF_SONGS,
    OUTPUT_DIR,
    album,
    originaldate,
    format_files,
)

# Format all the files using yapf
format_files()

# Rename files
system('py rename_files.py')

# And edit metadata!
system('py edit_metadata.py')

# Copy songs to the new directory
folder_name = album + ' (' + originaldate + ')'
path_of_output = path.join(OUTPUT_DIR, folder_name)
move(PATH_OF_SONGS, path_of_output)

# Restore the directory named `album`
mkdir(PATH_OF_SONGS)
