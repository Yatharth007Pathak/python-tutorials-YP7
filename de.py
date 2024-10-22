rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle

# Outer loop for each row
for i in range(rows, 0, -1):
    # Print characters in reverse order for the current row
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()  # Move to the next line after each row

# Inverted Right-Angle Triangle with Characters in Reverse Order by Row

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter an integer value for rows. 
This value determines the number of rows in the triangle.

Outer Loop for Rows:
for i in range(rows, 0, -1): initiates a loop that iterates from rows down to 1. Each iteration corresponds to one row in the triangle.

Inner Loop for Characters:
for j in range(i): initiates a loop that iterates i times for the current row. This loop prints characters for each column in the row.

Printing Characters:
print(chr(65 + j), end=" ") prints the character corresponding to 65 + j. 
The chr() function converts the ASCII value to its corresponding character, starting with 65, which corresponds to 'A'. 
The end=" " ensures that characters are printed on the same line, separated by spaces.

Line Break:
print() after the inner loop prints a newline character, moving the cursor to the next line. 
This completes the current row and prepares for the next one.
'''