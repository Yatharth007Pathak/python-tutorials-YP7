# Common Set Operations: Sets support a variety of operations that are based on mathematical set theory, such as union, intersection, difference, and symmetric difference.
 
fruits = {"apple", "orange", "cherry"}
my_set = {1, 2, 3, 4}
set1 = {1, 2, 3}
set2 = {3, 4, 5}
original_set = {1, 2, 3}


# We can add a single element to a set using the add() or update() method.
fruits.add("grape")
print(fruits)  # Output: {'apple', 'orange', 'cherry', 'grape'}

fruits_set = ["kiwi", "papaya"]
fruits.update(fruits_set)
print(fruits)  # Output: {'apple', 'orange', 'cherry', 'grape', 'kiwi', 'papaya'}


# We can remove elements from a set using the remove() or discard() methods.
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4}
my_set.discard(5)  # No error, even though 5 is not in the set
'''
remove(): Removes the specified element. Raises a KeyError if the element is not found.
discard(): Removes the specified element. Does not raise an error if the element is not found.
'''


print(set1, set2)


# The union of two sets contains all the unique elements from both sets. Use the union() method or the | operator.
union_set = set1.union(set2)  # or set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}


# The intersection of two sets contains only the elements that are present in both sets. Use the intersection() method or the & operator.
intersection_set = set1.intersection(set2)  # or set1 & set2
print(intersection_set)  # Output: {3}


# The difference between two sets contains the elements that are in the first set but not in the second set. Use the difference() method or the - operator.
difference_set1 = set1.difference(set2)  # or set1 - set2
print(difference_set1)  # Output: {1, 2}
difference_set2 = set2.difference(set1)  # or set2 - set1
print(difference_set2)  # Output: {4, 5}


# The symmetric difference contains elements that are in either of the sets but not in both. Use the symmetric_difference() method or the ^ operator.
symmetric_difference_set = set1.symmetric_difference(set2)  # or set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}


# pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
removed_element = my_set.pop()
print(removed_element)  # Output: 1 (or any other element, since it's arbitrary)


# clear(): Removes all elements from the set.
my_set.clear()
print(my_set)  # Output: set()


# copy(): Returns a shallow copy of the set.
copied_set = original_set.copy()
print(copied_set)  # Output: {1, 2, 3}