size = int(input("Enter the size of square: "))  # Size of the square
start_char = 'A'  # Starting character

# Outer loop for each row
for i in range(size):
    # Inner loop for each column
    for j in range(size):
        # Print incrementing alphabets
        print(chr(ord(start_char) + j), end=" ")
    print()  # Move to the next line after each row

# Square Pattern with Incrementing Alphabets

'''
Code Explanation:

Input Collection:
size = int(input("Enter the size of square: ")) prompts the user to input the size of the square. 
This will determine both the number of rows and columns in the grid.
start_char = 'A' sets the starting character for the grid.

Outer Loop for Rows:
for i in range(size): iterates through each row of the square grid. This loop runs size times, once for each row.

Inner Loop for Columns:
for j in range(size): iterates through each column within the current row. This loop also runs size times for each row.

Print Incrementing Alphabets:
print(chr(ord(start_char) + j), end=" ") prints characters starting from start_char and incrementing by the column index j.
ord(start_char) converts the starting character ('A') to its ASCII value.
chr(ord(start_char) + j) converts the incremented ASCII value back to a character.

Line Break:
print() after the inner loop moves the cursor to the next line after completing the current row.
'''