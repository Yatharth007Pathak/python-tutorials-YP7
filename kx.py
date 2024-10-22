'''
"a+": Append and Read
Opens the file for both appending and reading. The file pointer is at the end of the file, so new content is added at the end.
It creates a new file if it doesn’t exist.
'''

with open("text8.txt", "a+") as file:
    file.write("Appending new content.\n")
    file.seek(0)  # Move the pointer back to the start to read the content
    content = file.read()
    print(content)
