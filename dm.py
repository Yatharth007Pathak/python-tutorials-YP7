size = int(input("Enter the size of square: "))  # Size of the square

# Outer loop for each row
for i in range(size):
    # Inner loop for each column
    for j in range(size):
        # Print numbers incrementing by row
        print(i + 1, end=" ")
    print()  # Move to the next line after each row

# Square Pattern with Incrementing Numbers in Each Row

'''
Code Explanation:

Input Collection:
size = int(input("Enter the size of square: ")) prompts the user to input the size of the square, which determines both the number of rows and columns in the grid.

Outer Loop for Rows:
for i in range(size): iterates through each row of the square grid. It runs size times, once for each row.

Inner Loop for Columns:
for j in range(size): iterates through each column of the current row. It also runs size times for each row.

Print Numbers:
print(i + 1, end=" ") prints the row number incremented by 1. 
This means that all columns in a given row will have the same number, which is the row index plus one.

Line Break:
print() after the inner loop moves the cursor to the next line after completing the current row.
'''