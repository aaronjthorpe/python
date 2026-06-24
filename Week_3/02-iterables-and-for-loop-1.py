"""
We learnt about 'iterables'.  In Python, an 'iterable' is anything through which we can iterate.
To iterate is to loop through something or to attempt something multiple times.

Many classes ('data types') are iterable in Python.
Some include strings, lists, tuples, sets, and dictionaries.
We can also create an artificial iterable using the range() function.

We can iterate through an interable using a 'for' loop.  The idea here is that unlike the
artifical counter for a while loop, a for loop will loop a dynamic number of times based on the
number of items in the iterable.
For example - 'for every character in a string'.  'for every item in a list'.  'for every file in a folder'.  'for every number between 1 and 10.'
In other words, how ever many items we give a for loop, that's how many times it will run.

the standard for loop syntax is

for 'iteration' in 'iterable':
    repeat indented code.

where 'iteration' is a variable that we create when creating the for loop structure (it does not exist beforehand)
it represents the current iteration / the current loop / the current item being processed.
and 'iterable' represents an existing iterable object we can loop through such as a list or string.

"""

# an example using a string.  time/sleep is not necessary, but it helps to show 
# a) that we can run multiple lines of code each loop and b) a delay in between each loop
# my_string has 5 letters, so the loop will run 5 times.
# note that the variable character is not created before 'for', but my_string already exists.
import time
my_string = 'Hello'
for character in my_string:  # for every character that exists in my_string, repeat the indented code.
    print(character.upper())
    time.sleep(1)
print('Done!') # this line will run after all 5 loops are completed.