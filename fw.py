def add(n1=0, n2=0):
    print("n1:", n1)
    print("n2:", n2)
    sum = n1 + n2
    return sum


# Positional arguments
print("The sum is", add(2, 3))
print("The sum is", add(3, 2))


# Keyword arguments (named arguments)
print("The sum is", add(n1=2, n2=3))
print("The sum is", add(n2=3, n1=2))


# default arguments
print("The sum is", add(3))
print("The sum is", add())


# Arbitrary arguments *args
def AddAllNumbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
output = AddAllNumbers(2, 3, 4, 5, 6)
print("The sum is", output)


# Arbitrary arguments **kwargs
def StudentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x, "is", y)
StudentInfo(name="Yatharth", age=20, city="Almora")