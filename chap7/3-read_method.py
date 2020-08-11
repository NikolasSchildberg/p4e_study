def char_count(fhand):
	"""Given a file handle, this function counts the number
	of characters in the file"""
	char_counter = 0
	for line in fhand:
		for char in line:
			char_counter += 1
	return char_counter

# opening the file with a file handle
fhand = open("test1.txt")

# using the read method on the file handle
file_str = fhand.read() # using it empties the fhandle

# If it's not too big, print it out
filesize = char_count(file_str)
if (filesize > 200):
	print("That file is big!\n")
else:
	print("That's your file:\n")
	print(file_str)