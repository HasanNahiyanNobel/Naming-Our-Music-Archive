from os import system
from utilities import format_files

format_files()

# Rename files
system('py rename_files.py')
system('py edit_metadata.py')
