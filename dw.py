size = int(input("Enter the size of square: "))  # Size of the square
char = 65  # ASCII value for 'A'

# Outer loop for each row
for i in range(size):
    # Inner loop for each column
    for j in range(size):
        # Print consecutive alphabets
        print(chr(char + (i * size + j) % 26), end=" ")
    print()  # Move to the next line after each row

# Square Pattern with Consecutive Alphabets

'''
Code Explanation

Input Collection:
size = int(input("Enter the size of square: ")) takes the size of the square grid from the user.

Initialization:
char = 65 initializes the starting ASCII value for 'A'.

Outer Loop for Rows:
for i in range(size): iterates over each row of the grid.

Inner Loop for Columns:
for j in range(size): iterates over each column within the current row.

Print Consecutive Alphabets:
print(chr(char + (i * size + j) % 26), end=" ") prints consecutive alphabets:
(i * size + j) calculates the current position in a continuous sequence of characters.
% 26 ensures the sequence wraps around after 'Z', starting again at 'A'.

Line Break:
print() moves to the next line after completing each row.
'''