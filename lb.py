# Reading a File into a List: We can read all lines of a file into a list using the readlines() method.

# Reading a file into a list
with open('text12.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
