def some_function():
    global var
    var = 'Hi'
    print("Inside function:",var)

some_function()
print(var) # Works as expected, var='Hi' as set by some_function().  The warning from the editor (var is unbound), is a mistake

var = 'Something else'
print(var) # As expected, var is overwritten, changes to 'Something Else'
some_function()
print(var) # Here is the danger of global variables: if we're not paying attention and/or don't know what happens
# inside some_function(), we might expect var to still be 'Something else', but when we run the function on line 11,
# it changes the valueback to 'Hi'