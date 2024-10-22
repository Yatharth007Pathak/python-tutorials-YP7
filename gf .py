"""
Python's "Pass by Object Reference"
In Python, arguments are passed to functions as references to the objects (values) themselves, not the objects' actual memory locations. 
This means that whether the behavior resembles pass by value or pass by reference depends on the type of the object being passed.
"""


'''
Immutable Objects (like integers, strings, tuples):
When we pass an immutable object to a function, it behaves like pass by value because the object cannot be modified in place. 
If we try to change the value of the parameter, it creates a new object.
'''
def modify(x):
    x = x + 1
    print(x)  # Prints the new value

a = 10
modify(a)
print(a)  # Still prints 10, because integers are immutable

'''
Mutable Objects (like lists, dictionaries, sets):

When we pass a mutable object to a function, it behaves like pass by reference because the object can be modified in place. 
Any changes made to the object inside the function will be reflected outside the function as well.
'''
def modify(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify(my_list)
print(my_list)  # Prints [1, 2, 3, 4] because lists are mutable
