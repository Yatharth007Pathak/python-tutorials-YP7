# Since sets automatically remove duplicates, they are often used to filter out duplicate values from a list or other iterable.

# List with duplicate elements
my_list = [1, 2, 3, 4, 4, 5, 5, 6]

# Converting the list to a set to remove duplicates
unique_set = set(my_list)

print(unique_set)  # Output: {1, 2, 3, 4, 5, 6}