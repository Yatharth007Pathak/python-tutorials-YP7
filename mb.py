# Numpy library

# Creating a 1D array:
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Creating a 1D array of zeros with 5 elements
import numpy as np
zeros_arr = np.zeros(5)
print(zeros_arr)

# Creating a 2x3 array of ones
import numpy as np
ones_arr = np.ones((2, 3))
print(ones_arr)

# Creating two arrays and adding them:
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
sum_arr = arr1 + arr2
print(sum_arr)

# Creating a 1D array and slicing the array to get elements from index 1 to 3
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
sliced_arr = arr[1:4]
print(sliced_arr)

# Creating an array and fnding maximum and minimum
import numpy as np
arr = np.array([15, 3, 9, 8, 20])
max_value = np.max(arr)
min_value = np.min(arr)
print("Max:", max_value)
print("Min:", min_value)