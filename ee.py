# Lists can be modified by adding, removing, or changing elements.

fruits = ["apple", "orange", "cherry"]

# Adding elements to the end of list
fruits.append("grape")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']

# Inserting elements to a particular index
fruits.insert(1, "banana")
print(fruits)  # Output: ['apple', 'banana', 'orange', 'cherry', 'grape']

# Append another list to the end of current list
more_fruits = ["mango", "guava"]
fruits.extend(more_fruits)
print(fruits) # output: ['apple', 'banana', 'orange', 'cherry', 'grape', 'mango', 'guava']

# Removing the first occurrence of specified elements from a list
fruits.remove("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'grape', 'mango', 'guava']

# Removing items at given index or last item of a list
fruits.pop(2)
print(fruits) # output: ['apple', 'banana', 'grape', 'mango', 'guava']
fruits.pop()
print(fruits) # output: ['apple', 'banana', 'grape', 'mango']

# Removing specified element from list
del fruits[3]
print(fruits) # Output: ['apple', 'orange', 'grape']

# Changing an item in a list at an index
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'grape']

# Changing items in a list in a range
fruits[1:3] = ["strawberry", "papaya"]
print(fruits) # output: ['apple', 'strawberry', 'papaya']
fruits[1:3] = "apricot"
print(fruits) # output: ['apple', 'a', 'p', 'r', 'i', 'c', 'o', 't', 'mango']

# pop() method also returns element which was removed. del method doesn't return element which was removed.