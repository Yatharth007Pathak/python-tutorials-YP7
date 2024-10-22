"""
scipy is a Python library used for scientific and technical computing. 
It builds on numpy and provides additional functionality for optimization, integration, 
interpolation, eigenvalue problems, and other advanced mathematical computations.

Key Features of scipy:
Optimization: Functions for minimizing or maximizing objective functions, including nonlinear optimization.
Integration: Functions for numerical integration (e.g., integrating functions over a range).
Interpolation: Functions for interpolating data points, including linear and spline interpolation.
Linear Algebra: Advanced linear algebra operations, such as solving linear systems, eigenvalue problems, and singular value decomposition.
Statistics: Statistical functions for probability distributions, descriptive statistics, and hypothesis tests.
Signal Processing: Functions for signal processing tasks such as filtering and Fourier transforms.
"""

# Optimization

from scipy.optimize import minimize

# Objective function to minimize
def objective(x):
    return x**2 + 2*x + 1

# Minimizing the objective function
result = minimize(objective, x0=0)
print("Optimization result:", result)