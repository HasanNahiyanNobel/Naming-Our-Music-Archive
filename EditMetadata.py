#
# Author: Hasan Nahiyan Nobel
# Copyright: Attribution 4.0 International (CC BY 4.0)
#
import os

import eyed3

PATH_OF_SONGS = "G:\গীতাঞ্জলি\উত্তম সঙ্গীত\_উর্ধ্বগামী\Robert Johnson Complete Temp 1"

path = PATH_OF_SONGS
for file_path in os.scandir(path):
	tag = eyed3.load(file_path).tag
	tag.remove(file_path)
