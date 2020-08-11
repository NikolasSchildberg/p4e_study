""" Searching for string in lines"""
fhand = open("test1.txt")

#file_str = fhand.read()

compare = input("Enter the string: ")

for line in fhand:
	if line.startswith(compare):
		print(line[:len(line)-1])
		print(line,end='')