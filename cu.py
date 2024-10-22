rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle

# Outer loop for each row
for i in range(rows, 0, -1):
    # Print spaces to align the pyramid
    for space in range(rows - i):
        print(" ", end=" ")

    # Print numbers in decreasing order
    for j in range(1, i + 1):
        print(j, end=" ")

    print()  # Move to the next line after each row


# Inverted Pyramid shape with Numbers

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to enter an integer value for rows. 
This value determines the number of rows for the triangle.

Outer Loop for Rows:
for i in range(rows, 0, -1): initiates a loop that iterates from rows down to 1. Each iteration corresponds to one row in the triangle.

Spaces for Alignment:
for space in range(rows - i): prints spaces to center-align the numbers in the pyramid. 
The number of spaces decreases as the row number i decreases.
print(" ", end=" ") prints a space without moving to a new line, ensuring proper alignment of the pyramid.

Numbers in Increasing Order:
for j in range(1, i + 1): initiates a loop that prints numbers starting from 1 up to i for the current row.
print(j, end=" ") prints the current value of j followed by a space, ensuring that numbers in the same row are printed on the same line.

Line Break:
print() after the inner loops prints a newline character, moving the cursor to the next line. 
This completes the current row and prepares for the next one.
'''