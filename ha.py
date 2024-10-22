# Example of a Controlled Infinite Loop:

def controlled_infinite_loop():
    while True:
        user_input = input("Type 'exit' to stop the loop: ")
        if user_input.lower() == 'exit':
            print("Exiting the loop.")
            break

controlled_infinite_loop()

'''
Explanation: This loop runs indefinitely until the user types "exit". 
This is an example of how an infinite loop can be controlled by an external event (user input).
'''