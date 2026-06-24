long_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
fruits = ['apple','banana','cherry','date','elderberry']
nested_list = [123,456,['abc','def','ghi'],[0.0,0.1,0.2]] # This list contains 2 ints and 2 lists.  The two nested lists contain strings and floats, respectively.

# To access a single item from a list, simply use it's index.
print(fruits[1])  # displays 'banana'
print(nested_list[2][-1])  # displays 'ghi'.  The last item (-1) in the list at index 2 (['abc','def','ghi'])

# 'Slicing' is the concept of retrieving multiple items from a list.
# It supports up to 3 arguments in the same way that range() does:  start point, exclusive end, interval.
# The output of slicing is a list.
print(long_list[0:5])  # produces a list ['a','b','c','d','e'] (index 0 through 4 of long_list)
print(long_list[10:20:2])  # produces a list ['k','m','o','q','s'] (index 10,12,14,16,18 of long_list)
print(nested_list[3][1:3]) # returns [0.1,0,2] (index 1 and 2 of nested list at index 3 in nested_list) - note that even though we specify index 3 of the nested list which does not exist, this does not produce an error because we stop *before* that number i.e. include index 1 and 2.

# Leaving an argument blank will continue to the end of the list.
print(long_list[10:]) # start at index 10 and go to end of list (k - z)
print(long_list[:15]) # start at beginning of list and stop before index 15 (a - o)
print(long_list[::5]) # run from beginning to end, but only every 5th item (a,f,k,p,u,z)
print(fruits[::-1]) # a useful and common example - run through list from *end* to *beginning*, going backwards (-) 1 at a time.


# Slicing works with other iterables e.g. string as well
my_string = "Hello, world!"
print(my_string[::-1]) # !dlrow ,olleH
print(my_string[7:12].capitalize()) # World
