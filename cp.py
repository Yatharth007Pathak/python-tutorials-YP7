rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle

# Outer loop for each row
for i in range(1, rows + 1):
    # Print numbers in reverse order for the current row
    for j in range(rows, rows - i, -1):
        print(j, end=" ")
    print()  # Move to the next line after each row


# Right Angle Triangle with Numbers in Reverse Order

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter an integer value for rows. 
This value determines how many rows will be printed in the triangle.

Outer Loop for Rows:
for i in range(1, rows + 1): initiates a loop that iterates from 1 to rows (inclusive). 
Each iteration corresponds to one row in the triangle.

Inner Loop for Reverse Numbers:
for j in range(rows, rows - i, -1): initiates a loop that iterates in reverse, starting from rows down to rows - i + 1. 
This loop prints numbers in reverse order for the current row.

Printing Reverse Numbers:
print(j, end=" ") prints the current value of j followed by a space, without moving to a new line. 
This ensures that numbers in the same row are printed on the same line, separated by spaces.

Line Break:
print() after the inner loop prints a newline character, moving the cursor to the next line. 
This completes the current row and prepares for the next one.
'''