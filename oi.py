"""
Time complexity is a way to evaluate the efficiency of an algorithm in terms of how the runtime of the algorithm grows 
as the size of the input data increases. 
It provides an estimate of the amount of time an algorithm will take to complete, relative to the size of the input.

Here are a few common time complexities:

O(1): Constant time - The runtime doesn't change with the size of the input. For example, accessing an element in an array by index.

O(log n): Logarithmic time - The runtime grows logarithmically as the input size increases. 
This is common in algorithms that divide the problem in half each time, like binary search.

O(n): Linear time - The runtime grows linearly with the input size. For example, iterating through a list.

O(n log n): Linearithmic time - The runtime grows in proportion to n log n. 
This is typical of efficient sorting algorithms like mergesort and heapsort.

O(n^2): Quadratic time - The runtime grows quadratically with the input size. 
This is often seen in algorithms with nested loops, such as bubble sort.

O(2^n): Exponential time - The runtime grows exponentially with the input size. 
This is common in algorithms that solve problems by generating all possible solutions, 
such as the brute-force solution to the traveling salesman problem.

O(n!): Factorial time - The runtime grows factorially with the input size. 
This is often seen in algorithms that generate all permutations of the input, like solving the traveling salesman problem using brute-force.
"""

import time

# O(1) - Constant Time
def constant_time_operation(lst):
    return lst[0]  # Accessing the first element of the list

# O(log n) - Logarithmic Time (Binary Search)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n) - Linear Time
def linear_time_operation(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

# O(n log n) - Linearithmic Time (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# O(n^2) - Quadratic Time (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# O(2^n) - Exponential Time (Fibonacci)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# O(n!) - Factorial Time (Generate Permutations)
from itertools import permutations
def generate_permutations(arr):
    return list(permutations(arr))

# Example usage and timing
n = 10  # Size of list
lst = list(range(n))  # Example list

print("Constant Time Operation:", constant_time_operation(lst))

# Binary search requires a sorted list
sorted_lst = sorted(lst)
print("Binary Search:", binary_search(sorted_lst, 5))

print("Linear Time Operation:", linear_time_operation(lst))

merge_sort_lst = lst.copy()
merge_sort(merge_sort_lst)
print("Merge Sort Result:", merge_sort_lst)

bubble_sort_lst = lst.copy()
bubble_sort(bubble_sort_lst)
print("Bubble Sort Result:", bubble_sort_lst)

print("Fibonacci of 5:", fibonacci(5))

perm_list = [1, 2, 3]
print("Permutations of [1, 2, 3]:", generate_permutations(perm_list))

'''
O(1) - Constant Time: Directly accessing the first element of the list.
O(log n) - Logarithmic Time: Binary search on a sorted list.
O(n) - Linear Time: Finding the maximum value in the list.
O(n log n) - Linearithmic Time: Merge sort to sort the list.
O(n^2) - Quadratic Time: Bubble sort to sort the list.
O(2^n) - Exponential Time: Fibonacci sequence calculation using recursion.
O(n!) - Factorial Time: Generating all permutations of a list.
'''