rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle
char_code = 65  # ASCII value for 'A'

# Outer loop for each row
for i in range(1, rows + 1):
    # Print leading spaces for alignment
    for space in range(rows - i):
        print(" ", end=" ")
    # Print alphabets increasing from 'A' to the current row letter
    for j in range(i):
        print(chr(char_code + j), end=" ")
    # Print alphabets decreasing back to 'A'
    for j in range(i - 1, 0, -1):
        print(chr(char_code + j - 1), end=" ")
    print()  # Move to the next line after each row

# Pyramid Pattern with Alphabets Increasing to Maximum and Then Decreasing

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to input the number of rows for the triangle.

Starting Character Code:
char_code = 65 initializes the ASCII value for 'A'. The chr() function will use this value to convert it to the character 'A'.

Outer Loop for Rows:
for i in range(1, rows + 1): iterates from 1 up to rows, managing each row of the triangle.

Print Leading Spaces:
for space in range(rows - i): prints spaces to align the triangle in a centered format.
The number of spaces decreases as the row number increases.
print(" ", end=" ") prints a space without moving to a new line.

Print Increasing Alphabets:
for j in range(i): prints letters starting from 'A' up to the current row's last letter.
print(chr(char_code + j), end=" ") converts the ASCII value to the corresponding letter and prints it followed by a space.

Print Decreasing Alphabets:
for j in range(i - 1, 0, -1): prints letters in reverse order starting from one letter less than the last one in the increasing sequence.
print(chr(char_code + j - 1), end=" ") adjusts the ASCII value to print the character in reverse order.

Line Break:
print() after the inner loops moves the cursor to the next line after finishing the current row.
'''