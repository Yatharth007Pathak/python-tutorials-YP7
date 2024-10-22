# Pass by reference

def ModifyList(lst):
    lst.append(4)
    print("Inside function:", lst)

lst = [1, 2, 3]
ModifyList(lst)
print("Outside function:", lst)

'''
Let's break down the code line by line:

def ModifyList(lst):
Purpose: This line defines a new function called ModifyList.
lst: This is a parameter that the function accepts when it is called. It represents a list that will be passed to the function.

lst.append(4)
Purpose: Inside the ModifyList function, this line adds the integer 4 to the end of the list lst using the append() method.
Effect: The list lst is modified in place, meaning the change is applied directly to the list that was passed into the function.

print("Inside function:", lst)
Purpose: This line prints the string "Inside function:" followed by the current state of the list lst.
Context: This print statement helps to show the contents of the list lst after it has been modified inside the function.

lst = [1, 2, 3]
Purpose: This line creates a new list with the elements 1, 2, and 3, and assigns it to the variable lst.

ModifyList(lst)
Purpose: This line calls the ModifyList function, passing the list lst (which currently contains [1, 2, 3]) as an argument.
Effect: The function modifies the list by appending 4 to it, making the list [1, 2, 3, 4]. 
It also prints the modified list inside the function.

print("Outside function:", lst)
Purpose: This line prints the string "Outside function:" followed by the current state of the list lst.
Effect: Since lists are mutable objects, the modification made inside the ModifyList function affects the original list. 
Therefore, this line will print the list as [1, 2, 3, 4].

Output:
When you run this code, the output will be:
Inside function: [1, 2, 3, 4]
Outside function: [1, 2, 3, 4]

Explanation: The list lst is passed by reference to the ModifyList function, 
so when the list is modified within the function, the changes are reflected outside the function as well.
'''