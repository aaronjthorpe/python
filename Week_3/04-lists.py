"""
lists are extremely flexible Python objects.  They are collections of multiple values.
The items in a list can be of different data types (str, int, float, etc.)  lists can even contain other lists. 
lists are mutable - their values can be changed after creation
lists are ordered - Python keeps track of the position (or 'index') of each item in the list.
lists get less efficient and take more programming power the more items they store
"""
# example.  list of strings.
# each item is separated by commas.  Each item is a separate piece of data, so each is delimited (')
fruits = ['apple','banana','cherry','date']

# list of ints
numbers = [123,0,456,-999,789]

# list of different data types.  This list contains a string, an int, a float, a bool, and a list.
# putting a list inside a list is called 'nesting'  The nested list here contains an int, str, and bool.
random_junk = ['abc',123,3.1415,True,[1,'xyz',False]]

# An empty list can be created by declaring a variable and using square brackets
empty_list = []

# Position of items in the list can be accessed 'forward' starting at 0, or 'backward' staring at -1.

#   index    0        1        2       3
fruits = ['apple','banana','cherry','date']
#   index   -4       -3       -2      -1

# You cannot 'wrap around.'  In the example above, trying to access index 4, or index -5 will produce 'Index out of range' errors.

print(fruits.count('nope'))