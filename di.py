rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle
char = 65  # ASCII value for 'A'

# Outer loop for each row
for i in range(rows, 0, -1):
    # Print the same character for each column in the current row
    for j in range(i):
        print(chr(char), end=" ")
    print()  # Move to the next line after each row
    char += 1  # Move to the next character for the next row

# Inverted Right-Angle Triangle with Characters Repeating Each Row

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter the number of rows for the triangle.

Starting Character:
char = 65 initializes the ASCII value for 'A'. The chr() function converts this value to its corresponding character ('A').

Outer Loop for Rows:
for i in range(rows, 0, -1): iterates from rows down to 1. 
This loop controls the number of rows in the pattern and how many characters are printed in each row.

Print Characters:
for j in range(i): iterates i times for each row, printing the same character multiple times.
print(chr(char), end=" ") prints the character corresponding to the current ASCII value of char. 
The chr() function converts the ASCII value to its character.

Line Break:
print() after the inner loop prints a newline character to move to the next row.

Move to the Next Character:
char += 1 increments the ASCII value by 1 after each row, so the next row will start with the next character in sequence.
'''