rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop for each column in the current row
    for j in range(i):
        # Print characters starting from 'A'
        print(chr(65 + j), end=" ")
    print()  # Move to the next line after each row


# Right-Angle Triangle with Alphabets Increasing Each Row

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter an integer value for rows. 
This value determines the number of rows in the triangle.

Outer Loop for Rows:
for i in range(1, rows + 1): initiates a loop that iterates from 1 up to rows. Each iteration corresponds to one row in the triangle.

Inner Loop for Characters:
for j in range(i): initiates a loop that iterates i times for the current row. This loop prints characters for each column in the row.

Printing Characters:
print(chr(65 + j), end=" ") prints the character corresponding to 65 + j. 
The chr() function converts the ASCII value to its corresponding character. For example, 65 corresponds to 'A', 66 to 'B', and so on. 
The end=" " ensures that the characters are printed on the same line, separated by spaces.

Line Break:
print() after the inner loop prints a newline character, moving the cursor to the next line. 
This completes the current row and prepares for the next one.
'''