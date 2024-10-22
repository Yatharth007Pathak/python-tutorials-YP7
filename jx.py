"""
Duck typing is a concept where the type or class of an object is determined by its behavior (methods and properties) 
rather than its explicit inheritance from a class. 
In Python, this is often summarized as "If it looks like a duck and quacks like a duck, it must be a duck."
"""

class Dog:                                        # Define the Dog class
    def speak(self):                              # Method to return the sound a dog makes
        return "Woof!"

class Cat:                                        # Define the Cat class
    def speak(self):                              # Method to return the sound a cat makes
        return "Meow!"

def make_animal_speak(animal):                    # Define a function that takes an animal object and calls its speak method
    print(animal.speak())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the make_animal_speak function with Dog and Cat instances
make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!


# In this example, the make_animal_speak function can accept any object that has a speak method, regardless of its class.