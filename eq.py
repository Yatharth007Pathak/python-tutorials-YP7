color = ("green")
print(color) 
print(type(color))

print()

colour = ("green",)
print(colour)
print(type(colour))

# This code demonstrates the difference between creating a string and a tuple with a single element in Python.

'''
color is assigned the value "green".
Since there are no commas in the parentheses, Python interprets ("green") as a string, not as a tuple.
Therefore, color is a string, and type(color) returns <class 'str'>.

colour is assigned the value ("green",).
The comma after "green" indicates that this is a tuple with a single element.
Therefore, colour is a tuple, and type(colour) returns <class 'tuple'>.
'''