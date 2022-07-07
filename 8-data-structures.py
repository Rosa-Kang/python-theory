from hashlib import algorithms_available
from re import T
from sqlite3 import ProgrammingError


ProgrammingError
# Algorithms : a set of rules or steps used to solve problem ex.loops
# Data Structure : a particular way of organizing data in a computer ex. string, list etc

# Strings are not Mutable, whereas Lists are Mutable. because str object does not support item assignment
# fruit = 'Banana'
# fruit[2] = T #won't work as str doesn't support assignment.
# TypeError: 'str' object does not support item assignment

fruit = 'Banana'
x = fruit.lower()
print(x)

