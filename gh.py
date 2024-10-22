'''
Key Takeaways:

Immutable Objects (e.g., int, float, str, tuple):
Behave like they are passed by value because changes to the parameter inside the function do not affect the original object.

Mutable Objects (e.g., list, dict, set):
Behave like they are passed by reference because changes to the parameter inside the function affect the original object.

Python's Mechanism:
Python uses "pass by object reference." The function receives a reference to the object, 
but whether it can modify the original object depends on whether the object is mutable or immutable.
'''

# Immutable example
def modify_string(s):
    s = s + " world"
    print(s)  # Output: "hello world"

my_str = "hello"
modify_string(my_str)
print(my_str)  # Output: "hello"



# Mutable example
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]