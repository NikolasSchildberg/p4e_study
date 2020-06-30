# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:19:15 2020

@author: nschildberg
"""

# opens the file: creating file handle
# fhand = open("testfile.txt")

# reading the file via read method (since size is not too large)
# stringo = fhand.read()

# The following function takes a file handle, and goes
# through it, counting and printing each line
def print_count_lines(fhandle):
    line_count = 0
    for line in fhandle:
        print(line)
        line_count += 1
    return line_count
    
# This one counts the number of characters in file
def char_count(fhandle):
    count = 0
    for line in fhandle:
        for charac in line:
            count += 1
    return count

# Simple file searcher 1: prints lines that start with character
def print_lines_with(char):
    for line in fhand:
        if line.startswith(char):
            print(line,end='')


# ============= The main block of code ============================
# =================================================================

print("\n=== Line printer ===")

fhand = open("testfile.txt")
chare = input("PLease tell me the character: ")

print_lines_with(chare)