"""
Polymorphism allows objects of different classes to behave as objects of same Superclass.
Polymorphism allows different classes to be treated as instances of the same class through inheritance.
It means "many forms" and allows functions to use objects of different types.
Polymorphism allows methods to be used interchangeably with different objects, making code more flexible and scalable


Python supports several types of polymorphism:

Subtype Polymorphism -
Duck Typing: Polymorphism based on method and attribute presence rather than type.

Runtime Polymorphism: Resolved during runtime. This is achieved through method overriding.
Method Overriding: Subclasses provide specific implementations for methods defined in a superclass.

Compile time polymorphism: Resolved during compile time. Achieved through method overloading and operator overloading
Method Overloading: Achieved through default or variable-length arguments (Python does not support traditional overloading).
Operator Overloading: Custom behavior for operators applied to instances of a class.
"""

class Animal:                                   # Define the Animal class with an abstract speaks method
    def speaks(self):                           # Define the speaks method that will be overridden by subclasses
        pass                                    # This is a placeholder method

class Dog(Animal):                              # Define the Dog class that inherits from Animal
    def speaks(self):                           # Override the speaks method to provide Dog-specific behavior
        print("Bark")

class Cat(Animal):                              # Define the Cat class that inherits from Animal
    def speaks(self):                           # Override the speaks method to provide Cat-specific behavior
        print("Meow")

class Cow(Animal):                              # Define the Cow class that inherits from Animal
    def speaks(self):                           # Override the speaks method to provide Cow-specific behavior
        print("Mooh")

# Create instances of each animal
dog = Dog()
cat = Cat()
cow = Cow()

# Call the speaks method on each instance
dog.speaks()
cat.speaks()
cow.speaks()

'''
Let's analyze the provided code to understand the use of inheritance and method overriding in a class hierarchy:

class Animal:
This defines a base class named Animal. It provides a common interface for all animal types.

def speaks(self):
This is a method definition within the Animal class. It uses the pass statement, which means it does nothing. 
This method is intended to be overridden in subclasses to provide specific behaviors.

class Dog(Animal):
This defines a class named Dog that inherits from the Animal class. 
The Dog class will override the speaks method to provide its specific behavior.

def speaks(self):
This method overrides the speaks method from the Animal class. It provides the specific implementation for the Dog class.

print("Bark")
This line prints "Bark", which is the sound that a dog makes.

class Cat(Animal):
This defines a class named Cat that also inherits from the Animal class. 
The Cat class will override the speaks method to provide its specific behavior.

def speaks(self):
This method overrides the speaks method from the Animal class. It provides the specific implementation for the Cat class.

print("Meow")
This line prints "Meow", which is the sound that a cat makes.

class Cow(Animal):
This defines a class named Cow that inherits from the Animal class. 
The Cow class will override the speaks method to provide its specific behavior.

def speaks(self):
This method overrides the speaks method from the Animal class. It provides the specific implementation for the Cow class.

print("Mooh")
This line prints "Mooh", which is the sound that a cow makes.

dog = Dog()
This line creates an instance of the Dog class and assigns it to the variable dog.

cat = Cat()
This line creates an instance of the Cat class and assigns it to the variable cat.

cow = Cow()
This line creates an instance of the Cow class and assigns it to the variable cow.

dog.speaks()
This line calls the speaks method on the dog instance. Since Dog overrides the speaks method from Animal, it prints "Bark".

cat.speaks()
This line calls the speaks method on the cat instance. Since Cat overrides the speaks method from Animal, it prints "Meow".

cow.speaks()
This line calls the speaks method on the cow instance. Since Cow overrides the speaks method from Animal, it prints "Mooh".
'''