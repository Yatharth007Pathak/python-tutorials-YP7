# Input matrix size
rows1 = int(input("Enter number of rows for the first matrix: "))
cols1 = int(input("Enter number of columns for the first matrix: "))
rows2 = int(input("Enter number of rows for the second matrix: "))
cols2 = int(input("Enter number of columns for the second matrix: "))

# Ensure matrices can be multiplied
if cols1 != rows2:
    print("Error: Number of columns of the first matrix must be equal to the number of rows of the second matrix.")
else:
    # Input matrices
    print("Enter elements for the first matrix:")
    matrix1 = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols1)] for i in range(rows1)]
    
    print("Enter elements for the second matrix:")
    matrix2 = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols2)] for i in range(rows2)]

    # Compute product
    product = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]

    # Print matrices and their product
    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("Matrix 2:")
    for row in matrix2:
        print(row)

    print("Product of the matrices:")
    for row in product:
        print(row)


# Input two matrices and print their product

'''
 Here's a detailed breakdown:

rows1 = int(input("Enter number of rows for the first matrix: ")):
Prompts the user to input the number of rows for the first matrix.
Converts the input from a string to an integer and stores it in rows1.

cols1 = int(input("Enter number of columns for the first matrix: ")):
Prompts the user to input the number of columns for the first matrix.
Converts the input from a string to an integer and stores it in cols1.

rows2 = int(input("Enter number of rows for the second matrix: ")):
Prompts the user to input the number of rows for the second matrix.
Converts the input from a string to an integer and stores it in rows2.

cols2 = int(input("Enter number of columns for the second matrix: ")):
Prompts the user to input the number of columns for the second matrix.
Converts the input from a string to an integer and stores it in cols2.

if cols1 != rows2::
Checks if the number of columns in the first matrix (cols1) is not equal to the number of rows in the second matrix (rows2).
This condition ensures that the matrices can be multiplied. Matrix multiplication requires that the number of columns in the first matrix must be equal to the number of rows in the second matrix.

print("Error: Number of columns of the first matrix must be equal to the number of rows of the second matrix."):
Prints an error message if the matrices cannot be multiplied due to incompatible dimensions.

else::
This block executes if the matrices' dimensions are compatible for multiplication.

print("Enter elements for the first matrix:"):
Prints a message indicating that the user should enter elements for the first matrix.

matrix1 = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols1)] for i in range(rows1)]:
Uses a nested list comprehension to input elements for the first matrix.
Iterates over each row (i) and column (j), prompting the user to enter each element for the position (i+1, j+1).
Constructs a 2D list matrix1 where each inner list represents a row of the matrix.

print("Enter elements for the second matrix:"):
Prints a message indicating that the user should enter elements for the second matrix.

matrix2 = [[int(input(f"Enter element for position ({i+1}, {j+1}): ")) for j in range(cols2)] for i in range(rows2)]:
Uses a nested list comprehension to input elements for the second matrix.
Iterates over each row (i) and column (j), prompting the user to enter each element for the position (i+1, j+1).
Constructs a 2D list matrix2 where each inner list represents a row of the matrix.

product = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]:
Computes the product of the two matrices.
Uses a nested list comprehension to calculate each element of the product matrix.
For each element in the product matrix, it calculates the sum of the product of corresponding elements from matrix1 and matrix2.

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

print("Product of the matrices:"):
Prints a header to indicate that the product of the matrices will be displayed.

for row in product::
Iterates over each row in the product matrix.

print(row):
Prints each row of the product matrix.
'''