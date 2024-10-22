# Solving a Linear system:

from scipy.linalg import solve

# Coefficients of the linear system
A = [[1, 2], [3, 4]]
b = [5, 6]

# Solving the system of equations
x = solve(A, b)
print("Solution:", x)