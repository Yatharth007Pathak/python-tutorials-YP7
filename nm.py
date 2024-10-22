# Polynomial operations:

import sympy as sp

# Define the variable
x = sp.Symbol('x')

# Define a polynomial
poly = sp.Poly(x**3 - 6*x**2 + 11*x - 6, x)

# Factor the polynomial
factored_poly = sp.factor(poly)
print("Factored Polynomial:", factored_poly)
