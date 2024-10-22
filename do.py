size = int(input("Enter the size of square: "))  # Size of the square

# Outer loop for each row
for i in range(size):
    # Inner loop for each column
    for j in range(size):
        # Print numbers decrementing by row
        print(size - i, end=" ")
    print()  # Move to the next line after each row

# Square Pattern with Decrementing Numbers in Each Row

'''
Code Explanation:

Input Collection:
size = int(input("Enter the size of square: ")) prompts the user to input the size of the square, 
which will determine both the number of rows and columns in the grid.

Outer Loop for Rows:
for i in range(size): iterates through each row of the square grid. It runs size times, once for each row.

Inner Loop for Columns:
for j in range(size): iterates through each column of the current row. This loop also runs size times for each row.

Print Numbers:
print(size - i, end=" ") prints the number that is calculated by subtracting the row index i from the size of the square. 
This results in each row having the same number, which decreases as you move to the next row.

Line Break:
print() after the inner loop moves the cursor to the next line after completing the current row.
'''