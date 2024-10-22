''' Since tuples are immutable in Python, we can't sort a tuple in place. 
However, we can create a sorted version of the tuple by converting it into a list, sorting the list, and then converting it back to a tuple.'''

# Sorting a Tuple in Ascending Order

# Original tuple
my_tuple = (3, 1, 4, 2, 5)
# Convert the tuple to a list
temp_list = list(my_tuple)
# Sort the list
temp_list.sort()
# Convert the list back to a tuple
sorted_tuple = tuple(temp_list)
print("Sorted tuple in ascending order:", sorted_tuple) # Output: Sorted tuple in ascending order: (1, 2, 3, 4, 5)


# Sorting a Tuple in Descending Order

# Original tuple
my_tuple = (3, 1, 4, 2, 5)
# Convert the tuple to a list
temp_list = list(my_tuple)
# Sort the list in descending order
temp_list.sort(reverse=True)
# Convert the list back to a tuple
sorted_tuple = tuple(temp_list)
print("Sorted tuple in descending order:", sorted_tuple) # Output: Sorted tuple in descending order: (5, 4, 3, 2, 1)


# Using the sorted() Function

# Original tuple
my_tuple = (3, 1, 4, 2, 5)
# Use sorted() to get a sorted list and then convert it to a tuple
sorted_tuple = tuple(sorted(my_tuple))
print("Sorted tuple in ascending order:", sorted_tuple) # Output: Sorted tuple in ascending order: (1, 2, 3, 4, 5)


# Example: Sorting a Tuple of Strings

# Original tuple of strings
my_tuple = ("banana", "apple", "cherry", "date")
# Sorting the tuple in alphabetical order
sorted_tuple = tuple(sorted(my_tuple))
print("Sorted tuple of strings:", sorted_tuple) # Output: Sorted tuple of strings: ('apple', 'banana', 'cherry', 'date')