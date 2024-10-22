rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle

# Outer loop for each row
for i in range(rows, 0, -1):
    # Print characters in decreasing order for the current row
    for j in range(i):
        # Print the character starting from 'A'
        print(chr(65 + (rows - i + j)), end=" ")
    print()  # Move to the next line after each row

# Inverted Right-Angle Triangle with Alphabets Decreasing Each Row

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to input the number of rows for the triangle.

Outer Loop for Rows:
for i in range(rows, 0, -1): iterates from rows down to 1. This loop controls the number of rows and how many characters are printed in each row.

Print Characters in Decreasing Order:
for j in range(i): iterates i times for each row, printing characters in each column of the row.
print(chr(65 + (rows - i + j)), end=" ") prints characters starting from 'A' with an adjustment based on the current row and column index. 
The expression 65 + (rows - i + j) calculates the ASCII value for the character to be printed. Here:
65 is the ASCII value for 'A'.
rows - i + j adjusts the starting point for each row and column.

Line Break:
print() after the inner loop moves to the next line after completing the current row.
'''