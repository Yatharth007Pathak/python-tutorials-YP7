"""
Class: A user defined data-type. It is a blueprint for creating objects. 
It defines a set of attributes and methods that the objects created from the class will have.
Object: An instance of a class. It is a real-world entity with attributes (data) and methods (functions).
When a class is defined, no memory is allocated until an object of that class is created.

Class Constructor is a special funtion that gets invoked everytime an object is created for that class.
syntax:
class ClassName:
    def __init__(self, parameter1, parameter2, ...):
        # initialize insance variable (attributes) here
"""


class Student:                                          # Define the Student class
    def set_name(self, name):                           # Method to set the name of the student
        self.name = name                                # Assign the provided name to the 'name' attribute of the instance
 
    def get_name(self):                                 # Method to get the name of the student
        return self.name                                # Return the value of the 'name' attribute

student1 = Student()                                    # Create an instance of the Student class
student1.set_name("Yatharth")                           # Set the name for the student1 instance 
print(student1.get_name())                              # Print the name of the student1 instance

student2 = Student()                                    # Create another instance of the Student class
student2.set_name("Pathak")                             # Set the name for the student2 instance  
print(student2.get_name())                              # Print the name of the student2 instance



'''
let's break down the code step by step:

Class Definition:
class Student:
This defines a class named Student. A class is a blueprint for creating objects.

Method set_name:
def set_name(self, name):
    self.name = name
This method takes two arguments: self and name.
self refers to the instance of the class.
name is a parameter that is used to set the name attribute of the instance.
The name attribute is assigned the value passed to set_name.

Method get_name:
def get_name(self):
    return self.name
This method returns the value of the name attribute for the instance.
It uses self to access the name attribute.

Creating student1:
student1 = Student()
This creates an instance of the Student class named student1.

Setting the Name for student1:
student1.set_name("Yatharth")
This calls the set_name method on student1, passing "Yatharth" as the argument.
The name attribute of student1 is set to "Yatharth".

Getting and Printing the Name for student1:
print(student1.get_name())
This calls the get_name method on student1, which returns "Yatharth".
The print function then prints "Yatharth" to the console.

Creating student2:
student2 = Student()
This creates another instance of the Student class named student2.

Setting the Name for student2:
student2.set_name("Pathak")
This calls the set_name method on student2, passing "Pathak" as the argument.
The name attribute of student2 is set to "Pathak".

Getting and Printing the Name for student2:
print(student2.get_name())
This calls the get_name method on student2, which returns "Pathak".
The print function then prints "Pathak" to the console.
'''