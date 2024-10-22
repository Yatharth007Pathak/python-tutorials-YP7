# Function to calculate sum from 1 to n

def SumOnrToN(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

n = int(input("Enter n: "))

# call function
output = SumOnrToN(n)
print("Sum of all numbers till n is:", output)


'''
Here's a breakdown of each line of the code:

def SumOnrToN(n):
This line defines a function named SumOnrToN that takes one parameter, n.

    sum = 0
Initializes a variable sum to 0. This variable will be used to accumulate the sum of numbers from 1 to n.

    for i in range(1, n+1):
Starts a for loop that iterates over a range of numbers from 1 to n (inclusive). 
range(1, n+1) generates a sequence of numbers starting from 1 up to n, with n+1 ensuring that n is included in the sequence.

        sum += i
In each iteration of the loop, the current value of i is added to sum. This accumulates the total sum of numbers from 1 to n.

    return sum
After the loop completes, the function returns the final value of sum, which is the sum of all numbers from 1 to n.

n = int(input("Enter n: "))
Prompts the user to input a value, converts it to an integer, and assigns it to the variable n.

output = SumOnrToN(n)
Calls the SumOnrToN function with the user-provided value of n and stores the result in the variable output.

print("Sum of all numbers till n is:", output)
Prints the result stored in output, showing the sum of all numbers from 1 to n to the user.
'''