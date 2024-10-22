size = int(input("Enter the size of square: "))  # Size of the square

# Outer loop for each row
for i in range(size):
    # Inner loop for each column
    for j in range(size):
        # Print numbers decrementing by column
        print(size - j, end=" ")
    print()  # Move to the next line after each row

# Square Pattern with Decrementing Numbers

'''
Code Explanation:

Input Collection:
size = int(input("Enter the size of square: ")) prompts the user to input the size of the square, 
which will determine both the number of rows and columns in the grid.

Outer Loop for Rows:
for i in range(size): iterates over each row of the square grid. This loop runs size times, once for each row.

Inner Loop for Columns:
for j in range(size): iterates over each column of the current row. This loop also runs size times for each row.

Print Numbers:
print(size - j, end=" ") prints numbers starting from size and decreasing with each column. 
size - j calculates the number to print for the current column. For each row, this starts from size and decrements as j increases.

Line Break:
print() after the inner loop moves the cursor to the next line after completing the current row.
'''