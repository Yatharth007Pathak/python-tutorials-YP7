# Calculate a raised to power b

def power(a, b):
    
    # Base case
    if b == 0:
        return 1
    
    # Recursive case
    else:
        return a * power(a, b-1)
    
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(power(a, b))