from math import pi

print(pi)

#After we import a variable, or if it has been previously set
#We can override it's value.  This is fine if deliberate, but could be accidental
#My version of VS code gives a warning on line 8, but runs anyway.
pi = 3.14
print(pi)

#When we import again, it 'resets' the value.
from math import pi
print("again", pi)


# def display_message():
#     global message
#     message = "Hello"   # local variable
#     print(message)

# def some_other_function():
#     global message
#     message = 'Hi!'
#     print(message)

# def some_third_function():
#     print(message)


# display_message()
# some_other_function()
# some_third_function()

# print(message)

# #print(message)   


#global message


def some_function():
    
    print(message)  # accesses existing global variable
    print(message2) # this will produce an error since message2 is local to main() it is not available here


def main():
    global message
    message = 'hi'
    message2 = "This variable is local.  It will not be accessible outside of main."
    some_function()

if __name__ == '__main__':
    main()
