# Linear Algebra

from scipy.linalg import solve
import numpy as np

# Define a linear system Ax = b
A = np.array([[3, 2], [1, 2]])
b = np.array([5, 7])

# Solve for x
x = solve(A, b)
print("Solution to the linear system:", x)