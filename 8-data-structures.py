# Programming
# Algorithms : a set of rules or steps used to solve problem ex.loops
# Data Structure : a particular way of organizing data in a computer ex. string, list etc

# Strings are not Mutable, whereas Lists are Mutable. because str object does not support item assignment
# fruit = 'Banana'
# fruit[2] = T #won't work as str doesn't support assignment.
# TypeError: 'str' object does not support item assignment

# fruit = 'Banana'
# x = fruit.lower()
# print(x)

# # List Method
# x = list() #list() is reserved class in python
# print(type(x))
# print(dir(x))

# friends = ['Josh', 'Glen', 'Rose']
# friends.sort()
# print(friends)

# Average
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average: ', average)
