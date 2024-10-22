# Input matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix elements
print("Enter elements for the first matrix:")
matrix1 = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols)] for i in range(rows)]

print("Enter elements for the second matrix:")
matrix2 = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols)] for i in range(rows)]

# Calculate the difference of the matrices
matrix_diff = [[matrix1[i][j] - matrix2[i][j] for j in range(cols)] for i in range(rows)]

# Print matrices and their difference
print("Matrix 1:")
for row in matrix1:
    print(row)

print("Matrix 2:")
for row in matrix2:
    print(row)

print("Difference of the matrices:")
for row in matrix_diff:
    print(row)

    
# Input two matrices and print their difference

'''
Here's a detailed breakdown:

rows = int(input("Enter number of rows: ")):
Prompts the user to input the number of rows for the matrices.
Converts the input from a string to an integer and stores it in the variable rows.

cols = int(input("Enter number of columns: ")):
Prompts the user to input the number of columns for the matrices.
Converts the input from a string to an integer and stores it in the variable cols.

print("Enter elements for the first matrix:"):
Prints a message indicating that the user should now input the elements for the first matrix.

matrix1 = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols)] for i in range(rows)]:
Uses a nested list comprehension to create the first matrix matrix1.
Iterates over rows (i) and columns (j) to prompt the user to input each element for the position (i+1, j+1) 
(using 1-based indexing for clarity).
Constructs a 2D list (list of lists) where each inner list represents a row of the matrix.

print("Enter elements for the second matrix:"):
Prints a message indicating that the user should now input the elements for the second matrix.

matrix2 = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols)] for i in range(rows)]:
Similar to the first matrix, this line creates the second matrix matrix2 using a nested list comprehension.
Prompts the user to enter each element for the position (i+1, j+1) and stores it in the matrix.

matrix_diff = [[matrix1[i][j] - matrix2[i][j] for j in range(cols)] for i in range(rows)]:
Calculates the difference between the two matrices.
Uses a nested list comprehension to subtract corresponding elements of matrix2 from matrix1.
Constructs a new 2D list matrix_diff where each element is the result of the subtraction matrix1[i][j] - matrix2[i][j].

print("Matrix 1:"):
Prints a header to indicate that the first matrix will be displayed.

for row in matrix1::
Iterates over each row in matrix1.

print(row):
Prints each row of matrix1.

print("Matrix 2:"):
Prints a header to indicate that the second matrix will be displayed.

for row in matrix2::
Iterates over each row in matrix2.

print(row):
Prints each row of matrix2.

print("Difference of the matrices:"):
Prints a header to indicate that the difference of the matrices will be displayed.

for row in matrix_diff::
Iterates over each row in matrix_diff.

print(row):
Prints each row of matrix_diff.
'''