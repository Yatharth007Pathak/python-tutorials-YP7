"""
Radix sort is a non-comparative sorting algorithm that sorts numbers by processing their individual digits. 
It works by sorting the elements by their least significant digit first and then working its way to the most significant digit. 
It typically uses a stable subroutine, like counting sort, to sort the digits.

How Radix Sort Works:
Find the maximum number in the array to determine the number of digits.
Sort the array digit by digit, starting from the least significant digit (LSD) to the most significant digit (MSD).
Use a stable sorting algorithm (like counting sort) to sort the numbers based on each digit.

Key Points:
Time Complexity: O(d * (n + k)), where d is the number of digits in the largest number, n is the number of elements, 
and k is the range of digits (typically 0-9). For large datasets, Radix sort is faster than comparison-based algorithms like quicksort.
Space Complexity: O(n + k), similar to counting sort, since it requires additional space for the count and output arrays.

Stability: Radix sort is stable because it maintains the relative order of elements with equal digits when 
using a stable subroutine like counting sort.

Best Use Cases:
Radix sort is best suited for sorting large numbers or strings, 
especially when the number of digits (or character positions) is small compared to the size of the dataset.
"""

# Helper function to do Counting Sort based on a specific digit
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    
    # Output array to store the sorted order
    output = [0] * n
    # Count array for storing occurrences of digits (0-9)
    count = [0] * 10
    
    # Step 1: Store count of occurrences for each digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Step 2: Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Step 3: Build the output array by placing elements in the correct position
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Step 4: Copy the output array to arr[], so that arr now contains sorted numbers
    for i in range(n):
        arr[i] = output[i]

# Radix Sort function
def radix_sort(arr):
    # Step 1: Find the maximum number to know the number of digits
    max_val = max(arr)
    
    # Step 2: Do counting sort for every digit
    # exp is 10^i where i is the current digit number (1s, 10s, 100s, etc.)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print("Sorted array:", sorted_arr)

'''
Here's a pointwise breakdown of each line in the provided Radix Sort implementation:

def counting_sort_for_radix(arr, exp):
Defines a function called counting_sort_for_radix that takes an array arr and an exponent exp, 
which represents the digit place (units, tens, hundreds, etc.) being processed.

n = len(arr)
Gets the length of the array arr and stores it in the variable n.

output = [0] * n
Initializes an output array of size n with zeros. This array will hold the sorted elements based on the current digit.

count = [0] * 10
Initializes a count array of size 10 with zeros to store the count of occurrences for each digit (0-9).

for i in range(n):
Starts a loop to process each element of the array.

index = (arr[i] // exp) % 10
Calculates the digit to be counted by dividing the element arr[i] by exp and taking the remainder when divided by 10.

count[index] += 1
Increments the count for the digit at the index position in the count array.

for i in range(1, 10):
Starts a loop from 1 to 9 to update the count array to store cumulative counts.

count[i] += count[i - 1]
Updates count[i] to be the sum of counts up to the current index, so it reflects the position of digits in the output array.

i = n - 1
Initializes i to the last index of the array for processing elements in reverse order.

while i >= 0:
Starts a loop to place elements in their correct position in the output array.

index = (arr[i] // exp) % 10
Recalculates the digit for the element arr[i].

output[count[index] - 1] = arr[i]
Places the element arr[i] in the correct position in the output array based on its count.

count[index] -= 1
Decrements the count for the digit to handle any duplicates correctly.

i -= 1
Moves to the previous element in the array.

for i in range(n):
Starts a loop to copy the sorted elements from the output array back to the original arr array.

arr[i] = output[i]
Copies the sorted element from output to arr.

def radix_sort(arr):
Defines a function called radix_sort that takes an array arr to be sorted.

max_val = max(arr)
Finds the maximum value in the array to determine the number of digits in the largest number.

exp = 1
Initializes exp to 1, which represents the current digit place (units, tens, etc.).

while max_val // exp > 0:
Starts a loop that continues as long as exp is less than or equal to the maximum value (max_val). This loop processes each digit place.

counting_sort_for_radix(arr, exp)
Calls the counting_sort_for_radix function to sort the elements based on the current digit place exp.

exp *= 10
Multiplies exp by 10 to move to the next digit place (units to tens to hundreds, etc.).

return arr
Returns the sorted array.

arr = [170, 45, 75, 90, 802, 24, 2, 66]
Defines an example unsorted array.

sorted_arr = radix_sort(arr)
Calls the radix_sort function with arr and stores the sorted result in sorted_arr.

print("Sorted array:", sorted_arr)
Prints the sorted array with the label "Sorted array:" followed by the contents of sorted_arr.
'''