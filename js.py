#  Multilevel Inheritance: A class is derived from another derived class, creating a chain of inheritance.

class Animal:                                                           # Define the Animal class
    def speak(self):                                                    # Method to return a generic animal sound
        return "Animal sound"

class Dog(Animal):                                                      # Define the Dog class that inherits from Animal
    def bark(self):                                                     # Method specific to the Dog class to return a bark sound
        return "Woof!"

class Puppy(Dog):                                                       # Define the Puppy class that inherits from Dog
    def play(self):                                                     # Method specific to the Puppy class to describe playtime
        return "Puppy is playing"

# Puppy class inherits from Dog, which inherits from Animal
puppy = Puppy()                                                         # Create an instance of the Puppy class
print(puppy.speak())  # Outputs: Animal sound                           # Call the speak method inherited from the Animal class
print(puppy.bark())   # Outputs: Woof!                                  # Call the bark method inherited from the Dog class
print(puppy.play())   # Outputs: Puppy is playing                       # Call the play method specific to the Puppy class



'''
Let's break down the code to understand how inheritance works across multiple levels:

class Animal:
This line defines a class named Animal. It serves as the base class for other classes, providing common functionality that can be inherited.

def speak(self):
This line defines a method named speak within the Animal class. It takes one parameter, self, which refers to the instance of the class.

return "Animal sound"
Inside the speak method, this line returns the string "Animal sound". This provides a generic implementation of the speak behavior for animals.

class Dog(Animal):
This line defines a class named Dog, which inherits from the Animal class. This means Dog will have all the attributes and methods of Animal.

def bark(self):
This line defines a method named bark within the Dog class. It takes one parameter, self, which refers to the instance of the class.

return "Woof!"
Inside the bark method, this line returns the string "Woof!". This method provides a specific implementation of a dog's sound.

class Puppy(Dog):
This line defines a class named Puppy, which inherits from the Dog class. Since Dog inherits from Animal, 
the Puppy class indirectly inherits from Animal as well. The Puppy class extends the Dog class with additional functionality.

def play(self):
This line defines a method named play within the Puppy class. It takes one parameter, self, which refers to the instance of the class.

return "Puppy is playing"
Inside the play method, this line returns the string "Puppy is playing". This method provides a behavior specific to puppies.

puppy = Puppy()
This line creates an instance of the Puppy class and assigns it to the variable puppy. 
This instance has access to methods from the Puppy, Dog, and Animal classes.

print(puppy.speak())
This line calls the speak method on the puppy instance. Since Puppy inherits from Dog, which inherits from Animal, 
the speak method from the Animal class is used. This prints "Animal sound".

print(puppy.bark())
This line calls the bark method on the puppy instance. The bark method is defined in the Dog class, so it prints "Woof!".

print(puppy.play())
This line calls the play method on the puppy instance. The play method is specific to the Puppy class, so it prints "Puppy is playing".

Summary:
Inheritance Hierarchy: The Puppy class inherits from Dog, which in turn inherits from Animal. This forms a chain of inheritance: Puppy → Dog → Animal.
Method Access: The puppy instance has access to methods from all levels of the hierarchy:
speak from Animal
bark from Dog
play from Puppy
Behavior Extension: The Puppy class extends the Dog class by adding a new method (play), while still retaining inherited behaviors from Animal and Dog.
'''