# Optimization: Minimizing a Function:

from scipy.optimize import minimize

# Define a function to minimize
def objective_function(x):
    return (x - 3) ** 2

# Perform the minimization
result = minimize(objective_function, x0=0)
print("Minimum value:", result.fun)
print("Optimal x:", result.x)