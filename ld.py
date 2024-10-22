"""
A script is a python file that's intended to be run directly. When we run it, it should do something.

A module is a python file that's intended to be imported into scripts or other modules. 
It often defines members like classes, functions,and variables intended to be used in other files that import it.
"""


# ld.py
def loop_function():
    for i in range(5):
        print("This is loop iteration:", i)

'''
Breakdown:
Function Definition: def loop_function(): defines a function named loop_function.
Loop Inside Function: The for loop is now inside this function. It will only execute when the function is called.
'''