input_tuple = (1, 2, 3, 4, 5, 6)

list_ = []

for x in reversed(input_tuple):
    list_.append(x)

output_tuple = tuple(list_)
print(output_tuple)


'''
This code takes a tuple as input, reverses the elements, and then converts the reversed list back into a tuple.

Code Explanation

input_tuple = (1, 2, 3, 4, 5, 6)
The tuple input_tuple is initialized with the values (1, 2, 3, 4, 5, 6).

list_ = []
An empty list list_ is created to store the reversed elements of the tuple.

for x in reversed(input_tuple):
    list_.append(x)
The reversed() function is used to iterate over the input_tuple in reverse order.
Each element x from the reversed tuple is appended to the list_.

output_tuple = tuple(list_)
print(output_tuple)
The list list_ is converted back into a tuple using the tuple() function.
The resulting output_tuple is printed.

Output:
(6, 5, 4, 3, 2, 1)
Explanation:
The elements of the input_tuple are reversed, and the resulting tuple (6, 5, 4, 3, 2, 1) is printed.
'''