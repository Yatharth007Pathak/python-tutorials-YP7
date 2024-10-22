'''
In Python, understanding the concepts of 'pass by value' and 'pass by reference' can be a bit tricky because Python doesn't strictly use either. 
Instead, Python uses a model known as "pass by object reference" or "pass by assignment." Let's break this down:

Pass by Value:
Definition: In languages that use pass by value, a copy of the variable is passed to the function. 
Changes made to the parameter inside the function do not affect the original variable.
Python Context: Python does not use pass by value in the traditional sense because variables in Python are references to objects. 
When we pass an immutable object (e.g., an integer, string, or tuple) to a function, 
the function gets a reference to the object, but since the object is immutable, it cannot be changed.

Pass by Reference:
Definition: In languages that use pass by reference, the reference (or memory address) of the variable is passed to the function.
Changes made to the parameter inside the function affect the original variable.
Python Context: Python does not use pass by reference in the traditional sense either. 
However, when we pass a mutable object (e.g., a list, dictionary, or set) to a function, 
the function can modify the contents of the object because both the original and the parameter inside the function refer to the same object.
'''

'''
Python's "Pass by Object Reference":
Mutable Objects: If you pass a mutable object like a list or a dictionary to a function, the function can modify the original object.
Here, my_list is modified because lists are mutable.
'''
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

'''
Python's "Pass by Object Reference":
Immutable Objects: If you pass an immutable object like an integer, string, or tuple to a function, 
any modification inside the function will not affect the original object.
Here, my_value remains unchanged because integers are immutable, and assigning x = 10 creates a new object rather than modifying the original one.
'''
def modify_value(x):
    x = 10

my_value = 5
modify_value(my_value)
print(my_value)  # Output: 5


'''
Immutable Objects (e.g., int, float, str, tuple): Behave like pass by value since we can't change the original object.
Mutable Objects (e.g., list, dict, set): Behave like pass by reference since we can change the contents of the object within the function.
'''