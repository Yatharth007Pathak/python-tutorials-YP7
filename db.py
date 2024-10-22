rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle

# Outer loop for each row
for i in range(1, rows + 1):
    # Print spaces for alignment
    for space in range(rows - i):
        print(" ", end=" ")
    # Print characters starting from 'A'
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()  # Move to the next line after each row


# Right-Angle Triangle with Alphabets in Pyramid Shape

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter the number of rows for the triangle. 
This value determines the number of rows in the pattern.

Outer Loop for Rows:
for i in range(1, rows + 1): initiates a loop that iterates from 1 up to rows. Each iteration represents one row in the triangle.

Print Spaces for Alignment:
for space in range(rows - i): creates a loop to print spaces. 
The number of spaces decreases with each row, aligning the characters to form a right-angled triangle.

Print Characters:
for j in range(i): initiates a loop to print characters starting from 'A'. 
The number of characters in each row corresponds to the current row number i.
print(chr(65 + j), end=" ") prints characters starting from ASCII value 65 ('A'). 
The chr() function converts the ASCII value to its corresponding character. 
For example, when j is 0, it prints 'A'; when j is 1, it prints 'B', and so on.

Line Break:
print() after the inner loop prints a newline character, moving the cursor to the next line. 
This completes the current row and prepares for the next one.
'''