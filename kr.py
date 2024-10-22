# Reading Line by Line: To read a file line by line, we can use a loop with the readline() method.

# Open the file in read mode
file = open("text2.txt", "r")

# Read line by line
for line in file:
    print(line.strip())  # strip() removes the newline character

# Close the file
file.close()