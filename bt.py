# While loop

end_number = int(input("Enter the ending number: "))
number = 1
print(f"The natural numbers from 1 to {end_number} are:")
while number <= end_number:
    print(number)
    number += 1
'''
The program first prompts the user to input an end_number.
A variable number is initialized to 1. This will serve as the starting point for our loop.
The while loop condition checks whether number is less than or equal to end_number. If the condition is true, the loop continues.
Inside the loop, the current value of number is printed.
The number is then incremented by 1 using number += 1.
The loop repeats until number exceeds end_number
'''

end_number = int(input("Enter the ending number: "))
number = 1
sum_of_numbers = 0
while number <= end_number:
    sum_of_numbers += number
    number += 1
print(f"The sum of natural numbers from 1 to {end_number} is: {sum_of_numbers}")
'''
The user inputs an end_number.
The variables number and sum_of_numbers are initialized.
The while loop adds each number from 1 to end_number to sum_of_numbers.
The loop continues until number exceeds end_number.
After the loop, the total sum is printed.
'''

end_number = int(input("Enter the ending number: "))
number = 1
product_of_numbers = 1
while number <= end_number:
    product_of_numbers *= number
    number += 1
print(f"The product of natural numbers from 1 to {end_number} is: {product_of_numbers}")
'''
The user inputs an end_number.
The variables number and product_of_numbers are initialized.
The while loop multiplies each number from 1 to end_number with product_of_numbers.
The loop continues until number exceeds end_number.
After the loop, the total product is printed.
'''