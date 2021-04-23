#
# Author: Hasan Nahiyan Nobel
# Copyright: Attribution 4.0 International (CC BY 4.0)
#
import os

import eyed3

PATH_OF_SONGS = "G:\গীতাঞ্জলি\উত্তম সঙ্গীত\_উর্ধ্বগামী\Robert Johnson Complete Temp 1"
PATH_OF_LOG = "Metadata Log.csv"
CSV_DELIMITER = ','

open(PATH_OF_LOG, 'w').close() # Clear the file
log_of_metadata = open(PATH_OF_LOG, 'a') # Open it again, in append mode
log_of_metadata.write("Title" + CSV_DELIMITER
                      + "Artist" + CSV_DELIMITER
                      + "Album Artist" + CSV_DELIMITER
                      + "Album" + CSV_DELIMITER
                      + "#"
                      + '\n')

path = PATH_OF_SONGS
for file_path in os.scandir(path):
	file = eyed3.load(file_path)

	metadata = [str(file.tag.title).replace("None", ''),
	            str(file.tag.artist).replace("None", ''),
	            str(file.tag.album_artist).replace("None", ''),
	            str(file.tag.album).replace("None", ''),
	            str(file.tag.track_num)]

	while len(metadata) > 1:
		log_of_metadata.write(metadata.pop(0) + CSV_DELIMITER)

	log_of_metadata.write(metadata.pop() + '\n')
