"""
sympy is a Python library for symbolic mathematics. It provides tools for algebraic manipulations, calculus, equation solving, and more. 
Unlike numpy and scipy, which focus on numerical computations, sympy operates with symbolic expressions and exact arithmetic.

Key Features of sympy:
Symbolic Computation: Allows for algebraic manipulations and symbolic representation of mathematical expressions.
Calculus: Functions for differentiation, integration, limits, and series expansions.
Equation Solving: Tools for solving algebraic equations, systems of equations, and differential equations symbolically.
Simplification: Methods for simplifying expressions, expanding polynomials, and factoring.
Mathematical Functions: Includes functions for working with polynomials, matrices, and mathematical constants.
"""

# Symbolic Variables and Expressions:

import sympy as sp

# Define symbolic variables
x, y = sp.symbols('x y')

# Define a symbolic expression
expr = x**2 + 2*x + 1

# Simplify the expression
simplified_expr = sp.simplify(expr)
print("Simplified Expression:", simplified_expr)
