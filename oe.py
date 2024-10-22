"""
Python Modules is a single file (or files) that is imported under one import and used. 
It's simply a Python file (.py) containing a set of functions, classes, or variables.
Example:
math.py can be a module that contains various mathematical functions.
"""
import math
print(math.sqrt(16))


"""
Python Libraries are a collection of modules that together offer a set of functionality. 
It can include multiple modules and packages (a package is a collection of related modules). 
Libraries often provide more extensive functionality than a single module.
Example:
NumPy is a library for numerical computing, and it includes multiple modules like numpy.core, numpy.linalg, etc.
requests is a library that provides functionalities to send HTTP requests, encapsulating multiple modules inside.
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)


'''
Key Differences
Scope:
A module is a single file of Python code that can be imported.
A library is a collection of modules/packages that provide a wide range of functionalities.
Complexity:
A module is typically smaller and focused on a specific functionality.
A library is more comprehensive and may include several modules or packages.
'''