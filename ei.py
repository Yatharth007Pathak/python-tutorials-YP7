# List Methods

fruits = ["apple", "banana"]


# extend(): Extend the list by appending all the items from the iterable.
more_fruits = ["cherry", "orange"]
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# index(): Return the index of the first element with the specified value.
index = fruits.index("banana")
print(index)  # Output: 1

# count(): Return the number of times the specified element appears in the list.
count = fruits.count("apple")
print(count)  # Output: 1

# pop(): Remove and return the element at the specified position (default is the last element).
last_fruit = fruits.pop()
print(last_fruit)  # Output: 'orange'
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# clear(): Remove all items from the list.
fruits.clear()
print(fruits)  # Output: []

# copy(): Return a shallow copy of the list.
fruits = ["apple", "banana", "cherry"]
new_fruits = fruits.copy()
print(new_fruits)  # Output: ['apple', 'banana', 'cherry']