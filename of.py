list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

list3 = [1, 2, 3]
list4 = ['a', 'b']
zipped = zip(list3, list4)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b')]

'''
The zip() function in Python is used to combine two or more iterables (such as lists, tuples, etc.) element-wise, 
creating pairs (or tuples) of corresponding elements from each iterable. 
If the iterables are of different lengths, zip() stops when the shortest iterable is exhausted.

Syntax:
zip(iterable1, iterable2, ...)

Key Points:
Pairs elements: It pairs elements from the provided iterables based on their positions.
Stops at shortest length: If one iterable is shorter, zip() stops when the shortest one ends.
Useful for iterating in parallel: It can be used to loop through two (or more) iterables together.


'''