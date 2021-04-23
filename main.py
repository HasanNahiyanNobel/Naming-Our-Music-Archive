input_file = open("input.txt", 'r')
lines = input_file.readlines()
input_file.close()

for line in lines:
	song_name = line.split('\t')[1]
	print(song_name)
