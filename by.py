"""
In Python, the end parameter is used in the print() function to specify what should be printed at the end of the output. 
By default, the print() function ends with a newline character (\n), which means each call to print() will output its result on a new line. 
However, we can change this behavior by using the end parameter to append a different string instead of the newline character.
"""

# Print Numbers on the Same Line
for i in range(1, 6):
    print(i, end=' ')                      # Here, end=' ' specifies that a space should be added after each number instead of a newline.
print()


# Print Items Separated by a Custom String
for char in ['A', 'B', 'C']:
    print(char, end='-')                   # In this case, end='-' means each character is followed by a dash instead of a newline.
print()


# Print Without Any Separator
for word in ['Hello', 'World']:
    print(word, end='')                    # Here, end='' causes the outputs to be concatenated directly with no space or newline between them.
print()