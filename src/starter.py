"""
Author: Hasan Nahiyan Nobel
Copyright: Attribution 4.0 International (CC BY 4.0)
"""

from os import system, path, mkdir
from utilities import (
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

# Create a new folder in output directory
folder_name = album + ' (' + originaldate + ')'
output_path = path.join(OUTPUT_DIR, folder_name)
mkdir(output_path)
