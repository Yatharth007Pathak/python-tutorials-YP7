# Multiple conditions using 'and' and 'or'

eng_marks = int(input("Enter marks in english: "))
mth_marks = int(input("Enter marks in maths: "))
if eng_marks > 80 and mth_marks > 80:
    print("A grade")
elif eng_marks> 80 or mth_marks > 80:
    print("B grade")
else:
    print("C grade") 
# Python program that takes input marks for English and Math, then assigns a grade based on the marks entered.


number = int(input("Enter the number: "))
if number > 999 and number < 10000:
    print("It is a four digit number")
else:
    print("It is not a four digit number")
# Take a positive integer and tell if it is a four digit number or not


n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))
if n1 > n2 and n1 > n3:
    print(n1, "is the greatest number")
elif n2 > n1 and n2 > n3:
    print(n2, "is the greatest number")
else:
    print(n3, "is the greatest number")
# Take 3 positive integers and print the greatest of them