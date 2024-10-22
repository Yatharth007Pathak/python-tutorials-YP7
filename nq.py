# Expanding an expression:

import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Define an expression
expr = (x + y)**2

# Expand the expression
expanded_expr = sp.expand(expr)
print("Expanded expression:", expanded_expr)
