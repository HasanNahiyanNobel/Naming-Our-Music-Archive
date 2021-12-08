"""
Author: Hasan Nahiyan Nobel
Copyright: Attribution 4.0 International (CC BY 4.0)
"""

import glob
import os

# Constants
# TODO: Fix Algorithm.md according to this change
PATH_OF_SONGS = '../input/album'
PATH_OF_ALBUM_DATA = '../input/album_data.txt'
OUTPUT_DIR = '../output'

# Variables
title = ''
album = 'The Velvet Underground'
artist = 'The Velvet Underground'
albumartist = 'The Velvet Underground'
genre = 'Folk rock; Rock; Pop'
date = '1969'
originaldate = '1969'

# Format every .py file using yapf Google style
py_files = glob.glob('*.py')
for py_file in py_files:
    os.system('yapf ' + py_file + ' -i --style google --no-local-style')
