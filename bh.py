# Predict the output of of following loops

j = 0
while j <= 10:
    print(j)
    j = j + 1

print("\n")

x = 1
while x == 1:
    x = x -1 
    print(x)

print("\n")

i = 10
while i == 20:
    print("computer buff!")

print("\n")

a = 4
b = 0
while a >= 0:
    a -= 1
    b += 1
    if a == b:
        continue
    else:
        print(a,b)

print("\n")

p = 4
q = 0
while p >= 0:
    if p == q:
        break
    else:
        print(p,q)
    p -= 1
    q += 1