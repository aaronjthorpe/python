# An adjustment to first demo.
# Here we want to create a variable inside the function, but we want it to persist and be accessible to other functions.
# We can use the key word 'global' to promote a variable from local scope to global scope.
# The variable will persist and be available to other functions.


def some_function():
    global variable_in_function
    variable_in_function = 'Hello'
    print(variable_in_function)

# print(variable_in_function)  # This won't work here, because even though the function has been defined, it has not yet been called.

some_function()  

try:
    print(variable_in_function)
except NameError:
    print("This except block shouldn't be necessary now, because")
    print("variable_in_function is gloabl, and will be accessible outside the function.")
    print("So long as it is called after the function is ran at least once.")