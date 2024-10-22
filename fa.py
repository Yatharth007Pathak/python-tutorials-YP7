'''
In Python, sets themselves cannot be nested directly because sets are mutable and therefore cannot contain other sets. 
However, we can achieve something similar using a frozenset, which is an immutable version of a set, allowing it to be stored inside another set.
'''

# Create individual sets
set1 = frozenset({1, 2, 3})
set2 = frozenset({4, 5, 6})
set3 = frozenset({7, 8, 9})
# Create a nested set
nested_set = {set1, set2, set3}
# Print the nested set
print(nested_set)
# Output: {frozenset({1, 2, 3}), frozenset({4, 5, 6}), frozenset({8, 9, 7})}

'''
frozenset is used to make the sets immutable, allowing them to be added to another set.
The nested_set contains three frozensets, each representing a distinct set of numbers.
'''



'''
We cannot create a set of lists in Python because lists are mutable (i.e., they can be changed after creation). 
Since sets in Python require all their elements to be immutable (hashable), lists cannot be used as elements of a set.
However, we can achieve a similar outcome by using frozenset or tuple, both of which are immutable and can be used as elements within a set.
'''

# Using frozenset: If the elements in the list are themselves immutable, we can convert the list into a frozenset:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Convert lists to frozensets
set_of_frozensets = {frozenset(list1), frozenset(list2)}
print(set_of_frozensets)
# Output: {frozenset({1, 2, 3}), frozenset({4, 5, 6})}


# Using tuple: Alternatively, we can convert the lists into tuples:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Convert lists to tuples
set_of_tuples = {tuple(list1), tuple(list2)}
print(set_of_tuples)
# Outcome: {(1, 2, 3), (4, 5, 6)}

'''
frozenset and tuple are immutable, making them hashable and suitable as elements within a set.
This approach allows you to store collections of elements that were originally in lists, but now safely within a set.
'''