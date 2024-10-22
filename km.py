# Here are some basic Python code examples with different types of exceptions handled in the except block:

# Handling ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Handling ValueError
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid literal for integer conversion.")

# Handling IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Error: List index out of range.")

# Handling KeyError
try:
    my_dict = {'name': 'Alice'}
    print(my_dict['age'])
except KeyError:
    print("Error: Key not found in dictionary.")

# Handling TypeError
try:
    result = '2' + 3
except TypeError:
    print("Error: Cannot add string and integer.")

# Handling FileNotFoundError
try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")

# Handling AttributeError
try:
    my_list = [1, 2, 3]
    my_list.append(4)
    my_list.upper()  # This method doesn't exist for lists
except AttributeError:
    print("Error: List object has no attribute 'upper'.")

# Handling ImportError
try:
    import nonexistent_module # type: ignore
except ImportError:
    print("Error: Module not found.")

# Handling NameError
try:
    print(unknown_variable) # type: ignore
except NameError:
    print("Error: Variable is not defined.")

# Handling IOError
try:
    with open('file.txt', 'w') as file:
        file.write("Hello")
except IOError:
    print("Error: Input/output error occurred.")