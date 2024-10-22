# Simplification:

import sympy as sp

# Define symbols
x = sp.symbols('x')

# Define an expression
expr = (x**2 - 1) / (x - 1)

# Simplify the expression
simplified_expr = sp.simplify(expr)
print("Simplified expression:", simplified_expr)