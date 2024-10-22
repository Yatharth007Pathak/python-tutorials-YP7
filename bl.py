n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))
if n1 > n2:
    if n1 > n3:
        print(n1, "is the greatest number")
    else:
        print(n3, "is the greatest number")
else:
    if n2 > n3:
        print(n2, "is the greatest number")
    else:
        print(n3, "is the greatest number")

# Take 3 positive integers and print the greatest of them using nested if-else statement