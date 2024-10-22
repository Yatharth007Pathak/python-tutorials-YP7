rows = int(input("Enter the number of rows: "))  # Number of rows for the triangle

# Outer loop for each row
for i in range(1, rows + 1):
    # Print leading spaces for alignment
    for space in range(rows - i):
        print(" ", end=" ")
    # Print numbers increasing from 1 to the current row number
    for j in range(1, i + 1):
        print(j, end=" ")
    # Print numbers decreasing from the previous row number
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()  # Move to the next line after each row

# Pyramid Pattern with Numbers Increasing to Maximum and Then Decreasing

'''
Code Explanation:

Input Collection:
rows = int(input("Enter the number of rows: ")) prompts the user to input the number of rows for the triangle.

Outer Loop for Rows:
for i in range(1, rows + 1): iterates from 1 up to rows. This loop controls the number of rows and the content of each row.

Print Leading Spaces:
for space in range(rows - i): prints leading spaces for alignment to create a pyramid-like structure. 
The number of spaces decreases as the row number increases.
print(" ", end=" ") prints a space without moving to a new line.

Print Increasing Numbers:
for j in range(1, i + 1): prints numbers starting from 1 up to the current row number i.
print(j, end=" ") prints each number followed by a space.

Print Decreasing Numbers:
for j in range(i - 1, 0, -1): prints numbers in decreasing order starting from i - 1 down to 1.
print(j, end=" ") prints each number followed by a space.

Line Break:
print() after the inner loops moves to the next line after completing the current row.
'''