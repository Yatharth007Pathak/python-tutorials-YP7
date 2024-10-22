# Hierarchical Inheritance: Multiple classes inherit from the same base class.

class Animal:                                                  # Define the Animal class
    def speak(self):                                           # Method to return a generic animal sound
        return "Animal sound"

class Dog(Animal):                                             # Define the Dog class that inherits from Animal
    def bark(self):                                            # Method specific to the Dog class to return a bark sound
        return "Woof!"

class Cat(Animal):                                             # Define the Cat class that inherits from Animal
    def meow(self):                                            # Method specific to the Cat class to return a meow sound
        return "Meow!"

# Dog and Cat classes both inherit from Animal
dog = Dog()                                                    # Create an instance of the Dog class
cat = Cat()                                                    # Create an instance of the Cat class
print(dog.speak())  # Outputs: Animal sound                    # Call the speak method from the Animal class using the Dog instance
print(dog.bark())   # Outputs: Woof!                           # Call the bark method specific to the Dog class
print(cat.speak())  # Outputs: Animal sound                    # Call the speak method from the Animal class using the Cat instance
print(cat.meow())   # Outputs: Meow!                           # Call the meow method specific to the Cat class


'''
Let's break down the code to understand how inheritance is used and how it affects method access for different classes:

class Animal:
This defines a base class named Animal. It will provide common functionality that can be inherited by other classes.

def speak(self):
This method is defined within the Animal class. It takes self as a parameter, referring to the instance of the class.

return "Animal sound"
This line returns the string "Animal sound". This method provides a generic implementation of the speak behavior for all animals.

class Dog(Animal):
This defines a class named Dog, which inherits from the Animal class. This means Dog inherits all methods and attributes from Animal.

def bark(self):
This method is defined within the Dog class. It takes self as a parameter.

return "Woof!"
This line returns the string "Woof!". This method provides a specific behavior for dogs.

class Cat(Animal):
This defines a class named Cat, which also inherits from the Animal class. Like Dog, Cat inherits all methods and attributes from Animal.

def meow(self):
This method is defined within the Cat class. It takes self as a parameter.

return "Meow!"
This line returns the string "Meow!". This method provides a specific behavior for cats.

dog = Dog()
This line creates an instance of the Dog class and assigns it to the variable dog. 
This instance has access to both the speak method from Animal and the bark method from Dog.

cat = Cat()
This line creates an instance of the Cat class and assigns it to the variable cat. 
This instance has access to both the speak method from Animal and the meow method from Cat.

print(dog.speak())
This line calls the speak method on the dog instance. Since Dog inherits from Animal, 
it uses the speak method from the Animal class. This prints "Animal sound".

print(dog.bark())
This line calls the bark method on the dog instance. The bark method is defined in the Dog class, so it prints "Woof!".

print(cat.speak())
This line calls the speak method on the cat instance. Since Cat inherits from Animal, 
it uses the speak method from the Animal class. This prints "Animal sound".

print(cat.meow())
This line calls the meow method on the cat instance. The meow method is defined in the Cat class, so it prints "Meow!".

Summary:
Multiple Inheritance: Both Dog and Cat inherit from the Animal class. This demonstrates how multiple classes can share common functionality through inheritance.
Method Access: Each class (Dog and Cat) has access to:
speak method inherited from Animal.
Their own specific methods (bark for Dog and meow for Cat).
Behavior Extension: While Dog and Cat share common behavior (the speak method), they also have their own specific behaviors (bark and meow, respectively).
'''