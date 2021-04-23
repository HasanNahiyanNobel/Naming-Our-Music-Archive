#
# Author: Hasan Nahiyan Nobel
# Copyright: Attribution 4.0 International (CC BY 4.0)
#
import os

from mutagen.easyid3 import EasyID3

# Directory of the songs
path_of_songs = "G:\গীতাঞ্জলি\উত্তম সঙ্গীত\_উর্ধ্বগামী\Robert Johnson Complete Temp 1"

# Data to be added
title = ""
album = ""
artist = ""
albumartist = ""
genre = ""
date = ""

# Scan the directory and edit metadata
tracknumber = 1
for file_path in os.scandir(path_of_songs):
	audio = EasyID3(file_path)

	for key in audio.keys():
		audio[key] = ""

	audio["title"] = title
	audio["album"] = album
	audio["artist"] = artist
	audio["albumartist"] = albumartist
	audio["genre"] = genre
	audio["date"] = date
	audio["tracknumber"] = str(tracknumber)

	audio.save()

	tracknumber += 1
