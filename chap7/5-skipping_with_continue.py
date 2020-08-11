"""SKIPPING CODE FROM LOOP"""

fhand = open("test1.txt")

charo = input("Enter with the string: ")

# doesn't this loop cost a lot of unecesary operations,
# when rstripping each line, even useless ones???

for lin in fhand:
	lin = lin.rstrip()
	if not lin.startswith(charo):
		continue
	print(lin)
"""

# I'd rather d it like this
for lin in fhand:
	if lin.startswith(charo):
		print(lin,end='')
		#or
		#print(lin[;-1])
"""

print("End\n")