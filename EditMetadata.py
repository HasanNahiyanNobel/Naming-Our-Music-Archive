#
# Author: Hasan Nahiyan Nobel
# Copyright: Attribution 4.0 International (CC BY 4.0)
#
import os

from mutagen.easyid3 import EasyID3

PATH_OF_SONGS = "G:\গীতাঞ্জলি\উত্তম সঙ্গীত\_উর্ধ্বগামী\Robert Johnson Complete Temp 1"

ARTIST = "Robert Johnson"

for file_path in os.scandir(PATH_OF_SONGS):
	audio = EasyID3(file_path)
	print(audio)
