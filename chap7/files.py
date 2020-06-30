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
def print_lines_with(file,char):
    for line in file:
        if line.startswith(char):
            line = line.rstrip()
            print(line)

# Simple structure of search loop using continue
def print_interesting_lines(file,char):
    for line in file:
        # skips uninteresting lines
        if not line.startswith(char):
            continue
        line = line.rstrip()
        print(line)

# Using the find (string method) to search for desired lines into file
def search_with_find(file,substr):
    for line in file:
        if line.find(substr) == -1: continue
        print(line, end='')

# Asking the user to enter the file name and then opening it
def useropenfile():
    f_name = input("Please enter the name of the file you would like to open:")
    f_hand = open(f_name)
    f_content = f_hand.read()    
    return f_content

def menu():
    menumessage = "Hello! Choose from the following the option you would like to run:\n1 Search lines with substring\n2 No other options\n\nPlease enter the number of the desired option: "
    choice = input(menumessage)
    if choice == "1":
        search_with_find(useropenfile(),input("\nNow the string:\n"))
    else:
        print("\n\n\nERRROOORR!!!!! RUN, IT'S GONNA EXPLODE!!!\n\n\n")

# ============= The main block of code ============================
# =================================================================

print("\n===== Welcome! =====")
menu()