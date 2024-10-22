"""
Python doesn't have a built-in switch statement like some other programming languages (such as C or Java). 
However, we can achieve similar functionality using a dictionary to map cases to their corresponding actions or using the match statement, 
which was introduced in Python 3.10 as part of structural pattern matching.
"""

def switch_example(choice_):
    # Define a dictionary that maps choices to actions
    switch_dict = {
        1: "You chose option 1: Start",
        2: "You chose option 2: Stop",
        3: "You chose option 3: Pause",
        4: "You chose option 4: Exit"
    }
    # Get the action from the dictionary based on the user's choice
    # Default to "Invalid option" if the choice is not found
    return switch_dict.get(choice_, "Invalid option")

choice_ = int(input("Enter a choice_ (1-4): "))
result_ = switch_example(choice_)
print(result_)

'''
A dictionary switch_dict is created to map numerical keys (1, 2, 3, 4) to corresponding actions or messages.
The get method is used to retrieve the message associated with the user's choice. 
If the choice isn't found in the dictionary, it defaults to "Invalid option".
The program asks the user to input a choice and then uses the switch_example function to determine and print the result.
'''


def switch_example(choice):
    match choice:
        case 1:
            return "You chose option 1: Start"
        case 2:
            return "You chose option 2: Stop"
        case 3:
            return "You chose option 3: Pause"
        case 4:
            return "You chose option 4: Exit"
        case _:
            return "Invalid option"

choice = int(input("Enter a choice (1-4): "))
result = switch_example(choice)
print(result)

'''
The match statement provides a cleaner syntax for implementing a switch-like structure.
Each case checks for a specific value of choice, and the corresponding action is returned.
The _ case acts as a default case, catching any unmatched values and returning "Invalid option".
'''