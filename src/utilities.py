"""
Author: Hasan Nahiyan Nobel
Copyright: Attribution 4.0 International (CC BY 4.0)
"""

import glob
import os

# Constants
PATH_OF_SONGS = '../input/album'
PATH_OF_ALBUM_DATA = '../input/album_data.txt'
OUTPUT_DIR = '../output'

# Variables
album = ''
artist = ''
albumartist = ''
genre = ''
date = ''
originaldate = ''


# Format every .py file using yapf Google style
def format_files():
    py_files = glob.glob('*.py')
    for py_file in py_files:
        os.system('yapf ' + py_file + ' -i --style google --no-local-style')
