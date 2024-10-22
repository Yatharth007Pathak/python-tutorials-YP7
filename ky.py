'''
"x": Exclusive Creation
Opens the file for writing but only if it doesn’t already exist. If the file exists, an error occurs.
Useful for safely creating a new file without accidentally overwriting an existing one.
'''

try:
    with open("text9.txt", "x") as file:
        file.write("This file was created exclusively.\n")
except FileExistsError:
    print("File already exists!")