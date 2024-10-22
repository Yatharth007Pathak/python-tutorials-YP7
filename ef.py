# Sorting a list

numbers = [4, 2, 9, 1, 5, 6]                                      # List of integrs
fruits = ["apple", "banana", "cherry", "date"]                    # List of strings
students = [("Alice", 25), ("Bob", 22), ("Charlie", 23)]          # List of tuples

# Reverse method
# reverse() method reverse the elements of the list in place.
numbers.reverse()
print(numbers) # Output: [6, 5, 1, 9, 2, 4]


# Using sort() Method
# The sort() method sorts the list in place, meaning it modifies the original list and doesn't return a new list. By default, it sorts the list in ascending order.
numbers.sort()
print(numbers)  # Output: [1, 2, 4, 5, 6, 9]


# We can also sort the list in descending order by passing the reverse=True argument.
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 6, 5, 4, 2, 1]


# Using sorted() Function
# The sorted() function returns a new sorted list without changing the original list.
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 4, 5, 6, 9]
print(numbers)         # Output: [9, 6, 5, 4, 2, 1] (original list remains unchanged)


# We can also sort in descending order using the reverse=True argument.
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Output: [9, 6, 5, 4, 2, 1]


# Sorting Lists with Custom Keys
# If you want to sort a list based on a custom criterion, we can use the key parameter with a function
fruits.sort(key=len)
print(fruits)  # Output: ['date', 'apple', 'banana', 'cherry']


# Reverse Sorting
# We can sort in reverse order by using the reverse=True parameter with both sort() and sorted()
fruits.sort(key=len, reverse=True)
print(fruits)  # Output: ['banana', 'cherry', 'apple', 'date']


# Sorting a list in reversed alphanumeric order by passing the reverse=True argument.
fruits.sort(reverse=True)
print(fruits) # Output: ['date', 'cherry', 'banana', 'apple']


# Using the sorted() function with a custom key:
sorted_fruits = sorted(fruits, key=len)
print(sorted_fruits)  # Output: ['date', 'apple', 'cherry', 'banana']


# Sorting a list in alphanumeric order.
fruits.sort()
print(fruits) # Output: ["apple", "banana", "cherry", "date"]


# Sorting a list of strings by the last character using Lambda Functions
# Lambda functions are anonymous functions that can be used to create quick, one-off functions to be passed to the key parameter. This is useful for inline custom sorting.
fruits.sort(key=lambda x: x[-1])
print(fruits)  # Output: ['banana', 'apple', 'date', 'cherry']


# Sorting a list of tuples based on the second element
# We can define a custom function to determine the sort order by using the key parameter. The function should take one argument and return a value that will be used for sorting.
students.sort(key=lambda x: x[1])
print(students)  # Output: [('Bob', 22), ('Charlie', 23), ('Alice', 25)]