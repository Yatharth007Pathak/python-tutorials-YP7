# Substitution:

import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Define an expression
expr = x**2 + 2*x*y + y**2

# Substitute x=1 and y=2
substituted_expr = expr.subs({x: 1, y: 2})
print("Expression after substitution:", substituted_expr)