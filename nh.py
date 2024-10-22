# Differentiate the expression with respect to x:

import sympy as sp

# Define the variable
x = sp.Symbol('x')

# Define the expression
expr = x**2 + 3*x + 2  # Example expression

# Differentiate the expression with respect to x
diff_expr = sp.diff(expr, x)
print("Derivative:", diff_expr)