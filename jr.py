# Multiple Inheritance: A class can inherit from more than one base class.
# This allows the derived class to inherit attributes and methods from multiple classes.

class Father:                                          # Define the Father class
    def work(self):                                    # Method to describe the Father's work
        return "Father is working"

class Mother:                                          # Define the Mother class
    def cook(self):                                    # Method to describe the Mother's cooking
        return "Mother is cooking"

class Child(Father, Mother):                           # Define the Child class that inherits from both Father and Mother
    pass                                               # Inherits all methods from Father and Mother without additional methods or attributes

child = Child()                                        # Create an instance of the Child class, Child class inherits from both Father and Mother
print(child.work())  # Outputs: Father is working      # Call the work method inherited from the Father class
print(child.cook())  # Outputs: Mother is cooking      # Call the cook method inherited from the Mother class


'''
Let's break down the code to understand the concepts of multiple inheritance and method access:

class Father:
This line defines a new class named Father. This class has a method that describes the work of a father.

def work(self):
This line defines a method named work within the Father class. It takes one parameter, self, which refers to the instance of the class.

return "Father is working"
Inside the work method, this line returns the string "Father is working", describing what the Father class does.

class Mother:
This line defines a new class named Mother. This class has a method that describes the cooking of a mother.

def cook(self):
This line defines a method named cook within the Mother class. It takes one parameter, self, which refers to the instance of the class.

return "Mother is cooking"
Inside the cook method, this line returns the string "Mother is cooking", describing what the Mother class does.

class Child(Father, Mother):
This line defines a new class named Child that inherits from both the Father and Mother classes. 
This is an example of multiple inheritance, where a class (Child) inherits from more than one base class (Father and Mother).

pass
The pass statement is a placeholder indicating that the Child class does not add any new methods or attributes 
beyond those inherited from Father and Mother. It uses all the functionality provided by its parent classes as-is.

child = Child()
This line creates an instance of the Child class and assigns it to the variable child.
This instance has access to methods from both parent classes (Father and Mother).

print(child.work())
This line calls the work method on the child instance. Since Child inherits from Father, 
it uses the work method defined in the Father class. This prints "Father is working".

print(child.cook())
This line calls the cook method on the child instance. Since Child inherits from Mother, 
it uses the cook method defined in the Mother class. This prints "Mother is cooking".

Summary:
Multiple Inheritance: The Child class inherits from both Father and Mother, demonstrating multiple inheritance. This means that Child can access methods from both parent classes.
Method Access: The child instance can call both the work method from the Father class and the cook method from the Mother class.
Inheritance Hierarchy: In the case of multiple inheritance, the order in which base classes are listed can affect method resolution, but in this simple example, it shows straightforward access to methods from both parent classes.
'''