# Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix elements
matrix = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols)] for i in range(rows)]

# Compute transpose
transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

# Print matrix and its transpose
print("Matrix:")
for row in matrix:
    print(row)

print("Transpose of the matrix:")
for row in transpose:
    print(row)


# Input a matrix and print its transpose

'''
Here's a detailed breakdown:

rows = int(input("Enter number of rows: ")):
Prompts the user to input the number of rows for the matrix.
Converts the input to an integer and stores it in rows.

cols = int(input("Enter number of columns: ")):
Prompts the user to input the number of columns for the matrix.
Converts the input to an integer and stores it in cols.

matrix = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols)] for i in range(rows)]:
Uses a nested list comprehension to input the elements for the matrix.
The outer loop iterates over the rows (i), and the inner loop iterates over the columns (j).
For each position (i+1, j+1) in the matrix (using 1-based indexing for user clarity), 
the user is prompted to enter an integer, which is then added to the matrix.
Constructs a 2D list matrix where each inner list represents a row.

transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]:
Computes the transpose of the matrix.
The transpose of a matrix is obtained by swapping rows with columns.
The outer loop iterates over columns (i), and the inner loop iterates over rows (j).
For each element in the transposed matrix, matrix[j][i] is used to access elements from the original matrix 
and place them in the transposed position.

print("Matrix:"):
Prints a header to indicate that the original matrix will be displayed.

for row in matrix::
Iterates over each row in the original matrix.

print(row):
Prints each row of the original matrix.

print("Transpose of the matrix:"):
Prints a header to indicate that the transpose of the matrix will be displayed.

for row in transpose::
Iterates over each row in the transposed matrix.

print(row):
Prints each row of the transposed matrix.
'''