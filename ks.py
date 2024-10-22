# Writing to a File: To write data to a file, open it in write ("w") mode.

# Open the file in write mode
file = open("text3.txt", "w")

# Write some text to the file
file.write("Hello, World!\n")
file.write("This is another line.\n")

# Close the file
file.close()
