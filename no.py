# Basic symbolic arithmatic:

import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Define expressions
expr1 = x + y
expr2 = x**2 + 2*x*y + y**2

# Perform operations
sum_expr = expr1 + expr2
product_expr = expr1 * expr2

print("Sum of expressions:", sum_expr)
print("Product of expressions:", product_expr)
