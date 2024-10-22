# given a dictionary in python, write a python program to find sum of All Key-Value Products in the dictionary

# Sample dictionary with numeric keys and values
my_dict = {1: 10, 2: 20, 3: 30}

# Print all key-value pairs in the dictionary
print(my_dict.items())

# Calculate the sum of all key-value products
total_sum = sum(key * value for key, value in my_dict.items())

print("The sum of all key-value products in the dictionary is:", total_sum)


# Sum of Key-Value Products: Use sum(key * value for key, value in my_dict.items()) to calculate the sum of the products of keys and values.