"""
Method overriding is a type of polymorphism where a subclass provides a specific implementation of a method 
that is already defined in its superclass. 
The method in the subclass overrides the one in the superclass.
"""

class Animal:                                            # Define the Animal class with a general speak method
    def speak(self):                                     # Method to return a generic animal sound
        return "Some sound"

class Dog(Animal):                                       # Define the Dog class that inherits from Animal
    def speak(self):                                     # Override the speak method to return a dog's sound
        return "Woof!"

class Cat(Animal):                                       # Define the Cat class that inherits from Animal
    def speak(self):                                     # Override the speak method to return a cat's sound
        return "Meow!"

animals = [Dog(), Cat()]                                 # Create a list of Animal objects (Dog and Cat instances)

for animal in animals:                                   # Iterate through the list and call the speak method for each animal
    print(animal.speak())  # Output: Woof! Meow!



'''
In this example, the speak method is overridden in both Dog and Cat classes. 
When speak is called on an Animal reference, the method corresponding to the actual object type (Dog or Cat) is executed.
'''