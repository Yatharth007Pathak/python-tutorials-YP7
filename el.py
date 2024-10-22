# Python program to swap two elements in a list

n = int(input("Enter size of list: "))

list = []
for _ in range(n):
    num = int(input())
    list.append(num)

print(list)

idx1 = int(input("Enter index 1: "))
idx2 = int(input("Enter index 2: "))

temp = list[idx1]

list[idx1] = list[idx2]
list[idx2] = temp

print(list)


'''
Code Breakdown

Input Collection:
n = int(input("Enter size of list: ")): This prompts the user to enter the size of the list.
list = []: An empty list is initialized to store the elements.
for _ in range(n):: A loop runs n times to collect the elements for the list.
num = int(input()): Prompts the user to input a number.
list.append(num): Appends each input number to the list.

Output:
print(list): Prints the list after the append.

Index Input:
idx1 = int(input("Enter index 1: ")): Prompts the user to input the first index for swapping.
idx2 = int(input("Enter index 2: ")): Prompts the user to input the second index for swapping.

Swapping Elements:
temp = list[idx1]: Temporarily stores the element at idx1.
list[idx1] = list[idx2]: Replaces the element at idx1 with the element at idx2.
list[idx2] = temp: Replaces the element at idx2 with the originally stored element from idx1.

Output:
print(list): Prints the updated list after the swap.
'''