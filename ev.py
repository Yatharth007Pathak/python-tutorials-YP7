# python code to reverse a tuple


# Using Slicing
# Slicing with a step of -1 will reverse the tuple.

# Original tuple
numbers = (1, 2, 3, 4, 5)
# Reversing the tuple using slicing
reversed_numbers = numbers[::-1]
print("Reversed numbers:", reversed_numbers)


# Using the reversed() Function
# The reversed() function returns an iterator that reverses the tuple, and we can convert this iterator back into a tuple.

# Original tuple
my_numbers = (1, 2, 3, 4, 5)
# Reversing the tuple using the reversed() function
reversed_my_numbers = tuple(reversed(my_numbers))
print("Reversed my numbers:", reversed_my_numbers)


# Converting to a List and Reversing
# We can convert the tuple to a list, reverse the list, and then convert it back to a tuple.

# Original tuple
my_tuple = (1, 2, 3, 4, 5)
# Convert the tuple to a list
temp_list = list(my_tuple)
# Reverse the list
temp_list.reverse()
# Convert the list back to a tuple
reversed_tuple = tuple(temp_list)
print("Reversed tuple:", reversed_tuple)