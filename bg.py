# Looping statements

""" Python program that demonstrates the use of for loop."""

end_number = int(input("Enter the ending number: "))
print(f"The natural numbers from 1 to {end_number} are:")
for number in range(1, end_number + 1):
    print(number)
# Print Natural Numbers from 1 to a User-Specified Number


end_number = int(input("Enter the ending number: "))
sum_of_numbers = 0
for number in range(1, end_number + 1):
    sum_of_numbers += number
print(f"The sum of natural numbers from 1 to {end_number} is: {sum_of_numbers}")
# Sum of Natural Numbers from 1 to a User-Specified Number


end_number = int(input("Enter the ending number: "))
product_of_numbers = 1
for number in range(1, end_number + 1):
    product_of_numbers *= number
print(f"The product of natural numbers from 1 to {end_number} is: {product_of_numbers}")
# Product of Natural Numbers from 1 to a User-Specified Number

n = int(input("Enter n: "))
for i in range(1, n+1):
    print(i, "Jai Shree Ram")
# Print 'Jai Shree Ram' n number of times

list = [10, 20, 30, 40, 50, 60]
for j in list:
    print(j)
# Print elements of a list


""" Python program that demonstrates the use of while loop. """

number = 1
print("The natural numbers from 1 to 10 are:")
while number <= 10:
    print(number)
    number += 1
# Print Numbers from 1 to 10

number = 1
sum_of_numbers = 0
while number <= 10:
    sum_of_numbers += number
    number += 1
print("The sum of natural numbers from 1 to 10 is:", sum_of_numbers)
# Sum of Numbers from 1 to 10

number = 1
product_of_numbers = 1
while number <= 10:
    product_of_numbers *= number
    number += 1
print("The product of natural numbers from 1 to 10 is:", product_of_numbers)
# Product of Numbers from 1 to 10

count = 1
while count <= 10:
    print("Har Har Mahadev")
    count += 1
# Print 'Har Har Mahadev' n number of times

elements = ["apple", "banana", "cherry", "date", "elderberry"]
index = 0
while index < len(elements):
    print(elements[index])
    index += 1
# Print the elements of a list