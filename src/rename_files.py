"""
Author: Hasan Nahiyan Nobel
Copyright: Attribution 4.0 International (CC BY 4.0)
"""
import ntpath
import os
from utilities import PATH_OF_SONGS

# Declare final variables
START_OF_RENAME_INDEX = 1
PRINT_INPUT_TO_CONSOLE = False
SPLIT_CHAR = '\"'
COL_INDEX_IN_INPUT = 1

# Read from input file
input_file = open('../io/input.txt', 'r')
input_lines = input_file.readlines()
input_file.close()

# Save song names to array
file_names = []
index = 1
for line in input_lines:
    song_name = line.split(SPLIT_CHAR)[COL_INDEX_IN_INPUT].replace('\"', '')
    file_name = str(index).zfill(2) + '. ' + song_name
    file_names.append(file_name)
    index += 1

# Print song names to console if needed
if PRINT_INPUT_TO_CONSOLE:
    for file_name in file_names:
        print(file_name)

# Path of songs to be renamed
path = PATH_OF_SONGS

# Rename the files
index = START_OF_RENAME_INDEX
for file_path in os.scandir(path):
    file_name = ntpath.basename(file_path)

    directory = ntpath.dirname(file_path)
    file_extension = file_name.rsplit(
        '.', 1
    )[1]  # Splits to the last occurrence of '.' and takes the second element (which is the file extension)

    new_file_name = file_names[index - 1]

    # Create the new file path
    new_file_path = directory + '\\' + new_file_name + '.' + file_extension

    # Rename that path
    print('Renaming: ' + file_path.path)
    try:
        os.rename(file_path.path, new_file_path)
        print('New path: ' + new_file_path + '\n')
    except OSError:
        print('Some terrible error occurred.\n')

    index += 1