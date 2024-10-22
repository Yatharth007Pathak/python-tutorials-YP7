# If we have a Tuple of Tuples (a nested Tuple), we can access elements by specifying multiple indices.

# Nested Tuple
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Accessing elements in a nested Tuple
element_1_1 = matrix[0][0]  # 1 (first element of the first tuple)
element_1_2 = matrix[0][1]  # 2 (second element of the first tuple)
element_2_1 = matrix[1][0]  # 4 (first element of the second tuple)
element_2_3 = matrix[1][2]  # 6 (third element of the second tuple)

print(element_1_1)  # Output: 1
print(element_1_2)  # Output: 2
print(element_2_1)  # Output: 4
print(element_2_3)  # Output: 6