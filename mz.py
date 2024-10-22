"""
Common Modules in scipy:

scipy.optimize: Optimization algorithms and root-finding functions.
scipy.integrate: Integration and differential equation solvers.
scipy.interpolate: Interpolation techniques.
scipy.linalg: Linear algebra functions.
scipy.stats: Statistical functions and probability distributions.
scipy.signal: Signal processing tools.
"""

# Integration

from scipy.integrate import quad

# Function to integrate
def integrand(x):
    return x**2

# Integrate the function from 0 to 1
integral, error = quad(integrand, 0, 1)
print("Integral result:", integral)