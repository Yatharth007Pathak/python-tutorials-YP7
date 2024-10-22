# Example of Solving a System of Equations:

import sympy as sp

# Define the variable
x = sp.Symbol('x')

# Define symbolic variables
x, y = sp.symbols('x y')

# Define equations
eq1 = sp.Eq(x + y, 5)
eq2 = sp.Eq(x - y, 1)

# Solve the system of equations
solutions = sp.solve((eq1, eq2), (x, y))
print("Solutions:", solutions)