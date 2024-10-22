rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle
char = 90  # ASCII value for 'Z'

# Outer loop for each row
for i in range(rows):
    # Inner loop for each column in the current row
    for j in range(rows - i):
        # Print the character corresponding to the current ASCII value
        print(chr(char), end=" ")
    char -= 1  # Move to the previous character
    print()  # Move to the next line after each row


# Inverted Right-Angle Triangle with Alphabets in Reverse Order Starting from 'Z'

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter an integer value for rows. 
This value determines the number of rows in the triangle.

Initialize Starting Character:
char = 90 sets the starting character's ASCII value to 90, which corresponds to 'Z'.

Outer Loop for Rows:
for i in range(rows): initiates a loop that iterates from 0 up to rows - 1. Each iteration corresponds to one row in the triangle.

Inner Loop for Characters:
for j in range(rows - i): initiates a loop that iterates rows - i times for the current row. 
This loop prints characters for each column in the row.

Printing Characters:
print(chr(char), end=" ") prints the character corresponding to the current ASCII value of char. 
The chr() function converts the ASCII value to its corresponding character. 
For example, 90 corresponds to 'Z'. The end=" " ensures that characters are printed on the same line, separated by spaces.

Move to Previous Character:
char -= 1 decrements the ASCII value by 1 after each row, so the next row will print the previous character.

Line Break:
print() after the inner loop prints a newline character, moving the cursor to the next line. 
This completes the current row and prepares for the next one.
'''