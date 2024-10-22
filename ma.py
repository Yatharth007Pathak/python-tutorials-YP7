import numpy as np

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Perform element-wise operations
squared_array = array ** 2  # Square each element
sum_array = np.sum(array)   # Calculate the sum of the elements

# Basic statistics
mean_value = np.mean(array)   # Calculate the mean of the array
max_value = np.max(array)     # Find the maximum value in the array

# Print results
print("Original Array:", array)
print("Squared Array:", squared_array)
print("Sum of Array Elements:", sum_array)
print("Mean of Array Elements:", mean_value)
print("Maximum Value in Array:", max_value)
