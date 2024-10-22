# given a dictionary in python, write a python program to find the sum of all items in the dictionary

# To find the sum of all items in a dictionary in Python, we can sum the values associated with each key, assuming the values are numeric.

# Sample dictionary with numeric values
dict = {"a": 10, "b": 20, "c": 30}

# Print all values in the dictionary
print(dict.values())

# Calculate the sum of all values in the dictionary
total_sum = sum(dict.values())
print("The sum of all values in the dictionary is:", total_sum)


# Sum of Values: Use sum(dict.values()) to calculate the sum of all values in the dictionary.