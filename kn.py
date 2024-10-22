# Implement exception handling in python by showing division operation

a = int(input("Enter a:"))
b = int(input("Enter b:"))

try:
    result = a / b
except ZeroDivisionError:
    result = None
    print("Error: Cannot divivde by zero")
finally:
    print("Division operation completed", result)