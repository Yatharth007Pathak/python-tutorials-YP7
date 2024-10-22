"""
Traversing a string in Python means accessing each character in the string one by one. 
This is often done using loops, which allow us to perform operations on each character. 
Here are some common ways to traverse a string in Python:
"""


# Using a for Loop: We can use a for loop to iterate over each character in the string
my_string = "Hello, World!"
for char in my_string:
    print(char)
'''
Explanation: The loop iterates over each character in my_string, and char represents the current character being accessed. 
The print(char) statement outputs each character on a new line.
'''


# Using a for Loop with range(): We can also use the range() function along with indexing to traverse the string
my_string = "Hello, World!"
for i in range(len(my_string)):
    print(my_string[i])
'''
Explanation: Here, range(len(my_string)) generates a sequence of numbers from 0 to the length of the string minus 1. 
The loop then accesses each character by its index i.
'''


# Using a while Loop: A while loop can also be used for traversing a string
my_string = "Hello, World!"
i = 0
while i < len(my_string):
    print(my_string[i])
    i += 1
'''
Explanation: The loop starts with i = 0 and continues until i is less than the length of the string. 
The character at index i is accessed and printed in each iteration. The index i is then incremented by 1.
'''


# Traversing with Enumerate: The enumerate() function can be used if we need both the index and the character during traversal
my_string = "Hello, World!"
for index, char in enumerate(my_string):
    print(f"Character at index {index} is {char}")
'''
Explanation: enumerate(my_string) returns pairs of (index, character), 
where index is the position of the character in the string, and char is the character itself.
'''


# Reverse Traversal: You can also traverse the string in reverse order


# Using negative indexing:
my_string = "Hello, World!"
for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i])

# Using slicing:
my_string = "Hello, World!"
for char in my_string[::-1]:
    print(char)
'''
Explanation: The first method uses a for loop with range() starting from the last index (len(my_string) - 1) down to 0. 
The second method uses slicing [::-1] to reverse the string and then iterates over it.
'''

# Skipping Characters: We can skip characters while traversing by using step values in range() or slicing
my_string = "Hello, World!"
# Using range with step
for i in range(0, len(my_string), 2):
    print(my_string[i])
# Using slicing
for char in my_string[::2]:
    print(char)
'''
Explanation: Both examples traverse the string by skipping every second character. 
The first example uses range(0, len(my_string), 2), and the second example uses slicing [::2] to achieve this.
'''