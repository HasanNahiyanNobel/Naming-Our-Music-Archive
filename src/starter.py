"""
Author: Hasan Nahiyan Nobel
Copyright: Attribution 4.0 International (CC BY 4.0)
"""

from os import system
from utilities import format_files

# Format all the files using yapf
format_files()

# Rename files
system('py rename_files.py')

# And edit metadata!
system('py edit_metadata.py')
