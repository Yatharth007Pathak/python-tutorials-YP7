"""
Counting sort is a non-comparison-based sorting algorithm that works efficiently when the range of input values is small compared to the 
number of elements. It operates by counting the occurrences of each unique element in the input array and then uses this count 
information to place each element in its correct position in the output array.

Steps:
Find the range of the input values (find the maximum and minimum elements).
Create a count array to store the frequency of each element.
Calculate the cumulative sum of the count array to determine the positions of each element in the sorted array.
Place each element in its correct position in the output array.
Copy the sorted elements back to the original array (optional if required in-place sorting).

Key Points:
Time Complexity: O(n + k), where n is the number of elements in the input array, and k is the range of the input (max value - min value). 
Counting sort is linear when the range of the input values is not significantly larger than the number of elements.
Space Complexity: O(n + k) due to the use of the count array and output array.
Stability: Counting sort is a stable sorting algorithm, meaning it preserves the relative order of equal elements.

Best Use Cases:
Counting sort is particularly useful when the range of input values is limited and the values are integers (or can be mapped to integers). 
For example, it works well with sorting grades (0-100), or when the range of input values is known and not too large.
However, it is not suitable for large ranges or floating-point numbers.
"""

def counting_sort(arr):
    # Step 1: Find the maximum element in the array
    max_val = max(arr)
    min_val = min(arr)  # Handle negative values as well
    range_of_elements = max_val - min_val + 1

    # Step 2: Create a count array and initialize it with 0
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Step 3: Count the occurrences of each element
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    # Step 4: Modify the count array to store the cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 5: Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    # Step 6: Copy the sorted elements into the original array (if needed)
    for i in range(len(arr)):
        arr[i] = output[i]

    return arr

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)

'''
Here's a detailed pointwise breakdown of each line in the counting_sort function:

def counting_sort(arr):
This defines a function called counting_sort that takes an array arr as input to sort.

max_val = max(arr)
Finds the maximum value in the array arr and stores it in the variable max_val.

min_val = min(arr)
Finds the minimum value in the array arr and stores it in the variable min_val. This is done to handle negative values in the array.

range_of_elements = max_val - min_val + 1
Calculates the range of elements in the array as the difference between max_val and min_val, then adds 1 to account for the inclusive range.
This ensures that all elements can be represented in the count array.

count = [0] * range_of_elements
Creates a count array initialized with zeros, having a size equal to the range of elements in the input array. 
This array will track the occurrences of each element.

output = [0] * len(arr)
Creates an output array of the same length as arr, initialized with zeros. This will store the sorted output.

for i in range(len(arr)):
Starts a loop that iterates over each element in the array.

count[arr[i] - min_val] += 1
For each element arr[i], the corresponding index in the count array is incremented. 
The subtraction of min_val adjusts the index to account for any negative values in the array.

for i in range(1, len(count)):
This loop starts from index 1 and modifies the count array to store cumulative counts.

count[i] += count[i - 1]
Updates the count array so that each index now contains the cumulative count of elements up to that index.

for i in range(len(arr) - 1, -1, -1):
This loop iterates over the array from the last element to the first (in reverse order), 
placing elements in their correct position in the output array.

output[count[arr[i] - min_val] - 1] = arr[i]
Places the element arr[i] in the correct position in the output array based on its cumulative count in the count array. 
The count value is decremented by 1 to handle repeated values.

count[arr[i] - min_val] -= 1
Decrements the count for the current element after placing it in the output array to ensure that duplicate values are placed correctly.

for i in range(len(arr)):
This loop iterates over the output array.

arr[i] = output[i]
Copies the sorted elements from the output array back into the original arr array.

return arr
The function returns the sorted array arr.

arr = [4, 2, 2, 8, 3, 3, 1]
An example unsorted array is defined with the elements [4, 2, 2, 8, 3, 3, 1].

sorted_arr = counting_sort(arr)
The counting_sort function is called with arr as the argument, and the sorted array is stored in the variable sorted_arr.

print("Sorted array:", sorted_arr)
This line prints the sorted array with the label "Sorted array:" followed by the contents of sorted_arr.
'''