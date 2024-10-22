# If we have a list of lists (a nested list), we can access elements by specifying multiple indices.

# Nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
element_1_1 = matrix[0][0]  # 1 (first element of the first list)
element_1_2 = matrix[0][1]  # 2 (second element of the first list)
element_2_1 = matrix[1][0]  # 4 (first element of the second list)
element_2_3 = matrix[1][2]  # 6 (third element of the second list)

print(element_1_1)  # Output: 1
print(element_1_2)  # Output: 2
print(element_2_1)  # Output: 4
print(element_2_3)  # Output: 6


fruits = ["apple", "orange", "cherry"]
fruits.insert(2, ["kiwi", "papaya"])

print(fruits)
print(fruits[2][0])