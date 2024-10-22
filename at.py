# Arithmetic operators
print("sum:", 4+3)
print("difference:", 4-3)
print("product:", 4*3)
print("division:", 4/3)
print("floor division:", 4//3)
print("remainder:", 4%3)
print("exponentiation:", 4**3)

# Comparison operators
p1 = 4
p2 = 7
print(p1 == p2)
print(p1 != p2)
print(p1 > p2)
print(p1 < p2)
print(p1 >= p2)
print(p1 <= p2)
      
# Logical operators
exp1 = 2>1
exp2 = 5<4
print("exp1 and exp2:", exp1 and exp2)
print("exp1 or exp2:", exp1 or exp2)
print("not exp1:", not exp1)
print("not exp2:", not exp2)

# Assignment operators
n1 = 5
n2 = n1
print(n1, n2)
n2 += n1
print(n1, n2)
n2 -= n1
print(n1, n2)
n2 *= n1
print(n1, n2)
n2 /= n1
print(n1, n2)
n2 //= n1
print(n1, n2)
n2 %= n1
print(n1, n2)
n2 **= n1
print(n1, n2)

# Bitwise operators
a = 5
b = 7
print("a and b", a & b)
print("a or b", a | b)
print("a xor b", a ^ b)
print("not a", ~ a)
print("not b", ~ b)
print("bitwise left shift a", a << 1)
print("bitwise right shift b", b >> 1)


# Membership operators
fruits = ["apple", "banana", "cherry"]
print("if cherry is present in fruits:", "cherry" in fruits)
print("if mango is not present in fruits:", "mango" not in fruits)

# Identity operators
x = 5
y = 5
print("if x is y:", x is y)
print("if x is not y:", x is not y)
