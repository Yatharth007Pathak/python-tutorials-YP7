# Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix elements
print("Enter elements for the first matrix:")
matrix1 = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols)] for i in range(rows)]

print("Enter elements for the second matrix:")
matrix2 = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols)] for i in range(rows)]

# Calculate the sum of the matrices
matrix_sum = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]

# Print matrices and their sum
print("Matrix 1:")
for row in matrix1:
    print(row)

print("Matrix 2:")
for row in matrix2:
    print(row)

print("Sum of the matrices:")
for row in matrix_sum:
    print(row)


# Input two matrices and print their sum

'''
Here's a detailed breakdown:

rows = int(input("Enter number of rows: ")):
Prompts the user to enter the number of rows for the matrices.
Converts the input to an integer and assigns it to the variable rows.

cols = int(input("Enter number of columns: ")):
Prompts the user to enter the number of columns for the matrices.
Converts the input to an integer and assigns it to the variable cols.

print("Enter elements for the first matrix:"):
Prints a message indicating that the user should enter the elements for the first matrix.

matrix1 = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols)] for i in range(rows)]:
This line uses a nested list comprehension to create the first matrix matrix1.
It iterates over each row (i ranging from 0 to rows-1) and each column (j ranging from 0 to cols-1), 
prompting the user to enter an integer for each position (i+1, j+1) (1-based indexing for user clarity).
The result is a 2D list (list of lists) representing the matrix.

print("Enter elements for the second matrix:"):
Prints a message indicating that the user should enter the elements for the second matrix.

matrix2 = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols)] for i in range(rows)]:
Similar to the previous matrix, this line creates the second matrix matrix2 using a nested list comprehension.
It prompts the user to enter integers for each position (i+1, j+1) and stores them in the matrix.

matrix_sum = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]:
This line calculates the sum of the two matrices.
It iterates over each row (i) and each column (j), adding the corresponding elements from matrix1 and matrix2.
The result is a new 2D list matrix_sum where each element is the sum of the corresponding elements from matrix1 and matrix2.

print("Matrix 1:"):
Prints a header indicating that the first matrix will be displayed.

for row in matrix1::
Iterates over each row in matrix1.

print(row):
Prints the current row of matrix1.

print("Matrix 2:"):
Prints a header indicating that the second matrix will be displayed.

for row in matrix2::
Iterates over each row in matrix2.

print(row):
Prints the current row of matrix2.

print("Sum of the matrices:"):
Prints a header indicating that the sum of the matrices will be displayed.

for row in matrix_sum::
Iterates over each row in matrix_sum.

print(row):
Prints the current row of matrix_sum.
'''