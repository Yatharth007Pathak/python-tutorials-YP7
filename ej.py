# List Slicing: Lists can be sliced to create sublists.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

slice1 = numbers[2:5]  # Elements from index 2 to 4
slice2 = numbers[:3]   # Elements from start to index 2
slice3 = numbers[5:]   # Elements from index 5 to end
slice4 = numbers[::2]  # Every second element

print(slice1)  # Output: [2, 3, 4]
print(slice2)  # Output: [0, 1, 2]
print(slice3)  # Output: [5, 6, 7, 8, 9]
print(slice4)  # Output: [0, 2, 4, 6, 8]

'''
Slice 1: numbers[2:5]
Explanation: This slice extracts elements starting from index 2 up to, but not including, index 5.
Result: [2, 3, 4]
Indices: Corresponding to indices 2, 3, and 4.

Slice 2: numbers[:3]
Explanation: This slice extracts elements from the start of the list up to, but not including, index 3.
Result: [0, 1, 2]
Indices: Corresponding to indices 0, 1, and 2.

Slice 3: numbers[5:]
Explanation: This slice extracts elements starting from index 5 to the end of the list.
Result: [5, 6, 7, 8, 9]
Indices: Corresponding to indices 5 through 9.

Slice 4: numbers[::2]
Explanation: This slice extracts every second element from the list, starting from index 0.
Result: [0, 2, 4, 6, 8]
Indices: Corresponding to indices 0, 2, 4, 6, and 8.
Summary of Outputs
'''