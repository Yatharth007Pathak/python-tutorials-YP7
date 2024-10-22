# O(n) - Linear Time

def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Test
arr = [10, 20, 4, 45, 99]
print(find_max(arr))  # Output: 99