# To create en executable file: pyinstaller --clean -F --specpath=build --hidden-import=mutagen.id3 clear_metadata.py

import os
from os import scandir
from mutagen.id3 import ID3, ID3NoHeaderError

current_dir = os.getcwd()
print('Removing metadata from: ' + current_dir + '\n')

for file_path in scandir(current_dir):
    print('Processing: ' + os.path.basename(file_path))
    try:
        file = ID3(file_path)
        print('ID3 found. Deleting all the metadata.')
        # print(file.pprint())  # Print the metadata
        file.delete()
    except ID3NoHeaderError:
        print('No ID3 found.')
    print()
