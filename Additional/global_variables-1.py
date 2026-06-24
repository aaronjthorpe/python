def some_function():
    variable_in_function = 'Hello'
    print(variable_in_function)

some_function()  

try:
    print(variable_in_function)
except NameError:
    print("The code in the try block doesn't work because variable_in_function doesn't exist")
    print("That variable is created when the function is called, used in the function,")
    print("But then 'self-destructs' when the function completes.")