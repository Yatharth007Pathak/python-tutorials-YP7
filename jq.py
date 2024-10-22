# Single Inheritance: A class inherits from only one base (parent) class.

class Animal:                                                             # Define the Animal class
    def speak(self):                                                      # Method to return a generic animal sound
        return "Animal sound"

class Dog(Animal):                                                        # Define the Dog class that inherits from the Animal class
    def bark(self):                                                       # Method specific to the Dog class to return a bark sound
        return "Woof!"

# Dog class inherits from Animal
dog = Dog()                                                               # Create an instance of the Dog class
print(dog.speak())  # Outputs: Animal sound                               # Call the speak method inherited from the Animal class
print(dog.bark())   # Outputs: Woof!                                      # Call the bark method specific to the Dog class



'''
Let's break down the code and understand its purpose:

class Animal:
This line defines a new class named Animal. This class serves as a base class for other animal-related classes.

def speak(self):
This line defines a method named speak within the Animal class. It takes one parameter, self, which refers to the instance of the class.

return "Animal sound"
Inside the speak method, this line returns the string "Animal sound". 
This method provides a generic implementation for making a sound, which can be overridden or extended by subclasses.

class Dog(Animal):
This line defines a new class named Dog, which inherits from the Animal class. 
The Dog class is a subclass of Animal, meaning it inherits all properties and methods from Animal.

def bark(self):
This line defines a method named bark within the Dog class. It takes one parameter, self, which refers to the instance of the class.

return "Woof!"
Inside the bark method, this line returns the string "Woof!". This method provides a specific implementation for a dog's sound.

dog = Dog()
This line creates an instance of the Dog class and assigns it to the variable dog. 
The Dog instance has access to methods from both the Dog class and the Animal class.

print(dog.speak())
This line calls the speak method on the dog instance. 
Since Dog inherits from Animal, it uses the speak method defined in the Animal class. This prints "Animal sound".

print(dog.bark())
This line calls the bark method on the dog instance. The bark method is specific to the Dog class and prints "Woof!".

Summary:
Inheritance: The Dog class inherits from the Animal class, which means it can use the speak method from Animal.
Specific Implementation: The Dog class defines its own method, bark, which is specific to dogs.
Method Access: The dog instance can call both inherited methods (speak) and its own methods (bark).
'''