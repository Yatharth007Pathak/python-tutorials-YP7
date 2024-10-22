# If we open a file in append mode, the new data will be added to the end of the file:

# Open the file in append mode
file = open("text4.txt", "a")

# Append text to the file
file.write("This line is appended.\n")

# Close the file
file.close()