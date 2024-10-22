# Solving equations:

import sympy as sp

# Define the variable
x = sp.Symbol('x')

# Define an equation
equation = sp.Eq(x**2 - 4, 0)

# Solve the equation for x
solutions = sp.solve(equation, x)
print("Solutions:", solutions)