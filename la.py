# Writing Multiple Lines to a File: We can write a list of strings to a file using the writelines() method.

# Writing multiple lines to a file
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('text11.txt', 'w') as file:
    file.writelines(lines)
