"""
Python supports various data types, each suited for different kinds of operations. Here's an overview of the most common data types:
"""

''' Numeric Types
Integers (int): Whole numbers, positive or negative.
Floating Point Numbers (float): Numbers with decimal points.
Complex Numbers (complex): Numbers with a real and imaginary part. '''
age = 25
pi = 3.14159
complex_number = 2 + 3j
print(age, pi, complex_number)

''' Sequence Types
Strings (str): Textual data enclosed in single, double, or triple quotes.
lists (list): Ordered, mutable collections of items. Can contain elements of different types.
Tuples (tuple): Ordered, immutable collections of items. Can contain elements of different types.
Ranges (range): Immutable sequence of numbers, often used in loops. '''
greeting = "Hello, World!"
print(greeting)
fruits = ["apple", "banana", "cherry"]
print(fruits)
coordinates = (10, 20)
print(coordinates)
for i in range(5):
    print(i)

''' Mapping Types
Dictionaries (dict): Unordered collections of key-value pairs. Keys must be unique and immutable. '''
person = {"name": "Alice", "age": 30}
print(person)

''' Set Types
Sets (set): Unordered collections of unique items. Useful for membership tests and set operations.
Frozen Sets (frozenset): Immutable version of a set. Useful for creating sets that should not be changed. '''
unique_numbers = {1, 2, 3, 3}  # {1, 2, 3}
print(unique_numbers)
frozen_set = frozenset([1, 2, 3])
print(frozen_set)

''' Boolean Type
Booleans (bool): Represents truth values. Can be either True or False. '''
is_valid = True
print(is_valid)

''' binary Types
Bytes (bytes): Immutable sequences of bytes. Used for binary data.
Byte Arrays (bytearray): Mutable sequences of bytes.
Memory Views (memoryview): Memory view objects allow us to access the internal data of an object without copying it. '''
binary_data = b"hello"
print(binary_data)
byte_array = bytearray([65, 66, 67])
print(byte_array)
mv = memoryview(b"hello")
print(mv)

''' Type Checking and Conversion
Check Type: Use type() to find the data type of variable
Convert Type: Use type conversion functions like int(), float(), str() '''
print(type(10))           # <class 'int'>
print(type("hello"))      # <class 'str'>
print(type(fruits))       # <class 'list'>
num_str = "123"
num_int = int(num_str)  # Convert string to integer
print(num_str)