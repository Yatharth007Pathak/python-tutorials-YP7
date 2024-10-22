import keyword
print(keyword.kwlist)

# code to output the current list of reserved keywords in Python when run.

'''
import keyword: This line imports the keyword module, which is a built-in Python module. 
The keyword module provides a list of the keywords in Python.
print(keyword.kwlist): This line prints the list of Python keywords to the console.
keyword.kwlist: This is an attribute of the keyword module. It contains a list of all the Python keywords in the current version of Python.
print(): This function outputs the list of keywords to the console when called.
'''


'''
In Python, keywords are reserved words that have special meaning and cannot be used as identifiers (variable names, function names, etc.).
They are part of the Python language syntax and define the structure of Python programs. 
Keywords are case-sensitive and must be used exactly as they are.

Here's a list of Python keywords:

False: Represents the Boolean value false.
True: Represents the Boolean value true.
None: Represents the absence of a value or a null value.
and: Logical AND operator.
or: Logical OR operator.
not: Logical NOT operator.
if: Used to make a decision.
elif: Else if, used in conditional statements.
else: Used in conditional statements.
for: Used for looping over a sequence.
while: Used for looping as long as a condition is true.
break: Breaks out of the closest enclosing loop.
continue: Skips the rest of the current loop iteration and moves to the next one.
return: Exits a function and returns a value.
def: Used to define a function.
class: Used to define a class.
try: Wraps code in a block that will catch exceptions.
in: Checks if a value exists within an iterable.
is: Tests for object identity (i.e., whether two references point to the same object).
raise: Triggers an exception manually.
del: Deletes objects, such as variables or list elements.
pass: Acts as a placeholder for future code; does nothing.
except: Catches exceptions raised in a try block.
assert: Used for debugging; tests if a condition is true, and triggers an error if not.
async: Declares an asynchronous function or coroutine.
await: Waits for the completion of an asynchronous operation.
finally: Ensures that a block of code runs no matter what (often used with try and except).
import: Used to import modules.
from: Used with import to specify which part of a module to import.
as: Used to create an alias while importing a module.
with: Used to simplify exception handling by wrapping the execution of a block of code.
lambda: Creates an anonymous function in a single line.
yield: Returns a value from a generator function without stopping the function.
elif: Else if; extends an if statement to check additional conditions.
global: Declares a variable as global.
nonlocal: Declares a variable as non-local.
'''