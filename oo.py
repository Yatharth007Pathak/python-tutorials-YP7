# O(2^n) - Exponential Time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test
n = 5
print(fibonacci(n))  # Output: 5 (fibonacci(5) = 5)