"""This is an exercise on PYthon for Everybody -
chapter 7 - Files"""

# intro message
print("Welcome to the file reader\n")

# opening the file via a file handle
fhand = open("test1.txt")

# is is different from the above one?
# fhand = open('mboxtxt','r')

# we do not want to do this
#print(fhand)

char_count = 0

# we can use a for loop to iterate through the file,
# treating the file as a sequence of characters
for line in fhand:
	for chara in line:
		char_count += 1
		#print(char_count)

message = "This file has "+str(char_count)+" characters."
print(message)