"""
The numpy library in Python is a powerful library for numerical computing. It provides support for large, multi-dimensional arrays and matrices, 
along with a collection of mathematical functions to operate on these arrays efficiently.

Key Features of numpy:
Arrays: numpy introduces the ndarray object, which is a fast, flexible container for large data sets in Python. 
Unlike lists, numpy arrays are homogeneous, meaning all elements must be of the same data type.
Mathematical Functions: numpy provides a wide variety of mathematical functions such as trigonometric, statistical, 
and algebraic functions that can be applied element-wise to arrays.
Vectorization: Operations on numpy arrays are vectorized, meaning that you can perform element-wise operations without writing explicit loops. 
This is more efficient than using Python loops.
Broadcasting: numpy allows operations on arrays of different shapes by automatically expanding 
the smaller array to match the larger one, a process known as broadcasting.
Integration with other libraries: numpy is the foundation for many other scientific computing libraries in Python, 
such as pandas, scipy, and scikit-learn.
"""

import numpy as np

# Creating a 2D array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Performing an element-wise operation
array_sum = array + 10

print("Original Array:\n", array)
print("Array after adding 10:\n", array_sum)
