#
# Author: Hasan Nahiyan Nobel
# Copyright: Attribution 4.0 International (CC BY 4.0)
#

input_file = open("input.txt", 'r')
input_lines = input_file.readlines()
input_file.close()

start_index = 1
for line in input_lines:
	song_name = line.split('\t')[1].replace('\"', '')
	file_name = str(start_index) + ". " + song_name
	print(file_name)
	start_index += 1
