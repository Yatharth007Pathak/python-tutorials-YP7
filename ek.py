# Python program to swap two elements in a list

# Sample list
my_list = [10, 20, 30, 40, 50]

# Indices of the elements to be swapped
index1 = 1  # Element at index 1 (20)
index2 = 3  # Element at index 3 (40)

# Swapping elements
my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

# Display the list after swapping
print("List after swapping elements:", my_list)