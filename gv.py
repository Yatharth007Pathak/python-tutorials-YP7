"""
Infinite functions, also known as non-terminating or infinite loops, 
are functions or loops that continue executing indefinitely without reaching a stopping condition. 
These can be intentional (such as in servers that run continuously) or accidental (which usually results in an error or crash).
Infinite functions or loops in Python are useful in scenarios where a process needs to run continuously. 

Practical Use of Infinite Loops
While infinite loops might seem dangerous, they are used in real-world applications, such as:
Servers: A web server needs to run indefinitely, listening for requests and responding to them in an infinite loop.
Event loops: In graphical user interfaces (GUIs), an event loop runs indefinitely, waiting for user inputs like mouse clicks or key presses.
"""


# Infinite while Loop: An infinite loop can be created using a while loop without a termination condition.

def infinite_while_loop():
    while True:
        print("This will print forever!")

infinite_while_loop()


'''
Explanation: The loop condition True will always be true, so the loop never ends. 
This kind of loop is often used in servers or event-driven programs that are meant to run continuously
'''