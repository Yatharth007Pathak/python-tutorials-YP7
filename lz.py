"""
Commonly Used Functions in numpy library:
np.array(): Creates a numpy array.
np.zeros(), np.ones(): Creates arrays filled with zeros or ones.
np.arange(), np.linspace(): Generates arrays of evenly spaced values.
np.reshape(): Reshapes an array without changing its data.
np.dot(): Performs dot product between two arrays.
np.sum(), np.mean(), np.median(), np.std(): Computes sum, mean, median, and standard deviation.
"""

import numpy as np

# Creating a numpy array
arr = np.array([1, 2, 3, 4, 5])

# Performing element-wise addition
arr_add = arr + 10

# Mathematical operations
arr_sin = np.sin(arr)

# Array operations
arr_sum = np.sum(arr)
arr_mean = np.mean(arr)

# Printing results
print("arr_add =", arr_add)
print("arr_sin =", arr_sin)
print("arr_sum =", arr_sum)
print("arr_mean =", arr_mean)