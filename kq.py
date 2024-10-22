# Reading from a File: Once a file is opened in read mode, we can read its contents.

# Open the file in read mode
file = open("text2.txt", "r")

# Read the entire file content
content = file.read()
print(content)

# Close the file
file.close()