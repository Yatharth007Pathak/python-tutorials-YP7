"""
Importing python modules

1. Using import statement
import <module_name>
import <module1>, <module2>,...., <moduleN>

To access a particular method from any module:
ModuleName.functionName()

2. Using from statement: Used to access specific/ all attributes from a module
from <module> import <function1>
from <module> import <fun1>, <fun2>,...., <funN>
from <module> import *

To access a particular method from any module:
functionName()

"""

import math                   # Import all the functions of math module
print(math.sqrt(144))
# print(sin(45))              Output: NameError: name 'sin' is not defined
print(math.sin(45))

from math import sin
print(sin(0))
# print(sqrt(25))             Output: NameError: name 'sqrt' is not defined

from math import cos, cbrt
print(cos(0))
print(cbrt(27))

from math import *            # Import all the functions of math module
print(tan(0))