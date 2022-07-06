# Don't Repeat Yourself

# def statement : indicates the start of a function, and the following indented section of code is to be stored for later.

# print(), input(), float(), int() ... are Built-in functions


# Function & Invoke
# Once we have defined a function, we can cal (or invoke) it as many times as we like.
# This is store & reuse pattern

# Parameters
# A parameter is a variable which we use in the function definition.
# ex. def greet(lang):
#         if lang == 'es':
#             print('Hola')  
#         elif lang == 'fr':
#             print('Bonjour')
#         else:
#             print('Hello')

# Return Statement
# Often a function will take its arguments, do some computation, and return a value to be used as the value of the function call in the calling expression.
def greet():
    return('Hello')

# Return function is fruitful.
# A "Fruitful" function is one that produces a result (or return value)
# A return statement ends the function execution and 'sends back' the result of the function.