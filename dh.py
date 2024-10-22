rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle
char = 90  # ASCII value for 'Z'

# Outer loop for each row
for i in range(rows):
    # Inner loop for each column in the current row
    for j in range(rows - i):
        # Print the character corresponding to the current ASCII value
        print(chr(char - j), end=" ")
    print()  # Move to the next line after each row

# Inverted Right-Angle Triangle with Characters Starting from 'Z'

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter the number of rows for the triangle.

Starting Character:
char = 90 initializes the ASCII value for 'Z'. The chr() function will convert this value to its corresponding character ('Z').

Outer Loop for Rows:
for i in range(rows): iterates from 0 up to rows - 1, creating each row of the triangle.

Print Characters in Reverse Order:
for j in range(rows - i): iterates from 0 up to rows - i - 1, printing characters for each column in the current row.
print(chr(char - j), end=" ") prints characters in decreasing order starting from char. 
The chr() function converts the adjusted ASCII value back to a character. 
For example, char - j will start at the ASCII value of 'Z' and decrease with each subsequent column in the row.

Line Break:
print() after the inner loop prints a newline character to move to the next line after completing the current row.
'''