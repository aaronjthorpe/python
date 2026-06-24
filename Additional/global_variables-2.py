# Here, var is defined before the function is created.  It has a value of 'This message was set before the function'.
# when we print it on line 11, the output makes sense.
# Now for the 'tricky' part...
# At line 14, we create a new variable, also called var, with the value of 'Hello'.
# This variable is said to be 'local in scope' to the function.  We effectively have 2 variables both called var.
# Only one of the vars can be used at a time.  Within the function, we use the local variable if it exists.
# When the function finishes (after line 15), that local variable 'self-destructs'
# On line 19, we're still referencing the original var that was created on line 10.

var = 'This message was set before the function'
print(var)

def some_function():
    var = 'Hello'
    print(var)

some_function()  

print(var)


#In the example below, we create a variable, var2, *before the function is called*.  (We could also move line 28 to line 24 and it would work the same)
#Because no local variable var2 is created during the second_function, it uses the existing 'global variable' from outside the function.

def second_function():
    print(var2) 

var2 = 'Before second functon'
second_function()
print("***",var2,"***") # Asterisks here are just used to distinguish accessing var2 from inside vs. outside the function.