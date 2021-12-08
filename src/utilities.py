"""
Author: Hasan Nahiyan Nobel
Copyright: Attribution 4.0 International (CC BY 4.0)
"""

import glob
import os

# Directory of the songs
PATH_OF_SONGS = '../io/album'


# Format every .py file using yapf Google style
def format_files():
    py_files = glob.glob('*.py')
    for py_file in py_files:
        os.system('yapf ' + py_file + ' -i --style google --no-local-style')


format_files()
