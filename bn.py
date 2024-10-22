num = int(input("Enter a positive number: "))

if num % 15 == 0:
    print("Number is divisible by 15")
else:
    if  num % 3 == 0 or num % 5 == 0:
        print("Number is not divisible by 15")
        print("Number is divisible by 3 or 5")
    else:
        print("Number is neither divisible by 3 nor 5")


# Take positive integer and tell if it is divisible by 5 or 3 but not divisible by 15