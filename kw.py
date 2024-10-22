'''
w+": Write and Read
Opens the file for both writing and reading. It creates a new file if it doesn't exist or truncates the file (clears the content) if it does.
The file pointer is at the beginning of the file.
'''

with open("text7.txt", "w+") as file:
    file.write("This overwrites the file.\n")
    file.seek(0)  # Move the pointer back to the start to read the content
    content = file.read()
    print(content)
