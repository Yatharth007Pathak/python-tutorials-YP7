# Matrix operations:

import sympy as sp

# Define symbolic matrices
A = sp.Matrix([[1, 2], [3, 4]])
B = sp.Matrix([[5, 6], [7, 8]])

# Matrix addition
matrix_sum = A + B
print("Matrix Sum:\n", matrix_sum)

# Matrix multiplication
matrix_product = A * B
print("Matrix Product:\n", matrix_product)

# Inverse of a matrix
inverse_matrix = A.inv()
print("Inverse Matrix:\n", inverse_matrix)