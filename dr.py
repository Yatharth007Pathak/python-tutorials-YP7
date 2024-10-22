size = int(input("Enter the size of square: "))  # Size of the square
number = int(input("Enter the number: "))  # Number to fill the square

# Outer loop for each row
for i in range(size):
    # Inner loop for each column
    for j in range(size):
        # Print the same number in all cells
        print(number, end=" ")
    print()  # Move to the next line after each row

# Square Pattern with Same Number in All Cells

'''
Code Explanation:

Input Collection:
size = int(input("Enter the size of square: ")) prompts the user to input the size of the square. 
This will determine both the number of rows and columns in the grid.
number = int(input("Enter the number: ")) prompts the user to input the number to fill the square grid.

Outer Loop for Rows:
for i in range(size): iterates through each row of the square grid. This loop runs size times, once for each row.

Inner Loop for Columns:
for j in range(size): iterates through each column within the current row. This loop also runs size times for each row.

Print the Same Number:
print(number, end=" ") prints the value of number followed by a space.

Line Break:
print() after the inner loop moves the cursor to the next line after completing the current row.
'''