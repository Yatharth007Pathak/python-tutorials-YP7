# Number of rows
num_rows = int(input("Enter hte number of rows: "))

# Initialize the first row of Pascal's Triangle
previous_row = [1]

for i in range(num_rows):
    # Create a new row for Pascal's Triangle
    current_row = [1] * (i + 1)
    
    # Calculate the values of the current row
    for j in range(1, i):
        current_row[j] = previous_row[j - 1] + previous_row[j]
    
    # Print the row in a pyramid format
    print(' ' * (num_rows - i - 1), end='')
    for num in current_row:
        print(num, end=' ')
    print()
    
    # Update previous_row for the next iteration
    previous_row = current_row

# Python code snippet to generate a pyramid pattern of Pascal's Triangle

'''
This code generates and prints Pascal's Triangle, formatted in a pyramid shape. Here's a breakdown of how it works:

Input Collection:
num_rows = int(input("Enter the number of rows: ")) asks the user for the number of rows in Pascal's Triangle.

Initialize the First Row:
previous_row = [1] starts Pascal's Triangle with the first row.

Generating Pascal's Triangle:
for i in range(num_rows): iterates through each row from 0 to num_rows - 1.

Creating the Current Row:
current_row = [1] * (i + 1) initializes the current row with 1s. 
The length of the row is i + 1 because each row i in Pascal's Triangle has i + 1 elements.

Calculating Values:
for j in range(1, i): iterates through the elements of the row, excluding the first and last positions.
current_row[j] = previous_row[j - 1] + previous_row[j] calculates each element based on the values from the previous row.

Printing the Current Row:
print(' ' * (num_rows - i - 1), end='') adds spaces to center-align the row. The number of spaces decreases as the row index increases.
for num in current_row: prints each number in the current row.
print(num, end=' ') prints each number with a space between them.

Update Previous Row:
previous_row = current_row updates previous_row to be used for the next row in the following iteration.
'''