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

line_count = 0

# we can use a for loop to iterate through the file,
# treating the file as a sequence of characters
for line in fhand:
	line_count += 1
	print(line_count)

message = "\nThis file is "+str(line_count)+" lines long."
print(message)