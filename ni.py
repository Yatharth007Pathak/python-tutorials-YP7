# Integrate the expression with respect to x:

import sympy as sp

# Define the variable
x = sp.Symbol('x')

# Define the expression
expr = x**2 + 3*x + 2  # Example expression

# Integrate the expression with respect to x
integral_expr = sp.integrate(expr, x)
print("Integral:", integral_expr)