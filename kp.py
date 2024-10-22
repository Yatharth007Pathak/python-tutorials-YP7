# File input and output (I/O) in Python allows you to work with files on your computer. 

'''
Opening a File
Before we can read from or write to a file, we need to open it using the open() function. 
This function returns a file object, which provides methods and attributes to interact with the file.

syntax:
file = open("example.txt", "mode")

"example.txt" is the name of the file we want to work with.
"mode" specifies the mode in which the file should be opened. Common modes include:
"r": Read (default mode). Opens the file for reading; an error occurs if the file does not exist.
"w": Write. Opens the file for writing, creating a new file if it doesn't exist, or truncating the file if it does.
"a": Append. Opens the file for writing, but does not truncate the file; new data is written at the end.
"b": Binary mode. This can be combined with other modes (e.g., "rb" or "wb") to read or write binary files.
"x": Exclusive creation. Creates the file and opens it for writing; if the file already exists, an error occurs.
"t"	Text mode. Default mode for reading and writing text files
"r+"	Read and write. Opens the file for both reading and writing.
"w+"	Write and read. Opens the file for writing and reading, truncating the file.
"a+"	Append and read. Opens the file for appending and reading.
'''

# Writing to a file
with open('text1.txt', 'w') as file:
    file.write('Hello, world!')

# Reading from the file
with open('text1.txt', 'r') as file:
    content = file.read()
    print(content)