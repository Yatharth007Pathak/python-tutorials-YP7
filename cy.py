rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle
char = 65  # ASCII value for 'A'

# Outer loop for each row
for i in range(rows):
    # Inner loop for each column in the current row
    for j in range(i + 1):
        # Print the character corresponding to the current ASCII value
        print(chr(char), end=" ")
        char += 1  # Move to the next character
    print()  # Move to the next line after each row


# Right-Angle Triangle with Alphabets Increasing Row-wise

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter an integer value for rows. 
This value determines the number of rows in the triangle.

Initialize Starting ASCII Value:
char = 65 initializes a variable char to 65, which is the ASCII value for 'A'. This will be used to print characters starting from 'A'.

Outer Loop for Rows:
for i in range(rows): initiates a loop that iterates from 0 up to rows - 1. Each iteration corresponds to one row in the triangle.

Inner Loop for Columns:
for j in range(i + 1): initiates a loop that iterates i + 1 times for the current row. 
This loop prints characters for each column in the row.

Printing Characters:
print(chr(char), end=" ") prints the character corresponding to the current ASCII value of char, followed by a space, without moving to a new line. 
The chr() function converts the ASCII value to its corresponding character.
char += 1 increments the ASCII value by 1 to move to the next character for the subsequent print.

Line Break:
print() after the inner loop prints a newline character, moving the cursor to the next line. 
This completes the current row and prepares for the next one.
'''