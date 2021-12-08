from os import system
from utilities import format_files

# Format all the files using yapf
format_files()

# Rename files
system('py rename_files.py')

# And edit metadata!
system('py edit_metadata.py')
