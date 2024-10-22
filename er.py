''' Since tuples in Python are immutable, we cannot directly modify, add, or remove elements from a tuple once it has been created. 
However, there are ways to effectively "modify" a tuple by creating a new tuple with the desired changes.'''


# Changing an Element in a Tuple
# To change an element in a tuple, we can convert the tuple to a list, modify the list, and then convert it back to a tuple.

# Original tuple
my_tuple = (10, 20, 30, 40)
# Convert the tuple to a list
temp_list = list(my_tuple)
# Modify the element (change 20 to 25)
temp_list[1] = 25
# Convert the list back to a tuple
my_tuple = tuple(temp_list)
print(my_tuple)  # Output: (10, 25, 30, 40)


# Adding an Element to a Tuple
# To add an element to a tuple, you can concatenate it with another tuple containing the new element.

# Original tuple
my_tuple = (10, 20, 30)
# Adding an element (40) by concatenating tuples
my_tuple = my_tuple + (40,)
print(my_tuple)  # Output: (10, 20, 30, 40)


# Removing an Element from a Tuple
# To remove an element from a tuple, you can convert the tuple to a list, remove the element, and then convert it back to a tuple.

# Original tuple
my_tuple = (10, 20, 30, 40)
# Convert the tuple to a list
temp_list = list(my_tuple)
# Remove an element (30)
temp_list.remove(30)
# Convert the list back to a tuple
my_tuple = tuple(temp_list)
print(my_tuple)  # Output: (10, 20, 40)


# Replacing a Subset of a Tuple
# If you need to replace a subset of elements in a tuple, you can do so by slicing and concatenating new elements.

# Original tuple
my_tuple = (10, 20, 30, 40, 50)
# Replace elements 20, 30, 40 with 21, 31, 41
my_tuple = my_tuple[:1] + (21, 31, 41) + my_tuple[4:]
print(my_tuple)  # Output: (10, 21, 31, 41, 50)


# Inserting an Element into a Tuple
# To insert an element into a tuple at a specific position, you can split the tuple and concatenate it with the new element.

# Original tuple
my_tuple = (10, 20, 40, 50)
# Insert an element (30) at index 2
my_tuple = my_tuple[:2] + (30,) + my_tuple[2:]
print(my_tuple)  # Output: (10, 20, 30, 40, 50)


# Concatenating Tuples
# We can combine two or more tuples into one by using the + operator.

# Original tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# Concatenating tuples
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)