rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle

# Outer loop for each row
for i in range(1, rows + 1):
    # Print spaces to center align the pyramid
    for space in range(rows - i):
        print(" ", end=" ")

    # Print numbers in increasing order
    for j in range(1, i + 1):
        print(j, end=" ")

    print()  # Move to the next line after each row


# Right Angle Triangle with Pyramid Numbers

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter an integer value for rows. 
This value determines the number of rows in the pyramid.

Outer Loop for Rows:
for i in range(1, rows + 1): initiates a loop that iterates from 1 to rows (inclusive). Each iteration corresponds to one row in the pyramid.

Spaces for Center Alignment:
for space in range(rows - i): initiates a loop that prints spaces to center-align the pyramid. The number of spaces decreases as i increases.
print(" ", end=" ") prints a space without moving to the next line. This ensures proper alignment of the pyramid shape.

Numbers in Increasing Order:
for j in range(1, i + 1): initiates a loop that prints numbers starting from 1 up to i. This loop prints the numbers for the current row.
print(j, end=" ") prints the current value of j followed by a space, without moving to a new line. 
This ensures that numbers in the same row are printed on the same line.

Line Break:
print() after the inner loops prints a newline character, moving the cursor to the next line. 
This completes the current row and prepares for the next one.
'''