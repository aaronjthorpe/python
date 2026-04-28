#Floats (floating point numbers) are numbers that include a decimal point
#They are **approximate** numbers.
#In maths we have numbers such as 2/3 which is 0.66666666 recurring forever
#The computer cannot continue forever.  It must 'draw the line' somewhere.
#We can reduce approximation and create precision by rounding.

# A common issue with floats
print(0.1 + 0.2)   # This will equal 0.30000000000000004 because of binary math

print(round(0.1 + 0.2,4)) # round to 4 decimal places will be 0.3000 or 0.3

var = 0.3
print(type(var)) #var is a float

print(0.1 + 0.2 == var) # This will be False because 0.30000000000000004 is not equal to 0.3
print((round(0.1 + 0.2,4)) == var) # This will be True

#True and False are boolean values (data type bool) they can also be represented as ints (1 and 0)


# Operators
# + Addition
# + Concatenation
# - Subtraction 
# * Multiplication
# / Division
# = Assignment 
# == Checking equality
# != Not equals
# ** = To the power of
# // = floor division
# % = modulus