a = 2
b = 3
c = 5

a_str = str(a)
b_str = str(b)
c_str = str(c)

final_string = a_str + b_str + c_str
final_int = int(final_string)

print("final int:", final_int)
print(type(final_int))

'''
Here's what the code does:

Converts the integer values of a, b, and c to their string representations.
Concatenates these strings together.
Converts the concatenated string back to an integer.
'''