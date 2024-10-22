rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle

# Outer loop for each row
for i in range(1, rows + 1):
    # Print the same character for each column in the current row
    for j in range(i):
        print(chr(64 + i), end=" ")
    print()  # Move to the next line after each row


# Right-Angle Triangle with Alphabets Repeating Each Row

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter an integer value for rows. 
This value determines the number of rows in the triangle.

Outer Loop for Rows:
for i in range(1, rows + 1): initiates a loop that iterates from 1 up to rows. Each iteration corresponds to one row in the triangle.

Printing Characters:
for j in range(i): initiates a loop that iterates i times for the current row. This loop prints the same character for each column in the row.
print(chr(64 + i), end=" ") prints the character corresponding to 64 + i. 
The chr() function converts the ASCII value to its corresponding character. For example, if i is 1, 64 + i is 65, which corresponds to 'A'.
end=" " ensures that the characters are printed on the same line, separated by spaces.

Line Break:
print() after the inner loop prints a newline character, moving the cursor to the next line. 
This completes the current row and prepares for the next one.
'''