# For loop

print("The first 10 natural numbers are:")
for number in range(1, 11):
    print(number)

'''
The range function is used to generate a sequence of numbers from 1 to 10. 
The range(1, 11) generates numbers starting from 1 up to, but not including, 11.
The for loop iterates over each number in this range, and the print statement outputs each number.
'''


sum_of_numbers = 0
for number in range(1, 11):
    sum_of_numbers += number
print("The sum of the first 10 natural numbers is:", sum_of_numbers)

'''
A variable sum_of_numbers is initialized to 0 to store the sum.
The for loop iterates over each number from 1 to 10, and the += operator adds each number to sum_of_numbers.
After the loop completes, the program prints the total sum.
'''


product_of_numbers = 1
for number in range(1, 11):
    product_of_numbers *= number  # Multiply each number to the product
print("The product of the first 10 natural numbers is:", product_of_numbers)

'''
A variable product_of_numbers is initialized to 1 (since multiplying by 0 would result in 0).
The for loop iterates over each number from 1 to 10, and *= operator multiplies product_of_numbers by the current number in the sequence.
After the loop completes, the program prints the total product.
'''