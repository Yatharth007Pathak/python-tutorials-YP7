# Using with Statement: Using the with statement is a good practice as it automatically closes the file after the block of code is executed.

# Writing to a file using with statement
with open("text5.txt", "w") as file:
    file.write("This is a safer way to handle files.\n")

# Reading from a file using with statement
with open("text5.txt", "r") as file:
    content = file.read()
    print(content)