"""Try and except for receiving input"""

#input
file_name = input("Enter with file name: ")

# opening file
try:
	fhand = open(file_name)
except:
	print("File",file_name,"cannot be opened.")
	quit()
#counting the lines
counter =0
for i in fhand:
	counter += 1

# output
message = "There are "+str(counter)+" lines in "+file_name
print(message)