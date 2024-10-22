# Limit and Series Expansion:

import sympy as sp

# Define the variable
x = sp.Symbol('x')

# Calculate the limit of an expression as x approaches 0
limit_expr = sp.limit(1/x, x, 0, dir='+')
print("Limit:", limit_expr)

# Series expansion of an expression around x=0
series_expansion = sp.series(sp.sin(x), x, 0, 10)
print("Series Expansion:", series_expansion)