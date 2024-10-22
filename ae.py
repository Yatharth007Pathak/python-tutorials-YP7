if True:
    print("This is inside the if block")  # This will be executed because the condition is True
    if True:
        print("This is inside the nested if block")  # This will be executed because the condition is True
    print("This is still inside the first if block")  # This will be executed because it's inside the first if block
    if False:     
        print("This is inside the nested if block")  # This will not be executed because the condition is False
print("This is outside the if block")  # This will be executed because it's outside any if block


'''
Indentation in programming refers to the use of whitespace (spaces or tabs) at the beginning of a line to indicate a block of code. 
It is particularly important in languages like Python, where it is used to define the structure and nesting of the code. 
Indentation improves the readability of the code by visually representing the hierarchical structure of the program.

Importance of Indentation
Code Structure: Indentation helps in visually representing the hierarchy and structure of the code. 
It shows which code statements belong to which blocks or scopes.
Readability: Properly indented code is easier to read and understand. 
It helps other developers (and yourself) to quickly grasp the logic and flow of the program.
Syntax Requirement: In some languages, like Python, indentation is not just for readability but is a part of the syntax. 
Improper indentation can lead to syntax errors.

Python: Uses indentation to define blocks of code. There are no braces or keywords to indicate blocks; the level of indentation is crucial.
C/C++/Java: Uses braces {} to define blocks, but indentation is still used for readability
HTML/CSS/JavaScript: Uses indentation to improve readability, although it is not required by the syntax.
'''